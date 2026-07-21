# Competency Question SPARQL Queries

## Pedagogical Organization

### CQ-001: What are all the available pedagogical frameworks?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?framework ?name WHERE {
  ?framework a aplo-ont:PedagogicalFramework .
  OPTIONAL { ?framework aplo-ont:hasName ?name . }
}
ORDER BY ?framework
```

**Top 5 output rows:**

| framework | name |
| --- | --- |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy |
| aplo-r:pedagogicalFramework.Cognitive%20Apprenticeship | Cognitive Apprenticeship |
| aplo-r:pedagogicalFramework.Collaborative%20Learning | Collaborative Learning |
| aplo-r:pedagogicalFramework.Community%20of%20Inquiry | Community of Inquiry |
| aplo-r:pedagogicalFramework.Conceptual%20Change | Conceptual Change |

### CQ-002: What pedagogical elements are a pedagogical framework?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?framework ?frameworkName ?element ?elementName WHERE {
  ?framework a aplo-ont:PedagogicalFramework ;
             aplo-ont:hasElement ?element .
  ?element a aplo-ont:PedagogicalElement .
  OPTIONAL { ?framework aplo-ont:hasName ?frameworkName . }
  OPTIONAL { ?element aplo-ont:hasName ?elementName . }

}
ORDER BY ?framework ?element
```

**Top 5 output rows:**

| framework | frameworkName | element | elementName |
| --- | --- | --- | --- |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Analyze | Analyze |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Create | Create |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Evaluate | Evaluate |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember |

### CQ-003: What pedagogical element(s) follows another pedagogical element?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?previousElement ?previousElementLabel ?nextElement ?nextElementLabel WHERE {
  ?previousElement a aplo-ont:PedagogicalElement ;
                   aplo-ont:hasNextPedagogicalElement ?nextElement .
  ?nextElement a aplo-ont:PedagogicalElement .
  OPTIONAL { ?previousElement aplo-ont:hasName ?previousElementLabel . }
  OPTIONAL { ?nextElement aplo-ont:hasName ?nextElementLabel . }
}
ORDER BY ?previousElement ?nextElement
```

**Top 5 output rows:**

| previousElement | previousElementLabel | nextElement | nextElementLabel |
| --- | --- | --- | --- |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Analyze | Analyze | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Evaluate | Evaluate |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Analyze | Analyze |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Evaluate | Evaluate | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Create | Create |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply |

### CQ-004: What pedagogical framework(s) contain pedagogical element 'X'?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?framework ?frameworkLabel ?element ?elementLabel WHERE {
  ?framework a aplo-ont:PedagogicalFramework ;
             aplo-ont:hasElement ?element .
  ?element a aplo-ont:PedagogicalElement .
  OPTIONAL { ?element aplo-ont:hasName ?elementLabel . }
  OPTIONAL { ?framework aplo-ont:hasName ?frameworkLabel . }
}
ORDER BY ?element ?framework
```

**Top 5 output rows:**

| framework | frameworkLabel | element | elementLabel |
| --- | --- | --- | --- |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Analyze | Analyze |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Create | Create |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Evaluate | Evaluate |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember |

### CQ-005: Which instructional steps can support a learner working toward a given learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?learningObjective ?learningObjectiveLabel ?instructionalStep ?instructionalStepLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?skill .
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:developsSkill ?skill ;
                     aplo-ont:alignedWith ?instructionalStep .
  ?instructionalStep a aplo-ont:PedagogicalElement .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?instructionalStep aplo-ont:hasName ?instructionalStepLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }

}
ORDER BY ?learner ?learningObjective ?instructionalStep
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | learningObjective | learningObjectiveLabel | instructionalStep | instructionalStepLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Modeling | Modeling |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:learningObjective.Identifier%20Practice%20Session.Identify%20URI%20namespace%20and%20hash%20or%20slash%20patterns | Identify URI namespace and hash or slash patterns | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Coaching | Coaching |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats | aplo-r:pedagogicalElement.Community%20of%20Inquiry.Cognitive%20Presence | Cognitive Presence |

### CQ-006: What pedagogical frameworks are available for organizing an instructional intervention?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?framework ?frameworkLabel WHERE {
  ?framework a aplo-ont:PedagogicalFramework .
  OPTIONAL { ?framework aplo-ont:hasName ?frameworkLabel . }
}
ORDER BY ?framework
```

**Top 5 output rows:**

| framework | frameworkLabel |
| --- | --- |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy |
| aplo-r:pedagogicalFramework.Cognitive%20Apprenticeship | Cognitive Apprenticeship |
| aplo-r:pedagogicalFramework.Collaborative%20Learning | Collaborative Learning |
| aplo-r:pedagogicalFramework.Community%20of%20Inquiry | Community of Inquiry |
| aplo-r:pedagogicalFramework.Conceptual%20Change | Conceptual Change |

### CQ-007: Given a selected pedagogical framework, what instructional step should occur first?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?framework ?frameworkLabel ?firstStep ?firstStepLabel WHERE {
  ?framework a aplo-ont:PedagogicalFramework ;
             aplo-ont:hasElement ?firstStep .
  ?firstStep a aplo-ont:FirstPedagogicalElement .
  OPTIONAL { ?framework aplo-ont:hasName ?frameworkLabel . }
  OPTIONAL { ?firstStep aplo-ont:hasName ?firstStepLabel . }
}
ORDER BY ?framework ?firstStep
```

**Top 5 output rows:**

| framework | frameworkLabel | firstStep | firstStepLabel |
| --- | --- | --- | --- |
| aplo-r:pedagogicalFramework.Bloom%27s%20Taxonomy | Bloom's Taxonomy | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember |
| aplo-r:pedagogicalFramework.Cognitive%20Apprenticeship | Cognitive Apprenticeship | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Modeling | Modeling |
| aplo-r:pedagogicalFramework.Collaborative%20Learning | Collaborative Learning | aplo-r:pedagogicalElement.Collaborative%20Learning.Shared%20Problem%20Framing | Shared Problem Framing |
| aplo-r:pedagogicalFramework.Conceptual%20Change | Conceptual Change | aplo-r:pedagogicalElement.Conceptual%20Change.Prior%20Conception%20Elicitation | Prior Conception Elicitation |
| aplo-r:pedagogicalFramework.Experiential%20Learning%20Cycle | Experiential Learning Cycle | aplo-r:pedagogicalElement.Experiential%20Learning%20Cycle.Concrete%20Experience | Concrete Experience |

### CQ-008: Given the current instructional step, what step should occur next?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?currentStep ?currentStepLabel ?nextStep ?nextStepLabel WHERE {
  ?currentStep a aplo-ont:PedagogicalElement ;
               aplo-ont:hasNextPedagogicalElement ?nextStep .
  ?nextStep a aplo-ont:PedagogicalElement .
  OPTIONAL { ?currentStep aplo-ont:hasName ?currentStepLabel . }
  OPTIONAL { ?nextStep aplo-ont:hasName ?nextStepLabel . }

}
ORDER BY ?currentStep ?nextStep
```

**Top 5 output rows:**

| currentStep | currentStepLabel | nextStep | nextStepLabel |
| --- | --- | --- | --- |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Analyze | Analyze | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Evaluate | Evaluate |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Analyze | Analyze |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Evaluate | Evaluate | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Create | Create |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand |
| aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply |

### CQ-009: Which instructional steps support a given learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningObjective ?learningObjectiveLabel ?instructionalStep ?instructionalStepLabel WHERE {
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:alignedWith ?instructionalStep .
  ?instructionalStep a aplo-ont:PedagogicalElement .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?instructionalStep aplo-ont:hasName ?instructionalStepLabel . }
}
ORDER BY ?learningObjective ?instructionalStep
```

**Top 5 output rows:**

| learningObjective | learningObjectiveLabel | instructionalStep | instructionalStepLabel |
| --- | --- | --- | --- |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Coaching | Coaching |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Model%20provenance%20relationships%20with%20PROV-O | Model provenance relationships with PROV-O | aplo-r:pedagogicalElement.Collaborative%20Learning.Joint%20Construction | Joint Construction |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference | aplo-r:pedagogicalElement.Experiential%20Learning%20Cycle.Abstract%20Conceptualization | Abstract Conceptualization |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata | aplo-r:pedagogicalElement.Universal%20Design%20for%20Learning.Representation%20Options | Representation Options |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Model%20observations%20with%20SOSA%20SSN | Model observations with SOSA SSN | aplo-r:pedagogicalElement.Experiential%20Learning%20Cycle.Concrete%20Experience | Concrete Experience |

### CQ-010: Given the selected technique and learner situation, what instructional step should occur next?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?technique ?techniqueLabel ?situation ?situationLabel ?learningObjective ?learningObjectiveLabel ?currentStep ?currentStepLabel ?nextStep ?nextStepLabel WHERE {
  ?strategy a aplo-ont:LearningStrategy ;
            aplo-ont:hasPedagogicalTechnique ?technique ;
            aplo-ont:hasLearningObjective ?learningObjective .
  ?learningObjective aplo-ont:worksOnSituation ?situation ;
                     aplo-ont:alignedWith ?currentStep .
  ?currentStep aplo-ont:hasNextPedagogicalElement ?nextStep .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?currentStep aplo-ont:hasName ?currentStepLabel . }
  OPTIONAL { ?technique aplo-ont:hasName ?techniqueLabel . }
  OPTIONAL { ?situation rdf:value ?situationLabel . }
  OPTIONAL { ?nextStep aplo-ont:hasName ?nextStepLabel . }

}
ORDER BY ?technique ?situation ?currentStep
```

**Top 5 output rows:**

| technique | techniqueLabel | situation | situationLabel | learningObjective | learningObjectiveLabel | currentStep | currentStepLabel | nextStep | nextStepLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:pedagogicalTechnique.Accessibility%20Checkpoint | Accessibility Checkpoint | aplo-r:learningSituation.Secure%20KG%20Implementation%20Training | Secure KG Implementation Training | aplo-r:learningObjective.Secure%20KG%20Implementation%20Training.Explain%20RDF%20star%20statement%20annotations | Explain RDF star statement annotations | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply |
| aplo-r:pedagogicalTechnique.Accessibility%20Checkpoint | Accessibility Checkpoint | aplo-r:learningSituation.User%20Engagement%20KG%20Demonstration%20Planning | User Engagement KG Demonstration Planning | aplo-r:learningObjective.User%20Engagement%20KG%20Demonstration%20Planning.Select%20KG%20visualization%20tools | Select KG visualization tools | aplo-r:pedagogicalElement.Project%20Based%20Learning.Critique%20and%20Revision | Critique and Revision | aplo-r:pedagogicalElement.Project%20Based%20Learning.Public%20Product | Public Product |
| aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Remember | Remember | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand |
| aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Understand | Understand | aplo-r:pedagogicalElement.Bloom%27s%20Taxonomy.Apply | Apply |
| aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Modeling | Modeling | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Coaching | Coaching |

### CQ-011: What are all the available pedagogical techniques?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?technique ?name WHERE {
  ?technique a aplo-ont:PedagogicalTechnique .
  OPTIONAL { ?technique aplo-ont:hasName ?name . }
}
ORDER BY ?technique
```

**Top 5 output rows:**

| technique | name |
| --- | --- |
| aplo-r:pedagogicalTechnique.Accessibility%20Checkpoint | Accessibility Checkpoint |
| aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer |
| aplo-r:pedagogicalTechnique.Alternative%20Demonstration | Alternative Demonstration |
| aplo-r:pedagogicalTechnique.Analogical%20Comparison | Analogical Comparison |
| aplo-r:pedagogicalTechnique.Case%20Based%20Scenario | Case Based Scenario |

