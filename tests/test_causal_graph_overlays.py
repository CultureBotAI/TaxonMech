"""Tests for maintained curation/causal_graphs/ overlays, structured GENE_OR_PROTEIN
scope slots, OAK grounding prefix coverage, and granular trait edge extraction (#78)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from linkml_runtime.utils.schemaview import SchemaView

from taxonmech.extract import TRAIT_EDGE_FIELDS, extract_taxon_trait_edges
from taxonmech.seed import (
    Concept,
    Inventory,
    build_concepts,
    build_document,
    load_causal_graphs,
)
from taxonmech.validation.write_validated import emit_taxon_yaml, write_validated_taxon

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "src" / "taxonmech" / "schema" / "taxonmech.yaml"
TEMPLATES_DIR = REPO_ROOT / "src" / "taxonmech" / "templates"
ID_LABEL_CONF = REPO_ROOT / "conf" / "id_label_targets.yaml"


def _load_id_label_validator():
    script_path = REPO_ROOT / "scripts" / "validate_id_label_correspondence.py"
    spec = importlib.util.spec_from_file_location("validate_id_label_correspondence", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


STAGE2_STAGE3_EXEMPLAR_OVERLAYS: dict[str, dict] = {
    "NCBITaxon:562": {
        "label": "Escherichia coli",
        "rank": "SPECIES",
        "parent_id": "NCBITaxon:561",
        "domain": "BACTERIA",
        "overlay": {
            "identifier": "NCBITaxon:562",
            "causal_graphs": [
                {
                    "graph_id": "ecoli-lactose-catabolism",
                    "title": "Escherichia coli beta-galactosidase lactose catabolism",
                    "description": (
                        "Beta-galactosidase LacZ hydrolyzes beta-D-galactosides in "
                        "Escherichia coli (reference strain K-12 MG1655)."
                    ),
                    "nodes": [
                        {
                            "node_id": "lacZ",
                            "label": "Beta-galactosidase LacZ",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:P00722",
                            "xrefs": ["EC:3.2.1.23"],
                            "organism_taxon_id": "NCBITaxon:83333",
                            "proteome_id": "UP:UP000000625",
                            "gene_symbol": "lacZ",
                            "locus_tag": "b0344",
                            "sequence_length": 1024,
                            "sequence_crc64": "C23D36CB46AD9E78",
                            "sequence_version": 2,
                            "entry_status": "SWISS_PROT",
                        },
                        {
                            "node_id": "lactose-catabolism",
                            "label": "lactose catabolic process",
                            "node_type": "BIOLOGICAL_PROCESS",
                            "grounding": "GO:0005988",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "lacz-lactose-catabolism",
                            "subject": "lacZ",
                            "predicate": "capable of",
                            "predicate_id": "RO:0002215",
                            "object": "lactose-catabolism",
                            "evidence": [
                                {
                                    "reference": "PMID:9278503",
                                    "snippet": (
                                        "Complete genome sequence of Escherichia coli K-12 "
                                        "MG1655 annotates the lacZYA lactose operon."
                                    ),
                                }
                            ],
                        }
                    ],
                }
            ],
            "curation_history": [
                {
                    "timestamp": "2026-10-22T06:00:00Z",
                    "action": "UPDATED",
                    "agent": "stage6-canary",
                    "summary": "Added verified LacZ causal graph overlay for NCBITaxon:562.",
                }
            ],
        },
    },
    "NCBITaxon:1423": {
        "label": "Bacillus subtilis",
        "rank": "SPECIES",
        "parent_id": "NCBITaxon:653685",
        "domain": "BACTERIA",
        "overlay": {
            "identifier": "NCBITaxon:1423",
            "causal_graphs": [
                {
                    "graph_id": "bsubtilis-sporulation-spo0a",
                    "title": "Bacillus subtilis Spo0A master regulation of endospore formation",
                    "nodes": [
                        {
                            "node_id": "spo0A",
                            "label": "Stage 0 sporulation protein A",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:P06534",
                            "organism_taxon_id": "NCBITaxon:224308",
                            "strain_id": "kgmicrobe.strain:bacdive_1187",
                            "proteome_id": "UP:UP000001570",
                            "gene_symbol": "spo0A",
                            "locus_tag": "BSU_24220",
                            "sequence_length": 267,
                            "sequence_crc64": "9FEAA90BA04A7C3A",
                            "sequence_version": 2,
                            "entry_status": "SWISS_PROT",
                        },
                        {
                            "node_id": "endospore-formation",
                            "label": "endospore formation",
                            "node_type": "BIOLOGICAL_PROCESS",
                            "grounding": "GO:0034301",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "spo0a-endospore-formation",
                            "subject": "spo0A",
                            "predicate": "positively regulates",
                            "predicate_id": "RO:0002213",
                            "object": "endospore-formation",
                            "evidence": [
                                {
                                    "reference": "PMID:9384377",
                                    "snippet": (
                                        "Bacillus subtilis 168 genome and Spo0A phosphorelay "
                                        "control initiation of endospore formation."
                                    ),
                                }
                            ],
                        }
                    ],
                }
            ],
        },
    },
    "NCBITaxon:287": {
        "label": "Pseudomonas aeruginosa",
        "rank": "SPECIES",
        "parent_id": "NCBITaxon:136841",
        "domain": "BACTERIA",
        "overlay": {
            "identifier": "NCBITaxon:287",
            "causal_graphs": [
                {
                    "graph_id": "paeruginosa-pyocyanin-biosynthesis",
                    "title": "Pseudomonas aeruginosa PhzM/PhzS pyocyanin biosynthesis",
                    "nodes": [
                        {
                            "node_id": "phzM",
                            "label": "Phenazine-specific methyltransferase PhzM",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:Q9HWH2",
                            "xrefs": ["EC:2.1.1.329"],
                            "organism_taxon_id": "NCBITaxon:208964",
                            "proteome_id": "UP:UP000002438",
                            "gene_symbol": "phzM",
                            "locus_tag": "PA4209",
                            "sequence_length": 334,
                            "sequence_crc64": "2DF8D219E1A2BE7B",
                            "sequence_version": 1,
                            "entry_status": "SWISS_PROT",
                        },
                        {
                            "node_id": "pyocyanin-biosynthesis",
                            "label": "pyocyanin biosynthetic process",
                            "node_type": "PATHWAY",
                            "grounding": "GO:0042867",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "phzm-pyocyanin-biosynthesis",
                            "subject": "phzM",
                            "predicate": "capable of",
                            "predicate_id": "RO:0002215",
                            "object": "pyocyanin-biosynthesis",
                            "evidence": [
                                {
                                    "reference": "PMID:11566984",
                                    "snippet": (
                                        "PhzM and PhzS convert phenazine-1-carboxylic acid "
                                        "to pyocyanin in Pseudomonas aeruginosa PAO1."
                                    ),
                                }
                            ],
                        }
                    ],
                }
            ],
        },
    },
    "NCBITaxon:2190": {
        "label": "Methanocaldococcus jannaschii",
        "rank": "SPECIES",
        "parent_id": "NCBITaxon:2189",
        "domain": "ARCHAEA",
        "overlay": {
            "identifier": "NCBITaxon:2190",
            "causal_graphs": [
                {
                    "graph_id": "mjannaschii-methanogenesis-mcra",
                    "title": "Methanocaldococcus jannaschii methyl-coenzyme M reductase methanogenesis",
                    "nodes": [
                        {
                            "node_id": "mcrA",
                            "label": "Methyl-coenzyme M reductase I subunit alpha",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:Q58256",
                            "xrefs": ["EC:2.8.4.1"],
                            "organism_taxon_id": "NCBITaxon:243232",
                            "proteome_id": "UP:UP000000805",
                            "gene_symbol": "mcrA",
                            "locus_tag": "MJ_0846",
                            "sequence_length": 552,
                            "sequence_crc64": "41B3F8A21D7A4F48",
                            "sequence_version": 1,
                            "entry_status": "SWISS_PROT",
                        },
                        {
                            "node_id": "methanogenesis",
                            "label": "methanogenesis",
                            "node_type": "PATHWAY",
                            "grounding": "GO:0015948",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "mcra-methanogenesis",
                            "subject": "mcrA",
                            "predicate": "capable of",
                            "predicate_id": "RO:0002215",
                            "object": "methanogenesis",
                            "evidence": [
                                {
                                    "reference": "PMID:8688087",
                                    "snippet": (
                                        "Complete genome sequence of the methanogenic archaeon "
                                        "Methanococcus jannaschii DSM 2661 encodes McrABG."
                                    ),
                                }
                            ],
                        }
                    ],
                }
            ],
        },
    },
    "NCBITaxon:1859096": {
        "label": "Cryptococcus deuterogattii",
        "rank": "SPECIES",
        "parent_id": "NCBITaxon:5206",
        "domain": "EUKARYOTA",
        "overlay": {
            "identifier": "NCBITaxon:1859096",
            "causal_graphs": [
                {
                    "graph_id": "cdeuterogattii-capsule-cap59",
                    "title": "Cryptococcus deuterogattii R265 Cap59 polysaccharide capsule assembly",
                    "nodes": [
                        {
                            "node_id": "CAP59",
                            "label": "Capsule-associated protein CAP59",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:E6RCZ6",
                            "organism_taxon_id": "NCBITaxon:294750",
                            "proteome_id": "UP:UP000029445",
                            "gene_symbol": "CAP59",
                            "locus_tag": "CNBG_0565",
                            "sequence_length": 458,
                            "sequence_crc64": "D658F7CC1C6E1CA7",
                            "sequence_version": 1,
                            "entry_status": "TREMBL",
                        },
                        {
                            "node_id": "capsule-organization",
                            "label": "external encapsulating structure organization",
                            "node_type": "BIOLOGICAL_PROCESS",
                            "grounding": "GO:0045229",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "cap59-capsule-organization",
                            "subject": "CAP59",
                            "predicate": "capable of",
                            "predicate_id": "RO:0002215",
                            "object": "capsule-organization",
                            "evidence": [
                                {
                                    "reference": "PMID:25593184",
                                    "snippet": (
                                        "Comparative genomics of Cryptococcus gattii VGII R265 "
                                        "identifies conserved capsule biosynthesis determinants."
                                    ),
                                }
                            ],
                        }
                    ],
                }
            ],
        },
    },
}


def _make_minimal_inventory(
    causal_graphs: dict[str, list[dict]],
    causal_graph_events: dict[str, list[dict]],
) -> Inventory:
    taxa = {}
    parents = {}
    ranks = {}
    for tid, spec in STAGE2_STAGE3_EXEMPLAR_OVERLAYS.items():
        taxa[tid] = {
            "taxon_id": tid,
            "label": spec["label"],
            "rank": spec["rank"],
            "parent_id": spec["parent_id"],
            "genetic_code": "11" if spec["domain"] != "EUKARYOTA" else "1",
            "exact_synonyms": "",
            "related_synonyms": "",
            "broad_synonyms": "",
            "attested_by": "ncbitaxon|bacdive",
            "retired_into": "",
            "taxonomy_snapshot": "2026-03-01T00:00:00Z",
        }
        parents[tid] = spec["parent_id"]
        ranks[tid] = spec["rank"]
    root_map = {
        "NCBITaxon:561": ("Escherichia", "GENUS", "NCBITaxon:2"),
        "NCBITaxon:653685": ("Bacillus subtilis group", "SPECIES_GROUP", "NCBITaxon:2"),
        "NCBITaxon:136841": ("Pseudomonas aeruginosa group", "SPECIES_GROUP", "NCBITaxon:2"),
        "NCBITaxon:2189": ("Methanocaldococcus", "GENUS", "NCBITaxon:2157"),
        "NCBITaxon:5206": ("Cryptococcus", "GENUS", "NCBITaxon:2759"),
        "NCBITaxon:2": ("Bacteria", "DOMAIN", ""),
        "NCBITaxon:2157": ("Archaea", "DOMAIN", ""),
        "NCBITaxon:2759": ("Eukaryota", "DOMAIN", ""),
    }
    for tid, (lbl, rnk, par) in root_map.items():
        taxa[tid] = {
            "taxon_id": tid,
            "label": lbl,
            "rank": rnk,
            "parent_id": par,
            "genetic_code": "11",
            "exact_synonyms": "",
            "related_synonyms": "",
            "broad_synonyms": "",
            "attested_by": "ncbitaxon",
            "retired_into": "",
            "taxonomy_snapshot": "2026-03-01T00:00:00Z",
        }
        parents[tid] = par
        ranks[tid] = rnk

    return Inventory(
        taxa=taxa,
        gtdb={},
        lpsn={},
        lpsn_by_taxon={},
        strains={tid: [] for tid in STAGE2_STAGE3_EXEMPLAR_OVERLAYS},
        cc_strains={},
        media={},
        gold={},
        madin={},
        bacto={},
        causal_graphs=causal_graphs,
        causal_graph_events=causal_graph_events,
    )


def test_five_exemplar_causal_graph_overlays_roundtrip_and_render(tmp_path):
    """Exercise all 5 Stage 2 / Stage 3 exemplars through load_causal_graphs,
    build_document, LinkML write_validated_taxon, emit_taxon_yaml roundtrip,
    id_label_targets prefix config, and HTML template rendering (#78)."""
    overlays_dir = tmp_path / "causal_graphs"
    overlays_dir.mkdir()
    for tid, spec in STAGE2_STAGE3_EXEMPLAR_OVERLAYS.items():
        slug = tid.replace(":", "_")
        (overlays_dir / f"{slug}.yaml").write_text(
            yaml.safe_dump(spec["overlay"], sort_keys=False), encoding="utf-8"
        )

    graphs, events = load_causal_graphs(overlays_dir)
    assert set(graphs) == set(STAGE2_STAGE3_EXEMPLAR_OVERLAYS)
    assert "NCBITaxon:562" in events and len(events["NCBITaxon:562"]) == 1

    inventory = _make_minimal_inventory(graphs, events)
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["curie_url"] = lambda c, root="": f"https://example.org/{c}"
    env.filters["external_url"] = lambda v: v
    env.filters["deposit_label"] = lambda v: str(v).removeprefix("kgmicrobe.strain:")
    template = env.get_template("taxon-content.html")

    id_label_mod = _load_id_label_validator()
    id_label_cfg = yaml.safe_load(ID_LABEL_CONF.read_text(encoding="utf-8"))
    ignored_prefixes = {p.lower() for p in id_label_cfg.get("ignored_prefixes", [])}
    configured_adapters = {p.lower() for p in id_label_cfg.get("adapters", {})}
    known_prefixes = ignored_prefixes | configured_adapters

    declared_schema_prefixes = set(
        yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))["prefixes"]
    )

    out_taxa_dir = tmp_path / "taxa"
    out_taxa_dir.mkdir()
    concepts = {
        c.identifier: c
        for c in build_concepts(inventory, list(STAGE2_STAGE3_EXEMPLAR_OVERLAYS))
    }

    for tid, _spec in STAGE2_STAGE3_EXEMPLAR_OVERLAYS.items():
        concept = concepts[tid]
        assert isinstance(concept, Concept)
        doc = build_document(concept, inventory)
        assert "causal_graphs" in doc
        assert len(doc["causal_graphs"]) == 1

        node0 = doc["causal_graphs"][0]["nodes"][0]
        assert node0["node_type"] == "GENE_OR_PROTEIN"
        assert node0["grounding"].startswith("UniProtKB:")
        assert node0["organism_taxon_id"].startswith("NCBITaxon:")
        assert node0["proteome_id"].startswith("UP:UP")
        assert node0["entry_status"] in ("SWISS_PROT", "TREMBL")

        # Validate & write via write_validated_taxon (LinkML validation gate)
        out_path = out_taxa_dir / f"{tid.replace(':', '_')}.yaml"
        write_validated_taxon(doc, out_path)

        # Verify byte-for-byte reproducibility (verify_corpus.py contract)
        expected_yaml = emit_taxon_yaml(build_document(concept, inventory))
        actual_yaml = out_path.read_text(encoding="utf-8")
        assert actual_yaml == expected_yaml

        # Verify every CURIE prefix in causal_graphs is declared in schema and known to id_label_targets
        for g in doc["causal_graphs"]:
            for n in g["nodes"]:
                for curie in [
                    n.get("grounding"),
                    n.get("organism_taxon_id"),
                    n.get("strain_id"),
                    n.get("proteome_id"),
                    *(n.get("xrefs") or []),
                ]:
                    if curie and ":" in curie:
                        pfx = curie.split(":", 1)[0]
                        assert pfx in declared_schema_prefixes, f"undeclared schema prefix: {pfx}"
                        assert pfx.lower() in known_prefixes, f"unknown id_label prefix: {pfx}"
            for e in g["edges"]:
                pfx = e["predicate_id"].split(":", 1)[0]
                assert pfx in declared_schema_prefixes
                assert pfx.lower() in known_prefixes

        # Verify HTML rendering via taxon-content.html includes causal graph & grounding
        html = template.render(
            r=doc,
            root="../..",
            initial_strains=doc.get("strains") or [],
            strain_overflow=False,
            strain_shard_path=None,
            strain_page_size=200,
        )
        assert "Causal graphs" in html
        assert doc["causal_graphs"][0]["title"] in html
        assert node0["label"] in html
        assert id_label_mod is not None


