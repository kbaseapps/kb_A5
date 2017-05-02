
package us.kbase.kba5;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: A5_Params</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "read_libraries",
    "output_contigset_name",
    "min_contig",
    "opt_args"
})
public class A5Params {

    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("read_libraries")
    private List<String> readLibraries;
    @JsonProperty("output_contigset_name")
    private java.lang.String outputContigsetName;
    @JsonProperty("min_contig")
    private Long minContig;
    /**
     * <p>Original spec-file type: opt_args_type</p>
     * <pre>
     * Input parameters for running A5.
     * string workspace_name - the name of the workspace from which to take
     *    input and store output.
     * list<paired_end_lib> read_libraries - Illumina PairedEndLibrary files
     *     to assemble.
     * string output_contigset_name - the name of the output contigset
     * </pre>
     * 
     */
    @JsonProperty("opt_args")
    private OptArgsType optArgs;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("workspace_name")
    public java.lang.String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public A5Params withWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("read_libraries")
    public List<String> getReadLibraries() {
        return readLibraries;
    }

    @JsonProperty("read_libraries")
    public void setReadLibraries(List<String> readLibraries) {
        this.readLibraries = readLibraries;
    }

    public A5Params withReadLibraries(List<String> readLibraries) {
        this.readLibraries = readLibraries;
        return this;
    }

    @JsonProperty("output_contigset_name")
    public java.lang.String getOutputContigsetName() {
        return outputContigsetName;
    }

    @JsonProperty("output_contigset_name")
    public void setOutputContigsetName(java.lang.String outputContigsetName) {
        this.outputContigsetName = outputContigsetName;
    }

    public A5Params withOutputContigsetName(java.lang.String outputContigsetName) {
        this.outputContigsetName = outputContigsetName;
        return this;
    }

    @JsonProperty("min_contig")
    public Long getMinContig() {
        return minContig;
    }

    @JsonProperty("min_contig")
    public void setMinContig(Long minContig) {
        this.minContig = minContig;
    }

    public A5Params withMinContig(Long minContig) {
        this.minContig = minContig;
        return this;
    }

    /**
     * <p>Original spec-file type: opt_args_type</p>
     * <pre>
     * Input parameters for running A5.
     * string workspace_name - the name of the workspace from which to take
     *    input and store output.
     * list<paired_end_lib> read_libraries - Illumina PairedEndLibrary files
     *     to assemble.
     * string output_contigset_name - the name of the output contigset
     * </pre>
     * 
     */
    @JsonProperty("opt_args")
    public OptArgsType getOptArgs() {
        return optArgs;
    }

    /**
     * <p>Original spec-file type: opt_args_type</p>
     * <pre>
     * Input parameters for running A5.
     * string workspace_name - the name of the workspace from which to take
     *    input and store output.
     * list<paired_end_lib> read_libraries - Illumina PairedEndLibrary files
     *     to assemble.
     * string output_contigset_name - the name of the output contigset
     * </pre>
     * 
     */
    @JsonProperty("opt_args")
    public void setOptArgs(OptArgsType optArgs) {
        this.optArgs = optArgs;
    }

    public A5Params withOptArgs(OptArgsType optArgs) {
        this.optArgs = optArgs;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((((("A5Params"+" [workspaceName=")+ workspaceName)+", readLibraries=")+ readLibraries)+", outputContigsetName=")+ outputContigsetName)+", minContig=")+ minContig)+", optArgs=")+ optArgs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
