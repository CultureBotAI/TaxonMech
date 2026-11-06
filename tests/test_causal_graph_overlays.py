"""Tests for maintained curation/causal_graphs/ overlays, structured GENE_OR_PROTEIN
scope slots, OAK grounding prefix coverage, and granular trait edge extraction (#78)."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from linkml_runtime.utils.schemaview import SchemaView

from taxonmech.extract import TRAIT_EDGE_FIELDS, extract_taxon_trait_edges
from taxonmech.seed import (
    CAUSAL_NODE_TYPES,
    CURIE_PATTERN,
    EC_NUMBER_PATTERN,
    EDGE_ID_PATTERN,
    EVIDENCE_REFERENCE_PATTERN,
    NCBITAXON_ID_PATTERN,
    PROTEIN_ONLY_NODE_SLOTS,
    PROTEOME_ID_PATTERN,
    UNIPROT_ID_PATTERN,
    UNIPROT_PROTEIN_FIELDS,
    UNIPROT_PROTEINS_PATH,
    Concept,
    Inventory,
    build_concepts,
    build_document,
    load_causal_graphs,
    load_uniprot_proteins,
    validate_causal_graph_proteins,
    validate_causal_graph_structure,
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
                            "sequence_crc64": "9D295EF4CEF90B08",
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
                            "strain_id": "kgmicrobe.strain:bacdive_1156",
                            "proteome_id": "UP:UP000001570",
                            "gene_symbol": "spo0A",
                            "locus_tag": "BSU24220",
                            "sequence_length": 267,
                            "sequence_crc64": "2F4943A5A5061DD9",
                            "sequence_version": 1,
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
                            "xrefs": ["EC:2.1.1.327"],
                            "organism_taxon_id": "NCBITaxon:208964",
                            "proteome_id": "UP:UP000002438",
                            "gene_symbol": "phzM",
                            "locus_tag": "PA4209",
                            "sequence_length": 334,
                            "sequence_crc64": "27D9717ECA12A1B5",
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
                                    "reference": "PMID:11591691",
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
                            "locus_tag": "MJ0846",
                            "sequence_length": 553,
                            "sequence_crc64": "CC3AB9AC4F745A24",
                            "sequence_version": 2,
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
                            "node_id": "CNBG_1207",
                            "label": "Alpha-1,3-mannosyltransferase (CAP59 family)",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:A0A095C6P1",
                            "organism_taxon_id": "NCBITaxon:294750",
                            "proteome_id": "UP:UP000029445",
                            "gene_symbol": "CNBG_1207",
                            "locus_tag": "CNBG_1207",
                            "sequence_length": 457,
                            "sequence_crc64": "1EE9B113AD99C774",
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
                            "edge_id": "cnbg1207-capsule-organization",
                            "subject": "CNBG_1207",
                            "predicate": "capable of",
                            "predicate_id": "RO:0002215",
                            "object": "capsule-organization",
                            "evidence": [
                                {
                                    "reference": "PMID:21304167",
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
    cover the 15 species+strain exemplar records (290 evidence-backed edges and
    86 GENE_OR_PROTEIN nodes across 39 live-verified UniProtKB accessions), and
    satisfy schema prefix and id_label_targets rules (#78)."""
    overlays_dir = REPO_ROOT / "curation" / "causal_graphs"
    graphs, events = load_causal_graphs(overlays_dir)
    expected_ids = {
        "NCBITaxon:562",
        "NCBITaxon:83333",
        "NCBITaxon:511145",
        "NCBITaxon:1423",
        "NCBITaxon:224308",
        "NCBITaxon:287",
        "NCBITaxon:208964",
        "NCBITaxon:2190",
        "NCBITaxon:243232",
        "NCBITaxon:1859096",
        "NCBITaxon:294750",
        "NCBITaxon:40410",
        "NCBITaxon:283643",
        "NCBITaxon:5207",
        "NCBITaxon:235443",
    }
    assert set(graphs) == expected_ids
    assert set(events) == expected_ids
    total_edges = sum(
        len(e.get("evidence") or [])
        for tid in expected_ids
        for g in graphs[tid]
        for e in g.get("edges") or []
    )
    assert total_edges >= 290
    edge_count = sum(
        len(g.get("edges") or [])
        for tid in expected_ids
        for g in graphs[tid]
    )
    assert edge_count == 290
    protein_nodes = [
        n
        for tid in expected_ids
        for g in graphs[tid]
        for n in g.get("nodes") or []
        if n.get("node_type") == "GENE_OR_PROTEIN"
    ]
    assert len(protein_nodes) == 86
    expected_uniprot = {
        "UniProtKB:P02920",
        "UniProtKB:P00722",
        "UniProtKB:P03023",
        "UniProtKB:P07464",
        "UniProtKB:P0AA04",
        "UniProtKB:P0ACJ8",
        "UniProtKB:P00936",
        "UniProtKB:P16497",
        "UniProtKB:P39764",
        "UniProtKB:P69783",
        "UniProtKB:P06628",
        "UniProtKB:P06535",
        "UniProtKB:P06534",
        "UniProtKB:Q00828",
        "UniProtKB:P05043",
        "UniProtKB:Q08430",
        "UniProtKB:Q00829",
        "UniProtKB:Q9HWH2",
        "UniProtKB:Q9HWG9",
        "UniProtKB:P0DPB9",
        "UniProtKB:Q9HWH1",
        "UniProtKB:O69753",
        "UniProtKB:P20581",
        "UniProtKB:P54292",
        "UniProtKB:Q58256",
        "UniProtKB:Q58252",
        "UniProtKB:Q58255",
        "UniProtKB:Q58929",
        "UniProtKB:P61154",
        "UniProtKB:Q58261",
        "UniProtKB:Q58264",
        "UniProtKB:A0A095C6P1",
        "UniProtKB:A0A095CIC4",
        "UniProtKB:Q55P57",
        "UniProtKB:J9VG42",
        "UniProtKB:J9VY90",
        "UniProtKB:J9VQZ4",
        "UniProtKB:J9VQ26",
        "UniProtKB:J9VT33",
    }
    assert {n["grounding"] for n in protein_nodes} == expected_uniprot
    for n in protein_nodes:
        assert n.get("organism_taxon_id", "").startswith("NCBITaxon:")
        if n.get("proteome_id") is not None:
            assert n["proteome_id"].startswith("UP:UP")
        assert n.get("gene_symbol") or n.get("locus_tag")
        assert isinstance(n.get("sequence_length"), int) and n["sequence_length"] > 0
        assert isinstance(n.get("sequence_crc64"), str) and len(n["sequence_crc64"]) == 16
        assert isinstance(n.get("sequence_version"), int) and n["sequence_version"] >= 1
        assert n.get("entry_status") in ("SWISS_PROT", "TREMBL")
    assert sum(1 for n in protein_nodes if n.get("proteome_id")) == 84


