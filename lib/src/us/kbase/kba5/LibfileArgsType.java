
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
 * <p>Original spec-file type: libfile_args_type</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "libfile_library",
    "libfile_unpaired",
    "libfile_insert"
})
public class LibfileArgsType {

    @JsonProperty("libfile_library")
    private String libfileLibrary;
    @JsonProperty("libfile_unpaired")
    private String libfileUnpaired;
    @JsonProperty("libfile_insert")
    private Long libfileInsert;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("libfile_library")
    public String getLibfileLibrary() {
        return libfileLibrary;
    }

    @JsonProperty("libfile_library")
    public void setLibfileLibrary(String libfileLibrary) {
        this.libfileLibrary = libfileLibrary;
    }

    public LibfileArgsType withLibfileLibrary(String libfileLibrary) {
        this.libfileLibrary = libfileLibrary;
        return this;
    }

    @JsonProperty("libfile_unpaired")
    public String getLibfileUnpaired() {
        return libfileUnpaired;
    }

    @JsonProperty("libfile_unpaired")
    public void setLibfileUnpaired(String libfileUnpaired) {
        this.libfileUnpaired = libfileUnpaired;
    }

    public LibfileArgsType withLibfileUnpaired(String libfileUnpaired) {
        this.libfileUnpaired = libfileUnpaired;
        return this;
    }

    @JsonProperty("libfile_insert")
    public Long getLibfileInsert() {
        return libfileInsert;
    }

    @JsonProperty("libfile_insert")
    public void setLibfileInsert(Long libfileInsert) {
        this.libfileInsert = libfileInsert;
    }

    public LibfileArgsType withLibfileInsert(Long libfileInsert) {
        this.libfileInsert = libfileInsert;
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
        return ((((((((("LibfileArgsType"+" [libfileLibrary=")+ libfileLibrary)+", libfileUnpaired=")+ libfileUnpaired)+", libfileInsert=")+ libfileInsert)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
