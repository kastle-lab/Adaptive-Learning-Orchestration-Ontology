# Key Notions

- **Pedagogical Framework**
  - <u><b>Rationale</b></u>: Represents the ability to capture a pedagogical framework used for instructional design
  - <u>**Connected Pattern**</u>: [Part-Whole](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/part-whole), [Sequence](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/sequence)
  <!-- - <u>**Source Dataset(s)**</u>: [Dataset 1](url), [Dataset 2](url) -->

---

- **Pedagogical Element**
  - <u><b>Rationale</b></u>: Represents the atomic finite element that is part of a pedagogical framework
  - <u>**Connected Pattern**</u>: [Part-Whole](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/part-whole), [Sequence](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/sequence)

---

- **Pedagogical Technique**
  - <u><b>Rationale</b></u>: Represents the ability to capture a specific instructional method that is used in instruction design
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub)

---

- **Learning Objective**
  - <u><b>Rationale</b></u>: Represents the ability to capture a target learning outcome.
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub), [Description-Situation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/description-situation)

---

- **Learning Situation**
  - <u><b>Rationale</b></u>: Represents the ability to capture the current state or situation of learner (eg. prior knowledge etc).
  - <u>**Connected Pattern**</u>: [Description-Situation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/description-situation)

---

- **Learning Strategy**
  - <u><b>Rationale</b></u>: Represents the ability to capture how instructional components come together in a teaching plan.
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub), [Description-Situation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/description-situation)

---

- **Response**
  - <u><b>Rationale</b></u>: Represents the ability to capture an explicit feedback message or system output delivered to a learner.
  - <u>**Connected Pattern**</u>: [Rporting-Event](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/reporting-event), [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/provenance)

---

- **Learning Feeback**
  - <u><b>Rationale</b></u>: Represents the ability to capture an observation about a learner's performance or understanding.
  - <u>**Connected Pattern**</u>: [Observation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation), [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/provenance)

---

- **Learning Feeback Type**
  - <u><b>Rationale</b></u>: Represents the ability to capture categories of feedback like "corrective feedback", "motivational feedback", etc. These are controlled vocabulary classifications.
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub), [Taxonomy-Alignment](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/taxonomy-alignment)

---

- **Evaluation Technique**
  - <u><b>Rationale</b></u>: Represents the ability to capture what evaluation methods are utilized for assessment.
  - <u>**Connected Pattern**</u>: [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/provenance), [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/quantity)

---

- **Evaluation Metric**
  - <u><b>Rationale</b></u>: Represents the ability to capture what type of measurable unit of evaluation techniques was utilized.
  - <u>**Connected Pattern**</u>: [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/quantity), [Observation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation),

---

- **Evaluation Result**
  - <u><b>Rationale</b></u>: Represents the ability to capture what measurable value of evaluation technique was utilized.
  - <u>**Connected Pattern**</u>: [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/quantity), [Observation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation),

---

- **Evaluation Technique Type**
  - <u><b>Rationale</b></u>: Represents the abiltiy to capture categories of evaluation techniques, like "summative/formative", "automated", etc. These are controlled vocabulary classifications.
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub), [Taxonomy-Alignment](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/taxonomy-alignment)

---

- **Source**
  - <u><b>Rationale</b></u>: Represents the ability to capture an entity (teacher, LLM) that produced a Response.
  - <u>**Connected Pattern**</u>: [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/provenance), [Agent-Role](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/agent-role)

---

- **Learner**
  - <u><b>Rationale</b></u>: Represents the individual learning agent whose goals, preferences, challenges, awareness, and learning situations are modeled for personalization.
  - <u>**Connected Pattern**</u>: [Agent-Role](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/agent-role)

---

- **Learner Goal**
  - <u><b>Rationale</b></u>: Represents a learner-specific goal, such as acquiring a skill or reaching a target learning outcome.
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub), [Description-Situation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/description-situation)

---

- **Learner Preference**
  - <u><b>Rationale</b></u>: Represents learner-specific preferences used to personalize instruction, resources, feedback, delivery and recommendations (complementary to challenge).
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub)

---

- **Learning Challenge**
  - <u><b>Rationale</b></u>: Represents constraints, barriers, or needs that may affect a learner's ability to engage with instruction or learning material or process (complementary to preference).
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub)

---

- **Accessibility Challenge**
  - <u><b>Rationale</b></u>: Represents a specialized (subclass of) learning challenge related to accessibility needs, such as captions, screen-reader compatibility, alternative media, or extended time.
  - <u>**Connected Pattern**</u>: [Name-Stub](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/name-stub)

---

- **Awareness Observation**
  - <u><b>Rationale</b></u>: Represents an observation or assessment event that estimates a learner's awareness of a topic or skill
  - <u>**Connected Pattern**</u>: [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/quantity), [Observation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation), [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/provenance)

---

- **Skill**
  - <u><b>Rationale</b></u>: Represents a lightweight bridge concept connecting learner goals, learning objectives, topics, and future alignment acorss external skill or labor market ontologies.
  - <u>**Connected Pattern**</u>:

---

- **Evaluation Assessment Exercise**
  - <u><b>Rationale</b></u>: Represents an assessment activity or exercise through which a learner's understanding, awareness, or performance is evaluated with respect to a topic, skill, or learning objective.
  - <u>**Connected Pattern**</u>: [Observation](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/observation), [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/provenance)