def test_uniprot_proteins_catalog_and_lineage_validator():
    """Verify curation/uniprot_proteins.tsv schema and validate_causal_graph_proteins
    rejection of unpinned accessions, checksum/length/locus mismatches, and cross-species
    organism_taxon_id bindings (#78 / taxonmech-infra-0003)."""
    proteins = load_uniprot_proteins(UNIPROT_PROTEINS_PATH)
    assert len(proteins) == 39
    for uid, row in proteins.items():
        assert uid.startswith("UniProtKB:")
        assert tuple(row.keys()) == UNIPROT_PROTEIN_FIELDS

    overlays_dir = REPO_ROOT / "curation" / "causal_graphs"
    graphs, _events = load_causal_graphs(overlays_dir, uniprot_path=UNIPROT_PROTEINS_PATH)

    taxa = {
        "NCBITaxon:2": {"taxon_id": "NCBITaxon:2", "rank": "DOMAIN", "parent_id": ""},
        "NCBITaxon:561": {"taxon_id": "NCBITaxon:561", "rank": "GENUS", "parent_id": "NCBITaxon:2"},
        "NCBITaxon:562": {"taxon_id": "NCBITaxon:562", "rank": "SPECIES", "parent_id": "NCBITaxon:561"},
        "NCBITaxon:83333": {"taxon_id": "NCBITaxon:83333", "rank": "STRAIN", "parent_id": "NCBITaxon:562"},
        "NCBITaxon:511145": {
            "taxon_id": "NCBITaxon:511145",
            "rank": "NO_RANK",
            "parent_id": "NCBITaxon:83333",
        },
        "NCBITaxon:135461": {
            "taxon_id": "NCBITaxon:135461",
            "rank": "SUBSPECIES",
            "parent_id": "NCBITaxon:1423",
        },
        "NCBITaxon:1423": {"taxon_id": "NCBITaxon:1423", "rank": "SPECIES", "parent_id": "NCBITaxon:2"},
        "NCBITaxon:224308": {
            "taxon_id": "NCBITaxon:224308",
            "rank": "STRAIN",
            "parent_id": "NCBITaxon:135461",
        },
        "NCBITaxon:287": {"taxon_id": "NCBITaxon:287", "rank": "SPECIES", "parent_id": "NCBITaxon:2"},
        "NCBITaxon:208964": {"taxon_id": "NCBITaxon:208964", "rank": "STRAIN", "parent_id": "NCBITaxon:287"},
        "NCBITaxon:2157": {"taxon_id": "NCBITaxon:2157", "rank": "DOMAIN", "parent_id": ""},
        "NCBITaxon:2190": {"taxon_id": "NCBITaxon:2190", "rank": "SPECIES", "parent_id": "NCBITaxon:2157"},
        "NCBITaxon:243232": {"taxon_id": "NCBITaxon:243232", "rank": "STRAIN", "parent_id": "NCBITaxon:2190"},
        "NCBITaxon:2759": {"taxon_id": "NCBITaxon:2759", "rank": "DOMAIN", "parent_id": ""},
        "NCBITaxon:1859096": {
            "taxon_id": "NCBITaxon:1859096",
            "rank": "SPECIES",
            "parent_id": "NCBITaxon:2759",
        },
        "NCBITaxon:294750": {
            "taxon_id": "NCBITaxon:294750",
            "rank": "STRAIN",
            "parent_id": "NCBITaxon:1859096",
        },
        "NCBITaxon:40410": {"taxon_id": "NCBITaxon:40410", "rank": "SPECIES", "parent_id": "NCBITaxon:2759"},
        "NCBITaxon:283643": {
            "taxon_id": "NCBITaxon:283643",
            "rank": "STRAIN",
            "parent_id": "NCBITaxon:40410",
        },
        "NCBITaxon:5207": {"taxon_id": "NCBITaxon:5207", "rank": "SPECIES", "parent_id": "NCBITaxon:2759"},
        "NCBITaxon:235443": {"taxon_id": "NCBITaxon:235443", "rank": "STRAIN", "parent_id": "NCBITaxon:5207"},
    }
    validate_causal_graph_proteins(graphs, uniprot_proteins=proteins, taxa=taxa)

    # Negative control 1: unpinned accession (e.g. Q9HWH3 opmD instead of Q9HWG9 phzS)
    bad_unpinned = {
        "NCBITaxon:287": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "phzS",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:Q9HWH3",
                        "organism_taxon_id": "NCBITaxon:208964",
                        "proteome_id": "UP:UP000002438",
                        "gene_symbol": "phzS",
                        "locus_tag": "PA4217",
                        "sequence_length": 402,
                        "sequence_crc64": "F2BB36662ABAC790",
                        "sequence_version": 1,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="not registered in curation/uniprot_proteins.tsv"):
        validate_causal_graph_proteins(bad_unpinned, uniprot_proteins=proteins, taxa=taxa)

    # Negative control 2: sequence_crc64 mismatch
    bad_crc = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lacZ",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                        "organism_taxon_id": "NCBITaxon:83333",
                        "proteome_id": "UP:UP000000625",
                        "gene_symbol": "lacZ",
                        "locus_tag": "b0344",
                        "sequence_length": 1024,
                        "sequence_crc64": "0000000000000000",
                        "sequence_version": 2,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="sequence_crc64"):
        validate_causal_graph_proteins(bad_crc, uniprot_proteins=proteins, taxa=taxa)

    # Negative control 3: cross-species organism_taxon_id lineage mismatch
    # (assigning C. deneoformans B-3501A LAC1 UniProtKB:Q55P57 to C. deuterogattii NCBITaxon:1859096)
    bad_lineage = {
        "NCBITaxon:1859096": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lac1",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:Q55P57",
                        "organism_taxon_id": "NCBITaxon:283643",
                        "gene_symbol": "LAC1",
                        "locus_tag": "CNBG3550",
                        "sequence_length": 624,
                        "sequence_crc64": "A675C03F8940224B",
                        "sequence_version": 1,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="not lineage-consistent"):
        validate_causal_graph_proteins(bad_lineage, uniprot_proteins=proteins, taxa=taxa)

    # Strain inventory mapping for strain_id validation (#78 / taxonmech-infra-0003)
    strains = {
        "NCBITaxon:562": [{"strain_id": "kgmicrobe.strain:bacdive_155687"}],
        "NCBITaxon:1423": [{"strain_id": "kgmicrobe.strain:bacdive_1156"}],
        "NCBITaxon:287": [{"strain_id": "kgmicrobe.strain:bacdive_12795"}],
        "NCBITaxon:243232": [{"strain_id": "kgmicrobe.strain:bacdive_6981"}],
    }
    validate_causal_graph_proteins(graphs, uniprot_proteins=proteins, taxa=taxa, strains=strains)

    # Negative control 4: malformed strain_id on GENE_OR_PROTEIN
    bad_strain_fmt = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lacZ",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                        "organism_taxon_id": "NCBITaxon:83333",
                        "strain_id": "bacdive:155687",
                        "proteome_id": "UP:UP000000625",
                        "gene_symbol": "lacZ",
                        "locus_tag": "b0344",
                        "sequence_length": 1024,
                        "sequence_crc64": "9D295EF4CEF90B08",
                        "sequence_version": 2,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid 'strain_id'"):
        validate_causal_graph_proteins(
            bad_strain_fmt, uniprot_proteins=proteins, taxa=taxa, strains=strains
        )

    # Negative control 5: absent strain_id from bacdive_strains.tsv
    bad_strain_missing = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lacZ",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                        "organism_taxon_id": "NCBITaxon:83333",
                        "strain_id": "kgmicrobe.strain:bacdive_99999999",
                        "proteome_id": "UP:UP000000625",
                        "gene_symbol": "lacZ",
                        "locus_tag": "b0344",
                        "sequence_length": 1024,
                        "sequence_crc64": "9D295EF4CEF90B08",
                        "sequence_version": 2,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="is absent from bacdive_strains.tsv"):
        validate_causal_graph_proteins(
            bad_strain_missing, uniprot_proteins=proteins, taxa=taxa, strains=strains
        )

    # Negative control 6: cross-species strain_id (M. jannaschii bacdive_6981 on E. coli lacZ)
    bad_strain_lineage = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lacZ",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                        "organism_taxon_id": "NCBITaxon:83333",
                        "strain_id": "kgmicrobe.strain:bacdive_6981",
                        "proteome_id": "UP:UP000000625",
                        "gene_symbol": "lacZ",
                        "locus_tag": "b0344",
                        "sequence_length": 1024,
                        "sequence_crc64": "9D295EF4CEF90B08",
                        "sequence_version": 2,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="strain_id .* is not lineage-consistent"):
        validate_causal_graph_proteins(
            bad_strain_lineage, uniprot_proteins=proteins, taxa=taxa, strains=strains
        )


