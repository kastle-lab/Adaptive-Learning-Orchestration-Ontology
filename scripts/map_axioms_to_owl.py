from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD


DEFAULT_PREFIXES = {
    "": "https://aplo.cs.wright.edu/lod/ontology#",
    "owl": str(OWL),
    "rdf": str(RDF),
    "rdfs": str(RDFS),
    "xsd": str(XSD),
    "aplo-ont": "https://aplo.cs.wright.edu/lod/ontology#",
    "edu-ont": "https://edugate.cs.wright.edu/lod/ontology#",
}

DATATYPE_PREFIXES = {"xsd", "rdf", "rdfs"}
DATATYPE_TERMS = {"rdfs:Literal", "rdf:langString"}
SUBCLASS_PREDICATES = {"rdfs:subClassOf", "subClassOf", "subclassOf"}


@dataclass(frozen=True)
class AxiomRow:
    line_number: int
    pattern: str
    subject: str
    predicate: str
    object: str
    axiom_numbers: tuple[int, ...]
    rationale: str
    symmetry: str
    transitivity: str
    reflexivity: str


@dataclass
class OntologyContext:
    graph: Graph
    prefixes: dict[str, str]
    terms: dict[str, URIRef]
    classes: set[str]
    object_properties: set[str]
    datatype_properties: set[str]
    has_existing_graph: bool = False

    @property
    def default_entity_namespace(self) -> Namespace:
        if "aplo-ont" in self.prefixes:
            return Namespace(self.prefixes["aplo-ont"])
        if "" in self.prefixes:
            return Namespace(self.prefixes[""])
        return Namespace(next(iter(self.prefixes.values())))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate tabular axiom numbers into OWL/Turtle axioms with rdflib."
    )
    parser.add_argument(
        "--axioms",
        default="axioms/axioms.csv",
        type=Path,
        help="CSV file containing Subject, Predicate, Object, and Axioms applicable.",
    )
    parser.add_argument(
        "--existing",
        type=Path,
        help="Optional existing Turtle OWL file used for prefix/name matching.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path for the generated OWL/Turtle output.",
    )
    parser.add_argument(
        "--pattern",
        action="append",
        help=(
            "Optional pattern filter. May be repeated. Matches semicolon-separated "
            "Pattern cells case-insensitively."
        ),
    )
    parser.add_argument(
        "--property-characteristics",
        action="store_true",
        help="Also emit symmetric/asymmetric, transitive, reflexive/irreflexive property types.",
    )
    return parser.parse_args()


def parse_axiom_numbers(value: str) -> tuple[int, ...]:
    numbers = []
    for part in re.split(r"[,;\s]+", value.strip()):
        if not part:
            continue
        try:
            numbers.append(int(part))
        except ValueError as exc:
            raise ValueError(f"Invalid axiom number {part!r}") from exc
    return tuple(numbers)


def load_axiom_rows(path: Path) -> list[AxiomRow]:
    rows: list[AxiomRow] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"Pattern", "Subject", "Predicate",
                    "Object", "Axioms applicable"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(
                f"{path} is missing required columns: {', '.join(sorted(missing))}")

        for index, row in enumerate(reader, start=2):
            rows.append(
                AxiomRow(
                    line_number=index,
                    pattern=(row.get("Pattern") or "").strip(),
                    subject=(row.get("Subject") or "").strip(),
                    predicate=(row.get("Predicate") or "").strip(),
                    object=(row.get("Object") or "").strip(),
                    axiom_numbers=parse_axiom_numbers(
                        row.get("Axioms applicable") or ""),
                    rationale=(row.get("Rationale") or "").strip(),
                    symmetry=(row.get("Symmetry/Asymmetry (S/A)")
                              or "").strip().upper(),
                    transitivity=(row.get("Transitivity (T/F)")
                                  or "").strip().upper(),
                    reflexivity=(
                        row.get("Reflexivity/irreflexivity (R/I)") or "").strip().upper(),
                )
            )
    return rows


def build_graph() -> Graph:
    graph = Graph()
    for prefix, namespace in DEFAULT_PREFIXES.items():
        graph.bind(prefix, Namespace(namespace), replace=True)
    return graph