### CQ-012: What pedagogical element(s) can help in achieving a learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningObjective ?learningObjectiveLabel ?pedagogicalElement ?pedagogicalElementLabel WHERE {
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:alignedWith ?pedagogicalElement .
  ?pedagogicalElement a aplo-ont:PedagogicalElement .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?pedagogicalElement aplo-ont:hasName ?pedagogicalElementLabel . }
}
ORDER BY ?learningObjective ?pedagogicalElement
```

**Top 5 output rows:**

| learningObjective | learningObjectiveLabel | pedagogicalElement | pedagogicalElementLabel |
| --- | --- | --- | --- |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | aplo-r:pedagogicalElement.Cognitive%20Apprenticeship.Coaching | Coaching |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Model%20provenance%20relationships%20with%20PROV-O | Model provenance relationships with PROV-O | aplo-r:pedagogicalElement.Collaborative%20Learning.Joint%20Construction | Joint Construction |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference | aplo-r:pedagogicalElement.Experiential%20Learning%20Cycle.Abstract%20Conceptualization | Abstract Conceptualization |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata | aplo-r:pedagogicalElement.Universal%20Design%20for%20Learning.Representation%20Options | Representation Options |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Model%20observations%20with%20SOSA%20SSN | Model observations with SOSA SSN | aplo-r:pedagogicalElement.Experiential%20Learning%20Cycle.Concrete%20Experience | Concrete Experience |

### CQ-013: What modules are aligned to a learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningObjective ?learningObjectiveLabel ?module ?moduleLabel WHERE {
  ?module a edu-ont:Module ;
          aplo-ont:hasLearningObjective ?learningObjective .
  ?learningObjective a aplo-ont:LearningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?module rdf:value ?moduleLabel . }
}
ORDER BY ?learningObjective ?module
```

**Top 5 output rows:**

| learningObjective | learningObjectiveLabel | module | moduleLabel |
| --- | --- | --- | --- |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:module.What%20is%20an%20Identifier%3F | What is an Identifier? |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Model%20provenance%20relationships%20with%20PROV-O | Model provenance relationships with PROV-O | edu-r:module.PROV-O | PROV-O |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference | edu-r:module.Rules | Rules |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata | edu-r:module.Open%20Graph%20Protocol | Open Graph Protocol |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Model%20observations%20with%20SOSA%20SSN | Model observations with SOSA SSN | edu-r:module.SOSA%20%26%20SSN | SOSA & SSN |

### CQ-014: What media are aligned to a learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningObjective ?learningObjectiveLabel ?media ?mediaLabel WHERE {
  ?media a edu-ont:Media ;
         aplo-ont:supportsLearningObjective ?learningObjective .
  ?learningObjective a aplo-ont:LearningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?media rdf:value ?mediaLabel . }
}
ORDER BY ?learningObjective ?media
```

**Top 5 output rows:**

| learningObjective | learningObjectiveLabel | media | mediaLabel |
| --- | --- | --- | --- |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:media.What%20is%20an%20Identifier%3F | What is an Identifier? |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Model%20provenance%20relationships%20with%20PROV-O | Model provenance relationships with PROV-O | edu-r:media.PROV-O | PROV-O |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference | edu-r:media.Rules | Rules |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata | edu-r:media.Open%20Graph%20Protocol | Open Graph Protocol |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Model%20observations%20with%20SOSA%20SSN | Model observations with SOSA SSN | edu-r:media.SOSA%20%26%20SSN | SOSA & SSN |

### CQ-015: What learning objectives require prior knowledge of a topic?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningObjective ?learningObjectiveLabel ?topic ?topicLabel WHERE {
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:worksOnSituation ?situation .
  ?situation aplo-ont:requiresTopicKnowledge ?topic .
  ?topic a edu-ont:Topic .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?learningObjective ?topic
```

**Top 5 output rows:**

| learningObjective | learningObjectiveLabel | topic | topicLabel |
| --- | --- | --- | --- |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:topic.Graph | Graph |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:topic.OWL | OWL |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:topic.Ontology | Ontology |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | edu-r:topic.Schema | Schema |

### CQ-016: What learning objectives develop a skill?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningObjective ?learningObjectiveLabel ?skill ?skillLabel WHERE {
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:developsSkill ?skill .
  ?skill a aplo-ont:Skill .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }
}
ORDER BY ?learningObjective ?skill
```

**Top 5 output rows:**

| learningObjective | learningObjectiveLabel | skill | skillLabel |
| --- | --- | --- | --- |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns | aplo-r:skill.Identifier%20Pattern%20Recognition | Identifier Pattern Recognition |
| aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Model%20provenance%20relationships%20with%20PROV-O | Model provenance relationships with PROV-O | aplo-r:skill.Provenance%20Relationship%20Modeling | Provenance Relationship Modeling |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference | aplo-r:skill.Rule%20Based%20Inference%20Explanation | Rule Based Inference Explanation |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata | aplo-r:skill.Open%20Graph%20Metadata%20Mapping | Open Graph Metadata Mapping |
| aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Model%20observations%20with%20SOSA%20SSN | Model observations with SOSA SSN | aplo-r:skill.Observation%20Ontology%20Modeling | Observation Ontology Modeling |

### CQ-017: What learning objectives should be pursued by a learner for a target goal?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?skill ?skillLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?skill .
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:developsSkill ?skill .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }

}
ORDER BY ?learner ?goal ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | skill | skillLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition | aplo-r:learningObjective.Identifier%20Practice%20Session.Identify%20URI%20namespace%20and%20hash%20or%20slash%20patterns | Identify URI namespace and hash or slash patterns |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats |

### CQ-018: What learning objectives should be pursued by a learner for a target skill?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?targetSkill ?targetSkillLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?targetSkill .
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:developsSkill ?targetSkill .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?targetSkill rdf:value ?targetSkillLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }

}
ORDER BY ?learner ?targetSkill ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | targetSkill | targetSkillLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition | aplo-r:learningObjective.Identifier%20Practice%20Session.Identify%20URI%20namespace%20and%20hash%20or%20slash%20patterns | Identify URI namespace and hash or slash patterns |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats |

### CQ-019: What topics require prior knowledge for a learner for their goal?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?learningObjective ?learningObjectiveLabel ?topic ?topicLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?skill .
  ?learningObjective aplo-ont:developsSkill ?skill ;
                     aplo-ont:worksOnSituation ?situation .
  ?situation aplo-ont:requiresTopicKnowledge ?topic .
  ?topic a edu-ont:Topic .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?learner ?goal ?topic
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | learningObjective | learningObjectiveLabel | topic | topicLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:topic.Metadata | Metadata |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:topic.Metadata | Metadata |

### CQ-020: Which pedagogical techniques can be used to support a learner working toward a given learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningObjective ?learningObjectiveLabel ?technique ?techniqueLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective a aplo-ont:LearningObjective ;
                     aplo-ont:worksOnSituation ?situation .
  ?strategy a aplo-ont:LearningStrategy ;
            aplo-ont:hasLearningObjective ?learningObjective ;
            aplo-ont:hasPedagogicalTechnique ?technique .
  ?technique a aplo-ont:PedagogicalTechnique .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?technique aplo-ont:hasName ?techniqueLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?learningObjective ?technique
```

**Top 5 output rows:**

| learner | learnerLabel | learningObjective | learningObjectiveLabel | technique | techniqueLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Concept%20Mapping | Concept Mapping |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Dual%20Coding | Dual Coding |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Retrieval%20Practice | Retrieval Practice |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer |

### CQ-021: What instructional purpose does a selected pedagogical technique serve?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?technique ?techniqueLabel ?pedagogicalObjective ?pedagogicalObjectiveLabel WHERE {
  ?technique a aplo-ont:PedagogicalTechnique ;
             aplo-ont:servesPedagogicalObjective ?pedagogicalObjective .
  ?pedagogicalObjective a aplo-ont:PedagogicalObjective .
  OPTIONAL { ?technique aplo-ont:hasName ?techniqueLabel . }
  OPTIONAL { ?pedagogicalObjective aplo-ont:hasName ?pedagogicalObjectiveLabel . }
}
ORDER BY ?technique ?pedagogicalObjective
```

**Top 5 output rows:**

| technique | techniqueLabel | pedagogicalObjective | pedagogicalObjectiveLabel |
| --- | --- | --- | --- |
| aplo-r:pedagogicalTechnique.Accessibility%20Checkpoint | Accessibility Checkpoint | aplo-r:pedagogicalObjective.Improve%20Inclusive%20Design | Improve Inclusive Design |
| aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer | aplo-r:pedagogicalObjective.Prepare%20Prior%20Knowledge | Prepare Prior Knowledge |
| aplo-r:pedagogicalTechnique.Alternative%20Demonstration | Alternative Demonstration | aplo-r:pedagogicalObjective.Diversify%20Expression | Diversify Expression |
| aplo-r:pedagogicalTechnique.Analogical%20Comparison | Analogical Comparison | aplo-r:pedagogicalObjective.Support%20Transfer | Support Transfer |
| aplo-r:pedagogicalTechnique.Case%20Based%20Scenario | Case Based Scenario | aplo-r:pedagogicalObjective.Contextualize%20Learning | Contextualize Learning |

### CQ-022: What learning objectives are relevant to the learner’s current goal?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?skill .
  ?learningObjective aplo-ont:developsSkill ?skill .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?goal ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:learningObjective.Identifier%20Practice%20Session.Identify%20URI%20namespace%20and%20hash%20or%20slash%20patterns | Identify URI namespace and hash or slash patterns |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats |

### CQ-023: What learning objectives are relevant to the learner’s target skill?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?targetSkill ?targetSkillLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?targetSkill .
  ?learningObjective aplo-ont:developsSkill ?targetSkill .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?targetSkill rdf:value ?targetSkillLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?targetSkill ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | targetSkill | targetSkillLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition | aplo-r:learningObjective.Identifier%20Practice%20Session.Identify%20URI%20namespace%20and%20hash%20or%20slash%20patterns | Identify URI namespace and hash or slash patterns |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats |

### CQ-024: What prior topic knowledge is needed before the learner attempts a learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningObjective ?learningObjectiveLabel ?topic ?topicLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?situation aplo-ont:requiresTopicKnowledge ?topic .
  ?topic a edu-ont:Topic .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?learner ?learningObjective ?topic
```

**Top 5 output rows:**

| learner | learnerLabel | learningObjective | learningObjectiveLabel | topic | topicLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:topic.Metadata | Metadata |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:topic.Metadata | Metadata |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:topic.Knowledge%20Graph | Knowledge Graph |

### CQ-025: Which learning strategy is appropriate for a learner working toward a given objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningObjective ?learningObjectiveLabel ?strategy ?strategyLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?strategy a aplo-ont:LearningStrategy ;
            aplo-ont:hasLearningObjective ?learningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?strategy aplo-ont:hasName ?strategyLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?learningObjective ?strategy
```

**Top 5 output rows:**

| learner | learnerLabel | learningObjective | learningObjectiveLabel | strategy | strategyLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats | aplo-r:learningStrategy.RDF%20Practice%20Session.Schema%20Reasoning%20Strategy | Schema Reasoning Strategy |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningObjective.RDF%20Practice%20Session.Interpret%20RDF%20triple%20components | Interpret RDF triple components | aplo-r:learningStrategy.RDF%20Practice%20Session.Identifier%20and%20RDF%20Practice%20Strategy | Identifier and RDF Practice Strategy |

### CQ-026: Which pedagogical techniques are used by that learning strategy?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?strategy ?strategyLabel ?technique ?techniqueLabel WHERE {
  ?strategy a aplo-ont:LearningStrategy ;
            aplo-ont:hasPedagogicalTechnique ?technique .
  ?technique a aplo-ont:PedagogicalTechnique .
  OPTIONAL { ?technique aplo-ont:hasName ?techniqueLabel . }
  OPTIONAL { ?strategy aplo-ont:hasName ?strategyLabel . }
}
ORDER BY ?strategy ?technique
```

**Top 5 output rows:**

| strategy | strategyLabel | technique | techniqueLabel |
| --- | --- | --- | --- |
| aplo-r:learningStrategy.Collaborative%20KG%20Delivery%20Planning.Collaborative%20KG%20Implementation%20Strategy | Collaborative KG Implementation Strategy | aplo-r:pedagogicalTechnique.Collaborative%20Annotation | Collaborative Annotation |
| aplo-r:learningStrategy.Collaborative%20KG%20Delivery%20Planning.Collaborative%20KG%20Implementation%20Strategy | Collaborative KG Implementation Strategy | aplo-r:pedagogicalTechnique.Group%20Synthesis | Group Synthesis |
| aplo-r:learningStrategy.Collaborative%20KG%20Delivery%20Planning.Collaborative%20KG%20Implementation%20Strategy | Collaborative KG Implementation Strategy | aplo-r:pedagogicalTechnique.Jigsaw%20Activity | Jigsaw Activity |
| aplo-r:learningStrategy.Collaborative%20KG%20Delivery%20Planning.Collaborative%20KG%20Implementation%20Strategy | Collaborative KG Implementation Strategy | aplo-r:pedagogicalTechnique.Peer%20Review%20Protocol | Peer Review Protocol |
| aplo-r:learningStrategy.Consulting%20KG%20Opportunity%20Review.Consulting%20KG%20Value%20Strategy | Consulting KG Value Strategy | aplo-r:pedagogicalTechnique.Case%20Based%20Scenario | Case Based Scenario |