def test_load_causal_graphs_rejects_invalid_or_duplicate_overlays(tmp_path):
    """load_causal_graphs raises SystemExit on missing identifier, duplicate identifier,
    or empty causal_graphs."""
    bad_dir = tmp_path / "bad_missing"
    bad_dir.mkdir()
    (bad_dir / "missing.yaml").write_text("causal_graphs: []\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="missing or invalid 'identifier'"):
        load_causal_graphs(bad_dir)

    dup_dir = tmp_path / "bad_dup"
    dup_dir.mkdir()
    (dup_dir / "a.yaml").write_text(
        "identifier: NCBITaxon:562\ncausal_graphs:\n  - graph_id: g1\n", encoding="utf-8"
    )
    (dup_dir / "b.yaml").write_text(
        "identifier: NCBITaxon:562\ncausal_graphs:\n  - graph_id: g2\n", encoding="utf-8"
    )
    with pytest.raises(SystemExit, match="duplicate causal-graph overlay"):
        load_causal_graphs(dup_dir)


def test_extract_taxon_trait_edges_preserves_granular_assertions(tmp_path):
    """extract_taxon_trait_edges retains per-taxon predicates, object CURIEs,
    and literature/knowledge-source provenance without collapsing to counts (#78)."""
    edges_tsv = tmp_path / "edges.tsv"
    edges_tsv.write_text(
        "id\tsubject\tpredicate\tobject\trelation\tpublications\t"
        "primary_knowledge_source\taggregator_knowledge_source\n"
        "e1\tNCBITaxon:562\tbiolink:has_phenotype\tMETPO:1000615\tRO:0002200\t"
        "PMID:1001|PMID:1002\tinfores:madin_etal\tinfores:kg-microbe\n"
        "e2\tNCBITaxon:562\tbiolink:capable_of\tGO:0009061\tRO:0002215\t"
        "PMID:1003\tinfores:bactotraits\tinfores:kg-microbe\n"
        "e3\tNCBITaxon:1423\tMETPO:2000517\tmediadive.medium:1\tMETPO:2000517\t"
        "\tinfores:mediadive\tinfores:kg-microbe\n"
        "e4\tkgmicrobe.strain:bacdive_1\tMETPO:2000517\tmediadive.medium:1\t"
        "METPO:2000517\t\tinfores:mediadive\tinfores:kg-microbe\n",
        encoding="utf-8",
    )
    rows = extract_taxon_trait_edges(edges_tsv, source="MADIN")
    assert len(rows) == 3
    assert list(rows[0].keys()) == TRAIT_EDGE_FIELDS
    assert rows[0]["taxon_id"] == "NCBITaxon:562"
    assert rows[0]["object_id"] == "GO:0009061"
    assert rows[1]["taxon_id"] == "NCBITaxon:562"
    assert rows[1]["object_id"] == "METPO:1000615"
    assert rows[1]["publications"] == "PMID:1001|PMID:1002"
    assert rows[2]["taxon_id"] == "NCBITaxon:1423"
    assert rows[2]["object_id"] == "mediadive.medium:1"
    assert SchemaView(str(SCHEMA_PATH)) is not None


def test_committed_curation_causal_graphs_overlays_load_and_validate():
    """Verify that all committed curation/causal_graphs/*.yaml overlays load cleanly,
    cover the 10 species+strain exemplar records (44 evidence-backed edges), and
    satisfy schema prefix and id_label_targets rules (#78)."""
    overlays_dir = REPO_ROOT / "curation" / "causal_graphs"
    graphs, events = load_causal_graphs(overlays_dir)
    expected_ids = {
        "NCBITaxon:562",
        "NCBITaxon:83333",
        "NCBITaxon:1423",
        "NCBITaxon:224308",
        "NCBITaxon:287",
        "NCBITaxon:208964",
        "NCBITaxon:2190",
        "NCBITaxon:243232",
        "NCBITaxon:1859096",
        "NCBITaxon:294750",
    }
    assert expected_ids.issubset(set(graphs))
    assert expected_ids.issubset(set(events))
    total_edges = sum(
        len(e.get("evidence") or [])
        for tid in expected_ids
        for g in graphs[tid]
        for e in g.get("edges") or []
    )
    assert total_edges >= 44
    edge_count = sum(
        len(g.get("edges") or [])
        for tid in expected_ids
        for g in graphs[tid]
    )
    assert edge_count == 44