def test_validate_causal_graph_structure_and_sources_catalog():
    """Verify validate_causal_graph_structure enforces node_id/edge_id uniqueness,
    edge endpoint referential integrity, non-self-loop edges, and evidence references,
    and conf/sources.yaml registers uniprot_proteins (#78 / taxonmech-infra-0001 / 0003)."""
    sources_cfg = yaml.safe_load((REPO_ROOT / "conf" / "sources.yaml").read_text(encoding="utf-8"))
    assert "uniprot_proteins" in sources_cfg.get("sources", {})
    assert "curation/uniprot_proteins.tsv" in sources_cfg["sources"]["uniprot_proteins"]["via"]

    dup_node = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n1", "label": "Node 1 dup", "node_type": "PATHWAY"},
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="duplicate node_id 'n1'"):
        validate_causal_graph_structure(dup_node)

    dangling_edge = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "regulates",
                        "object": "missing-node",
                        "evidence": [{"reference": "PMID:1"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="object 'missing-node' does not reference a defined node_id"):
        validate_causal_graph_structure(dangling_edge)

    self_loop = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "regulates",
                        "object": "n1",
                        "evidence": [{"reference": "PMID:1"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="self-loop subject == object 'n1'"):
        validate_causal_graph_structure(self_loop)

    missing_ev = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n2", "label": "Node 2", "node_type": "TRAIT"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "regulates",
                        "object": "n2",
                        "evidence": [{}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="each evidence item requires non-empty 'reference'"):
        validate_causal_graph_structure(missing_ev)


def test_validate_causal_graph_node_edge_and_protein_ec_invariants(tmp_path):
    """Verify Cycle 4 Stage 6 (#189) invariants across validate_causal_graph_structure,
    load_uniprot_proteins, and validate_causal_graph_proteins."""
    sv = SchemaView(str(SCHEMA_PATH))
    enum_values = set(sv.get_enum("CausalNodeTypeEnum").permissible_values.keys())
    assert enum_values == CAUSAL_NODE_TYPES
    assert PROTEIN_ONLY_NODE_SLOTS == (
        "organism_taxon_id",
        "strain_id",
        "proteome_id",
        "gene_symbol",
        "locus_tag",
        "sequence_length",
        "sequence_crc64",
        "sequence_version",
        "entry_status",
    )
    assert CURIE_PATTERN.match("GO:0006099")
    assert EDGE_ID_PATTERN.match("edge-1")
    assert EC_NUMBER_PATTERN.match("EC:2.8.4.1")
    assert EC_NUMBER_PATTERN.match("EC:2.8.4.-")
    assert EVIDENCE_REFERENCE_PATTERN.match("PMID:12345")
    assert EVIDENCE_REFERENCE_PATTERN.match("DOI:10.1099/ijsem.0.001")

    # 1. Invalid node_type
    bad_node_type = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [{"node_id": "n1", "label": "Node 1", "node_type": "PHENOTYPE"}],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid node_type 'PHENOTYPE'"):
        validate_causal_graph_structure(bad_node_type)

    # 2. Protein-only slot on non-GENE_OR_PROTEIN node
    bad_protein_slot = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Pathway",
                        "node_type": "PATHWAY",
                        "gene_symbol": "tnaA",
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match=r"non-GENE_OR_PROTEIN node \(PATHWAY\) cannot declare \['gene_symbol'\]",
    ):
        validate_causal_graph_structure(bad_protein_slot)

    # 3. Invalid grounding CURIE
    bad_grounding = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Pathway",
                        "node_type": "PATHWAY",
                        "grounding": "not a curie",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid 'grounding' CURIE 'not a curie'"):
        validate_causal_graph_structure(bad_grounding)

    # 4. TAXON node without NCBITaxon: grounding
    bad_taxon_grounding = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Taxon node",
                        "node_type": "TAXON",
                        "grounding": "GO:0008150",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="TAXON grounding must start with 'NCBITaxon:'"):
        validate_causal_graph_structure(bad_taxon_grounding)

    # 5. Duplicate xrefs or xref duplicating grounding
    dup_xref = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Pathway",
                        "node_type": "PATHWAY",
                        "grounding": "GO:0006569",
                        "xrefs": ["GO:0006569"],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="duplicate xref 'GO:0006569'"):
        validate_causal_graph_structure(dup_xref)

    # 6. Invalid edge_id or predicate_id CURIE
    bad_edge_id = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n2", "label": "Node 2", "node_type": "CHEMICAL"},
                ],
                "edges": [
                    {
                        "edge_id": "1bad_edge",
                        "subject": "n1",
                        "predicate": "produces",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:1"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid edge_id '1bad_edge'"):
        validate_causal_graph_structure(bad_edge_id)

    bad_pred_id = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n2", "label": "Node 2", "node_type": "CHEMICAL"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "produces",
                        "predicate_id": "invalid predicate id",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:1"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid 'predicate_id' CURIE"):
        validate_causal_graph_structure(bad_pred_id)

    # 7. Duplicate parallel edge (subject, predicate_id or predicate, object)
    dup_triple = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n2", "label": "Node 2", "node_type": "CHEMICAL"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "produces",
                        "predicate_id": "RO:0002234",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:1"}],
                    },
                    {
                        "edge_id": "e2",
                        "subject": "n1",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:2"}],
                    },
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="duplicate parallel edge"):
        validate_causal_graph_structure(dup_triple)

    # 8. Invalid or duplicate evidence reference
    bad_ev_ref = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n2", "label": "Node 2", "node_type": "CHEMICAL"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "produces",
                        "object": "n2",
                        "evidence": [{"reference": "not-a-curie"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid evidence reference 'not-a-curie'"):
        validate_causal_graph_structure(bad_ev_ref)

    dup_ev_ref = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {"node_id": "n1", "label": "Node 1", "node_type": "PATHWAY"},
                    {"node_id": "n2", "label": "Node 2", "node_type": "CHEMICAL"},
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "produces",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:1"}, {"reference": "PMID:1"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="duplicate evidence reference 'PMID:1'"):
        validate_causal_graph_structure(dup_ev_ref)

    # 9. load_uniprot_proteins required descriptive fields and EC number format
    header = "\t".join(UNIPROT_PROTEIN_FIELDS)
    missing_gene_and_locus = tmp_path / "missing_gene_locus.tsv"
    missing_gene_and_locus.write_text(
        f"{header}\n"
        "UniProtKB:P0A853\tTNAA_ECOLI\tSWISS_PROT\tTryptophanase\t"
        "NCBITaxon:83333\tEscherichia coli (strain K12)\tUP:UP000000625\t\t\t"
        "EC:4.1.99.1\t471\tC6ECAD1DC1AA5B26\t2\t2026_01\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="requires gene_symbol or locus_tag"):
        load_uniprot_proteins(missing_gene_and_locus)

    bad_ec_tsv = tmp_path / "bad_ec.tsv"
    bad_ec_tsv.write_text(
        f"{header}\n"
        "UniProtKB:P0A853\tTNAA_ECOLI\tSWISS_PROT\tTryptophanase\t"
        "NCBITaxon:83333\tEscherichia coli (strain K12)\tUP:UP000000625\ttnaA\tb3708\t"
        "4.1.99.1\t471\tC6ECAD1DC1AA5B26\t2\t2026_01\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="invalid EC number '4.1.99.1'"):
        load_uniprot_proteins(bad_ec_tsv)

    # 10. validate_causal_graph_proteins checks EC xref syntax and TAXON node lineage
    proteins = load_uniprot_proteins(UNIPROT_PROTEINS_PATH)
    taxa = {
        "NCBITaxon:2": {"parent_id": "", "rank": "DOMAIN"},
        "NCBITaxon:562": {"parent_id": "NCBITaxon:2", "rank": "SPECIES"},
        "NCBITaxon:83333": {"parent_id": "NCBITaxon:562", "rank": "STRAIN"},
        "NCBITaxon:1423": {"parent_id": "NCBITaxon:2", "rank": "SPECIES"},
    }
    strains = {
        "NCBITaxon:562": [{"strain_id": "kgmicrobe.strain:bacdive_155687"}],
        "NCBITaxon:1423": [{"strain_id": "kgmicrobe.strain:bacdive_1156"}],
    }

    bad_ec_xref_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lacZ",
                        "label": "Beta-galactosidase (LacZ)",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                        "entry_status": "SWISS_PROT",
                        "gene_symbol": "lacZ",
                        "locus_tag": "b0344",
                        "organism_taxon_id": "NCBITaxon:83333",
                        "proteome_id": "UP:UP000000625",
                        "sequence_length": 1024,
                        "sequence_crc64": "9D295EF4CEF90B08",
                        "sequence_version": 2,
                        "xrefs": ["EC:invalid"],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid EC xref 'EC:invalid'"):
        validate_causal_graph_proteins(
            bad_ec_xref_graph, uniprot_proteins=proteins, taxa=taxa, strains=strains
        )

    absent_taxon_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "missing-taxon",
                        "label": "Unknown taxon",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:99999999",
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit, match="TAXON grounding NCBITaxon:99999999 is absent from ncbitaxon_taxa.tsv"
    ):
        validate_causal_graph_proteins(
            absent_taxon_graph, uniprot_proteins=proteins, taxa=taxa, strains=strains
        )

    bad_taxon_lineage_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "other-taxon",
                        "label": "Bacillus subtilis",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:1423",
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit, match="TAXON grounding NCBITaxon:1423 is not lineage-consistent with NCBITaxon:562"
    ):
        validate_causal_graph_proteins(
            bad_taxon_lineage_graph, uniprot_proteins=proteins, taxa=taxa, strains=strains
        )


def test_curation_guide_and_overlay_readme_document_causal_graphs_and_uniprot_fields() -> None:
    """docs/CURATION.md and curation/causal_graphs/README.md stay synchronized with
    the live causal-graph overlay pipeline, all 14 UNIPROT_PROTEIN_FIELDS columns,
    and the species-vs-strain strain_id binding rule (#197, #78)."""
    curation_doc = (REPO_ROOT / "docs" / "CURATION.md").read_text(encoding="utf-8")
    assert "Curator-owned overlays for `causal_graphs`, `definition`, `evidence`" not in curation_doc
    for expected_token in (
        "curation/causal_graphs/*.yaml",
        "curation/uniprot_proteins.tsv",
        "load_causal_graphs()",
        "validate_causal_graph_structure()",
        "load_uniprot_proteins()",
        "validate_causal_graph_proteins()",
    ):
        assert expected_token in curation_doc, f"docs/CURATION.md missing {expected_token!r}"

    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    assert "UNIPROT_PROTEIN_FIELDS" in overlay_readme
    for col in UNIPROT_PROTEIN_FIELDS:
        assert f"`{col}`" in overlay_readme, f"curation/causal_graphs/README.md missing column {col!r}"
    for binding_token in (
        "BACDIVE_STRAIN_ID_PATTERN",
        "_taxa_lineage_compatible",
        "Species vs. Strain `strain_id` Binding Rule",
    ):
        assert binding_token in overlay_readme, (
            f"curation/causal_graphs/README.md missing {binding_token!r}"
        )

    graphs, _ = load_causal_graphs()
    overlay_strain_ids = {
        node["strain_id"]
        for graph_list in graphs.values()
        for graph in graph_list
        for node in graph.get("nodes", [])
        if "strain_id" in node
    }
    readme_strain_ids = set(re.findall(r"kgmicrobe\.strain:bacdive_[1-9][0-9]*", overlay_readme))
    assert readme_strain_ids == overlay_strain_ids, (
        f"README strain_ids {sorted(readme_strain_ids)} != overlay strain_ids {sorted(overlay_strain_ids)}"
    )


def test_causal_graph_node_connectivity_and_id_patterns_enforced(tmp_path: Path):
    """validate_causal_graph_structure and validate_causal_graph_proteins must reject
    disconnected nodes, malformed graph_id/node_id/UniProtKB/proteome_id/NCBITaxon IDs,
    and above-species host or organism taxa (#199, #78)."""
    assert UNIPROT_ID_PATTERN.match("UniProtKB:P00722")
    assert UNIPROT_ID_PATTERN.match("UniProtKB:A0A1S6LVH0")
    assert not UNIPROT_ID_PATTERN.match("UniProtKB:bad")
    assert NCBITAXON_ID_PATTERN.match("NCBITaxon:562")
    assert not NCBITAXON_ID_PATTERN.match("NCBITaxon:0")
    assert PROTEOME_ID_PATTERN.match("UP:UP000000625")
    assert not PROTEOME_ID_PATTERN.match("UP:UP625")

    # 1. Disconnected node in CausalGraph
    disconnected_graphs = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "n2",
                        "label": "lactose catabolic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005988",
                    },
                    {
                        "node_id": "orphan_node",
                        "label": "beta-galactosidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004565",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:9278503"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="disconnected node_id"):
        validate_causal_graph_structure(disconnected_graphs)

    # 2. Malformed graph_id
    bad_graph_id = {
        "NCBITaxon:562": [
            {
                "graph_id": "123 bad graph id",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "E. coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "n2",
                        "label": "lactose",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005988",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:9278503"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid graph_id"):
        validate_causal_graph_structure(bad_graph_id)

    # 3. Malformed node_id
    bad_node_id = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "123-bad-node",
                        "label": "E. coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "n2",
                        "label": "lactose",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005988",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "123-bad-node",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:9278503"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid node_id"):
        validate_causal_graph_structure(bad_node_id)

    # 4. Genus-level host or organism_taxon_id rejected by species-or-below scope check
    taxa = {
        "NCBITaxon:2": {"parent_id": "", "rank": "DOMAIN"},
        "NCBITaxon:561": {"parent_id": "NCBITaxon:2", "rank": "GENUS"},
        "NCBITaxon:562": {"parent_id": "NCBITaxon:561", "rank": "SPECIES"},
    }
    proteins = load_uniprot_proteins()
    genus_host_graph = {
        "NCBITaxon:561": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Escherichia",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:561",
                    },
                    {
                        "node_id": "n2",
                        "label": "lactose",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005988",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "n1",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "n2",
                        "evidence": [{"reference": "PMID:9278503"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="must be species-or-below"):
        validate_causal_graph_proteins(genus_host_graph, uniprot_proteins=proteins, taxa=taxa)

    # 5. Malformed proteome_id in uniprot_proteins.tsv rejected
    bad_proteome_tsv = tmp_path / "bad_proteome.tsv"
    lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    bad_proteome_tsv.write_text(
        lines[0] + "\n" + lines[1].replace("UP:UP000029445", "UP:UP29445") + "\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="invalid proteome_id"):
        load_uniprot_proteins(bad_proteome_tsv)


def test_causal_graph_provenance_problems_gate(tmp_path: Path):
    """scripts/check_provenance.py causal_graph_provenance_problems() must pass on the
    committed repository and report out-of-scope overlays or filename-stem mismatches (#199)."""
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    assert mod.causal_graph_provenance_problems(REPO_ROOT) == []

    # Set up a minimal synthetic repo_root to test failure modes
    curation_dir = tmp_path / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    overlays_dir.mkdir(parents=True)
    (curation_dir / "uniprot_proteins.tsv").write_text(
        UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (curation_dir / "seed_scope.tsv").write_text(
        "identifier\tadded\treason\nNCBITaxon:1423\t2026-01-01\ttest\n",
        encoding="utf-8",
    )
    # Write NCBITaxon:562 overlay under a mismatched filename stem and omitted from seed_scope.tsv
    ecoli_overlay = (REPO_ROOT / "curation" / "causal_graphs" / "NCBITaxon_562.yaml").read_text(
        encoding="utf-8"
    )
    (overlays_dir / "wrong_stem.yaml").write_text(ecoli_overlay, encoding="utf-8")

    failures = mod.causal_graph_provenance_problems(tmp_path)
    assert any("not present in curation/seed_scope.tsv" in f for f in failures)
    assert any("does not match identifier 'NCBITaxon:562'" in f for f in failures)


def test_schema_guide_and_overlay_readme_document_cycle5_provenance_and_ec_pattern_invariants():
    """docs/SCHEMA.md must document scripts/check_provenance.py causal_graph_provenance_problems()
    and Cycle 5 structural/provenance invariants, and curation/causal_graphs/README.md must
    document the exact 4-part EC_NUMBER_PATTERN regex rather than 'EC:<digits>' (#206, #199, #78)."""
    schema_doc = (REPO_ROOT / "docs" / "SCHEMA.md").read_text(encoding="utf-8")
    for expected_token in (
        "scripts/check_provenance.py",
        "causal_graph_provenance_problems()",
        "EDGE_ID_PATTERN",
        "NCBITAXON_ID_PATTERN",
        "PROTEOME_ID_PATTERN",
        "UNIPROT_ID_PATTERN",
        "EC_NUMBER_PATTERN",
        EC_NUMBER_PATTERN.pattern,
        "_taxon_is_species_or_below",
        "curation/seed_scope.tsv",
    ):
        assert expected_token in schema_doc, f"docs/SCHEMA.md missing {expected_token!r}"

    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    assert "(`EC:<digits>`)" not in overlay_readme
    assert EC_NUMBER_PATTERN.pattern in overlay_readme


def test_cycle6_stage6_causal_graph_and_uniprot_provenance_invariants(tmp_path: Path):
    """Verify Cycle 6 Stage 6 (#208) invariants across validate_causal_graph_structure,
    load_causal_graphs, validate_causal_graph_proteins, and causal_graph_provenance_problems."""
    # 1. Duplicate graph_id on the same taxon rejected directly by validate_causal_graph_structure
    dup_gid = {
        "NCBITaxon:562": [
            {"graph_id": "g1"},
            {"graph_id": "g1"},
        ]
    }
    with pytest.raises(SystemExit, match="duplicate graph_id 'g1'"):
        validate_causal_graph_structure(dup_gid)

    # 2. TAXON node missing grounding or with malformed NCBITaxon:0 grounding rejected
    missing_taxon_grounding = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="TAXON grounding must start with 'NCBITaxon:'"):
        validate_causal_graph_structure(missing_taxon_grounding)

    malformed_taxon_grounding = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "n1",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:0",
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="invalid TAXON grounding 'NCBITaxon:0'"):
        validate_causal_graph_structure(malformed_taxon_grounding)

    # 3. load_causal_graphs requires non-empty title, nodes, and edges on every loaded graph
    missing_title_dir = tmp_path / "missing_title"
    missing_title_dir.mkdir()
    (missing_title_dir / "NCBITaxon_562.yaml").write_text(
        "identifier: NCBITaxon:562\ncausal_graphs:\n  - graph_id: g1\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="requires non-empty 'title'"):
        load_causal_graphs(missing_title_dir)

    missing_nodes_dir = tmp_path / "missing_nodes"
    missing_nodes_dir.mkdir()
    (missing_nodes_dir / "NCBITaxon_562.yaml").write_text(
        "identifier: NCBITaxon:562\ncausal_graphs:\n  - graph_id: g1\n    title: T1\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="'nodes' must be a non-empty list"):
        load_causal_graphs(missing_nodes_dir)

    missing_edges_dir = tmp_path / "missing_edges"
    missing_edges_dir.mkdir()
    (missing_edges_dir / "NCBITaxon_562.yaml").write_text(
        "identifier: NCBITaxon:562\n"
        "causal_graphs:\n"
        "  - graph_id: g1\n"
        "    title: T1\n"
        "    nodes:\n"
        "      - node_id: n1\n"
        "        label: E. coli\n"
        "        node_type: TAXON\n"
        "        grounding: NCBITaxon:562\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="'edges' must be a non-empty list"):
        load_causal_graphs(missing_edges_dir)

    # 4. Ancestor-species strain_id rejected on infraspecific strain overlay with strains: []
    proteins = load_uniprot_proteins(UNIPROT_PROTEINS_PATH)
    taxa = {
        "NCBITaxon:2": {"parent_id": "", "rank": "DOMAIN"},
        "NCBITaxon:561": {"parent_id": "NCBITaxon:2", "rank": "GENUS"},
        "NCBITaxon:562": {"parent_id": "NCBITaxon:561", "rank": "SPECIES"},
        "NCBITaxon:83333": {"parent_id": "NCBITaxon:562", "rank": "STRAIN"},
    }
    strains = {
        "NCBITaxon:562": [{"strain_id": "kgmicrobe.strain:bacdive_155687"}],
    }
    ancestor_strain_on_strain_overlay = {
        "NCBITaxon:83333": [
            {
                "graph_id": "g1",
                "nodes": [
                    {
                        "node_id": "lacZ",
                        "label": "Beta-galactosidase (LacZ)",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                        "organism_taxon_id": "NCBITaxon:83333",
                        "strain_id": "kgmicrobe.strain:bacdive_155687",
                        "proteome_id": "UP:UP000000625",
                        "gene_symbol": "lacZ",
                        "locus_tag": "b0344",
                        "sequence_length": 1024,
                        "sequence_crc64": "9D295EF4CEF90B08",
                        "sequence_version": 2,
                        "entry_status": "SWISS_PROT",
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="strain_id 'kgmicrobe.strain:bacdive_155687' .* is not lineage-consistent with NCBITaxon:83333",
    ):
        validate_causal_graph_proteins(
            ancestor_strain_on_strain_overlay,
            uniprot_proteins=proteins,
            taxa=taxa,
            strains=strains,
        )

    # 5. causal_graph_provenance_problems detects unreferenced uniprot_proteins.tsv rows
    # and missing curation_history
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_repo"
    curation_dir = synth_root / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    overlays_dir.mkdir(parents=True)
    (curation_dir / "uniprot_proteins.tsv").write_text(
        UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (curation_dir / "seed_scope.tsv").write_text(
        "identifier\tadded\treason\nNCBITaxon:562\t2026-01-01\ttest\n",
        encoding="utf-8",
    )
    ecoli_data = yaml.safe_load(
        (REPO_ROOT / "curation" / "causal_graphs" / "NCBITaxon_562.yaml").read_text(
            encoding="utf-8"
        )
    )
    ecoli_data.pop("curation_history", None)
    (overlays_dir / "NCBITaxon_562.yaml").write_text(
        yaml.safe_dump(ecoli_data, sort_keys=False),
        encoding="utf-8",
    )
    failures = mod.causal_graph_provenance_problems(synth_root)
    assert any("not referenced by any GENE_OR_PROTEIN node" in f for f in failures)
    assert any("missing or empty 'curation_history'" in f for f in failures)


def test_curation_guide_and_overlay_readme_document_required_curation_history_and_provenance():
    """curation/causal_graphs/README.md must describe curation_history as required and include
    it in the Overlay File Contract YAML example, and docs/CURATION.md must document
    scripts/check_provenance.py causal_graph_provenance_problems() (#214, #208, #78)."""
    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    assert "optional curation `history`" not in overlay_readme
    assert "optional `curation_history`" not in overlay_readme
    assert "required non-empty `curation_history`" in overlay_readme

    match = re.search(r"```yaml\n(.*?)\n```", overlay_readme, flags=re.DOTALL)
    assert match is not None, "curation/causal_graphs/README.md missing yaml code block"
    example_doc = yaml.safe_load(match.group(1))
    assert isinstance(example_doc, dict)
    assert example_doc.get("identifier") == "NCBITaxon:562"
    assert isinstance(example_doc.get("causal_graphs"), list) and example_doc["causal_graphs"]
    assert isinstance(example_doc.get("curation_history"), list) and example_doc["curation_history"]

    curation_doc = (REPO_ROOT / "docs" / "CURATION.md").read_text(encoding="utf-8")
    for expected_token in (
        "scripts/check_provenance.py",
        "causal_graph_provenance_problems()",
        "required `curation_history`",
        "curation/seed_scope.tsv",
    ):
        assert expected_token in curation_doc, f"docs/CURATION.md missing {expected_token!r}"

