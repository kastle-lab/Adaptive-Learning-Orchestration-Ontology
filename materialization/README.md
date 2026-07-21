# Materialization

Generated RDF/Turtle graph fragments created from [synthetic_data/](../synthetic_data/) using [foundry_mappings/](../foundry_mappings/).

Each subfolder corresponds to one source CSV and usually contains:

- `output-<source>-<row>.ttl` for row-level graph fragments.
- `output-cv-<source>-<index>.ttl` for controlled vocabulary fragments, when present.

Common generated prefixes include `aplo-ont`, `aplo-r`, `edu-ont`, `edu-r`, `rdf`, `xsd`, and sometimes `time`.
