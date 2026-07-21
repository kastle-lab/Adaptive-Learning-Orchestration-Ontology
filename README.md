# Adaptive Pedagogical Learning Orchestration (APLO) Ontology
APLO takes its name from the Greek word `απλό` (`aplo`), meaning simple. APLO provides a simple symbolic orchestration interface for adaptive educational systems: a way to connect pedagogical structure, learning objectives, learner context, assessment evidence, feedback, and evolving learner awareness without treating those concerns as separate data silos.

This repository contains the ontology artifacts for the APLO ontology: schema, design notes, competency questions, axiom tables, synthetic data, mappings, and generated RDF used to document and validate the ontology.

## Key Resources
- [Key notions](documentation/key-notions.md) describes the main concepts modeled by the ontology.
- [Competency questions](documentation/competency-questions.md) lists the questions the ontology is intended to answer.
- [Full schema PDF](schema/full-schema.pdf) provides a visual review of the complete schema.
- [Full schema OWL](schema/full-schema.owl) is the aggregate OWL ontology artifact.
- [Axioms CSV](axioms/axioms.csv) documents tabular axiom and constraint rationale.
- [Materialization notes](materialization/README.md) describe the generated RDF/Turtle fragments.

## Repository Map
| Directory | Intent |
| --- | --- |
| [schema/](schema/) | Holds the ontology itself and visual schema exports, including OWL, GraphML, and PDF views of the full ontology and its modules. |
| [documentation/](documentation/) | Explains the design in paper-facing language: key notions, competency questions, and SPARQL-oriented CQ notes. |
| [axioms/](axioms/) | Captures the tabular axiom and constraint rationale that supports the ontology specification. |
| [synthetic_data/](synthetic_data/) | Provides synthetic CSV data used to instantiate the ontology for validation examples. |
| [foundry_mappings/](foundry_mappings/) | Defines how each synthetic CSV file is mapped into RDF using the ontology vocabulary. |
| [materialization/](materialization/) | Stores generated `.ttl` graph fragments used to inspect and validate instantiated APLO data. |
| [scripts/](scripts/) | Contains helper scripts for exporting pattern summaries, generating OWL axioms, and uploading Turtle files. |

## Namespaces
| Prefix | Namespace |
| --- | --- |
| `aplo-ont` | `https://aplo.cs.wright.edu/lod/ontology#` |
| `aplo-r` | `https://aplo.cs.wright.edu/lod/resource#` |

## Tooling
[Kastle Foundry](https://github.com/kastle-lab/foundry) was used to materialize RDF/Turtle graph fragments from the synthetic CSV data and YAML mappings.

## Validation Status
<p>
  <a href="http://oops.linkeddata.es">
    <img src="https://oops.linkeddata.es/images/conformance/oops_free.png"
      alt="free pitfalls were found" height="69.6" width="100" />
  </a>
</p>

The ontology has been checked with OOPS and reported no detected pitfalls.

## License
This repository is licensed under the terms in [LICENSE](LICENSE).
