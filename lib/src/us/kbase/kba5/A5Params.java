
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
 * <pre>
 * Input parameters for running A5.
 *  workspace_name - the name of the workspace from which to take input and store output.
 *  output_contigset_name - the name of the output contigset
 *  libfile_args - parameters for each input paired end reads
 *  min_contig_length - minimum length of contigs in the assembly output
 *  metagenome - metagenome option to A5
 *  @optional min_contig_length
 *  @optional metagenome
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "output_contigset_name",
    "libfile_args",
    "min_contig_length",
    "metagenome"
})
public class A5Params {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("output_contigset_name")
    private String outputContigsetName;
    @JsonProperty("libfile_args")
    private List<LibfileArgsType> libfileArgs;
    @JsonProperty("min_contig_length")
    private Long minContigLength;
    @JsonProperty("metagenome")
    private Long metagenome;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public A5Params withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("output_contigset_name")
    public String getOutputContigsetName() {
        return outputContigsetName;
    }

    @JsonProperty("output_contigset_name")
    public void setOutputContigsetName(String outputContigsetName) {
        this.outputContigsetName = outputContigsetName;
    }

    public A5Params withOutputContigsetName(String outputContigsetName) {
        this.outputContigsetName = outputContigsetName;
        return this;
    }

    @JsonProperty("libfile_args")
    public List<LibfileArgsType> getLibfileArgs() {
        return libfileArgs;
    }

    @JsonProperty("libfile_args")
    public void setLibfileArgs(List<LibfileArgsType> libfileArgs) {
        this.libfileArgs = libfileArgs;
    }

    public A5Params withLibfileArgs(List<LibfileArgsType> libfileArgs) {
        this.libfileArgs = libfileArgs;
        return this;
    }

    @JsonProperty("min_contig_length")
    public Long getMinContigLength() {
        return minContigLength;
    }

    @JsonProperty("min_contig_length")
    public void setMinContigLength(Long minContigLength) {
        this.minContigLength = minContigLength;
    }

    public A5Params withMinContigLength(Long minContigLength) {
        this.minContigLength = minContigLength;
        return this;
    }

    @JsonProperty("metagenome")
    public Long getMetagenome() {
        return metagenome;
    }

    @JsonProperty("metagenome")
    public void setMetagenome(Long metagenome) {
        this.metagenome = metagenome;
    }

    public A5Params withMetagenome(Long metagenome) {
        this.metagenome = metagenome;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("A5Params"+" [workspaceName=")+ workspaceName)+", outputContigsetName=")+ outputContigsetName)+", libfileArgs=")+ libfileArgs)+", minContigLength=")+ minContigLength)+", metagenome=")+ metagenome)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