### CQ-027: Which modules support the learning objective selected for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningObjective ?learningObjectiveLabel ?module ?moduleLabel WHERE {
  ?learner aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?module a edu-ont:Module ;
          aplo-ont:hasLearningObjective ?learningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?module rdf:value ?moduleLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?learningObjective ?module
```

**Top 5 output rows:**

| learner | learnerLabel | learningObjective | learningObjectiveLabel | module | moduleLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:module.What%20is%20an%20Ontology%3F | What is an Ontology? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats | edu-r:module.RDF%20Serializations | RDF Serializations |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningObjective.RDF%20Practice%20Session.Interpret%20RDF%20triple%20components | Interpret RDF triple components | edu-r:module.RDF | RDF |

### CQ-028: Which media resources support the learning objective selected for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningObjective ?learningObjectiveLabel ?media ?mediaLabel WHERE {
  ?learner aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?media a edu-ont:Media ;
         aplo-ont:supportsLearningObjective ?learningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?media rdf:value ?mediaLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?learningObjective ?media
```

**Top 5 output rows:**

| learner | learnerLabel | learningObjective | learningObjectiveLabel | media | mediaLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:media.What%20is%20an%20Ontology%3F | What is an Ontology? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats | edu-r:media.RDF%20Serializations | RDF Serializations |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningObjective.RDF%20Practice%20Session.Interpret%20RDF%20triple%20components | Interpret RDF triple components | edu-r:media.RDF | RDF |

### CQ-029: Given the learner’s goal, current awareness, preferences, and challenges, what learning objective should be pursued next?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?currentAwareness ?currentAwarenessLabel ?awarenessLevel ?awarenessLevelLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal ;
           aplo-ont:hasAwarenessObservation ?currentAwareness ;
           aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge .
  ?currentAwareness aplo-ont:hasAwarenessLevel ?awarenessLevel ;
                    aplo-ont:onSkill ?skill .
  ?goal aplo-ont:targetsSkill ?skill .
  ?learningObjective aplo-ont:developsSkill ?skill .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?currentAwareness rdf:value ?currentAwarenessLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }

}
ORDER BY ?learner ?goal ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | currentAwareness | currentAwarenessLabel | awarenessLevel | awarenessLevelLabel | preference | preferenceLabel | challenge | challengeLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | AwarenessObservation | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | AwarenessObservation | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | AwarenessObservation | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |

### CQ-030: Given the learner’s current awareness and selected learning objective, what pedagogical technique is appropriate?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?learningObjective ?learningObjectiveLabel ?strategy ?strategyLabel ?technique ?techniqueLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onSkill ?skill .
  ?learningObjective aplo-ont:developsSkill ?skill .
  ?strategy aplo-ont:hasLearningObjective ?learningObjective ;
            aplo-ont:hasPedagogicalTechnique ?technique .
  ?technique a aplo-ont:PedagogicalTechnique .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?technique aplo-ont:hasName ?techniqueLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?strategy aplo-ont:hasName ?strategyLabel . }

}
ORDER BY ?learner ?learningObjective ?technique
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | learningObjective | learningObjectiveLabel | strategy | strategyLabel | technique | techniqueLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy | aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy | aplo-r:pedagogicalTechnique.Concept%20Mapping | Concept Mapping |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy | aplo-r:pedagogicalTechnique.Dual%20Coding | Dual Coding |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy | aplo-r:pedagogicalTechnique.Retrieval%20Practice | Retrieval Practice |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy | aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer |

### CQ-031: What information supports the system’s selection of a learning objective, pedagogical technique, resource, or feedback response?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?awarenessObservation ?awarenessObservationLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?learningObjective ?learningObjectiveLabel ?technique ?techniqueLabel ?module ?moduleLabel ?media ?mediaLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal ;
           aplo-ont:hasAwarenessObservation ?awarenessObservation ;
           aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge .
  ?awarenessObservation aplo-ont:onSkill ?skill .
  ?learningObjective aplo-ont:developsSkill ?skill .
  OPTIONAL { ?strategy aplo-ont:hasLearningObjective ?learningObjective ; aplo-ont:hasPedagogicalTechnique ?technique . }
  OPTIONAL { ?module a edu-ont:Module ; aplo-ont:hasLearningObjective ?learningObjective . }
  OPTIONAL { ?media a edu-ont:Media ; aplo-ont:supportsLearningObjective ?learningObjective . }
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?technique aplo-ont:hasName ?techniqueLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?module rdf:value ?moduleLabel . }
  OPTIONAL { ?media rdf:value ?mediaLabel . }
}
ORDER BY ?learner ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | awarenessObservation | awarenessObservationLabel | preference | preferenceLabel | challenge | challengeLabel | learningObjective | learningObjectiveLabel | technique | techniqueLabel | module | moduleLabel | media | mediaLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Concept%20Mapping | Concept Mapping | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Dual%20Coding | Dual Coding | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Retrieval%20Practice | Retrieval Practice | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:pedagogicalTechnique.Advance%20Organizer | Advance Organizer | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-032: What learning objectives does an assessment exercise evaluate?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?assessmentExercise ?assessmentExerciseLabel ?evaluationTechnique ?evaluationTechniqueLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?assessmentExercise a aplo-ont:EvaluationAssessmentExercise ;
                      aplo-ont:usesTechnique ?evaluationTechnique .
  ?evaluationTechnique aplo-ont:assessesLearningObjective ?learningObjective .
  ?learningObjective a aplo-ont:LearningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }

}
ORDER BY ?assessmentExercise ?learningObjective
```

**Top 5 output rows:**

| assessmentExercise | assessmentExerciseLabel | evaluationTechnique | evaluationTechniqueLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata |

### CQ-033: What learning objectives are assessed by an evaluation technique?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationTechnique ?evaluationTechniqueLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?evaluationTechnique a aplo-ont:EvaluationTechnique ;
                       aplo-ont:assessesLearningObjective ?learningObjective .
  ?learningObjective a aplo-ont:LearningObjective .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
}
ORDER BY ?evaluationTechnique ?learningObjective
```

**Top 5 output rows:**

| evaluationTechnique | evaluationTechniqueLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Collaborative%20KG%20Delivery%20Planning.Identify%20identifier%20patterns | Identify identifier patterns |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Explain%20rule%20based%20inference | Explain rule based inference |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Consulting%20KG%20Opportunity%20Review.Map%20Open%20Graph%20metadata | Map Open Graph metadata |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Data%20Analysis%20KG%20Modeling%20Practice.Compare%20open%20and%20closed%20world%20assumptions | Compare open and closed world assumptions |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningObjective.Data%20Analysis%20KG%20Modeling%20Practice.Interpret%20Datalog%20rules | Interpret Datalog rules |

### CQ-034: What evaluation metrics are used by an evaluation technique?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationTechnique ?evaluationTechniqueLabel ?metric ?metricLabel WHERE {
  ?evaluationTechnique a aplo-ont:EvaluationTechnique ;
                       aplo-ont:hasEvaluationMetric ?metric .
  ?metric a aplo-ont:EvaluationMetric .
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
  OPTIONAL { ?metric rdf:value ?metricLabel . }
}
ORDER BY ?evaluationTechnique ?metric
```

**Top 5 output rows:**

| evaluationTechnique | evaluationTechniqueLabel | metric | metricLabel |
| --- | --- | --- | --- |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationMetric.Correctness%20Flag | Correctness Flag |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationMetric.Score%20Percent | Score Percent |
| aplo-r:evaluationTechnique.Mastery%20Reassessment | Mastery Reassessment | aplo-r:evaluationMetric.Rubric%20Level | Rubric Level |
| aplo-r:evaluationTechnique.Mastery%20Reassessment | Mastery Reassessment | aplo-r:evaluationMetric.Score%20Percent | Score Percent |
| aplo-r:evaluationTechnique.Ontology%20Modeling%20Review | Ontology Modeling Review | aplo-r:evaluationMetric.Confidence%20Rating | Confidence Rating |

### CQ-035: What evaluation technique type does an evaluation technique belong to?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationTechnique ?evaluationTechniqueLabel ?techniqueType ?techniqueTypeLabel WHERE {
  ?evaluationTechnique a aplo-ont:EvaluationTechnique ;
                       aplo-ont:hasEvaluationTechniqueType ?techniqueType .
  ?techniqueType a aplo-ont:EvaluationTechniqueType .
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
  OPTIONAL { ?techniqueType rdf:value ?techniqueTypeLabel . }

}
ORDER BY ?evaluationTechnique ?techniqueType
```

**Top 5 output rows:**

| evaluationTechnique | evaluationTechniqueLabel | techniqueType | techniqueTypeLabel |
| --- | --- | --- | --- |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationTechniqueType.Automated | Automated |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationTechniqueType.Formative | Formative |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationTechniqueType.Low%20Stakes | Low Stakes |
| aplo-r:evaluationTechnique.Mastery%20Reassessment | Mastery Reassessment | aplo-r:evaluationTechniqueType.Automated | Automated |
| aplo-r:evaluationTechnique.Mastery%20Reassessment | Mastery Reassessment | aplo-r:evaluationTechniqueType.Summative | Summative |

### CQ-036: What are the available assessment exercises that use a given evaluation technique?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationTechnique ?evaluationTechniqueLabel ?assessmentExercise ?assessmentExerciseLabel WHERE {
  ?assessmentExercise a aplo-ont:EvaluationAssessmentExercise ;
                      aplo-ont:usesTechnique ?evaluationTechnique .
  ?evaluationTechnique a aplo-ont:EvaluationTechnique .
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
}
ORDER BY ?evaluationTechnique ?assessmentExercise
```

**Top 5 output rows:**

| evaluationTechnique | evaluationTechniqueLabel | assessmentExercise | assessmentExerciseLabel |
| --- | --- | --- | --- |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Dublin%20Core.Dublin%20Core%20Metadata%20Mapping%20Task | Dublin Core |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Dublin%20Core.Dublin%20Core%20Metadata%20Mapping%20Task | Dublin Core Metadata Mapping Task |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.History%20of%20the%20Semantic%20Web.Semantic%20Web%20Timeline%20Explanation | History of the Semantic Web |

### CQ-037: What modules contain assessment exercises?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?module ?moduleLabel ?assessmentExercise ?assessmentExerciseLabel WHERE {
  ?module a edu-ont:Module ;
          aplo-ont:hasAssessmentExercise ?assessmentExercise .
  ?assessmentExercise a aplo-ont:EvaluationAssessmentExercise .
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?module rdf:value ?moduleLabel . }
}
ORDER BY ?module ?assessmentExercise
```

**Top 5 output rows:**

| module | moduleLabel | assessmentExercise | assessmentExerciseLabel |
| --- | --- | --- | --- |
| edu-r:module.Datalog | Datalog | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog |
| edu-r:module.Datalog | Datalog | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace |
| edu-r:module.Deploying%20a%20Knowledge%20Graph | Deploying a Knowledge Graph | aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | Deploying a Knowledge Graph |
| edu-r:module.Deploying%20a%20Knowledge%20Graph | Deploying a Knowledge Graph | aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | KG Deployment Readiness Review |
| edu-r:module.Description%20Logic | Description Logic | aplo-r:evaluationAssessmentExercise.Description%20Logic.Description%20Logic%20Constraint%20Review | Description Logic |