def local_name(term: str | URIRef) -> str:
    value = str(term)
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    if "#" in value:
        return value.rsplit("#", 1)[1]
    if "/" in value:
        return value.rstrip("/").rsplit("/", 1)[1]
    if ":" in value:
        return value.split(":", 1)[1]
    return value


def namespace_prefixes(graph: Graph) -> dict[str, str]:
    prefixes = dict(DEFAULT_PREFIXES)
    for prefix, namespace in graph.namespaces():
        prefixes[prefix or ""] = str(namespace)
    return prefixes


def is_prefixed(term: str) -> bool:
    return bool(re.match(r"^[A-Za-z][\w-]*:[^\s]+$", term))


def is_datatype(term: str) -> bool:
    if term in DATATYPE_TERMS:
        return True
    if is_prefixed(term):
        return term.split(":", 1)[0] in DATATYPE_PREFIXES and term != "rdfs:Class"
    return False


def uri_for_prefixed(term: str, prefixes: dict[str, str]) -> URIRef:
    prefix, name = term.split(":", 1)
    if prefix not in prefixes:
        raise ValueError(f"Unknown prefix {prefix!r} in term {term!r}")
    return URIRef(prefixes[prefix] + name)


def resolve(term: str, ctx: OntologyContext) -> URIRef:
    term = term.strip()
    if not term:
        raise ValueError("Cannot resolve an empty term")
    if term.startswith("<") and term.endswith(">"):
        return URIRef(term[1:-1])
    if is_prefixed(term):
        return uri_for_prefixed(term, ctx.prefixes)
    if term in ctx.terms:
        return ctx.terms[term]
    return URIRef(str(ctx.default_entity_namespace) + term)


def collect_terms(graph: Graph) -> tuple[dict[str, URIRef], set[str], set[str], set[str]]:
    terms: dict[str, URIRef] = {}
    classes: set[str] = set()
    object_properties: set[str] = set()
    datatype_properties: set[str] = set()

    for subject in set(graph.subjects()) | set(graph.objects()):
        if isinstance(subject, URIRef):
            terms.setdefault(local_name(subject), subject)

    for subject, _, kind in graph.triples((None, RDF.type, None)):
        if not isinstance(subject, URIRef):
            continue
        name = local_name(subject)
        terms[name] = subject
        if kind == OWL.Class:
            classes.add(name)
        elif kind == OWL.ObjectProperty:
            object_properties.add(name)
        elif kind == OWL.DatatypeProperty:
            datatype_properties.add(name)

    for subject, label in graph.subject_objects(RDFS.label):
        if isinstance(subject, URIRef) and isinstance(label, Literal):
            label_text = str(label)
            if re.fullmatch(r"[A-Za-z_][\w.-]*", label_text):
                terms.setdefault(label_text, subject)

    return terms, classes, object_properties, datatype_properties


def parse_existing_ontology(path: Path | None) -> OntologyContext:
    graph = build_graph()
    has_existing_graph = path is not None
    if path is not None:
        graph.parse(path, format="turtle")

    prefixes = namespace_prefixes(graph)
    for prefix, namespace in prefixes.items():
        graph.bind(prefix, Namespace(namespace), replace=True)
    terms, classes, object_properties, datatype_properties = collect_terms(
        graph)
    return OntologyContext(
        graph=graph,
        prefixes=prefixes,
        terms=terms,
        classes=classes,
        object_properties=object_properties,
        datatype_properties=datatype_properties,
        has_existing_graph=has_existing_graph,
    )


def pattern_matches(row: AxiomRow, filters: Iterable[str] | None) -> bool:
    if not filters:
        return True
    wanted = {item.strip().casefold() for item in filters}
    row_patterns = {item.strip().casefold() for item in row.pattern.split(";")}
    return bool(wanted.intersection(row_patterns))


def add_restriction(
    graph: Graph,
    property_: URIRef | BNode,
    predicate: URIRef,
    value: URIRef | Literal,
    filler: URIRef | None = None,
) -> BNode:
    restriction = BNode()
    graph.add((restriction, RDF.type, OWL.Restriction))
    graph.add((restriction, OWL.onProperty, property_))
    graph.add((restriction, predicate, value))
    if filler is not None:
        graph.add((restriction, OWL.onDataRange if is_datatype_iri(
            filler) else OWL.onClass, filler))
    return restriction


