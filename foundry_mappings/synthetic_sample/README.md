# Synthetic Sample Foundry Mappings

This directory contains one Kastle Foundry YAML mapping for each CSV file in
`data/synthetic_sample/`.

## Coverage

The mappings cover the synthetic sample's four ontology areas:

- Pedagogical framework: frameworks, elements, techniques, and pedagogical objectives.
- Learning objective: objectives, strategies, modules, and media.
- Learner model: learners, goals, preferences, skills, situations, challenges, awareness levels, and awareness observations.
- Evaluation: assessment exercises, techniques, metrics, results, feedback, responses, sources, workload levels, and feedback/technique type vocabularies.

The source CSVs use `|` for multi-valued cells. These mappings rely on
Foundry's `split: " | "` support to emit one RDF object per value.
Controlled vocabularies such as awareness levels, evaluation technique types,
learning feedback types, and workload levels are defined in the mapping YAMLs;
Foundry emits readable `rdf:value` labels for each controlled vocabulary
individual.

Entity URIs use the row values needed to identify the coherent resource in the
knowledge graph. For example:

- Awareness observations use learner, topic, skill, and observation name.
- Learning objectives use learning situation and objective name.
- Learning strategies use learning situation and strategy name.
- Response-like entities use learner, source, and response/result/feedback name.
- Temporal extents use parent identity plus an explicit time key.
- Assessment exercises use connected content context and exercise name.
- Sources such as `Instructor Reviewer`, `Learning Platform`, and `Learner Alex`
  are modeled as ordinary source instances from `sources.csv`.

Temporal columns are represented as `aplo-ont:TemporalExtent` resources with W3C
Time predicates for point and interval values.

## Running

Run each mapping against the matching CSV file. For example:

```bash
cd foundry
python kastle-foundry.py \
  -m mappings/synthetic_sample/learning_objectives.yaml \
  -d ../data/synthetic_sample/learning_objectives.csv \
  -o output/synthetic_sample/learning_objectives \
  --namespace https://aplo.cs.wright.edu/ \
  --prefix aplo
```

Use the same stem for the remaining files, for example
`skills.yaml` with `skills.csv`.