### CQ-038: What media resources contain assessment exercises?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?media ?mediaLabel ?assessmentExercise ?assessmentExerciseLabel WHERE {
  ?media a edu-ont:Media ;
         aplo-ont:hasAssessmentExercise ?assessmentExercise .
  ?assessmentExercise a aplo-ont:EvaluationAssessmentExercise .
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?media rdf:value ?mediaLabel . }
}
ORDER BY ?media ?assessmentExercise
```

**Top 5 output rows:**

| media | mediaLabel | assessmentExercise | assessmentExerciseLabel |
| --- | --- | --- | --- |
| edu-r:media.Datalog | Datalog | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog |
| edu-r:media.Datalog | Datalog | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace |
| edu-r:media.Deploying%20a%20Knowledge%20Graph | Deploying a Knowledge Graph | aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | Deploying a Knowledge Graph |
| edu-r:media.Deploying%20a%20Knowledge%20Graph | Deploying a Knowledge Graph | aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | KG Deployment Readiness Review |
| edu-r:media.Description%20Logic | Description Logic | aplo-r:evaluationAssessmentExercise.Description%20Logic.Description%20Logic%20Constraint%20Review | Description Logic |

### CQ-039: What topics are evaluated by an assessment exercise?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?assessmentExercise ?assessmentExerciseLabel ?topic ?topicLabel WHERE {
  ?assessmentExercise a aplo-ont:EvaluationAssessmentExercise ;
                      aplo-ont:evaluatesTopicAwarenessOf ?topic .
  ?topic a edu-ont:Topic .
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?assessmentExercise ?topic
```

**Top 5 output rows:**

| assessmentExercise | assessmentExerciseLabel | topic | topicLabel |
| --- | --- | --- | --- |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog | edu-r:topic.Inference | Inference |
| aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace | edu-r:topic.Inference | Inference |
| aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | Deploying a Knowledge Graph | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | KG Deployment Readiness Review | edu-r:topic.Knowledge%20Graph | Knowledge Graph |
| aplo-r:evaluationAssessmentExercise.Description%20Logic.Description%20Logic%20Constraint%20Review | Description Logic | edu-r:topic.Expressivity | Expressivity |

### CQ-040: What evaluation result(s) contribute to a learner awareness observation?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationResult ?evaluationResultLabel ?awarenessObservation ?awarenessObservationLabel ?value ?metric ?metricLabel WHERE {
  ?evaluationResult a aplo-ont:EvaluationResult ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  ?awarenessObservation a aplo-ont:AwarenessObservation .
  OPTIONAL { ?evaluationResult aplo-ont:hasValue ?value . }
  OPTIONAL { ?evaluationResult aplo-ont:hasUnit ?metric . }
  OPTIONAL { ?metric rdf:value ?metricLabel . }
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
}
ORDER BY ?awarenessObservation ?evaluationResult
```

**Top 5 output rows:**

| evaluationResult | evaluationResultLabel | awarenessObservation | awarenessObservationLabel | value | metric | metricLabel |
| --- | --- | --- | --- | --- | --- | --- |
| aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | 88 | aplo-r:evaluationMetric.Score%20Percent | Score Percent |
| aplo-r:evaluationResult.Learner%20Blair.Learning%20Platform.SPARQL%20Query%20Practice%20Score | SPARQL Query Practice Score | aplo-r:awarenessObservation.Learner%20Blair.Query.SPARQL%20Query%20Construction.SPARQL%20Awareness%20After%20Practice | SPARQL Awareness After Practice | 82 | aplo-r:evaluationMetric.Score%20Percent | Score Percent |
| aplo-r:evaluationResult.Learner%20Blair.Learning%20Platform.RDF%20Triple%20Quiz%20Score | RDF Triple Quiz Score | aplo-r:awarenessObservation.Learner%20Blair.Triple.RDF%20Triple%20Interpretation.RDF%20Triple%20Awareness%20After%20Quiz | RDF Triple Awareness After Quiz | 76 | aplo-r:evaluationMetric.Score%20Percent | Score Percent |
| aplo-r:evaluationResult.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Plan%20Evidence%20Rating | Knowledge Engineering Workflow Plan Evidence Rating | aplo-r:awarenessObservation.Learner%20Cameron.Knowledge%20Graph.Knowledge%20Engineering%20Workflow%20Planning.Knowledge%20Engineering%20Workflow%20Planning%20Application%20Snapshot | Knowledge Engineering Workflow Planning Application Snapshot | 83 | aplo-r:evaluationMetric.Score%20Percent | Score Percent |
| aplo-r:evaluationResult.Learner%20Cameron.Learning%20Platform.Set%20Relationship%20Diagram%20Task%20Checkpoint%20Score | Set Relationship Diagram Task Checkpoint Score | aplo-r:awarenessObservation.Learner%20Cameron.Union.Set%20Relationship%20Reasoning.Set%20Relationship%20Reasoning%20Practice%20Update | Set Relationship Reasoning Practice Update | 68 | aplo-r:evaluationMetric.Score%20Percent | Score Percent |

### CQ-041: What assessment exercises can be used to evaluate the learner’s progress toward a learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningObjective ?learningObjectiveLabel ?evaluationTechnique ?evaluationTechniqueLabel ?assessmentExercise ?assessmentExerciseLabel WHERE {
  ?learner aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?evaluationTechnique aplo-ont:assessesLearningObjective ?learningObjective .
  ?assessmentExercise aplo-ont:usesTechnique ?evaluationTechnique .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }

}
ORDER BY ?learner ?learningObjective ?assessmentExercise
```

**Top 5 output rows:**

| learner | learnerLabel | learningObjective | learningObjectiveLabel | evaluationTechnique | evaluationTechniqueLabel | assessmentExercise | assessmentExerciseLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Datalog.Datalog%20Rule%20Trace | Datalog Rule Trace |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Dublin%20Core.Dublin%20Core%20Metadata%20Mapping%20Task | Dublin Core |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.Dublin%20Core.Dublin%20Core%20Metadata%20Mapping%20Task | Dublin Core Metadata Mapping Task |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:evaluationAssessmentExercise.History%20of%20the%20Semantic%20Web.Semantic%20Web%20Timeline%20Explanation | History of the Semantic Web |

### CQ-042: What assessment exercises evaluate the topic or skill currently being learned?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?topic ?topicLabel ?skill ?skillLabel ?assessmentExercise ?assessmentExerciseLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onTopic ?topic ;
                        aplo-ont:onSkill ?skill .
  ?assessmentExercise aplo-ont:evaluatesTopicAwarenessOf ?topic .
  OPTIONAL { ?assessmentExercise rdf:value ?assessmentExerciseLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }
}
ORDER BY ?learner ?topic ?assessmentExercise
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | topic | topicLabel | skill | skillLabel | assessmentExercise | assessmentExerciseLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | Deploying a Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:evaluationAssessmentExercise.Deploying%20a%20Knowledge%20Graph.KG%20Deployment%20Readiness%20Review | KG Deployment Readiness Review |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:evaluationAssessmentExercise.Introduction%20to%20Knowledge%20Engineering.Knowledge%20Engineering%20Workflow%20Plan | Introduction to Knowledge Engineering |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:evaluationAssessmentExercise.Introduction%20to%20Knowledge%20Engineering.Knowledge%20Engineering%20Workflow%20Plan | Knowledge Engineering Workflow Plan |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:evaluationAssessmentExercise.Survey%20of%20Visualization%20Tools.Visualization%20Tool%20Selection%20Brief | Survey of Visualization Tools |

### CQ-043: What evaluation method was used to assess the learner’s progress?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?evaluationResult ?evaluationResultLabel ?evaluationTechnique ?evaluationTechniqueLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?evaluationResult a aplo-ont:EvaluationResult ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  ?evaluationTechnique aplo-ont:hasEvaluationMetric ?metric .
  ?evaluationResult aplo-ont:hasUnit ?metric .
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
}
ORDER BY ?learner ?awarenessObservation ?evaluationTechnique
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | evaluationResult | evaluationResultLabel | evaluationTechnique | evaluationTechniqueLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationTechnique.Mastery%20Reassessment | Mastery Reassessment |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationTechnique.Query%20Practice%20Check | Query Practice Check |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationTechnique.Short%20Explanation%20Rubric | Short Explanation Rubric |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationTechnique.Triple%20Interpretation%20Quiz | Triple Interpretation Quiz |

### CQ-044: What evaluation evidence is available for deciding whether the learner should continue, review, or receive feedback?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?evaluationResult ?evaluationResultLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL { ?evaluationResult a aplo-ont:EvaluationResult ; aplo-ont:affectsAwarenessObservation ?awarenessObservation . }
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
}
ORDER BY ?learner ?awarenessObservation
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | evaluationResult | evaluationResultLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Mastery%20Awareness | Mastery Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Proficient%20Awareness | Proficient Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |

### CQ-045: What metric was used to interpret the assessment result?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationResult ?evaluationResultLabel ?metric ?metricLabel ?value WHERE {
  ?evaluationResult a aplo-ont:EvaluationResult ;
                    aplo-ont:hasUnit ?metric .
  ?metric a aplo-ont:EvaluationMetric .
  OPTIONAL { ?evaluationResult aplo-ont:hasValue ?value . }
  OPTIONAL { ?metric rdf:value ?metricLabel . }
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
}
ORDER BY ?evaluationResult ?metric
```

**Top 5 output rows:**

| evaluationResult | evaluationResultLabel | metric | metricLabel | value |
| --- | --- | --- | --- | --- |
| aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | 88 |
| aplo-r:evaluationResult.Learner%20Blair.Learning%20Platform.RDF%20Triple%20Quiz%20Score | RDF Triple Quiz Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | 76 |
| aplo-r:evaluationResult.Learner%20Blair.Learning%20Platform.SPARQL%20Query%20Practice%20Score | SPARQL Query Practice Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | 82 |
| aplo-r:evaluationResult.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Plan%20Evidence%20Rating | Knowledge Engineering Workflow Plan Evidence Rating | aplo-r:evaluationMetric.Score%20Percent | Score Percent | 83 |
| aplo-r:evaluationResult.Learner%20Cameron.Learning%20Platform.Set%20Relationship%20Diagram%20Task%20Checkpoint%20Score | Set Relationship Diagram Task Checkpoint Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | 68 |

### CQ-046: What assessment results indicate low awareness or difficulty for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?evaluationResult ?evaluationResultLabel ?value WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:hasAwarenessLevel ?awarenessLevel .
  ?evaluationResult a aplo-ont:EvaluationResult ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  OPTIONAL { ?evaluationResult aplo-ont:hasValue ?value . }
  FILTER(CONTAINS(LCASE(STR(?awarenessLevel)), "low") || (BOUND(?value) && xsd:decimal(?value) <= 70))
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
}
ORDER BY ?learner ?awarenessObservation
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | evaluationResult | evaluationResultLabel | value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:awarenessObservation.Learner%20Cameron.Union.Set%20Relationship%20Reasoning.Set%20Relationship%20Reasoning%20Practice%20Update | Set Relationship Reasoning Practice Update | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness | aplo-r:evaluationResult.Learner%20Cameron.Learning%20Platform.Set%20Relationship%20Diagram%20Task%20Checkpoint%20Score | Set Relationship Diagram Task Checkpoint Score | 68 |
| aplo-r:learner.Learner%20Casey | Learner Casey | aplo-r:awarenessObservation.Learner%20Casey.OWL.OWL%20Axiom%20Analysis.OWL%20Modeling%20Awareness%20After%20Review | OWL Modeling Awareness After Review | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness | aplo-r:evaluationResult.Learner%20Casey.Instructor%20Reviewer.OWL%20Modeling%20Review%20Rubric%20Result | OWL Modeling Review Rubric Result | 2 |
| aplo-r:learner.Learner%20Casey | Learner Casey | aplo-r:awarenessObservation.Learner%20Casey.Schema.RDFS%20Schema%20Reasoning.RDFS%20Schema%20Awareness%20After%20Review | RDFS Schema Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:evaluationResult.Learner%20Casey.Instructor%20Reviewer.RDFS%20Schema%20Rubric%20Result | RDFS Schema Rubric Result | 3 |
| aplo-r:learner.Learner%20Connie | Learner Connie | aplo-r:awarenessObservation.Learner%20Connie.Conjunction.Propositional%20Statement%20Reasoning.Propositional%20Statement%20Reasoning%20Revision%20State | Propositional Statement Reasoning Revision State | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness | aplo-r:evaluationResult.Learner%20Connie.Learning%20Platform.Proposition%20Truth%20Table%20Task%20Review%20Result | Proposition Truth Table Task Review Result | 66 |
| aplo-r:learner.Learner%20Connie | Learner Connie | aplo-r:awarenessObservation.Learner%20Connie.Ontology.Modular%20Ontology%20Design.Modular%20Ontology%20Design%20Revision%20State | Modular Ontology Design Revision State | aplo-r:awarenessLevel.Proficient%20Awareness | Proficient Awareness | aplo-r:evaluationResult.Learner%20Connie.Instructor%20Reviewer.Modular%20Ontology%20Boundary%20Review%20Review%20Result | Modular Ontology Boundary Review Review Result | 3 |

### CQ-047: Given assessment evidence and feedback history, should the learner continue, review, or receive additional support?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?evaluationResult ?evaluationResultLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL {
    ?evaluationResult a aplo-ont:EvaluationResult ;
                      aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  }
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
}
ORDER BY ?learner ?awarenessObservation
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | evaluationResult | evaluationResultLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Mastery%20Awareness | Mastery Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Proficient%20Awareness | Proficient Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |

### CQ-048: What learning feedback was given from an evaluation technique?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?evaluationTechnique ?evaluationTechniqueLabel ?learningFeedback ?learningFeedbackLabel WHERE {
  ?evaluationTechnique a aplo-ont:EvaluationTechnique ;
                       aplo-ont:assessesLearningFeedback ?learningFeedback .
  ?learningFeedback a aplo-ont:LearningFeedback .
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
}
ORDER BY ?evaluationTechnique ?learningFeedback
```

