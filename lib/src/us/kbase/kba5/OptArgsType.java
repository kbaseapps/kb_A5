
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
    "min_span",
    "min_coverage",
    "min_overlap"
})
public class OptArgsType {

    @JsonProperty("min_span")
    private Long minSpan;
    @JsonProperty("min_coverage")
    private Long minCoverage;
    @JsonProperty("min_overlap")
    private Long minOverlap;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("min_span")
    public Long getMinSpan() {
        return minSpan;
    }

    @JsonProperty("min_span")
    public void setMinSpan(Long minSpan) {
        this.minSpan = minSpan;
    }

    public OptArgsType withMinSpan(Long minSpan) {
        this.minSpan = minSpan;
        return this;
    }

    @JsonProperty("min_coverage")
    public Long getMinCoverage() {
        return minCoverage;
    }

    @JsonProperty("min_coverage")
    public void setMinCoverage(Long minCoverage) {
        this.minCoverage = minCoverage;
    }

    public OptArgsType withMinCoverage(Long minCoverage) {
        this.minCoverage = minCoverage;
        return this;
    }

    @JsonProperty("min_overlap")
    public Long getMinOverlap() {
        return minOverlap;
    }

    @JsonProperty("min_overlap")
    public void setMinOverlap(Long minOverlap) {
        this.minOverlap = minOverlap;
    }

    public OptArgsType withMinOverlap(Long minOverlap) {
        this.minOverlap = minOverlap;
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
        return ((((((((("OptArgsType"+" [minSpan=")+ minSpan)+", minCoverage=")+ minCoverage)+", minOverlap=")+ minOverlap)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
