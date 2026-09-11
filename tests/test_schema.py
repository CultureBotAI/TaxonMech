"""Schema-level checks: it loads, and the corpus only uses values it declares."""

from __future__ import annotations

import yaml
from linkml_runtime.utils.schemaview import SchemaView


def _schema(schema_path):
    return SchemaView(str(schema_path))


def test_schema_loads_with_its_imports(schema_path):
    view = _schema(schema_path)
    assert "TaxonRecord" in view.all_classes()
    # The vendored mech_shared module must resolve, or Discussion/Dataset
    # silently disappear from the record shape.
    assert "Discussion" in view.all_classes()
    assert "Dataset" in view.all_classes()


def test_taxon_record_is_the_only_tree_root(schema_path):
    view = _schema(schema_path)
    roots = [name for name, cls in view.all_classes().items() if cls.tree_root]
    assert roots == ["TaxonRecord"]


def test_vendored_canon_ref_is_an_immutable_claw_commit(repo_root):
    """mech_shared.yaml and history.yaml are vendored from claw at the commit in
    scripts/.vendored_canon_ref, and scripts/check_vendored_sync.sh compares
    the bytes against that commit in CI."""
    ref = (repo_root / "scripts" / ".vendored_canon_ref").read_text().strip()
    assert len(ref) == 40 and all(c in "0123456789abcdef" for c in ref), ref
    for vendored in ("mech_shared.yaml", "history.yaml"):
        assert (repo_root / "src" / "taxonmech" / "schema" / vendored).is_file()


def _permissible(view, enum_name: str) -> set[str]:
    return set(view.get_enum(enum_name).permissible_values)


def test_corpus_uses_only_declared_enum_values(schema_path, records):
    view = _schema(schema_path)
    checks = [
        ("rank", "TaxonRankEnum",
         lambda d: [d.get("rank")] + [a.get("rank") for a in d.get("lineage") or []]),
        ("taxon_domain", "TaxonDomainEnum", lambda d: [d.get("taxon_domain")]),
        ("mapping_status", "MappingStatusEnum", lambda d: [d.get("mapping_status")]),
        ("grounding_status", "GroundingStatusEnum", lambda d: [d.get("grounding_status")]),
        ("source", "TaxonSourceEnum",
         lambda d: [a.get("source") for a in d.get("source_attestations") or []]
         + [m.get("source") for m in d.get("taxonomy_mappings") or []]
         + [s.get("source") for s in d.get("strains") or []]
         + [g.get("source") for s in d.get("strains") or [] for g in s.get("genome_assemblies") or []]
         + [g.get("source") for s in d.get("strains") or [] for g in s.get("genome_records") or []]
         + [n.get("source") for n in d.get("nomenclature") or []]),
        ("assertion_unit", "AssertionUnitEnum",
         lambda d: [a.get("assertion_unit") for a in d.get("source_attestations") or []]),
        ("synonym_type", "SynonymTypeEnum",
         lambda d: [s.get("synonym_type") for s in d.get("synonyms") or []]),
        ("node_type", "CausalNodeTypeEnum",
         lambda d: [n.get("node_type") for g in d.get("causal_graphs") or [] for n in g.get("nodes") or []]),
    ]
    for field, enum_name, extract in checks:
        allowed = _permissible(view, enum_name)
        bad = set()
        for _, doc in records:
            for value in extract(doc):
                if value is not None and value not in allowed:
                    bad.add(value)
        assert not bad, f"{field}: values not in {enum_name}: {sorted(bad)}"


def test_domain_directories_match_the_enum(repo_root, schema_path):
    """The filesystem layout is derived from TaxonDomainEnum."""
    view = _schema(schema_path)
    allowed = {v.lower() for v in _permissible(view, "TaxonDomainEnum")}
    taxa = repo_root / "data" / "taxa"
    if not taxa.exists():
        return
    unexpected = {d.name for d in taxa.iterdir() if d.is_dir()} - allowed
    assert not unexpected, f"domain directories not in the enum: {sorted(unexpected)}"


def test_schema_prefixes_cover_every_curie_in_the_corpus(schema_path, records):
    """A CURIE whose prefix the schema does not declare cannot be expanded to a
    URI, so it is not resolvable by any downstream consumer."""
    declared = set(yaml.safe_load(schema_path.read_text(encoding="utf-8"))["prefixes"])
    used = set()

    def add(curie):
        if isinstance(curie, str) and ":" in curie and not curie.startswith(("http://", "https://")):
            used.add(curie.split(":", 1)[0])

    for _, doc in records:
        add(doc["identifier"])
        add(doc.get("parent_taxon"))
        for key in ("xrefs", "replaces"):
            for c in doc.get(key) or []:
                add(c)
        for a in doc.get("lineage") or []:
            add(a.get("taxon_id"))
        for n in doc.get("nomenclature") or []:
            add(n.get("name_id"))
            for key in ("type_strain_designations", "publications", "sequence_accessions"):
                for c in n.get(key) or []:
                    add(c)
        for m in doc.get("taxonomy_mappings") or []:
            add(m.get("source_id"))
        for s in doc.get("strains") or []:
            add(s.get("strain_id"))
            add(s.get("source_id"))
            for g in s.get("genome_assemblies") or []:
                add(g.get("assembly_id"))
                add(g.get("source_id"))
                add(g.get("taxon_id"))
            for g in s.get("genome_records") or []:
                add(g.get("genome_id"))
                add(g.get("source_id"))
                add(g.get("taxon_id"))
            for c in s.get("culture_collection_ids") or []:
                add(c)
        for g in doc.get("causal_graphs") or []:
            for n in g.get("nodes") or []:
                add(n.get("grounding"))
            for e in g.get("edges") or []:
                add(e.get("predicate_id"))
    missing = used - declared
    assert not missing, f"prefixes used in the corpus but undeclared in the schema: {sorted(missing)}"