**Top 5 output rows:**

| evaluationTechnique | evaluationTechniqueLabel | learningFeedback | learningFeedbackLabel |
| --- | --- | --- | --- |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningFeedback.Learner%20Cameron.Learning%20Platform.Set%20Relationship%20Reasoning%20Coaching%20Note | Set Relationship Reasoning Coaching Note |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningFeedback.Learner%20Carla.Learning%20Platform.Identifier%20Pattern%20Recognition%20Practice%20Cue | Identifier Pattern Recognition Practice Cue |
| aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check | aplo-r:learningFeedback.Learner%20Chris.Learning%20Platform.Open%20Graph%20Metadata%20Mapping%20Next%20Step%20Note | Open Graph Metadata Mapping Next Step Note |

### CQ-049: What types of learning feedback are available/retrieved?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?feedbackType ?feedbackTypeLabel WHERE {
  ?feedbackType a aplo-ont:LearningFeedbackType .
  OPTIONAL { ?feedbackType rdf:value ?feedbackTypeLabel . }

}
ORDER BY ?feedbackType
```

**Top 5 output rows:**

| feedbackType | feedbackTypeLabel |
| --- | --- |
| aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learningFeedbackType.Motivational%20Feedback | Motivational Feedback |
| aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |

### CQ-050: When is the feedback delivered?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningFeedback ?learningFeedbackLabel ?timeNode ?timeNodeLabel ?timeValue WHERE {
  ?learningFeedback a aplo-ont:LearningFeedback ;
                    aplo-ont:hasResponseTime ?timeNode .
  OPTIONAL { ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?timeNode rdf:value ?timeValue . }
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
}
ORDER BY ?learningFeedback ?timeValue
```

**Top 5 output rows:**

| learningFeedback | learningFeedbackLabel | timeNode | timeValue |
| --- | --- | --- | --- |
| aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns | aplo-r:temporalExtent.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns.2026-01-15T10%3A09%3A00Z | 2026-01-15T10:09:00+00:00 |
| aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern | Corrective Feedback on SPARQL Pattern | aplo-r:temporalExtent.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern.2026-01-19T13%3A22%3A00Z | 2026-01-19T13:22:00+00:00 |
| aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components | Corrective Feedback on Triple Components | aplo-r:temporalExtent.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components.2026-01-17T11%3A16%3A00Z | 2026-01-17T11:16:00+00:00 |
| aplo-r:learningFeedback.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Planning%20Extension%20Prompt | Knowledge Engineering Workflow Planning Extension Prompt | aplo-r:temporalExtent.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Planning%20Extension%20Prompt.2026-03-04T14%3A07%3A00Z | 2026-03-04T14:07:00+00:00 |

### CQ-051: When is the response delivered?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?response ?responseLabel ?timeNode ?timeNodeLabel ?timeValue WHERE {
  ?response a aplo-ont:Response ;
            aplo-ont:hasResponseTime ?timeNode .
  OPTIONAL { ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?timeNode rdf:value ?timeValue . }
  OPTIONAL { ?response rdf:value ?responseLabel . }
}
ORDER BY ?response ?timeValue
```

**Top 5 output rows:**

| response | responseLabel | timeNode | timeValue |
| --- | --- | --- | --- |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Ontology Explanation Response | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Your explanation identifies classes and properties; revise it to mention axioms and shared semantics | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Connect ontology components to the purpose of shared machine-interpretable meaning | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:response.Learner%20Alex.Learner%20Alex.Learner%20Ontology%20Explanation | An ontology defines the concepts and relationships for a domain so data can be interpreted consistently | aplo-r:temporalExtent.Learner%20Alex.Learner%20Alex.Learner%20Ontology%20Explanation.2026-01-16T14%3A00%3A00Z%20to%202026-01-16T14%3A25%3A00Z | ISO 8601 UTC |

### CQ-052: What feedbacks are corrective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningFeedback ?learningFeedbackLabel ?feedbackType ?feedbackTypeLabel WHERE {
  ?learningFeedback a aplo-ont:LearningFeedback ;
                    aplo-ont:hasLearningFeedbackType ?feedbackType .
  FILTER(CONTAINS(LCASE(STR(?feedbackType)), "corrective"))
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
  OPTIONAL { ?feedbackType rdf:value ?feedbackTypeLabel . }

}
ORDER BY ?learningFeedback
```

**Top 5 output rows:**

| learningFeedback | learningFeedbackLabel | feedbackType | feedbackTypeLabel |
| --- | --- | --- | --- |
| aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern | Corrective Feedback on SPARQL Pattern | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components | Corrective Feedback on Triple Components | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learningFeedback.Learner%20Cameron.Learning%20Platform.Set%20Relationship%20Reasoning%20Coaching%20Note | Set Relationship Reasoning Coaching Note | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learningFeedback.Learner%20Connie.Instructor%20Reviewer.Knowledge%20Graph%20Documentation%20Planning%20Coaching%20Note | Knowledge Graph Documentation Planning Coaching Note | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |

### CQ-053: What feedbacks are motivational?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learningFeedback ?learningFeedbackLabel ?feedbackType ?feedbackTypeLabel WHERE {
  ?learningFeedback a aplo-ont:LearningFeedback ;
                    aplo-ont:hasLearningFeedbackType ?feedbackType .
  FILTER(CONTAINS(LCASE(STR(?feedbackType)), "motivational"))
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
  OPTIONAL { ?feedbackType rdf:value ?feedbackTypeLabel . }

}
ORDER BY ?learningFeedback
```

**Top 5 output rows:**

| learningFeedback | learningFeedbackLabel | feedbackType | feedbackTypeLabel |
| --- | --- | --- | --- |
| aplo-r:learningFeedback.Learner%20Casey.Learning%20Platform.Mastery%20Feedback%20on%20RDF%20RDFS%20Basics | Mastery Feedback on RDF RDFS Basics | aplo-r:learningFeedbackType.Motivational%20Feedback | Motivational Feedback |
| aplo-r:learningFeedback.Learner%20Chris.Learning%20Platform.Rule%20Based%20Inference%20Explanation%20Revision%20Guidance | Rule Based Inference Explanation Revision Guidance | aplo-r:learningFeedbackType.Motivational%20Feedback | Motivational Feedback |
| aplo-r:learningFeedback.Learner%20Connie.Instructor%20Reviewer.Modular%20Ontology%20Design%20Next%20Step%20Note | Modular Ontology Design Next Step Note | aplo-r:learningFeedbackType.Motivational%20Feedback | Motivational Feedback |
| aplo-r:learningFeedback.Learner%20Connie.Instructor%20Reviewer.Ontology%20Tool%20Selection%20Review%20Comment | Ontology Tool Selection Review Comment | aplo-r:learningFeedbackType.Motivational%20Feedback | Motivational Feedback |
| aplo-r:learningFeedback.Learner%20Connie.Learning%20Platform.Schema.org%20Vocabulary%20Alignment%20Extension%20Prompt | Schema.org Vocabulary Alignment Extension Prompt | aplo-r:learningFeedbackType.Motivational%20Feedback | Motivational Feedback |

### CQ-054: What responses originated from a human?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?response ?responseLabel ?source ?sourceLabel WHERE {
  ?response a aplo-ont:Response ;
            aplo-ont:hasSource ?source .
  ?source a aplo-ont:Source .
  FILTER(CONTAINS(LCASE(STR(?source)), "human") || CONTAINS(LCASE(STR(?source)), "teacher") || CONTAINS(LCASE(STR(?source)), "instructor"))
  OPTIONAL { ?source rdf:value ?sourceLabel . }
  OPTIONAL { ?response rdf:value ?responseLabel . }
}
ORDER BY ?response
```

**Top 5 output rows:**

| response | responseLabel | source | sourceLabel |
| --- | --- | --- | --- |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Ontology Explanation Response | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Your explanation identifies classes and properties; revise it to mention axioms and shared semantics | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Connect ontology components to the purpose of shared machine-interpretable meaning | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Plan%20Evidence%20Rating | Knowledge Engineering Workflow Plan Evidence Rating | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |

### CQ-055: What feedback should be given based on the learner’s assessment evidence?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?evaluationResult ?evaluationResultLabel ?learningFeedback ?learningFeedbackLabel ?feedbackType ?feedbackTypeLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  OPTIONAL {
    ?evaluationResult a aplo-ont:EvaluationResult ;
                      aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  }
  ?learningFeedback aplo-ont:affectsAwarenessObservation ?awarenessObservation ;
                    aplo-ont:hasLearningFeedbackType ?feedbackType .
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
  OPTIONAL { ?feedbackType rdf:value ?feedbackTypeLabel . }

}
ORDER BY ?learner ?awarenessObservation ?learningFeedback
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | evaluationResult | evaluationResultLabel | learningFeedback | learningFeedbackLabel | feedbackType | feedbackTypeLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Mastery%20Awareness | Mastery Awareness | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Proficient%20Awareness | Proficient Awareness | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |

### CQ-056: What type of feedback was given to the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningFeedback ?learningFeedbackLabel ?feedbackType ?feedbackTypeLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?learningFeedback a aplo-ont:LearningFeedback ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation ;
                    aplo-ont:hasLearningFeedbackType ?feedbackType .
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?feedbackType rdf:value ?feedbackTypeLabel . }

}
ORDER BY ?learner ?learningFeedback ?feedbackType
```

**Top 5 output rows:**

| learner | learnerLabel | learningFeedback | learningFeedbackLabel | feedbackType | feedbackTypeLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern | Corrective Feedback on SPARQL Pattern | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components | Corrective Feedback on Triple Components | aplo-r:learningFeedbackType.Corrective%20Feedback | Corrective Feedback |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learningFeedback.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Planning%20Extension%20Prompt | Knowledge Engineering Workflow Planning Extension Prompt | aplo-r:learningFeedbackType.Strategic%20Feedback | Strategic Feedback |

### CQ-057: When was feedback delivered to the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningFeedback ?learningFeedbackLabel ?timeNode ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?learningFeedback a aplo-ont:LearningFeedback ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation ;
                    aplo-ont:hasResponseTime ?timeNode .
  OPTIONAL { ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?timeNode rdf:value ?timeValue . }
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?learningFeedback ?timeValue
```

**Top 5 output rows:**

| learner | learnerLabel | learningFeedback | learningFeedbackLabel | timeNode | timeValue |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns | aplo-r:temporalExtent.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns.2026-01-15T10%3A09%3A00Z | 2026-01-15T10:09:00+00:00 |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern | Corrective Feedback on SPARQL Pattern | aplo-r:temporalExtent.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern.2026-01-19T13%3A22%3A00Z | 2026-01-19T13:22:00+00:00 |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components | Corrective Feedback on Triple Components | aplo-r:temporalExtent.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components.2026-01-17T11%3A16%3A00Z | 2026-01-17T11:16:00+00:00 |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learningFeedback.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Planning%20Extension%20Prompt | Knowledge Engineering Workflow Planning Extension Prompt | aplo-r:temporalExtent.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Planning%20Extension%20Prompt.2026-03-04T14%3A07%3A00Z | 2026-03-04T14:07:00+00:00 |

