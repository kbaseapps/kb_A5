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

    /* Input parameters for running A5.
        string workspace_name - the name of the workspace from which to take
           input and store output.
        list<paired_end_lib> read_libraries - Illumina PairedEndLibrary files
            to assemble.
        string output_contigset_name - the name of the output contigset
    */
    typedef structure {
        int min_span;       /* default 2000 */
        int min_coverage;   /* default 3 */
        int min_overlap;    /* default 2000 */
    } opt_args_type;

    typedef structure {
        string               workspace_name;
        list<paired_end_lib> read_libraries;                /*  input reads  */
        string               output_contigset_name;         /*  name of output contigs */
        int                  min_contig;                    /*  (=200) minimum size of contig */
        opt_args_type        opt_args;
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
