
package us.kbase.kba5;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "begin",
    "end",
    "preprocessed"
})
public class OptArgsType {

    @JsonProperty("begin")
    private Long begin;
    @JsonProperty("end")
    private Long end;
    @JsonProperty("preprocessed")
    private Long preprocessed;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("begin")
    public Long getBegin() {
        return begin;
    }

    @JsonProperty("begin")
    public void setBegin(Long begin) {
        this.begin = begin;
    }

    public OptArgsType withBegin(Long begin) {
        this.begin = begin;
        return this;
    }

    @JsonProperty("end")
    public Long getEnd() {
        return end;
    }

    @JsonProperty("end")
    public void setEnd(Long end) {
        this.end = end;
    }

    public OptArgsType withEnd(Long end) {
        this.end = end;
        return this;
    }

    @JsonProperty("preprocessed")
    public Long getPreprocessed() {
        return preprocessed;
    }

    @JsonProperty("preprocessed")
    public void setPreprocessed(Long preprocessed) {
        this.preprocessed = preprocessed;
    }

    public OptArgsType withPreprocessed(Long preprocessed) {
        this.preprocessed = preprocessed;
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
        return ((((((((("OptArgsType"+" [begin=")+ begin)+", end=")+ end)+", preprocessed=")+ preprocessed)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