### CQ-058: When was the response delivered to the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?response ?responseLabel ?timeNode ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?response a aplo-ont:Response ;
            aplo-ont:affectsAwarenessObservation ?awarenessObservation ;
            aplo-ont:hasResponseTime ?timeNode .
  OPTIONAL { ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?timeNode rdf:value ?timeValue . }
  OPTIONAL { ?response rdf:value ?responseLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?response ?timeValue
```

**Top 5 output rows:**

| learner | learnerLabel | response | responseLabel | timeNode | timeValue |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Ontology Explanation Response | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Your explanation identifies classes and properties; revise it to mention axioms and shared semantics | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Connect ontology components to the purpose of shared machine-interpretable meaning | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:temporalExtent.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation.2026-01-16T14%3A30%3A00Z | 2026-01-16T14:30:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:response.Learner%20Alex.Learner%20Alex.Learner%20Ontology%20Explanation | An ontology defines the concepts and relationships for a domain so data can be interpreted consistently | aplo-r:temporalExtent.Learner%20Alex.Learner%20Alex.Learner%20Ontology%20Explanation.2026-01-16T14%3A00%3A00Z%20to%202026-01-16T14%3A25%3A00Z | ISO 8601 UTC |

### CQ-059: Who or what produced the response?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?response ?responseLabel ?source ?sourceLabel WHERE {
  ?response a aplo-ont:Response ;
            aplo-ont:hasSource ?source .
  ?source a aplo-ont:Source .
  OPTIONAL { ?source rdf:value ?sourceLabel . }
  OPTIONAL { ?response rdf:value ?responseLabel . }
}
ORDER BY ?response ?source
```

**Top 5 output rows:**

| response | responseLabel | source | sourceLabel |
| --- | --- | --- | --- |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Ontology Explanation Response | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Your explanation identifies classes and properties; revise it to mention axioms and shared semantics | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Connect ontology components to the purpose of shared machine-interpretable meaning | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Learner%20Alex.Learner%20Ontology%20Explanation | An ontology defines the concepts and relationships for a domain so data can be interpreted consistently | aplo-r:source.Learner%20Alex | Learner Alex |

### CQ-060: Which responses came from a human source?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?response ?responseLabel ?source ?sourceLabel WHERE {
  ?response a aplo-ont:Response ;
            aplo-ont:hasSource ?source .
  FILTER(CONTAINS(LCASE(STR(?source)), "human") || CONTAINS(LCASE(STR(?source)), "teacher") || CONTAINS(LCASE(STR(?source)), "instructor"))
  OPTIONAL { ?source rdf:value ?sourceLabel . }
  OPTIONAL { ?response rdf:value ?responseLabel . }
}
ORDER BY ?response
```

**Top 5 output rows:**

| response | responseLabel | source | sourceLabel |
| --- | --- | --- | --- |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Ontology Explanation Response | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Your explanation identifies classes and properties; revise it to mention axioms and shared semantics | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Connect ontology components to the purpose of shared machine-interpretable meaning | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |
| aplo-r:response.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Plan%20Evidence%20Rating | Knowledge Engineering Workflow Plan Evidence Rating | aplo-r:source.Instructor%20Reviewer | Instructor Reviewer |

### CQ-061: Which responses came from an automated or AI source?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?response ?responseLabel ?source ?sourceLabel WHERE {
  ?response a aplo-ont:Response ;
            aplo-ont:hasSource ?source .
  FILTER(CONTAINS(LCASE(STR(?source)), "platform") || CONTAINS(LCASE(STR(?source)), "automated") || CONTAINS(LCASE(STR(?source)), "ai") || CONTAINS(LCASE(STR(?source)), "llm"))
  OPTIONAL { ?source rdf:value ?sourceLabel . }
  OPTIONAL { ?response rdf:value ?responseLabel . }
}
ORDER BY ?response
```

**Top 5 output rows:**

| response | responseLabel | source | sourceLabel |
| --- | --- | --- | --- |
| aplo-r:response.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:source.Learning%20Platform | Learning Platform |
| aplo-r:response.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check scored result: 82 Score Percent for Semantic Web Vocabulary Recall with correct examples and one missed boundary case. | aplo-r:source.Learning%20Platform | Learning Platform |
| aplo-r:response.Learner%20Blair.Learner%20Blair.Learner%20SPARQL%20Query%20Attempt | Learner SPARQL Query Attempt | aplo-r:source.Learner%20Blair | Learner Blair |
| aplo-r:response.Learner%20Blair.Learner%20Blair.Learner%20SPARQL%20Query%20Attempt | SELECT ?s WHERE { ?s a ?type } | aplo-r:source.Learner%20Blair | Learner Blair |
| aplo-r:response.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns | aplo-r:source.Learning%20Platform | Learning Platform |

### CQ-062: What feedback may affect the learner’s next learning strategy?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?learningFeedback ?learningFeedbackLabel ?strategy ?strategyLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?learningFeedback a aplo-ont:LearningFeedback ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation ;
                    aplo-ont:affectsStrategy ?strategy .
  ?strategy a aplo-ont:LearningStrategy .
  OPTIONAL { ?strategy aplo-ont:hasName ?strategyLabel . }
  OPTIONAL { ?learningFeedback rdf:value ?learningFeedbackLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?learningFeedback ?strategy
```

**Top 5 output rows:**

| learner | learnerLabel | learningFeedback | learningFeedbackLabel | strategy | strategyLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation | aplo-r:learningStrategy.Foundational%20Semantic%20Web%20Study.Semantic%20Web%20Foundations%20Strategy | Semantic Web Foundations Strategy |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Identifier%20Patterns | Corrective Feedback on Identifier Patterns | aplo-r:learningStrategy.Identifier%20Practice%20Session.Identifier%20and%20RDF%20Practice%20Strategy | Identifier and RDF Practice Strategy |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20SPARQL%20Pattern | Corrective Feedback on SPARQL Pattern | aplo-r:learningStrategy.SPARQL%20Query%20Practice.Query%20Construction%20Strategy | Query Construction Strategy |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningFeedback.Learner%20Blair.Learning%20Platform.Corrective%20Feedback%20on%20Triple%20Components | Corrective Feedback on Triple Components | aplo-r:learningStrategy.RDF%20Practice%20Session.Identifier%20and%20RDF%20Practice%20Strategy | Identifier and RDF Practice Strategy |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learningFeedback.Learner%20Cameron.Instructor%20Reviewer.Knowledge%20Engineering%20Workflow%20Planning%20Extension%20Prompt | Knowledge Engineering Workflow Planning Extension Prompt | aplo-r:learningStrategy.KG%20Curriculum%20Design%20Studio.Curriculum%20KG%20Foundations%20Strategy | Curriculum KG Foundations Strategy |

### CQ-063: How did the learner’s awareness change after feedback or response?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?feedbackOrResponse ?feedbackOrResponseLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:hasAwarenessLevel ?awarenessLevel ;
                        aplo-ont:atTime ?timeNode .
  {
    ?feedbackOrResponse a aplo-ont:LearningFeedback ;
                        aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  }
  UNION
  {
    ?feedbackOrResponse a aplo-ont:Response ;
                        aplo-ont:affectsAwarenessObservation ?awarenessObservation .
  }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?feedbackOrResponse rdf:value ?feedbackOrResponseLabel . }
}
ORDER BY ?learner ?timeNode ?feedbackOrResponse
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | feedbackOrResponse | feedbackOrResponseLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:response.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:response.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check scored result: 82 Score Percent for Semantic Web Vocabulary Recall with correct examples and one missed boundary case. |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:learningFeedback.Learner%20Alex.Instructor%20Reviewer.Strategic%20Feedback%20on%20Ontology%20Explanation | Strategic Feedback on Ontology Explanation |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Ontology Explanation Response |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness | aplo-r:response.Learner%20Alex.Instructor%20Reviewer.Ontology%20Explanation%20Response | Your explanation identifies classes and properties; revise it to mention axioms and shared semantics |

### CQ-064: What learner goals does a learner have?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal a aplo-ont:LearnerGoal .
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?goal
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learnerGoal.Design%20KG%20Curriculum%20Sequence | Design KG Curriculum Sequence |
| aplo-r:learner.Learner%20Carla | Learner Carla | aplo-r:learnerGoal.Coordinate%20Collaborative%20KG%20Delivery | Coordinate Collaborative KG Delivery |
| aplo-r:learner.Learner%20Casey | Learner Casey | aplo-r:learnerGoal.Improve%20Ontology%20Modeling%20Decisions | Improve Ontology Modeling Decisions |

### CQ-065: What skills are targeted by a learner goal?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?goal ?goalLabel ?skill ?skillLabel WHERE {
  ?goal a aplo-ont:LearnerGoal ;
        aplo-ont:targetsSkill ?skill .
  ?skill a aplo-ont:Skill .
  OPTIONAL { ?skill rdf:value ?skillLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
}
ORDER BY ?goal ?skill
```

**Top 5 output rows:**

| goal | goalLabel | skill | skillLabel |
| --- | --- | --- | --- |
| aplo-r:learnerGoal.Apply%20Logic%20to%20Knowledge%20Graph%20Modeling | Apply Logic to Knowledge Graph Modeling | aplo-r:skill.Description%20Logic%20Constraint%20Reasoning | Description Logic Constraint Reasoning |
| aplo-r:learnerGoal.Apply%20Logic%20to%20Knowledge%20Graph%20Modeling | Apply Logic to Knowledge Graph Modeling | aplo-r:skill.Knowledge%20Graph%20Structure%20Explanation | Knowledge Graph Structure Explanation |
| aplo-r:learnerGoal.Apply%20Logic%20to%20Knowledge%20Graph%20Modeling | Apply Logic to Knowledge Graph Modeling | aplo-r:skill.Logic%20Operator%20Recognition | Logic Operator Recognition |
| aplo-r:learnerGoal.Assess%20Knowledge%20Graph%20Consulting%20Opportunities | Assess Knowledge Graph Consulting Opportunities | aplo-r:skill.Observation%20Ontology%20Modeling | Observation Ontology Modeling |
| aplo-r:learnerGoal.Assess%20Knowledge%20Graph%20Consulting%20Opportunities | Assess Knowledge Graph Consulting Opportunities | aplo-r:skill.Open%20Graph%20Metadata%20Mapping | Open Graph Metadata Mapping |

### CQ-066: What learner preferences does a learner have?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasLearnerPreference ?preference .
  ?preference a aplo-ont:LearnerPreference .
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }

}
ORDER BY ?learner ?preference
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerPreference.Guided%20Practice%20Preference | Guided Practice Preference |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learnerPreference.Guided%20Practice%20Preference | Guided Practice Preference |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learnerPreference.Scaffolded%20Sequence%20Preference | Scaffolded Sequence Preference |

### CQ-067: What learner challenges does a learner have?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?challenge ?challengeLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasLearningChallenge ?challenge .
  ?challenge a aplo-ont:LearningChallenge .
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?challenge
```

**Top 5 output rows:**

| learner | learnerLabel | challenge | challengeLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Low%20Confidence%20With%20Formal%20Syntax | LearningChallenge |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Low%20Confidence%20With%20Formal%20Syntax | Low Confidence With Formal Syntax |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Screen%20Reader%20Requirement | AccessibilityChallenge |

### CQ-068: What accessibility issues does a learner have?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?accessibilityChallenge ?accessibilityChallengeLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasLearningChallenge ?accessibilityChallenge .
  ?accessibilityChallenge a aplo-ont:LearningChallenge ;
                          rdf:value "AccessibilityChallenge"^^xsd:string .
  OPTIONAL { ?accessibilityChallenge rdf:value ?accessibilityChallengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?accessibilityChallenge
```

**Top 5 output rows:**

| learner | learnerLabel | accessibilityChallenge | accessibilityChallengeLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Screen%20Reader%20Requirement | AccessibilityChallenge |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Screen%20Reader%20Requirement | Screen Reader Requirement |

