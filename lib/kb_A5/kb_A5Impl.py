# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statements should live
from __future__ import print_function
import os
import re
import uuid
from pprint import pformat
from pprint import pprint
from biokbase.workspace.client import Workspace as workspaceService
import subprocess
import numpy as np
from ReadsUtils.ReadsUtilsClient import ReadsUtils
from ReadsUtils.baseclient import ServerError
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from KBaseReport.KBaseReportClient import KBaseReport
from kb_quast.kb_quastClient import kb_quast
import time
from datetime import datetime
import psutil

class ShockException(Exception):
    pass

#END_HEADER


class kb_A5:
    '''
    Module Name:
    kb_A5

    Module Description:
    A KBase module: kb_A5
    A simple wrapper for A5 Assembler
    https://github.com/levinas/a5
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbaseapps/kb_A5.git"
    GIT_COMMIT_HASH = "133529613cba4163e314095f564573734ff5f74b"

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    DISABLE_A5_OUTPUT = False  # should be False in production

    PARAM_IN_WS = 'workspace_name'
    PARAM_IN_CS_NAME = 'output_contigset_name'
    PARAM_IN_MIN_CONTIG = 'min_contig_length'
    PARAM_IN_METAGENOME = 'metagenome'
    PARAM_IN_LIBFILE_ARGS = 'libfile_args'
    PARAM_IN_LIBRARY = 'libfile_library'
    PARAM_IN_UNPAIRED = 'libfile_unpaired'
    PARAM_IN_INSERT = 'libfile_insert'
    INPUT_LIBFILE = 'generated_input_libfile'

    INVALID_WS_OBJ_NAME_RE = re.compile('[^\\w\\|._-]')
    INVALID_WS_NAME_RE = re.compile('[^\\w:._-]')

    THREADS_PER_CORE = 1

    URL_WS = 'workspace-url'
    URL_SHOCK = 'shock-url'
    URL_KB_END = 'kbase-endpoint'

    TRUE = 'true'
    FALSE = 'false'

    # code taken from kb_SPAdes

    def log(self, message, prefix_newline=False):
        print(('\n' if prefix_newline else '') +
              str(time.time()) + ': ' + str(message))


    def get_input_reads(self, params, token):
        print('in get input reads')

        wsname = params[self.PARAM_IN_WS]
        libfile_args = params[self.PARAM_IN_LIBFILE_ARGS]

        obj_ids = []
        for libarg in libfile_args:
            read_name = libarg[self.PARAM_IN_LIBRARY]
            r = read_name if '/' in read_name else (wsname + '/' + read_name)
            obj_ids.append({'ref': r})
            libarg['ref_library'] = r

            if self.PARAM_IN_UNPAIRED in libarg and libarg[self.PARAM_IN_UNPAIRED] is not None:
                read_name = libarg[self.PARAM_IN_UNPAIRED]
                r = read_name if '/' in read_name else (wsname + '/' + read_name)
                obj_ids.append({'ref': r})
                libarg['ref_unpaired'] = r

        ws = workspaceService(self.workspaceURL, token=token)
        ws_info = ws.get_object_info_new({'objects': obj_ids})
        reads_params = []

        reftoname = {}
        for wsi, oid in zip(ws_info, obj_ids):
            ref = oid['ref']
            reads_params.append(ref)
            obj_name = wsi[1]
            reftoname[ref] = wsi[7] + '/' + obj_name

        readcli = ReadsUtils(self.callbackURL, token=token,
                             service_ver='dev')

        typeerr = ('Supported types: KBaseFile.SingleEndLibrary ' +
                   'KBaseFile.PairedEndLibrary ' +
                   'KBaseAssembly.SingleEndLibrary ' +
                   'KBaseAssembly.PairedEndLibrary')

        try:
            reads = readcli.download_reads({'read_libraries': reads_params,
                                            'interleaved': 'true',
                                            'gzipped': None
                                            })['files']
        except ServerError as se:
            self.log('logging stacktrace from dynamic client error')
            self.log(se.data)
            if typeerr in se.message:
                prefix = se.message.split('.')[0]
                raise ValueError(
                    prefix + '. Only the types ' +
                    'KBaseAssembly.PairedEndLibrary ' +
                    'and KBaseFile.PairedEndLibrary are supported')
            else:
                raise

        self.log('Got reads data from converter:\n' + pformat(reads))
        print("READS:")
        pprint(reads)
        return reads


    def generate_libfile(self, libfile_args, reads, outdir):
        print ("in GENERATE libfile")
        pprint(libfile_args)

        if not os.path.exists(outdir):
            os.makedirs(outdir)

        libfile_name = os.path.join(outdir, self.INPUT_LIBFILE)
        with open(libfile_name, 'w') as libf:
            for libarg in libfile_args:
                libf.write('[LIB]\n')
                library = reads[libarg['ref_library']]['files']['fwd']
                libf.write('shuf='+library+'\n')
                if self.PARAM_IN_UNPAIRED in libarg and libarg[self.PARAM_IN_UNPAIRED] is not None:
                    unpaired = reads[libarg['ref_unpaired']]['files']['fwd']
                    libf.write('up='+unpaired+'\n')
                if self.PARAM_IN_INSERT in libarg and libarg[self.PARAM_IN_INSERT] is not None:
                    if (int(libarg[self.PARAM_IN_INSERT])) > 0:
                        libf.write('ins='+str(libarg[self.PARAM_IN_INSERT])+'\n')
            libf.close()
        return libfile_name


    def exec_A5(self, libfile, params, outdir):

        output_files_prefix = params[self.PARAM_IN_CS_NAME]
        a5_cmd = ['a5_pipeline.pl']

        threads = psutil.cpu_count() * self.THREADS_PER_CORE
        a5_cmd.append('--threads=' + str(threads))

        if self.PARAM_IN_METAGENOME in params and params[self.PARAM_IN_METAGENOME]:
            a5_cmd.append('--metagenome')

        a5_cmd.append(libfile),
        a5_cmd.append(output_files_prefix)

        print("\nA5 CMD:     " + str(a5_cmd))
        self.log(a5_cmd)

        if self.DISABLE_A5_OUTPUT:
            with open(os.devnull, 'w') as null:
                p = subprocess.Popen(a5_cmd, cwd=outdir, shell=False,
                                     stdout=null, stderr=null)
        else:
            p = subprocess.Popen(a5_cmd, cwd=outdir, shell=False)

        retcode = p.wait()

        self.log('Return code: ' + str(retcode))
        if p.returncode != 0:
            raise ValueError('Error running A5, return code: ' +
                             str(retcode) + '\n')


    # adapted from
    # https://github.com/kbase/transform/blob/master/plugins/scripts/convert/
    # trns_transform_KBaseFile_AssemblyFile_to_KBaseGenomes_ContigSet.py
    # which was adapted from an early version of
    # https://github.com/kbase/transform/blob/master/plugins/scripts/upload/
    # trns_transform_FASTA_DNA_Assembly_to_KBaseGenomes_ContigSet.py

    def load_stats(self, input_file_name):
        self.log('Starting conversion of FASTA to KBaseGenomeAnnotations.Assembly')
        self.log('Building Object.')
        if not os.path.isfile(input_file_name):
            raise Exception('The input file name {0} is not a file!'.format(
                input_file_name))
        with open(input_file_name, 'r') as input_file_handle:
            contig_id = None
            sequence_len = 0
            fasta_dict = dict()
            first_header_found = False
            # Pattern for replacing white space
            pattern = re.compile(r'\s+')
            for current_line in input_file_handle:
                if (current_line[0] == '>'):
                    # found a header line
                    # Wrap up previous fasta sequence
                    if not first_header_found:
                        first_header_found = True
                    else:
                        fasta_dict[contig_id] = sequence_len
                        sequence_len = 0
                    fasta_header = current_line.replace('>', '').strip()
                    try:
                        contig_id = fasta_header.strip().split(' ', 1)[0]
                    except:
                        contig_id = fasta_header.strip()
                else:
                    sequence_len += len(re.sub(pattern, '', current_line))
        # wrap up last fasta sequence, should really make this a method
        if not first_header_found:
            raise Exception("There are no contigs in this file")
        else:
            fasta_dict[contig_id] = sequence_len
        return fasta_dict


    def load_report(self, input_file_name, params, wsname):
        fasta_stats = self.load_stats(input_file_name)
        lengths = [fasta_stats[contig_id] for contig_id in fasta_stats]

        assembly_ref = params[self.PARAM_IN_WS] + '/' + params[self.PARAM_IN_CS_NAME]

        report = ''
        report += 'Assembly saved to: ' + assembly_ref + '\n'
        report += 'Assembled into ' + str(len(lengths)) + ' contigs.\n'
        report += 'Avg Length: ' + str(sum(lengths) / float(len(lengths))) + \
            ' bp.\n'

        # compute a simple contig length distribution
        bins = 10
        counts, edges = np.histogram(lengths, bins)  # @UndefinedVariable
        report += 'Contig Length Distribution (# of contigs -- min to max ' +\
            'basepairs):\n'
        for c in range(bins):
            report += '   ' + str(counts[c]) + '\t--\t' + str(edges[c]) +\
                ' to ' + str(edges[c + 1]) + ' bp\n'
        print('Running QUAST')
        kbq = kb_quast(self.callbackURL)
        quastret = kbq.run_QUAST({'files': [{'path': input_file_name,
                                             'label': params[self.PARAM_IN_CS_NAME]}]})
        print('Saving report')
        kbr = KBaseReport(self.callbackURL)
        report_info = kbr.create_extended_report(
            {'message': report,
             'objects_created': [{'ref': assembly_ref, 'description': 'Assembled contigs'}],
             'direct_html_link_index': 0,
             'html_links': [{'shock_id': quastret['shock_id'],
                             'name': 'report.html',
                             'label': 'QUAST report'}
                            ],
             'report_object_name': 'kb_A5-_report_' + str(uuid.uuid4()),
             'workspace_name': params['workspace_name']
            })
        reportName = report_info['name']
        reportRef = report_info['ref']
        return reportName, reportRef


    def make_ref(self, object_info):
        return str(object_info[6]) + '/' + str(object_info[0]) + \
            '/' + str(object_info[4])


    def process_params(self, params):
        if (self.PARAM_IN_WS not in params or
                not params[self.PARAM_IN_WS]):
            raise ValueError(self.PARAM_IN_WS + ' parameter is required')
        if self.INVALID_WS_NAME_RE.search(params[self.PARAM_IN_WS]):
            raise ValueError('Invalid workspace name ' +
                             params[self.PARAM_IN_WS])
        if self.PARAM_IN_LIBFILE_ARGS not in params:
            raise ValueError(self.PARAM_IN_LIBFILE_ARGS + ' parameter is required')
        if type(params[self.PARAM_IN_LIBFILE_ARGS]) != list:
            raise ValueError(self.PARAM_IN_LIBFILE_ARGS + ' must be a list')
        if not params[self.PARAM_IN_LIBFILE_ARGS]:
            raise ValueError('At least one reads library must be provided')
        for libarg in params[self.PARAM_IN_LIBFILE_ARGS]:
            if self.PARAM_IN_UNPAIRED in libarg and libarg[self.PARAM_IN_UNPAIRED] is not None:
                val = libarg[self.PARAM_IN_UNPAIRED].strip().lower()
                if val == 'none':
                    libarg[self.PARAM_IN_UNPAIRED] = None
            if self.PARAM_IN_INSERT in libarg and libarg[self.PARAM_IN_INSERT] is not None:
                if not isinstance(libarg[self.PARAM_IN_INSERT], int):
                    raise ValueError('insert value must be of type int')

        if (self.PARAM_IN_CS_NAME not in params or
                not params[self.PARAM_IN_CS_NAME]):
            raise ValueError(self.PARAM_IN_CS_NAME + ' parameter is required')
        if self.INVALID_WS_OBJ_NAME_RE.search(params[self.PARAM_IN_CS_NAME]):
            raise ValueError('Invalid workspace object name ' +
                             params[self.PARAM_IN_CS_NAME])

        if self.PARAM_IN_MIN_CONTIG in params and params[self.PARAM_IN_MIN_CONTIG] is not None:
            if not isinstance(params[self.PARAM_IN_MIN_CONTIG], int):
                raise ValueError('min_contig must be of type int')


    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callbackURL = os.environ['SDK_CALLBACK_URL']
        self.log('Callback URL: ' + self.callbackURL)
        self.workspaceURL = config[self.URL_WS]
        self.shockURL = config[self.URL_SHOCK]
        self.catalogURL = config[self.URL_KB_END] + '/catalog'
        self.scratch = os.path.abspath(config['scratch'])
        if not os.path.exists(self.scratch):
            os.makedirs(self.scratch)
        #END_CONSTRUCTOR
        pass


    def run_A5(self, ctx, params):
        """
        Run A5 on paired end libraries
        :param params: instance of type "A5_Params" (Input parameters for
           running A5. workspace_name - the name of the workspace from which
           to take input and store output. output_contigset_name - the name
           of the output contigset libfile_args - parameters for each input
           paired end reads min_contig_length - minimum length of contigs in
           the assembly output metagenome - metagenome option to A5 @optional
           min_contig_length @optional metagenome) -> structure: parameter
           "workspace_name" of String, parameter "output_contigset_name" of
           String, parameter "libfile_args" of list of type
           "libfile_args_type" (Parameters for a paired end library entry in
           the input 'libfile') -> structure: parameter "libfile_library" of
           type "paired_end_lib" (The workspace object name of a
           PairedEndLibrary file, whether of the KBaseAssembly or KBaseFile
           type.), parameter "libfile_unpaired" of String, parameter
           "libfile_insert" of Long, parameter "min_contig_length" of Long,
           parameter "metagenome" of type "bool" (A boolean - 0 for false, 1
           for true. @range (0, 1))
        :returns: instance of type "A5_Output" (Output parameters for A5 run.
           string report_name - the name of the KBaseReport.Report workspace
           object. string report_ref - the workspace reference of the
           report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_A5
        
        print("===================  IN run_A5")

        # A whole lot of this is adapted or outright copied from
        # https://github.com/msneddon/MEGAHIT
        self.log('Running run_A5 with params:\n' + pformat(params))

        # the reads should really be specified as a list of absolute ws refs
        # but the narrative doesn't do that yet
        self.process_params(params)
        pprint(params)

        token = ctx['token']

        # get absolute refs from ws
        wsname = params[self.PARAM_IN_WS]
        print("Workspace name: " + wsname)

        # set the output location
        timestamp = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000)
        outdir = os.path.join(self.scratch, 'A5_dir' + str(timestamp))

        reads = self.get_input_reads(params, token)
        libFile = self.generate_libfile(params[self.PARAM_IN_LIBFILE_ARGS], reads, outdir)
        a5_output_prefix = params[self.PARAM_IN_CS_NAME]

        self.exec_A5(libFile, params, outdir)
        self.log('A5 output dir: ' + a5_output_prefix)

        # parse the output and save back to KBase

        output_contigs = os.path.join(outdir, a5_output_prefix + ".contigs.fasta")

        min_contig_len = 0

        if self.PARAM_IN_MIN_CONTIG in params and params[self.PARAM_IN_MIN_CONTIG] is not None:
            if (int(params[self.PARAM_IN_MIN_CONTIG])) > 0:
                min_contig_len = int(params[self.PARAM_IN_MIN_CONTIG])

        self.log('Uploading FASTA file to Assembly')
        assemblyUtil = AssemblyUtil(self.callbackURL, token=ctx['token'], service_ver='dev')

        assemblyUtil.save_assembly_from_fasta({'file': {'path': output_contigs},
                                               'workspace_name': wsname,
                                               'assembly_name': params[self.PARAM_IN_CS_NAME],
                                               'min_contig_length': min_contig_len
                                               })

        report_name, report_ref = self.load_report(output_contigs, params, wsname)

        output = {'report_name': report_name,
                  'report_ref': report_ref
                  }

        #END run_A5

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_A5 return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        del ctx  # shut up pep8
        #END_STATUS
        return [returnVal]
