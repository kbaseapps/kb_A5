/*
A KBase module: kb_A5
A simple wrapper for A5 Assembler
https://github.com/levinas/a5
*/

module kb_A5 {

    /*
        A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int bool;

    /*
       The workspace object name of a PairedEndLibrary file, whether of the
       KBaseAssembly or KBaseFile type.
    */

    typedef string paired_end_lib;

    /*
        Parameters for a paired end library entry in the input 'libfile'
    */

    typedef structure {
        paired_end_lib   libfile_library;    /* paired end */
        string           libfile_unpaired;   /*  unpaired reads */
        int              libfile_insert;     /*  insert value   */
    } libfile_args_type;

    /*
       Input parameters for running A5.
        workspace_name - the name of the workspace from which to take input and store output.
        output_contigset_name - the name of the output contigset
        libfile_args - parameters for each input paired end reads
        min_contig_length - minimum length of contigs in the assembly output
        metagenome - metagenome option to A5

        @optional min_contig_length
        @optional metagenome
    */

    typedef structure {
        string                   workspace_name;
        string                   output_contigset_name;    /*  name of output contigs */
        list<libfile_args_type>  libfile_args;             /*  arguments to create the libfile */
        int                      min_contig_length;        /*  (=200) minimum size of contig */
        bool                     metagenome;                /*  metagenome option */
    } A5_Params;
    
    /*
       Output parameters for A5 run.
        string report_name - the name of the KBaseReport.Report workspace object.
        string report_ref - the workspace reference of the report.
    */

    typedef structure {
        string report_name;
        string report_ref;
    } A5_Output;
    
    /* Run A5 on paired end libraries */
    funcdef run_A5(A5_Params params) returns(A5_Output output)
        authentication required;
};