### CQ-069: What media satisfy both learner preferences and accessibility challenges?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?media ?mediaLabel WHERE {
  ?learner aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?media a edu-ont:Media ;
         aplo-ont:supportsLearningObjective ?learningObjective .
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?media rdf:value ?mediaLabel . }

}
ORDER BY ?learner ?media
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel | challenge | challengeLabel | media | mediaLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-070: What module(s) satisfy both learner preferences and accessibility challenges?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?module ?moduleLabel WHERE {
  ?learner aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?module a edu-ont:Module ;
          aplo-ont:hasLearningObjective ?learningObjective .
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?module rdf:value ?moduleLabel . }

}
ORDER BY ?learner ?module
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel | challenge | challengeLabel | module | moduleLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-071: What learner situation should be considered when selecting a learning objective?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?situation ?situationLabel ?learningObjective ?learningObjectiveLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?situation rdf:value ?situationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?situation ?learningObjective
```

**Top 5 output rows:**

| learner | learnerLabel | situation | situationLabel | learningObjective | learningObjectiveLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningSituation.RDF%20Practice%20Session | RDF Practice Session | aplo-r:learningObjective.RDF%20Practice%20Session.Compare%20RDF%20serialization%20formats | Compare RDF serialization formats |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningSituation.RDF%20Practice%20Session | RDF Practice Session | aplo-r:learningObjective.RDF%20Practice%20Session.Interpret%20RDF%20triple%20components | Interpret RDF triple components |

### CQ-072: Which media resources satisfy both the learner’s preferences and accessibility needs?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?media ?mediaLabel WHERE {
  ?learner aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?media a edu-ont:Media ;
         aplo-ont:supportsLearningObjective ?learningObjective .
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?media rdf:value ?mediaLabel . }

}
ORDER BY ?learner ?media
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel | challenge | challengeLabel | media | mediaLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-073: Which modules satisfy both the learner’s preferences and accessibility needs?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?module ?moduleLabel WHERE {
  ?learner aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?module a edu-ont:Module ;
          aplo-ont:hasLearningObjective ?learningObjective .
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?module rdf:value ?moduleLabel . }

}
ORDER BY ?learner ?module
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel | challenge | challengeLabel | module | moduleLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-074: Which learning resources are appropriate for the learner’s current situation?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?situation ?situationLabel ?learningObjective ?learningObjectiveLabel ?resource ?resourceLabel WHERE {
  ?learner aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  { ?resource a edu-ont:Module ; aplo-ont:hasLearningObjective ?learningObjective . }
  UNION
  { ?resource a edu-ont:Media ; aplo-ont:supportsLearningObjective ?learningObjective . }
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?resource rdf:value ?resourceLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?situation rdf:value ?situationLabel . }

}
ORDER BY ?learner ?resource
```

**Top 5 output rows:**

| learner | learnerLabel | situation | situationLabel | learningObjective | learningObjectiveLabel | resource | resourceLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Explain%20what%20an%20ontology%20represents | Explain what an ontology represents | edu-r:media.What%20is%20an%20Ontology%3F | What is an Ontology? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:module.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:module.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-075: What goals is the learner currently pursuing?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasGoal ?goal .
  ?goal a aplo-ont:LearnerGoal .
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?goal
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learnerGoal.Design%20KG%20Curriculum%20Sequence | Design KG Curriculum Sequence |
| aplo-r:learner.Learner%20Carla | Learner Carla | aplo-r:learnerGoal.Coordinate%20Collaborative%20KG%20Delivery | Coordinate Collaborative KG Delivery |
| aplo-r:learner.Learner%20Casey | Learner Casey | aplo-r:learnerGoal.Improve%20Ontology%20Modeling%20Decisions | Improve Ontology Modeling Decisions |

### CQ-076: What skills are targeted by the learner’s goals?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?skill ?skillLabel WHERE {
  ?learner aplo-ont:hasGoal ?goal .
  ?goal aplo-ont:targetsSkill ?skill .
  ?skill a aplo-ont:Skill .
  OPTIONAL { ?skill rdf:value ?skillLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?goal ?skill
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | skill | skillLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerGoal.Interpret%20RDF%20Graph%20Data | Interpret RDF Graph Data | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison |

### CQ-077: What preferences should be considered when selecting resources or activities for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasLearnerPreference ?preference .
  ?preference a aplo-ont:LearnerPreference .
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }

}
ORDER BY ?learner ?preference
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learnerPreference.Guided%20Practice%20Preference | Guided Practice Preference |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learnerPreference.Guided%20Practice%20Preference | Guided Practice Preference |
| aplo-r:learner.Learner%20Cameron | Learner Cameron | aplo-r:learnerPreference.Scaffolded%20Sequence%20Preference | Scaffolded Sequence Preference |

### CQ-078: What learning challenges should be considered when selecting resources or activities?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?challenge ?challengeLabel WHERE {
  ?learner a aplo-ont:Learner ;
           aplo-ont:hasLearningChallenge ?challenge .
  ?challenge a aplo-ont:LearningChallenge .
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?challenge
```

**Top 5 output rows:**

| learner | learnerLabel | challenge | challengeLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Low%20Confidence%20With%20Formal%20Syntax | LearningChallenge |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Low%20Confidence%20With%20Formal%20Syntax | Low Confidence With Formal Syntax |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Screen%20Reader%20Requirement | AccessibilityChallenge |

### CQ-079: What accessibility needs should be considered when selecting resources or activities?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?accessibilityChallenge ?accessibilityChallengeLabel WHERE {
  ?learner aplo-ont:hasLearningChallenge ?accessibilityChallenge .
  ?accessibilityChallenge a aplo-ont:LearningChallenge ;
                          rdf:value "AccessibilityChallenge"^^xsd:string .
  OPTIONAL { ?accessibilityChallenge rdf:value ?accessibilityChallengeLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner ?accessibilityChallenge
```

**Top 5 output rows:**

| learner | learnerLabel | accessibilityChallenge | accessibilityChallengeLabel |
| --- | --- | --- | --- |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Screen%20Reader%20Requirement | AccessibilityChallenge |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:learningChallenge.Screen%20Reader%20Requirement | Screen Reader Requirement |

### CQ-080: What learner context should be considered before selecting the next instructional step?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?goal ?goalLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?situation ?situationLabel ?awarenessObservation ?awarenessObservationLabel WHERE {
  ?learner a aplo-ont:Learner .
  OPTIONAL { ?learner aplo-ont:hasGoal ?goal . }
  OPTIONAL { ?learner aplo-ont:hasLearnerPreference ?preference . }
  OPTIONAL { ?learner aplo-ont:hasLearningChallenge ?challenge . }
  OPTIONAL { ?learner aplo-ont:hasSituation ?situation . }
  OPTIONAL { ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?goal rdf:value ?goalLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?situation rdf:value ?situationLabel . }

}
ORDER BY ?learner
```

**Top 5 output rows:**

| learner | learnerLabel | goal | goalLabel | preference | preferenceLabel | challenge | challengeLabel | situation | situationLabel | awarenessObservation | awarenessObservationLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerGoal.Build%20Semantic%20Web%20Foundations | Build Semantic Web Foundations | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningSituation.Foundational%20Semantic%20Web%20Study | Foundational Semantic Web Study | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check |

### CQ-081: Given learner preferences and accessibility needs, what resource should be selected for the next instructional step?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?preference ?preferenceLabel ?challenge ?challengeLabel ?learningObjective ?learningObjectiveLabel ?resource ?resourceLabel WHERE {
  ?learner aplo-ont:hasLearnerPreference ?preference ;
           aplo-ont:hasLearningChallenge ?challenge ;
           aplo-ont:hasSituation ?situation .
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  { ?resource a edu-ont:Module ; aplo-ont:hasLearningObjective ?learningObjective . }
  UNION
  { ?resource a edu-ont:Media ; aplo-ont:supportsLearningObjective ?learningObjective . }
  OPTIONAL { ?learningObjective aplo-ont:hasName ?learningObjectiveLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?preference rdf:value ?preferenceLabel . }
  OPTIONAL { ?challenge rdf:value ?challengeLabel . }
  OPTIONAL { ?resource rdf:value ?resourceLabel . }

}
ORDER BY ?learner ?resource
```

**Top 5 output rows:**

| learner | learnerLabel | preference | preferenceLabel | challenge | challengeLabel | learningObjective | learningObjectiveLabel | resource | resourceLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Worked%20Examples%20Preference | Worked Examples Preference | aplo-r:learningChallenge.Limited%20Study%20Time | Limited Study Time | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Recall%20core%20metadata%20terminology | Recall core metadata terminology | edu-r:media.What%20is%20Metadata%3F | What is Metadata? |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:learnerPreference.Immediate%20Feedback%20Preference | Immediate Feedback Preference | aplo-r:learningChallenge.Limited%20Study%20Time | LearningChallenge | aplo-r:learningObjective.Foundational%20Semantic%20Web%20Study.Describe%20the%20purpose%20of%20a%20knowledge%20graph | Describe the purpose of a knowledge graph | edu-r:media.What%20is%20a%20Knowledge%20Graph%3F | What is a Knowledge Graph? |

### CQ-082: What is the learner's current awareness level for a topic?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?topic ?topicLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onTopic ?topic ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL { ?awarenessObservation aplo-ont:atTime ?timeNode . ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL {
    ?awarenessObservation rdf:value ?awarenessObservationLabel .
    FILTER(?awarenessObservationLabel NOT IN ("AwarenessObservation"^^xsd:string, "CurrentAwarenessObservation"^^xsd:string))
  }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?learner ?topic DESC(?timeValue)
```

**Top 5 output rows:**

| learner | learnerLabel | topic | topicLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | timeValue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-14T09:00:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Metadata | Metadata | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Ontology | Ontology | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | edu-r:topic.Query | Query | aplo-r:awarenessObservation.Learner%20Blair.Query.SPARQL%20Query%20Construction.SPARQL%20Awareness%20After%20Practice | SPARQL Awareness After Practice | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | edu-r:topic.RDF%2FXML | RDF/XML | aplo-r:awarenessObservation.Learner%20Blair.RDF%2FXML.RDF%20Serialization%20Comparison.RDF%20Serialization%20Current%20Awareness | RDF Serialization Current Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-17T12:00:00+00:00 |

### CQ-083: What is the learner's current awareness level of a skill?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?skill ?skillLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onSkill ?skill ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL { ?awarenessObservation aplo-ont:atTime ?timeNode . ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }
}
ORDER BY ?learner ?skill DESC(?timeValue)
```

**Top 5 output rows:**

| learner | learnerLabel | skill | skillLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | timeValue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-14T09:00:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition | aplo-r:awarenessObservation.Learner%20Blair.URI.Linked%20Data%20Identifier%20Recognition.Identifier%20Awareness%20After%20Check | Identifier Awareness After Check | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:awarenessObservation.Learner%20Blair.RDF%2FXML.RDF%20Serialization%20Comparison.RDF%20Serialization%20Current%20Awareness | RDF Serialization Current Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-17T12:00:00+00:00 |

### CQ-084: What topics have low awareness for a learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?topic ?topicLabel ?awarenessLevel ?awarenessLevelLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onTopic ?topic ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  FILTER(CONTAINS(LCASE(STR(?awarenessLevel)), "low"))
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?learner ?topic
```

**Top 5 output rows:**

| learner | learnerLabel | topic | topicLabel | awarenessLevel | awarenessLevelLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |
| aplo-r:learner.Learner%20Blair | Learner Blair | edu-r:topic.RDF%2FXML | RDF/XML | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |

### CQ-085: What skills have low awareness for a learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?skill ?skillLabel ?awarenessLevel ?awarenessLevelLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onSkill ?skill ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  FILTER(CONTAINS(LCASE(STR(?awarenessLevel)), "low"))
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?skill
```

**Top 5 output rows:**

| learner | learnerLabel | skill | skillLabel | awarenessLevel | awarenessLevelLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |

### CQ-086: What awareness observations are most latest?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:atTime ?timeNode .
  ?timeNode time:inXSDDateTime ?timeValue .
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY DESC(?timeValue)
LIMIT 25
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | timeValue |
| --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Riley | Learner Riley | aplo-r:awarenessObservation.Learner%20Riley.Query.GraphQL%20Query%20Mapping.KG%20Resource%20Development%20Awareness | KG Resource Development Awareness | 2026-03-24T14:40:00+00:00 |
| aplo-r:learner.Learner%20Riley | Learner Riley | aplo-r:awarenessObservation.Learner%20Riley.Triple.RDF%20Graph%20Interpretation.KG%20Facilitation%20Planning%20Awareness | KG Facilitation Planning Awareness | 2026-03-23T14:20:00+00:00 |
| aplo-r:learner.Learner%20Riley | Learner Riley | aplo-r:awarenessObservation.Learner%20Riley.Metadata.Semantic%20Web%20Vocabulary%20Recall.Semantic%20Web%20Foundation%20Baseline%20Awareness | Semantic Web Foundation Baseline Awareness | 2026-03-22T14:00:00+00:00 |
| aplo-r:learner.Learner%20Morgan | Learner Morgan | aplo-r:awarenessObservation.Learner%20Morgan.Metadata.Dublin%20Core%20Metadata%20Mapping.Executive%20KG%20Value%20Framing%20Awareness | Executive KG Value Framing Awareness | 2026-03-21T13:40:00+00:00 |
| aplo-r:learner.Learner%20Morgan | Learner Morgan | aplo-r:awarenessObservation.Learner%20Morgan.Ontology.Modular%20Ontology%20Design.Modular%20Ontology%20Contribution%20Planning%20Awareness | Modular Ontology Contribution Planning Awareness | 2026-03-20T13:20:00+00:00 |

