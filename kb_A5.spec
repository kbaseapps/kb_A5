/*
A KBase module: kb_A5
A simple wrapper for A5 Assembler
https://github.com/levinas/a5
*/

module kb_A5 {

    /* The workspace object name of a PairedEndLibrary file, whether of the
       KBaseAssembly or KBaseFile type.
    */
    typedef string paired_end_lib;
    typedef string single_end_lib;

    typedef structure {
        paired_end_lib   libfile_library;          /* paired end */
        single_end_lib   libfile_unpaired;         /*  unpaired reads */
        int              libfile_insert;           /*  insert value   */
    } libfile_args_type;

    typedef structure {
        int                      step_begin;           /* pipeline step:  1 - 5  */
        int                      step_end;             /* pipeline step:  1 - 5  */
    } pipeline_args_type;

    /* Input parameters for running A5.
        string workspace_name - the name of the workspace from which to take
           input and store output.
        list<libfile_args_type> list of entries in the libfile - SingleEndLibrary or PairedEndLibrary files
            to assemble.
        string output_contigset_name - the name of the output contigset
    */
    typedef structure {
        string                   workspace_name;
        string                   output_contigset_name;         /*  name of output contigs */
        int                      min_contig_length;             /*  (=200) minimum size of contig */
        list<libfile_args_type>  libfile_args;                  /*  arguments to create the libfile */
        pipeline_args_type       pipeline_args;                 /*  begin and end of pipeline steps */
    } A5_Params;
    
    /* Output parameters for A5 run.
        string report_name - the name of the KBaseReport.Report workspace
            object.
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