def inverse_property_node(graph: Graph, property_: URIRef) -> BNode:
    node = BNode()
    graph.add((node, OWL.inverseOf, property_))
    return node


def cardinality(value: int) -> Literal:
    return Literal(value, datatype=XSD.nonNegativeInteger)


def is_datatype_iri(iri: URIRef) -> bool:
    value = str(iri)
    return (
        value.startswith(str(XSD))
        or value in {str(RDFS.Literal), str(RDF.langString)}
    )


def add_axiom(graph: Graph, row: AxiomRow, number: int, ctx: OntologyContext) -> bool:
    subject = resolve(row.subject, ctx)
    predicate = resolve(row.predicate, ctx)
    obj = resolve(row.object, ctx)

    if number == 1:
        graph.add((subject, RDFS.subClassOf, obj))
    elif number == 2:
        graph.add((subject, OWL.disjointWith, obj))
    elif number == 3:
        graph.add((predicate, RDFS.domain, subject))
    elif number == 4:
        restriction = add_restriction(
            graph, predicate, OWL.someValuesFrom, obj)
        graph.add((restriction, RDFS.subClassOf, subject))
    elif number == 5:
        graph.add((predicate, RDFS.range, obj))
    elif number == 6:
        restriction = add_restriction(graph, predicate, OWL.allValuesFrom, obj)
        graph.add((subject, RDFS.subClassOf, restriction))
    elif number == 7:
        restriction = add_restriction(
            graph, predicate, OWL.someValuesFrom, obj)
        graph.add((subject, RDFS.subClassOf, restriction))
    elif number == 8:
        if is_datatype(row.object):
            return False
        restriction = add_restriction(graph, inverse_property_node(
            graph, predicate), OWL.someValuesFrom, subject)
        graph.add((obj, RDFS.subClassOf, restriction))
    elif number == 9:
        graph.add((predicate, RDF.type, OWL.FunctionalProperty))
    elif number == 10:
        restriction = add_restriction(
            graph,
            predicate,
            OWL.maxQualifiedCardinality,
            cardinality(1),
            obj,
        )
        graph.add((OWL.Thing, RDFS.subClassOf, restriction))
    elif number == 11:
        restriction = add_restriction(
            graph, predicate, OWL.maxCardinality, cardinality(1))
        graph.add((subject, RDFS.subClassOf, restriction))
    elif number == 12:
        restriction = add_restriction(
            graph,
            predicate,
            OWL.maxQualifiedCardinality,
            cardinality(1),
            obj,
        )
        graph.add((subject, RDFS.subClassOf, restriction))
    elif number == 13:
        graph.add((predicate, RDF.type, OWL.InverseFunctionalProperty))
    elif number == 14:
        if is_datatype(row.subject):
            return False
        restriction = add_restriction(
            graph,
            inverse_property_node(graph, predicate),
            OWL.maxQualifiedCardinality,
            cardinality(1),
            subject,
        )
        graph.add((OWL.Thing, RDFS.subClassOf, restriction))
    elif number == 15:
        if is_datatype(row.object):
            return False
        restriction = add_restriction(
            graph,
            inverse_property_node(graph, predicate),
            OWL.maxCardinality,
            cardinality(1),
        )
        graph.add((obj, RDFS.subClassOf, restriction))
    elif number == 16:
        if is_datatype(row.object) or is_datatype(row.subject):
            return False
        restriction = add_restriction(
            graph,
            inverse_property_node(graph, predicate),
            OWL.maxQualifiedCardinality,
            cardinality(1),
            subject,
        )
        graph.add((obj, RDFS.subClassOf, restriction))
    elif number == 17:
        restriction = add_restriction(
            graph,
            predicate,
            OWL.minQualifiedCardinality,
            cardinality(0),
            obj,
        )
        graph.add((subject, RDFS.subClassOf, restriction))
    else:
        raise ValueError(
            f"Unsupported axiom number {number} on CSV line {row.line_number}")
    return True