### CQ-087: Which modules or media address the topics where the learner has low awareness?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?topic ?topicLabel ?awarenessLevel ?awarenessLevelLabel ?resource ?resourceLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onTopic ?topic ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  FILTER(CONTAINS(LCASE(STR(?awarenessLevel)), "low"))
  ?learningObjective aplo-ont:worksOnSituation ?situation .
  ?situation aplo-ont:requiresTopicKnowledge ?topic .
  { ?resource a edu-ont:Module ; aplo-ont:hasLearningObjective ?learningObjective . }
  UNION
  { ?resource a edu-ont:Media ; aplo-ont:supportsLearningObjective ?learningObjective . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }
  OPTIONAL { ?resource rdf:value ?resourceLabel . }

}
ORDER BY ?learner ?topic ?resource
```

**Top 5 output rows:**

| learner | learnerLabel | topic | topicLabel | awarenessLevel | awarenessLevelLabel | resource | resourceLabel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | edu-r:media.Deploying%20a%20Knowledge%20Graph | Deploying a Knowledge Graph |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | edu-r:media.Description%20Logic | Description Logic |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | edu-r:media.Dublin%20Core | Dublin Core |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | edu-r:media.GraphQL | GraphQL |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | edu-r:media.History%20of%20the%20Semantic%20Web | History of the Semantic Web |

### CQ-088: What is the learner’s current awareness level for a topic?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?topic ?topicLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onTopic ?topic ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL { ?awarenessObservation aplo-ont:atTime ?timeNode . ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }
}
ORDER BY ?learner ?topic DESC(?timeValue)
```

**Top 5 output rows:**

| learner | learnerLabel | topic | topicLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | timeValue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-14T09:00:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Metadata | Metadata | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Ontology | Ontology | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | edu-r:topic.Query | Query | aplo-r:awarenessObservation.Learner%20Blair.Query.SPARQL%20Query%20Construction.SPARQL%20Awareness%20After%20Practice | SPARQL Awareness After Practice | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | edu-r:topic.RDF%2FXML | RDF/XML | aplo-r:awarenessObservation.Learner%20Blair.RDF%2FXML.RDF%20Serialization%20Comparison.RDF%20Serialization%20Current%20Awareness | RDF Serialization Current Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-17T12:00:00+00:00 |

### CQ-089: What is the learner’s current awareness level for a skill?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?skill ?skillLabel ?awarenessObservation ?awarenessObservationLabel ?awarenessLevel ?awarenessLevelLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onSkill ?skill ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL { ?awarenessObservation aplo-ont:atTime ?timeNode . ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }

}
ORDER BY ?learner ?skill DESC(?timeValue)
```

**Top 5 output rows:**

| learner | learnerLabel | skill | skillLabel | awarenessObservation | awarenessObservationLabel | awarenessLevel | awarenessLevelLabel | timeValue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-14T09:00:00+00:00 |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition | aplo-r:awarenessObservation.Learner%20Blair.URI.Linked%20Data%20Identifier%20Recognition.Identifier%20Awareness%20After%20Check | Identifier Awareness After Check | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:awarenessObservation.Learner%20Blair.RDF%2FXML.RDF%20Serialization%20Comparison.RDF%20Serialization%20Current%20Awareness | RDF Serialization Current Awareness | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-17T12:00:00+00:00 |

### CQ-090: Which topics show low awareness for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?topic ?topicLabel ?awarenessLevel ?awarenessLevelLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onTopic ?topic ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  FILTER(CONTAINS(LCASE(STR(?awarenessLevel)), "low"))
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }

}
ORDER BY ?learner ?topic
```

**Top 5 output rows:**

| learner | learnerLabel | topic | topicLabel | awarenessLevel | awarenessLevelLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |
| aplo-r:learner.Learner%20Blair | Learner Blair | edu-r:topic.RDF%2FXML | RDF/XML | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |

### CQ-091: Which skills show low awareness for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?skill ?skillLabel ?awarenessLevel ?awarenessLevelLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:onSkill ?skill ;
                        aplo-ont:hasAwarenessLevel ?awarenessLevel .
  FILTER(CONTAINS(LCASE(STR(?awarenessLevel)), "low"))
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }

}
ORDER BY ?learner ?skill
```

**Top 5 output rows:**

| learner | learnerLabel | skill | skillLabel | awarenessLevel | awarenessLevelLabel |
| --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:skill.RDF%20Serialization%20Comparison | RDF Serialization Comparison | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness |

### CQ-092: What awareness observations are available for the learner over time?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?topic ?topicLabel ?skill ?skillLabel ?awarenessLevel ?awarenessLevelLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:hasAwarenessLevel ?awarenessLevel .
  OPTIONAL { ?awarenessObservation aplo-ont:onTopic ?topic . }
  OPTIONAL { ?awarenessObservation aplo-ont:onSkill ?skill . }
  OPTIONAL { ?awarenessObservation aplo-ont:atTime ?timeNode . ?timeNode time:inXSDDateTime ?timeValue . }
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?awarenessLevel rdf:value ?awarenessLevelLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL { ?topic rdf:value ?topicLabel . }
  OPTIONAL { ?skill rdf:value ?skillLabel . }

}
ORDER BY ?learner ?timeValue
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | topic | topicLabel | skill | skillLabel | awarenessLevel | awarenessLevelLabel | timeValue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | edu-r:topic.Metadata | Metadata | aplo-r:skill.Semantic%20Web%20Vocabulary%20Recall | Semantic Web Vocabulary Recall | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Ontology.Ontology%20Concept%20Explanation.Ontology%20Awareness%20After%20Review | Ontology Awareness After Review | edu-r:topic.Ontology | Ontology | aplo-r:skill.Ontology%20Concept%20Explanation | Ontology Concept Explanation | aplo-r:awarenessLevel.Working%20Awareness | Working Awareness |  |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | edu-r:topic.Knowledge%20Graph | Knowledge Graph | aplo-r:skill.Knowledge%20Graph%20Purpose%20Explanation | Knowledge Graph Purpose Explanation | aplo-r:awarenessLevel.Low%20Awareness | Low Awareness | 2026-01-14T09:00:00+00:00 |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:awarenessObservation.Learner%20Blair.Triple.RDF%20Triple%20Interpretation.RDF%20Triple%20Awareness%20After%20Quiz | RDF Triple Awareness After Quiz | edu-r:topic.Triple | Triple | aplo-r:skill.RDF%20Triple%20Interpretation | RDF Triple Interpretation | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness |  |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:awarenessObservation.Learner%20Blair.URI.Linked%20Data%20Identifier%20Recognition.Identifier%20Awareness%20After%20Check | Identifier Awareness After Check | edu-r:topic.URI | URI | aplo-r:skill.Linked%20Data%20Identifier%20Recognition | Linked Data Identifier Recognition | aplo-r:awarenessLevel.Basic%20Awareness | Basic Awareness |  |

### CQ-093: What is the most recent awareness observation for the learner?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?timeValue WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?awarenessObservation aplo-ont:atTime ?timeNode .
  ?timeNode time:inXSDDateTime ?timeValue .
  OPTIONAL { ?awarenessObservation rdf:value ?awarenessObservationLabel . }
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
}
ORDER BY ?learner DESC(?timeValue)
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | timeValue |
| --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Knowledge%20Graph.Knowledge%20Graph%20Purpose%20Explanation.Knowledge%20Graph%20Initial%20Awareness | Knowledge Graph Initial Awareness | 2026-01-14T09:00:00+00:00 |
| aplo-r:learner.Learner%20Blair | Learner Blair | aplo-r:awarenessObservation.Learner%20Blair.RDF%2FXML.RDF%20Serialization%20Comparison.RDF%20Serialization%20Current%20Awareness | RDF Serialization Current Awareness | 2026-01-17T12:00:00+00:00 |
| aplo-r:learner.Learner%20Morgan | Learner Morgan | aplo-r:awarenessObservation.Learner%20Morgan.Metadata.Dublin%20Core%20Metadata%20Mapping.Executive%20KG%20Value%20Framing%20Awareness | Executive KG Value Framing Awareness | 2026-03-21T13:40:00+00:00 |
| aplo-r:learner.Learner%20Morgan | Learner Morgan | aplo-r:awarenessObservation.Learner%20Morgan.Ontology.Modular%20Ontology%20Design.Modular%20Ontology%20Contribution%20Planning%20Awareness | Modular Ontology Contribution Planning Awareness | 2026-03-20T13:20:00+00:00 |
| aplo-r:learner.Learner%20Morgan | Learner Morgan | aplo-r:awarenessObservation.Learner%20Morgan.Query.SPARQL%20Query%20Pattern%20Construction.SPARQL%20Query%20Pattern%20Readiness%20Observation | SPARQL Query Pattern Readiness Observation | 2026-03-19T13:00:00+00:00 |

### CQ-094: What assessment evidence contributed to the learner’s current awareness observation?

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX aplo-ont: <https://aplo.cs.wright.edu/lod/ontology#>
PREFIX edu-ont: <https://edugate.cs.wright.edu/lod/ontology#>

SELECT DISTINCT ?learner ?learnerLabel ?awarenessObservation ?awarenessObservationLabel ?evaluationResult ?evaluationResultLabel ?evaluationMetric ?evaluationMetricLabel ?evaluationTechnique ?evaluationTechniqueLabel WHERE {
  ?learner aplo-ont:hasAwarenessObservation ?awarenessObservation .
  ?evaluationResult a aplo-ont:EvaluationResult ;
                    aplo-ont:affectsAwarenessObservation ?awarenessObservation ;
                    aplo-ont:hasUnit ?evaluationMetric .
  ?evaluationTechnique aplo-ont:hasEvaluationMetric ?evaluationMetric .
  OPTIONAL { ?learner rdf:value ?learnerLabel . }
  OPTIONAL {
    ?awarenessObservation rdf:value ?awarenessObservationLabel .
    FILTER(?awarenessObservationLabel NOT IN ("AwarenessObservation"^^xsd:string, "CurrentAwarenessObservation"^^xsd:string))
  }
  OPTIONAL { ?evaluationResult rdf:value ?evaluationResultLabel . }
  OPTIONAL { ?evaluationMetric rdf:value ?evaluationMetricLabel . }
  OPTIONAL { ?evaluationTechnique rdf:value ?evaluationTechniqueLabel . }
}
ORDER BY ?learner ?awarenessObservation ?evaluationResult
```

**Top 5 output rows:**

| learner | learnerLabel | awarenessObservation | awarenessObservationLabel | evaluationResult | evaluationResultLabel | evaluationMetric | evaluationMetricLabel | evaluationTechnique | evaluationTechniqueLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | aplo-r:evaluationTechnique.Auto%20Scored%20Concept%20Check | Auto Scored Concept Check |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | aplo-r:evaluationTechnique.Mastery%20Reassessment | Mastery Reassessment |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | aplo-r:evaluationTechnique.Query%20Practice%20Check | Query Practice Check |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | aplo-r:evaluationTechnique.Short%20Explanation%20Rubric | Short Explanation Rubric |
| aplo-r:learner.Learner%20Alex | Learner Alex | aplo-r:awarenessObservation.Learner%20Alex.Metadata.Semantic%20Web%20Vocabulary%20Recall.Metadata%20Awareness%20After%20Check | Metadata Awareness After Check | aplo-r:evaluationResult.Learner%20Alex.Learning%20Platform.Metadata%20Concept%20Check%20Score | Metadata Concept Check Score | aplo-r:evaluationMetric.Score%20Percent | Score Percent | aplo-r:evaluationTechnique.Triple%20Interpretation%20Quiz | Triple Interpretation Quiz |