def declaration_plan(rows: list[AxiomRow], ctx: OntologyContext) -> dict[str, set[URIRef]]:
    plan: dict[str, set[URIRef]] = {
        "classes": set(),
        "object_properties": set(),
        "datatype_properties": set(),
    }
    for row in rows:
        subject = resolve(row.subject, ctx)
        obj = resolve(row.object, ctx)
        if not is_datatype(row.subject) and local_name(subject) not in ctx.classes:
            plan["classes"].add(subject)
        if not is_datatype(row.object) and local_name(obj) not in ctx.classes:
            plan["classes"].add(obj)

        if row.predicate in SUBCLASS_PREDICATES:
            continue
        predicate = resolve(row.predicate, ctx)
        if is_datatype(row.object):
            if local_name(predicate) not in ctx.datatype_properties:
                plan["datatype_properties"].add(predicate)
        elif local_name(predicate) not in ctx.object_properties:
            plan["object_properties"].add(predicate)
    return plan


def add_declarations(graph: Graph, rows: list[AxiomRow], ctx: OntologyContext) -> dict[str, set[URIRef]]:
    plan = declaration_plan(rows, ctx)
    for class_ in plan["classes"]:
        graph.add((class_, RDF.type, OWL.Class))
    for property_ in plan["object_properties"]:
        graph.add((property_, RDF.type, OWL.ObjectProperty))
    for property_ in plan["datatype_properties"]:
        graph.add((property_, RDF.type, OWL.DatatypeProperty))
    return plan


def graph_term(graph: Graph, term: URIRef) -> str:
    try:
        return graph.qname(term)
    except Exception:
        return str(term)


def print_declaration_log(ctx: OntologyContext, plan: dict[str, set[URIRef]]) -> None:
    if not ctx.has_existing_graph or not any(plan.values()):
        return

    labels = {
        "classes": "classes",
        "object_properties": "object properties",
        "datatype_properties": "datatype properties",
    }
    print("Declared missing CSV terms in existing ontology:")
    for key in ("classes", "object_properties", "datatype_properties"):
        values = sorted(graph_term(ctx.graph, term) for term in plan[key])
        if values:
            print(f"  {labels[key]}: {', '.join(values)}")


def add_characteristics(graph: Graph, row: AxiomRow, ctx: OntologyContext) -> None:
    if row.predicate in SUBCLASS_PREDICATES or is_datatype(row.object):
        return
    predicate = resolve(row.predicate, ctx)
    if row.symmetry == "S":
        graph.add((predicate, RDF.type, OWL.SymmetricProperty))
    elif row.symmetry == "A":
        graph.add((predicate, RDF.type, OWL.AsymmetricProperty))
    if row.transitivity == "T":
        graph.add((predicate, RDF.type, OWL.TransitiveProperty))
    if row.reflexivity == "R":
        graph.add((predicate, RDF.type, OWL.ReflexiveProperty))
    elif row.reflexivity == "I":
        graph.add((predicate, RDF.type, OWL.IrreflexiveProperty))


def select_rows(rows: list[AxiomRow], ctx: OntologyContext, args: argparse.Namespace) -> list[AxiomRow]:
    selected = []
    for row in rows:
        if not pattern_matches(row, args.pattern):
            continue
        selected.append(row)
    return selected


def add_rows_to_graph(
    rows: list[AxiomRow],
    ctx: OntologyContext,
    include_declarations: bool,
    include_characteristics: bool,
) -> int:
    graph = ctx.graph
    if include_declarations:
        add_declarations(graph, rows, ctx)

    emitted_count = 0
    for row in rows:
        for number in row.axiom_numbers:
            if add_axiom(graph, row, number, ctx):
                emitted_count += 1
        if include_characteristics:
            add_characteristics(graph, row, ctx)
    return emitted_count


def main() -> int:
    args = parse_args()
    rows = load_axiom_rows(args.axioms)
    ctx = parse_existing_ontology(args.existing)
    selected = select_rows(rows, ctx, args)
    if not selected:
        raise SystemExit(
            "No axiom rows matched the selected filters/existing ontology.")

    include_declarations = True
    plan = declaration_plan(selected, ctx)
    print_declaration_log(ctx, plan)
    emitted = add_rows_to_graph(
        selected,
        ctx,
        include_declarations=include_declarations,
        include_characteristics=args.property_characteristics,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    ctx.graph.serialize(destination=args.output, format="turtle")

    print(f"Wrote {args.output}")
    print(f"Rows translated: {len(selected)}")
    print(f"Axioms emitted: {emitted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
