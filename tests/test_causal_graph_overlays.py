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
    CAUSAL_EDGE_KEYS,
    CAUSAL_GRAPH_KEYS,
    CAUSAL_NODE_KEYS,
    CAUSAL_NODE_TYPES,
    CHEBI_ID_PATTERN,
    CURATION_EVENT_KEYS,
    CURIE_PATTERN,
    EC_NUMBER_PATTERN,
    EDGE_ID_PATTERN,
    EVIDENCE_ITEM_KEYS,
    EVIDENCE_REFERENCE_PATTERN,
    GO_ID_PATTERN,
    ISO_UTC_TIMESTAMP_PATTERN,
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
    validate_causal_graph_events,
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
                            "node_id": "taxon",
                            "label": "Escherichia coli",
                            "node_type": "TAXON",
                            "grounding": "NCBITaxon:562",
                        },
                        {
                            "node_id": "lacZ",
                            "label": "Beta-galactosidase LacZ",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:P00722",
                            "xrefs": ["EC:3.2.1.23"],
                            "organism_taxon_id": "NCBITaxon:83333",
                            "strain_id": "kgmicrobe.strain:bacdive_155687",
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
                            "edge_id": "taxon-expresses-lacz",
                            "subject": "taxon",
                            "predicate": "expresses",
                            "predicate_id": "RO:0002292",
                            "object": "lacZ",
                            "evidence": [
                                {
                                    "reference": "PMID:9278503",
                                    "snippet": (
                                        "Complete genome sequence of Escherichia coli K-12 "
                                        "MG1655 annotates the lacZYA lactose operon."
                                    ),
                                }
                            ],
                        },
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
                        },
                    ],
                }
            ],
            "curation_history": [
                {
                    "timestamp": "2026-10-22T06:00:00Z",
                    "curator": "stage6-canary",
                    "action": "UPDATED",
                    "changes": "Added verified LacZ causal graph overlay for NCBITaxon:562.",
                    "llm_assisted": True,
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
                            "node_id": "taxon",
                            "label": "Bacillus subtilis",
                            "node_type": "TAXON",
                            "grounding": "NCBITaxon:1423",
                        },
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
                            "edge_id": "taxon-expresses-spo0a",
                            "subject": "taxon",
                            "predicate": "expresses",
                            "predicate_id": "RO:0002292",
                            "object": "spo0A",
                            "evidence": [
                                {
                                    "reference": "PMID:9384377",
                                    "snippet": (
                                        "Bacillus subtilis 168 genome and Spo0A phosphorelay "
                                        "control initiation of endospore formation."
                                    ),
                                }
                            ],
                        },
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
                        },
                    ],
                }
            ],
            "curation_history": [
                {
                    "timestamp": "2026-10-22T06:00:00Z",
                    "curator": "stage6-canary",
                    "action": "UPDATED",
                    "changes": "Added verified Spo0A causal graph overlay for NCBITaxon:1423.",
                    "llm_assisted": True,
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
                            "node_id": "taxon",
                            "label": "Pseudomonas aeruginosa",
                            "node_type": "TAXON",
                            "grounding": "NCBITaxon:287",
                        },
                        {
                            "node_id": "phzM",
                            "label": "Phenazine-specific methyltransferase PhzM",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:Q9HWH2",
                            "xrefs": ["EC:2.1.1.327"],
                            "organism_taxon_id": "NCBITaxon:208964",
                            "strain_id": "kgmicrobe.strain:bacdive_12795",
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
                            "edge_id": "taxon-expresses-phzm",
                            "subject": "taxon",
                            "predicate": "expresses",
                            "predicate_id": "RO:0002292",
                            "object": "phzM",
                            "evidence": [
                                {
                                    "reference": "PMID:11591691",
                                    "snippet": (
                                        "PhzM and PhzS convert phenazine-1-carboxylic acid "
                                        "to pyocyanin in Pseudomonas aeruginosa PAO1."
                                    ),
                                }
                            ],
                        },
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
                        },
                    ],
                }
            ],
            "curation_history": [
                {
                    "timestamp": "2026-10-22T06:00:00Z",
                    "curator": "stage6-canary",
                    "action": "UPDATED",
                    "changes": "Added verified PhzM causal graph overlay for NCBITaxon:287.",
                    "llm_assisted": True,
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
                            "node_id": "taxon",
                            "label": "Methanocaldococcus jannaschii",
                            "node_type": "TAXON",
                            "grounding": "NCBITaxon:2190",
                        },
                        {
                            "node_id": "mcrA",
                            "label": "Methyl-coenzyme M reductase I subunit alpha",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:Q58256",
                            "xrefs": ["EC:2.8.4.1"],
                            "organism_taxon_id": "NCBITaxon:243232",
                            "strain_id": "kgmicrobe.strain:bacdive_6981",
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
                            "edge_id": "taxon-expresses-mcra",
                            "subject": "taxon",
                            "predicate": "expresses",
                            "predicate_id": "RO:0002292",
                            "object": "mcrA",
                            "evidence": [
                                {
                                    "reference": "PMID:8688087",
                                    "snippet": (
                                        "Complete genome sequence of the methanogenic archaeon "
                                        "Methanococcus jannaschii DSM 2661 encodes McrABG."
                                    ),
                                }
                            ],
                        },
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
                        },
                    ],
                }
            ],
            "curation_history": [
                {
                    "timestamp": "2026-10-22T06:00:00Z",
                    "curator": "stage6-canary",
                    "action": "UPDATED",
                    "changes": "Added verified McrA causal graph overlay for NCBITaxon:2190.",
                    "llm_assisted": True,
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
                            "node_id": "taxon",
                            "label": "Cryptococcus deuterogattii",
                            "node_type": "TAXON",
                            "grounding": "NCBITaxon:1859096",
                        },
                        {
                            "node_id": "CNBG_1207",
                            "label": "Alpha-1,3-mannosyltransferase (CAP59 family)",
                            "node_type": "GENE_OR_PROTEIN",
                            "grounding": "UniProtKB:A0A095C6P1",
                            "organism_taxon_id": "NCBITaxon:294750",
                            "proteome_id": "UP:UP000029445",
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
                            "edge_id": "taxon-expresses-cnbg1207",
                            "subject": "taxon",
                            "predicate": "expresses",
                            "predicate_id": "RO:0002292",
                            "object": "CNBG_1207",
                            "evidence": [
                                {
                                    "reference": "PMID:21304167",
                                    "snippet": (
                                        "Comparative genomics of Cryptococcus gattii VGII R265 "
                                        "identifies conserved capsule biosynthesis determinants."
                                    ),
                                }
                            ],
                        },
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
                        },
                    ],
                }
            ],
            "curation_history": [
                {
                    "timestamp": "2026-10-22T06:00:00Z",
                    "curator": "stage6-canary",
                    "action": "UPDATED",
                    "changes": "Added verified Cap59/CNBG_1207 causal graph overlay for NCBITaxon:1859096.",
                    "llm_assisted": True,
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
    validate_causal_graph_structure, validate_causal_graph_events,
    validate_causal_graph_proteins, causal_graph_provenance_problems,
    build_document, LinkML write_validated_taxon, emit_taxon_yaml roundtrip,
    id_label_targets prefix config, and HTML template rendering (#256, #249, #246, #78)."""
    overlays_dir = tmp_path / "causal_graphs"
    overlays_dir.mkdir()
    for tid, spec in STAGE2_STAGE3_EXEMPLAR_OVERLAYS.items():
        slug = tid.replace(":", "_")
        (overlays_dir / f"{slug}.yaml").write_text(
            yaml.safe_dump(spec["overlay"], sort_keys=False), encoding="utf-8"
        )

    graphs, events = load_causal_graphs(overlays_dir)
    assert set(graphs) == set(STAGE2_STAGE3_EXEMPLAR_OVERLAYS)
    assert set(events) == set(STAGE2_STAGE3_EXEMPLAR_OVERLAYS)
    for tid in STAGE2_STAGE3_EXEMPLAR_OVERLAYS:
        assert len(events[tid]) == 1
        assert events[tid][0].get("llm_assisted") is True

    validate_causal_graph_structure(graphs)
    validate_causal_graph_events(events)

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

    expected_exemplar_strains = {
        "NCBITaxon:562": "kgmicrobe.strain:bacdive_155687",
        "NCBITaxon:1423": "kgmicrobe.strain:bacdive_1156",
        "NCBITaxon:287": "kgmicrobe.strain:bacdive_12795",
        "NCBITaxon:2190": "kgmicrobe.strain:bacdive_6981",
        "NCBITaxon:1859096": None,
    }

    for tid, _spec in STAGE2_STAGE3_EXEMPLAR_OVERLAYS.items():
        concept = concepts[tid]
        assert isinstance(concept, Concept)
        doc = build_document(concept, inventory)
        assert "causal_graphs" in doc
        assert len(doc["causal_graphs"]) == 1

        taxon_nodes = [
            n for n in doc["causal_graphs"][0]["nodes"] if n["node_type"] == "TAXON"
        ]
        assert len(taxon_nodes) == 1
        assert taxon_nodes[0]["node_id"] == "taxon"
        assert taxon_nodes[0]["grounding"] == tid
        assert taxon_nodes[0]["label"] == _spec["label"]

        protein_nodes = [
            n for n in doc["causal_graphs"][0]["nodes"] if n["node_type"] == "GENE_OR_PROTEIN"
        ]
        assert len(protein_nodes) == 1
        node0 = protein_nodes[0]
        assert node0["node_type"] == "GENE_OR_PROTEIN"
        assert node0["grounding"].startswith("UniProtKB:")
        assert node0["organism_taxon_id"].startswith("NCBITaxon:")
        assert node0.get("strain_id") == expected_exemplar_strains[tid]
        assert node0["proteome_id"].startswith("UP:UP")
        assert node0["entry_status"] in ("SWISS_PROT", "TREMBL")

        expresses_edges = [
            e
            for e in doc["causal_graphs"][0]["edges"]
            if e.get("predicate_id") == "RO:0002292"
        ]
        assert len(expresses_edges) == 1
        assert expresses_edges[0]["subject"] == "taxon"
        assert expresses_edges[0]["predicate"] == "expresses"
        assert expresses_edges[0]["object"] == node0["node_id"]

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

    # Verify all 5 STAGE2_STAGE3_EXEMPLAR_OVERLAYS pass validate_causal_graph_proteins()
    # and causal_graph_provenance_problems() in scripts/check_provenance.py (#256, #249, #78)
    synth_root = tmp_path / "synth_exemplars"
    curation_dir = synth_root / "curation"
    synth_overlays_dir = curation_dir / "causal_graphs"
    raw_dir = synth_root / "data" / "raw"
    synth_overlays_dir.mkdir(parents=True)
    raw_dir.mkdir(parents=True)
    for tid, spec in STAGE2_STAGE3_EXEMPLAR_OVERLAYS.items():
        slug = tid.replace(":", "_")
        (synth_overlays_dir / f"{slug}.yaml").write_text(
            yaml.safe_dump(spec["overlay"], sort_keys=False), encoding="utf-8"
        )
    exemplar_uids = {
        "UniProtKB:P00722",
        "UniProtKB:P06534",
        "UniProtKB:Q9HWH2",
        "UniProtKB:Q58256",
        "UniProtKB:A0A095C6P1",
    }
    raw_uniprot_lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    uniprot_header = raw_uniprot_lines[0]
    selected_uniprot_rows = [
        line
        for line in raw_uniprot_lines[1:]
        if line.split("\t", 1)[0] in exemplar_uids
    ]
    assert len(selected_uniprot_rows) == 5
    (curation_dir / "uniprot_proteins.tsv").write_text(
        uniprot_header + "\n" + "\n".join(selected_uniprot_rows) + "\n",
        encoding="utf-8",
    )
    scope_lines = ["identifier\tadded\treason"] + [
        f"{tid}\t2026-01-01\texemplar test" for tid in STAGE2_STAGE3_EXEMPLAR_OVERLAYS
    ]
    (curation_dir / "seed_scope.tsv").write_text(
        "\n".join(scope_lines) + "\n",
        encoding="utf-8",
    )
    taxa_rows = dict(inventory.taxa)
    strain_taxa_meta = {
        "NCBITaxon:83333": ("Escherichia coli K-12", "STRAIN", "NCBITaxon:562"),
        "NCBITaxon:224308": (
            "Bacillus subtilis subsp. subtilis str. 168",
            "STRAIN",
            "NCBITaxon:1423",
        ),
        "NCBITaxon:208964": ("Pseudomonas aeruginosa PAO1", "STRAIN", "NCBITaxon:287"),
        "NCBITaxon:243232": (
            "Methanocaldococcus jannaschii DSM 2661",
            "STRAIN",
            "NCBITaxon:2190",
        ),
        "NCBITaxon:294750": (
            "Cryptococcus deuterogattii R265",
            "STRAIN",
            "NCBITaxon:1859096",
        ),
    }
    for s_tid, (s_lbl, s_rnk, s_par) in strain_taxa_meta.items():
        taxa_rows[s_tid] = {
            "taxon_id": s_tid,
            "label": s_lbl,
            "rank": s_rnk,
            "parent_id": s_par,
        }
    taxa_tsv_lines = ["taxon_id\tlabel\trank\tparent_id"] + [
        f"{t_id}\t{row['label']}\t{row['rank']}\t{row['parent_id']}"
        for t_id, row in taxa_rows.items()
    ]
    (raw_dir / "ncbitaxon_taxa.tsv").write_text(
        "\n".join(taxa_tsv_lines) + "\n",
        encoding="utf-8",
    )
    bacdive_tsv_lines = [
        "strain_id\tlabel\tdesignations\tculture_collection_ids\ttaxon_ids\t"
        "is_type_strain\tbacdive_id\tgenome_accessions\tbiosample_accessions",
        "kgmicrobe.strain:bacdive_155687\tEscherichia coli MG1655\tMG1655\t"
        "DSM:18039\tNCBITaxon:562\tfalse\tbacdive.strain:155687\t\t",
        "kgmicrobe.strain:bacdive_1156\tBacillus subtilis 168\t168\t"
        "DSM:402\tNCBITaxon:1423\ttrue\tbacdive.strain:1156\t\t",
        "kgmicrobe.strain:bacdive_12795\tPseudomonas aeruginosa PAO1\tPAO1\t"
        "DSM:22644\tNCBITaxon:287\tfalse\tbacdive.strain:12795\t\t",
        "kgmicrobe.strain:bacdive_6981\tMethanocaldococcus jannaschii DSM 2661\tJAL-1\t"
        "DSM:2661\tNCBITaxon:2190\ttrue\tbacdive.strain:6981\t\t",
    ]
    (raw_dir / "bacdive_strains.tsv").write_text(
        "\n".join(bacdive_tsv_lines) + "\n",
        encoding="utf-8",
    )
    strains_map = {
        tid: [{"strain_id": sid, "taxon_ids": tid}]
        for tid, sid in expected_exemplar_strains.items()
        if sid is not None
    }
    uniprot_subset = load_uniprot_proteins(
        curation_dir / "uniprot_proteins.tsv",
        taxa=taxa_rows,
    )
    validate_causal_graph_proteins(
        graphs,
        uniprot_proteins=uniprot_subset,
        taxa=taxa_rows,
        strains=strains_map,
    )
    prov_script = REPO_ROOT / "scripts" / "check_provenance.py"
    prov_spec = importlib.util.spec_from_file_location("check_provenance", prov_script)
    prov_mod = importlib.util.module_from_spec(prov_spec)
    assert prov_spec.loader is not None
    prov_spec.loader.exec_module(prov_mod)
    assert prov_mod.causal_graph_provenance_problems(synth_root) == []


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
    cover the 15 species+strain exemplar records (485 evidence-backed edges and
    130 GENE_OR_PROTEIN nodes across 59 live-verified UniProtKB accessions), and
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
    assert total_edges >= 485
    edge_count = sum(
        len(g.get("edges") or [])
        for tid in expected_ids
        for g in graphs[tid]
    )
    assert edge_count == 485
    protein_nodes = [
        n
        for tid in expected_ids
        for g in graphs[tid]
        for n in g.get("nodes") or []
        if n.get("node_type") == "GENE_OR_PROTEIN"
    ]
    assert len(protein_nodes) == 130
    expected_uniprot = {
        "UniProtKB:P02920",
        "UniProtKB:P00722",
        "UniProtKB:P03023",
        "UniProtKB:P07464",
        "UniProtKB:P08839",
        "UniProtKB:P0AA04",
        "UniProtKB:P0ACJ8",
        "UniProtKB:P0AEW4",
        "UniProtKB:P00936",
        "UniProtKB:P16497",
        "UniProtKB:P33883",
        "UniProtKB:P39764",
        "UniProtKB:P50456",
        "UniProtKB:P69783",
        "UniProtKB:P69786",
        "UniProtKB:P70962",
        "UniProtKB:P06628",
        "UniProtKB:P06535",
        "UniProtKB:P06534",
        "UniProtKB:Q00828",
        "UniProtKB:P05043",
        "UniProtKB:Q08430",
        "UniProtKB:Q00829",
        "UniProtKB:Q7WY62",
        "UniProtKB:O31661",
        "UniProtKB:O31671",
        "UniProtKB:Q9HWH2",
        "UniProtKB:Q9HWG9",
        "UniProtKB:Q9I4X0",
        "UniProtKB:P0DPB9",
        "UniProtKB:Q9HWH1",
        "UniProtKB:O69753",
        "UniProtKB:P20581",
        "UniProtKB:P25084",
        "UniProtKB:P54291",
        "UniProtKB:P54292",
        "UniProtKB:Q57766",
        "UniProtKB:Q58194",
        "UniProtKB:Q58256",
        "UniProtKB:Q58252",
        "UniProtKB:Q58255",
        "UniProtKB:Q58441",
        "UniProtKB:Q58929",
        "UniProtKB:P61154",
        "UniProtKB:Q58261",
        "UniProtKB:Q58264",
        "UniProtKB:Q59030",
        "UniProtKB:A0A095C6P1",
        "UniProtKB:A0A095CIC4",
        "UniProtKB:Q55P57",
        "UniProtKB:Q56R42",
        "UniProtKB:J9VE33",
        "UniProtKB:J9VG42",
        "UniProtKB:J9VHN6",
        "UniProtKB:J9VMN6",
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
    assert sum(1 for n in protein_nodes if n.get("proteome_id")) == 128


def test_uniprot_proteins_catalog_and_lineage_validator():
    """Verify curation/uniprot_proteins.tsv schema and validate_causal_graph_proteins
    rejection of unpinned accessions, checksum/length/locus mismatches, and cross-species
    organism_taxon_id bindings (#78 / taxonmech-infra-0003)."""
    proteins = load_uniprot_proteins(UNIPROT_PROTEINS_PATH)
    assert len(proteins) == 59
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


def test_cycle7_stage6_closed_keys_curation_events_and_provenance_invariants(tmp_path: Path):
    """Verify Cycle 7 Stage 6 (#216) closed-key schemas, CurationEvent timestamp/chronology,
    per-graph GENE_OR_PROTEIN grounding uniqueness, and provenance checks."""
    # 0. Key sets match LinkML schema slots and README YAML example passes structural + event gates
    sv = SchemaView(str(SCHEMA_PATH))
    for cls_name, key_set in (
        ("CausalGraph", CAUSAL_GRAPH_KEYS),
        ("CausalNode", CAUSAL_NODE_KEYS),
        ("CausalEdge", CAUSAL_EDGE_KEYS),
        ("EvidenceItem", EVIDENCE_ITEM_KEYS),
        ("CurationEvent", CURATION_EVENT_KEYS),
    ):
        schema_slots = frozenset(slot.name for slot in sv.class_induced_slots(cls_name))
        assert schema_slots == key_set
    assert ISO_UTC_TIMESTAMP_PATTERN.match("2026-11-05T18:00:00Z")
    assert not ISO_UTC_TIMESTAMP_PATTERN.match("2026-11-05")

    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    match = re.search(r"```yaml\n(.*?)\n```", overlay_readme, flags=re.DOTALL)
    assert match is not None
    readme_doc = yaml.safe_load(match.group(1))
    validate_causal_graph_structure({readme_doc["identifier"]: readme_doc["causal_graphs"]})
    validate_causal_graph_events({readme_doc["identifier"]: readme_doc["curation_history"]})

    # 1. Unknown keys rejected on CausalGraph, CausalNode, CausalEdge, EvidenceItem
    base_graph = {
        "graph_id": "g1",
        "title": "Test Graph",
        "nodes": [
            {
                "node_id": "t1",
                "label": "Escherichia coli",
                "node_type": "TAXON",
                "grounding": "NCBITaxon:562",
            },
            {
                "node_id": "p1",
                "label": "lactose catabolic process",
                "node_type": "BIOLOGICAL_PROCESS",
                "grounding": "GO:0005988",
            },
        ],
        "edges": [
            {
                "edge_id": "e1",
                "subject": "t1",
                "predicate": "capable of",
                "predicate_id": "RO:0002215",
                "object": "p1",
                "evidence": [
                    {
                        "reference": "PMID:9278503",
                        "snippet": "Complete genome sequence of E. coli K-12.",
                    }
                ],
            }
        ],
    }

    bad_graph_key = {"NCBITaxon:562": [{**base_graph, "extra_graph_field": "x"}]}
    with pytest.raises(SystemExit, match="unexpected CausalGraph keys"):
        validate_causal_graph_structure(bad_graph_key)

    bad_node_key = {
        "NCBITaxon:562": [
            {
                **base_graph,
                "nodes": [
                    {**base_graph["nodes"][0], "extra_node_field": "x"},
                    base_graph["nodes"][1],
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="unexpected CausalNode keys"):
        validate_causal_graph_structure(bad_node_key)

    bad_edge_key = {
        "NCBITaxon:562": [
            {
                **base_graph,
                "edges": [{**base_graph["edges"][0], "extra_edge_field": "x"}],
            }
        ]
    }
    with pytest.raises(SystemExit, match="unexpected CausalEdge keys"):
        validate_causal_graph_structure(bad_edge_key)

    bad_ev_key = {
        "NCBITaxon:562": [
            {
                **base_graph,
                "edges": [
                    {
                        **base_graph["edges"][0],
                        "evidence": [{"reference": "PMID:9278503", "extra_ev": "x"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="unexpected EvidenceItem keys"):
        validate_causal_graph_structure(bad_ev_key)

    # 2. CurationEvent validation: unknown keys, bad timestamp, out-of-order timestamps, non-bool llm_assisted
    with pytest.raises(SystemExit, match="unexpected CurationEvent keys"):
        validate_causal_graph_events(
            {
                "NCBITaxon:562": [
                    {
                        "timestamp": "2026-10-22T06:00:00Z",
                        "curator": "curator",
                        "action": "UPDATED",
                        "changes": "change",
                        "agent": "invalid",
                    }
                ]
            }
        )

    with pytest.raises(SystemExit, match="invalid ISO-8601 UTC timestamp"):
        validate_causal_graph_events(
            {
                "NCBITaxon:562": [
                    {
                        "timestamp": "2026-10-22",
                        "curator": "curator",
                        "action": "UPDATED",
                        "changes": "change",
                    }
                ]
            }
        )

    with pytest.raises(SystemExit, match="precedes previous event"):
        validate_causal_graph_events(
            {
                "NCBITaxon:562": [
                    {
                        "timestamp": "2026-10-23T06:00:00Z",
                        "curator": "curator",
                        "action": "UPDATED",
                        "changes": "later change",
                    },
                    {
                        "timestamp": "2026-10-22T06:00:00Z",
                        "curator": "curator",
                        "action": "UPDATED",
                        "changes": "earlier change",
                    },
                ]
            }
        )

    with pytest.raises(SystemExit, match="requires non-empty 'curator'"):
        validate_causal_graph_events(
            {
                "NCBITaxon:562": [
                    {
                        "timestamp": "2026-10-22T06:00:00Z",
                        "curator": "   ",
                        "action": "UPDATED",
                        "changes": "change",
                    }
                ]
            }
        )

    with pytest.raises(SystemExit, match="'llm_assisted' must be a boolean"):
        validate_causal_graph_events(
            {
                "NCBITaxon:562": [
                    {
                        "timestamp": "2026-10-22T06:00:00Z",
                        "curator": "curator",
                        "action": "UPDATED",
                        "changes": "change",
                        "llm_assisted": "yes",
                    }
                ]
            }
        )

    # 3. Duplicate GENE_OR_PROTEIN grounding within the same CausalGraph rejected
    proteins = load_uniprot_proteins(UNIPROT_PROTEINS_PATH)
    taxa = {
        "NCBITaxon:2": {"parent_id": "", "rank": "DOMAIN"},
        "NCBITaxon:561": {"parent_id": "NCBITaxon:2", "rank": "GENUS"},
        "NCBITaxon:562": {"parent_id": "NCBITaxon:561", "rank": "SPECIES"},
        "NCBITaxon:83333": {"parent_id": "NCBITaxon:562", "rank": "STRAIN"},
    }
    lacz_node_a = {
        "node_id": "lacZ_a",
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
    }
    lacz_node_b = {**lacz_node_a, "node_id": "lacZ_b"}
    dup_protein_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "nodes": [lacz_node_a, lacz_node_b],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="duplicate GENE_OR_PROTEIN grounding 'UniProtKB:P00722'",
    ):
        validate_causal_graph_proteins(
            dup_protein_graph,
            uniprot_proteins=proteins,
            taxa=taxa,
        )

    # 4. causal_graph_provenance_problems detects missing host TAXON node,
    # missing full 4-part EC xref, and missing evidence notes/snippet
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_repo_c7"
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
    graph0 = ecoli_data["causal_graphs"][0]
    # Change host TAXON node to TRAIT, strip EC:3.2.1.23 from lacZ, and strip snippet/notes
    for n in graph0["nodes"]:
        if n.get("node_type") == "TAXON":
            n["node_type"] = "TRAIT"
            n["grounding"] = "OMP:0000001"
        elif n.get("node_id") == "lacZ":
            n["xrefs"] = []
    graph0["edges"][0]["evidence"][0].pop("snippet", None)
    graph0["edges"][0]["evidence"][0].pop("notes", None)

    (overlays_dir / "NCBITaxon_562.yaml").write_text(
        yaml.safe_dump(ecoli_data, sort_keys=False),
        encoding="utf-8",
    )
    failures = mod.causal_graph_provenance_problems(synth_root)
    assert any("missing TAXON node grounded to NCBITaxon:562" in f for f in failures)
    assert any(
        "full 4-part EC xrefs [] != reference ['EC:3.2.1.23'] for UniProtKB:P00722" in f
        for f in failures
    )
    assert any("missing 'notes' or 'snippet'" in f for f in failures)


def test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract():
    """curation/causal_graphs/README.md must cite current src/taxonmech/seed.py line ranges
    for load_uniprot_proteins() and validate_causal_graph_proteins() strain_id validation,
    and document the reciprocal full 4-part EC: CausalNode.xrefs ordering invariant in the
    UNIPROT_PROTEIN_FIELDS ec_numbers table row (#222, #216, #78)."""
    import inspect

    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    src_lines, start_line = inspect.getsourcelines(load_uniprot_proteins)
    end_line = start_line + len(src_lines) - 1
    expected_load_range = f"{start_line}–{end_line}"
    assert expected_load_range in overlay_readme, (
        f"curation/causal_graphs/README.md missing load_uniprot_proteins() range {expected_load_range!r}"
    )
    assert "302–347" not in overlay_readme
    assert "555–560" not in overlay_readme
    assert "653–670" not in overlay_readme
    assert "743–748" not in overlay_readme
    assert "843–860" not in overlay_readme
    assert "803–808" not in overlay_readme
    assert "903–920" not in overlay_readme
    assert "lines 861–866,\n961–978" in overlay_readme or "lines 861–866, 961–978" in overlay_readme

    ec_row_lines = [
        line for line in overlay_readme.splitlines() if line.startswith("| `ec_numbers` |")
    ]
    assert len(ec_row_lines) == 1
    ec_row = ec_row_lines[0]
    expected_ec_phrase = (
        "all full 4-part (non-wildcard) `EC:` CURIEs in `ec_numbers` "
        "must appear in `CausalNode.xrefs` in matching order"
    )
    assert expected_ec_phrase in ec_row
    assert "scripts/check_provenance.py" in ec_row


def test_cycle8_stage6_uniprot_catalog_node_grounding_and_protein_edge_topology_gates(
    tmp_path: Path,
):
    """Enforce UNIPROT_ENTRY_NAME_PATTERN and entry_name/(organism_taxon_id, locus_tag)
    uniqueness in load_uniprot_proteins(), per-graph node grounding uniqueness and
    predicate<->predicate_id consistency in validate_causal_graph_structure(), and
    required edge predicate_id plus GENE_OR_PROTEIN RO:0002292/outgoing-edge topology
    in causal_graph_provenance_problems() (#224, #78)."""
    import importlib.util

    # 1. load_uniprot_proteins rejects invalid entry_name, duplicate entry_name,
    # and duplicate (organism_taxon_id, locus_tag)
    raw_lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    header = raw_lines[0]
    row_p00722 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P00722\t"))
    row_p02920 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P02920\t"))

    bad_entry_tsv = tmp_path / "bad_entry_name.tsv"
    bad_entry_tsv.write_text(
        header + "\n" + row_p00722.replace("BGAL_ECOLI", "bgal-ecoli", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="invalid entry_name 'bgal-ecoli'"):
        load_uniprot_proteins(bad_entry_tsv)

    dup_entry_tsv = tmp_path / "dup_entry_name.tsv"
    dup_entry_tsv.write_text(
        header
        + "\n"
        + row_p00722
        + "\n"
        + row_p02920.replace("LACY_ECOLI", "BGAL_ECOLI", 1)
        + "\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="duplicate entry_name 'BGAL_ECOLI'"):
        load_uniprot_proteins(dup_entry_tsv)

    dup_locus_tsv = tmp_path / "dup_locus.tsv"
    dup_locus_tsv.write_text(
        header + "\n" + row_p00722 + "\n" + row_p02920.replace("b0343", "b0344", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match=r"duplicate \(organism_taxon_id, locus_tag\) \('NCBITaxon:83333', 'b0344'\)",
    ):
        load_uniprot_proteins(dup_locus_tsv)

    # 2. validate_causal_graph_structure rejects duplicate non-protein grounding
    # and inconsistent predicate<->predicate_id pairings within a CausalGraph
    dup_grounding_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                    {
                        "node_id": "proc_b",
                        "label": "lactose transport duplicate",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "causally upstream of or within",
                        "predicate_id": "RO:0002418",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                    {
                        "edge_id": "e2",
                        "subject": "proc_a",
                        "predicate": "causally upstream of or within",
                        "predicate_id": "RO:0002418",
                        "object": "proc_b",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="duplicate node grounding 'GO:0015767' in graph 'g1'"):
        validate_causal_graph_structure(dup_grounding_graph)

    inconsistent_pred_id_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                    {
                        "node_id": "proc_b",
                        "label": "lactose catabolic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005990",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "causally upstream of or within",
                        "predicate_id": "RO:0002418",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                    {
                        "edge_id": "e2",
                        "subject": "proc_a",
                        "predicate": "enables",
                        "predicate_id": "RO:0002418",
                        "object": "proc_b",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="predicate_id 'RO:0002418' mapped to inconsistent predicate 'enables'",
    ):
        validate_causal_graph_structure(inconsistent_pred_id_graph)

    inconsistent_pred_label_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                    {
                        "node_id": "proc_b",
                        "label": "lactose catabolic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005990",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                    {
                        "edge_id": "e2",
                        "subject": "proc_a",
                        "predicate": "enables",
                        "predicate_id": "RO:0002418",
                        "object": "proc_b",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="predicate 'enables' mapped to inconsistent predicate_id 'RO:0002418'",
    ):
        validate_causal_graph_structure(inconsistent_pred_label_graph)

    # 3. causal_graph_provenance_problems detects missing edge predicate_id,
    # missing host-TAXON RO:0002292 (expresses) edge to GENE_OR_PROTEIN,
    # and GENE_OR_PROTEIN without outgoing functional/regulatory/causal edge
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_repo_c8"
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
    graph0 = ecoli_data["causal_graphs"][0]
    # Remove predicate_id from e3 (lactose_transport -> lactose_catabolism),
    # change e1 (taxon -> lacY) predicate_id so lacY is not expressed via RO:0002292,
    # and flip e2 (lacY -> lactose_transport) direction so lacY has no outgoing edge
    for e in graph0["edges"]:
        if e["edge_id"] == "e1":
            e["predicate"] = "part of"
            e["predicate_id"] = "BFO:0000050"
        elif e["edge_id"] == "e2":
            e["subject"], e["object"] = e["object"], e["subject"]
        elif e["edge_id"] == "e3":
            e.pop("predicate_id", None)

    (overlays_dir / "NCBITaxon_562.yaml").write_text(
        yaml.safe_dump(ecoli_data, sort_keys=False),
        encoding="utf-8",
    )
    failures = mod.causal_graph_provenance_problems(synth_root)
    assert any(
        "node 'lacY': GENE_OR_PROTEIN node is not linked from host TAXON node via RO:0002292 (expresses)"
        in f
        for f in failures
    )
    assert any(
        "node 'lacY': GENE_OR_PROTEIN node has no outgoing functional/regulatory/causal edge" in f
        for f in failures
    )
    assert any("edge 'e3': missing 'predicate_id'" in f for f in failures)


def test_overlay_readme_example_passes_structure_events_proteins_and_provenance_gates(
    tmp_path: Path,
):
    """The Overlay File Contract YAML example in curation/causal_graphs/README.md must include
    strain_id: kgmicrobe.strain:bacdive_155687 on lacZ and the required host-TAXON RO:0002292
    (expresses) edge to its GENE_OR_PROTEIN node, and pass validate_causal_graph_structure(),
    validate_causal_graph_events(), validate_causal_graph_proteins(), and
    causal_graph_provenance_problems() (#246, #234, #224, #78)."""
    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    match = re.search(r"```yaml\n(.*?)\n```", overlay_readme, flags=re.DOTALL)
    assert match is not None, "curation/causal_graphs/README.md missing yaml code block"
    readme_yaml = match.group(1)
    readme_doc = yaml.safe_load(readme_yaml)
    tid = readme_doc["identifier"]
    assert tid == "NCBITaxon:562"
    graph0 = readme_doc["causal_graphs"][0]
    lacz_nodes = [n for n in graph0["nodes"] if n.get("node_id") == "lacZ"]
    assert len(lacz_nodes) == 1
    assert lacz_nodes[0].get("strain_id") == "kgmicrobe.strain:bacdive_155687"
    expresses_edges = [
        e
        for e in graph0["edges"]
        if e.get("subject") == "taxon"
        and e.get("predicate") == "expresses"
        and e.get("predicate_id") == "RO:0002292"
        and e.get("object") == "lacZ"
    ]
    assert len(expresses_edges) == 1

    validate_causal_graph_structure({tid: readme_doc["causal_graphs"]})
    validate_causal_graph_events({tid: readme_doc["curation_history"]})

    proteins = load_uniprot_proteins(UNIPROT_PROTEINS_PATH)
    taxa = {
        "NCBITaxon:2": {"label": "Bacteria", "parent_id": "", "rank": "DOMAIN"},
        "NCBITaxon:561": {"label": "Escherichia", "parent_id": "NCBITaxon:2", "rank": "GENUS"},
        "NCBITaxon:562": {
            "label": "Escherichia coli",
            "parent_id": "NCBITaxon:561",
            "rank": "SPECIES",
        },
        "NCBITaxon:83333": {
            "label": "Escherichia coli K-12",
            "parent_id": "NCBITaxon:562",
            "rank": "STRAIN",
        },
    }
    strains = {
        "NCBITaxon:562": [
            {
                "strain_id": "kgmicrobe.strain:bacdive_155687",
                "taxon_ids": "NCBITaxon:562",
            }
        ],
    }
    validate_causal_graph_proteins(
        {tid: readme_doc["causal_graphs"]},
        uniprot_proteins=proteins,
        taxa=taxa,
        strains=strains,
    )

    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_readme_example"
    curation_dir = synth_root / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    raw_dir = synth_root / "data" / "raw"
    overlays_dir.mkdir(parents=True)
    raw_dir.mkdir(parents=True)
    raw_lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    header = raw_lines[0]
    row_p00722 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P00722\t"))
    (curation_dir / "uniprot_proteins.tsv").write_text(
        header + "\n" + row_p00722 + "\n",
        encoding="utf-8",
    )
    (curation_dir / "seed_scope.tsv").write_text(
        "identifier\tadded\treason\nNCBITaxon:562\t2026-01-01\ttest\n",
        encoding="utf-8",
    )
    (raw_dir / "ncbitaxon_taxa.tsv").write_text(
        "taxon_id\tlabel\trank\tparent_id\n"
        "NCBITaxon:2\tBacteria\tDOMAIN\t\n"
        "NCBITaxon:561\tEscherichia\tGENUS\tNCBITaxon:2\n"
        "NCBITaxon:562\tEscherichia coli\tSPECIES\tNCBITaxon:561\n"
        "NCBITaxon:83333\tEscherichia coli K-12\tSTRAIN\tNCBITaxon:562\n",
        encoding="utf-8",
    )
    (raw_dir / "bacdive_strains.tsv").write_text(
        "strain_id\tlabel\tdesignations\tculture_collection_ids\ttaxon_ids\t"
        "is_type_strain\tbacdive_id\tgenome_accessions\tbiosample_accessions\n"
        "kgmicrobe.strain:bacdive_155687\tEscherichia coli MG1655\tMG1655\t"
        "DSM:18039\tNCBITaxon:562\tfalse\tbacdive.strain:155687\t\t\n",
        encoding="utf-8",
    )
    (overlays_dir / "NCBITaxon_562.yaml").write_text(readme_yaml + "\n", encoding="utf-8")
    assert mod.causal_graph_provenance_problems(synth_root) == []


def test_cycle9_stage6_uniprot_release_org_proteome_consistency_and_causal_graph_node_label_edge_typing_gates(
    tmp_path: Path,
):
    """Enforce UNIPROT_RELEASE_PATTERN, organism_taxon_id->(organism_label, proteome_id)
    and proteome_id->organism_taxon_id consistency, and organism_label correspondence in
    load_uniprot_proteins(), per-graph CausalNode.label uniqueness and TAXON/RO:0002292
    edge endpoint typing in validate_causal_graph_structure(), and required CausalNode
    grounding plus TAXON label correspondence in causal_graph_provenance_problems() (#236, #78)."""
    raw_lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    header = raw_lines[0]
    row_p00722 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P00722\t"))
    row_p02920 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P02920\t"))
    row_p06534 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P06534\t"))

    # 1a. Invalid release_version rejected
    bad_rel_tsv = tmp_path / "bad_release.tsv"
    bad_rel_tsv.write_text(
        header + "\n" + row_p00722.replace("2026_02", "2026-13", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="invalid release_version '2026-13'"):
        load_uniprot_proteins(bad_rel_tsv)

    # 1b. organism_label mismatch against ncbitaxon_taxa.tsv rejected when taxa provides label
    good_tsv = tmp_path / "good_single.tsv"
    good_tsv.write_text(header + "\n" + row_p00722 + "\n", encoding="utf-8")
    mismatched_taxa = {
        "NCBITaxon:2": {"parent_id": "", "rank": "DOMAIN", "label": "Bacteria"},
        "NCBITaxon:561": {"parent_id": "NCBITaxon:2", "rank": "GENUS", "label": "Escherichia"},
        "NCBITaxon:562": {
            "parent_id": "NCBITaxon:561",
            "rank": "SPECIES",
            "label": "Escherichia coli",
        },
        "NCBITaxon:83333": {
            "parent_id": "NCBITaxon:562",
            "rank": "STRAIN",
            "label": "Escherichia coli str. K-12 wrong label",
        },
    }
    with pytest.raises(
        SystemExit,
        match="organism_label 'Escherichia coli K-12' != ncbitaxon_taxa.tsv label",
    ):
        load_uniprot_proteins(good_tsv, taxa=mismatched_taxa)

    # 1c. Inconsistent (organism_label, proteome_id) for the same organism_taxon_id rejected
    inconsistent_org_tsv = tmp_path / "inconsistent_org.tsv"
    inconsistent_org_tsv.write_text(
        header
        + "\n"
        + row_p00722
        + "\n"
        + row_p02920.replace("UP:UP000000625", "UP:UP000001570", 1)
        + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match=r"inconsistent \(organism_label, proteome_id\).*for NCBITaxon:83333",
    ):
        load_uniprot_proteins(inconsistent_org_tsv)

    # 1d. Same proteome_id mapped to multiple organism_taxon_id values rejected
    dup_proteome_tsv = tmp_path / "dup_proteome.tsv"
    dup_proteome_tsv.write_text(
        header
        + "\n"
        + row_p00722
        + "\n"
        + row_p06534.replace("UP:UP000001570", "UP:UP000000625", 1)
        + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match="proteome_id 'UP:UP000000625' mapped to multiple organism_taxon_id values",
    ):
        load_uniprot_proteins(dup_proteome_tsv)

    # 2a. Duplicate CausalNode.label within the same CausalGraph rejected
    dup_label_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                    {
                        "node_id": "proc_b",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005990",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "causally upstream of or within",
                        "predicate_id": "RO:0002418",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                    {
                        "edge_id": "e2",
                        "subject": "proc_a",
                        "predicate": "causally upstream of or within",
                        "predicate_id": "RO:0002418",
                        "object": "proc_b",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="duplicate node label 'lactose transport' in graph 'g1'"):
        validate_causal_graph_structure(dup_label_graph)

    # 2b. Edge targeting a TAXON node as object rejected
    edge_to_taxon_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "proc_a",
                        "predicate": "causally upstream of or within",
                        "predicate_id": "RO:0002418",
                        "object": "taxon",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(SystemExit, match="object 'taxon' cannot target a TAXON node"):
        validate_causal_graph_structure(edge_to_taxon_graph)

    # 2c. RO:0002292 (expresses) edge targeting a non-GENE_OR_PROTEIN object rejected
    expresses_non_protein_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "expresses",
                        "predicate_id": "RO:0002292",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match=r"RO:0002292 \(expresses\) object 'proc_a' must be a GENE_OR_PROTEIN node",
    ):
        validate_causal_graph_structure(expresses_non_protein_graph)

    # 3. causal_graph_provenance_problems detects missing CausalNode.grounding,
    # TAXON label mismatch against ncbitaxon_taxa.tsv, and non-host-TAXON RO:0002292 subject
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_repo_c9"
    curation_dir = synth_root / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    raw_dir = synth_root / "data" / "raw"
    overlays_dir.mkdir(parents=True)
    raw_dir.mkdir(parents=True)
    (curation_dir / "uniprot_proteins.tsv").write_text(
        UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (curation_dir / "seed_scope.tsv").write_text(
        "identifier\tadded\treason\nNCBITaxon:562\t2026-01-01\ttest\n",
        encoding="utf-8",
    )
    (raw_dir / "ncbitaxon_taxa.tsv").write_text(
        "taxon_id\tparent_id\trank\tlabel\n"
        "NCBITaxon:2\t\tDOMAIN\tBacteria\n"
        "NCBITaxon:561\tNCBITaxon:2\tGENUS\tEscherichia\n"
        "NCBITaxon:562\tNCBITaxon:561\tSPECIES\tEscherichia coli\n"
        "NCBITaxon:83333\tNCBITaxon:562\tSTRAIN\tEscherichia coli K-12\n"
        "NCBITaxon:224308\tNCBITaxon:562\tSTRAIN\tBacillus subtilis subsp. subtilis str. 168\n"
        "NCBITaxon:208964\tNCBITaxon:562\tSTRAIN\tPseudomonas aeruginosa PAO1\n"
        "NCBITaxon:243232\tNCBITaxon:562\tSTRAIN\tMethanocaldococcus jannaschii DSM 2661\n"
        "NCBITaxon:294750\tNCBITaxon:562\tSTRAIN\tCryptococcus deuterogattii R265\n"
        "NCBITaxon:235443\tNCBITaxon:562\tSTRAIN\tCryptococcus neoformans H99\n"
        "NCBITaxon:283643\tNCBITaxon:562\tSTRAIN\tCryptococcus deneoformans B-3501A\n",
        encoding="utf-8",
    )
    ecoli_data = yaml.safe_load(
        (REPO_ROOT / "curation" / "causal_graphs" / "NCBITaxon_562.yaml").read_text(
            encoding="utf-8"
        )
    )
    graph0 = ecoli_data["causal_graphs"][0]
    for n in graph0["nodes"]:
        if n["node_id"] == "taxon":
            n["label"] = "Escherichia coli wrong label"
        elif n["node_id"] == "lactose_transport":
            n.pop("grounding", None)
    graph0["edges"].append(
        {
            "edge_id": "bad_expresses",
            "subject": "lactose_transport",
            "predicate": "expresses",
            "predicate_id": "RO:0002292",
            "object": "lacZ",
            "evidence": [
                {
                    "reference": "PMID:9278503",
                    "snippet": "Synthetic non-host-TAXON expresses edge for test.",
                }
            ],
        }
    )
    (overlays_dir / "NCBITaxon_562.yaml").write_text(
        yaml.safe_dump(ecoli_data, sort_keys=False),
        encoding="utf-8",
    )
    failures = mod.causal_graph_provenance_problems(synth_root)
    assert any(
        "node 'taxon': TAXON label 'Escherichia coli wrong label' != "
        "ncbitaxon_taxa.tsv label 'Escherichia coli' for NCBITaxon:562" in f
        for f in failures
    )
    assert any("node 'lactose_transport': missing 'grounding' CURIE" in f for f in failures)
    assert any(
        "edge 'bad_expresses': RO:0002292 (expresses) subject 'lactose_transport' "
        "must be a host TAXON node" in f
        for f in failures
    )


def test_cycle10_stage6_uniprot_gene_crc64_mnemonic_and_causal_graph_prefix_strain_id_gates(
    tmp_path: Path,
):
    """Enforce per-organism (organism_taxon_id, gene_symbol) and (organism_taxon_id,
    sequence_crc64) uniqueness, entry_name organism suffix consistency, and entry_status
    prefix alignment in load_uniprot_proteins(), CausalNode.grounding prefix-to-node_type
    domain isolation and single RO:0002292 (expresses) edge per GENE_OR_PROTEIN object in
    validate_causal_graph_structure(), and required host-subtree strain_id provenance in
    causal_graph_provenance_problems() (#249, #246, #78)."""
    raw_lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    header = raw_lines[0]
    row_p00722 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P00722\t"))
    row_p02920 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P02920\t"))
    row_trembl = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:A0A095C6P1\t"))

    # 1a. Duplicate (organism_taxon_id, gene_symbol) rejected
    dup_gene_tsv = tmp_path / "dup_gene.tsv"
    dup_gene_tsv.write_text(
        header + "\n" + row_p00722 + "\n" + row_p02920.replace("\tlacY\t", "\tlacZ\t", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match=r"duplicate \(organism_taxon_id, gene_symbol\) \('NCBITaxon:83333', 'lacZ'\)",
    ):
        load_uniprot_proteins(dup_gene_tsv)

    # 1b. Duplicate (organism_taxon_id, sequence_crc64) rejected
    dup_crc_tsv = tmp_path / "dup_crc.tsv"
    dup_crc_tsv.write_text(
        header
        + "\n"
        + row_p00722
        + "\n"
        + row_p02920.replace("24A8062F628CDA32", "9D295EF4CEF90B08", 1)
        + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match=r"duplicate \(organism_taxon_id, sequence_crc64\) \('NCBITaxon:83333', '9D295EF4CEF90B08'\)",
    ):
        load_uniprot_proteins(dup_crc_tsv)

    # 1c. Inconsistent entry_name organism suffix across the same organism_taxon_id rejected
    bad_suffix_tsv = tmp_path / "bad_suffix.tsv"
    bad_suffix_tsv.write_text(
        header
        + "\n"
        + row_p00722
        + "\n"
        + row_p02920.replace("LACY_ECOLI", "LACY_BACSU", 1)
        + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match="inconsistent entry_name organism suffix 'BACSU' != 'ECOLI' for NCBITaxon:83333",
    ):
        load_uniprot_proteins(bad_suffix_tsv)

    # 1d. TREMBL entry_name prefix != bare accession rejected
    bad_trembl_tsv = tmp_path / "bad_trembl.tsv"
    bad_trembl_tsv.write_text(
        header + "\n" + row_trembl.replace("A0A095C6P1_9BASI", "CAP59_9BASI", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match="TREMBL entry_name prefix 'CAP59' != accession 'A0A095C6P1'",
    ):
        load_uniprot_proteins(bad_trembl_tsv)

    # 1e. SWISS_PROT entry_name prefix == bare accession rejected
    bad_sp_tsv = tmp_path / "bad_sp.tsv"
    bad_sp_tsv.write_text(
        header + "\n" + row_p00722.replace("BGAL_ECOLI", "P00722_ECOLI", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match="SWISS_PROT entry_name prefix 'P00722' must not equal accession 'P00722'",
    ):
        load_uniprot_proteins(bad_sp_tsv)

    # 2a. Non-TAXON node using NCBITaxon: grounding rejected
    non_taxon_ncbitaxon_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "NCBITaxon:83333",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match=r"non-TAXON node \(BIOLOGICAL_PROCESS\) cannot use NCBITaxon: grounding 'NCBITaxon:83333'",
    ):
        validate_causal_graph_structure(non_taxon_ncbitaxon_graph)

    # 2b. Non-GENE_OR_PROTEIN node using UniProtKB: grounding rejected
    non_protein_uniprot_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "func_a",
                        "label": "beta-galactosidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "UniProtKB:P00722",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "func_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match=(
            r"non-GENE_OR_PROTEIN node \(MOLECULAR_FUNCTION\) "
            r"cannot use UniProtKB: grounding 'UniProtKB:P00722'"
        ),
    ):
        validate_causal_graph_structure(non_protein_uniprot_graph)

    # 2c. GENE_OR_PROTEIN node with non-UNIPROT_ID_PATTERN grounding rejected
    bad_protein_grounding_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "lacZ",
                        "label": "Beta-galactosidase LacZ",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "GO:0004565",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "expresses",
                        "predicate_id": "RO:0002292",
                        "object": "lacZ",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="GENE_OR_PROTEIN grounding 'GO:0004565' must match UNIPROT_ID_PATTERN",
    ):
        validate_causal_graph_structure(bad_protein_grounding_graph)

    # 2d. Duplicate RO:0002292 (expresses) edge targeting the same GENE_OR_PROTEIN object rejected
    dup_expresses_graph = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "sub_taxon",
                        "label": "Escherichia coli K-12",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:83333",
                    },
                    {
                        "node_id": "lacZ",
                        "label": "Beta-galactosidase LacZ",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "UniProtKB:P00722",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "expresses",
                        "predicate_id": "RO:0002292",
                        "object": "lacZ",
                        "evidence": [{"reference": "PMID:7000781"}],
                    },
                    {
                        "edge_id": "e2",
                        "subject": "sub_taxon",
                        "predicate": "expresses",
                        "predicate_id": "RO:0002292",
                        "object": "lacZ",
                        "evidence": [{"reference": "PMID:9278503"}],
                    },
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match=r"duplicate RO:0002292 \(expresses\) edge targeting 'lacZ'",
    ):
        validate_causal_graph_structure(dup_expresses_graph)

    # 3. causal_graph_provenance_problems detects missing strain_id when host taxon has a
    # lineage-compatible BacDive strain in its subtree
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_repo_c10"
    curation_dir = synth_root / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    raw_dir = synth_root / "data" / "raw"
    overlays_dir.mkdir(parents=True)
    raw_dir.mkdir(parents=True)
    (curation_dir / "uniprot_proteins.tsv").write_text(
        header + "\n" + row_p00722 + "\n",
        encoding="utf-8",
    )
    (curation_dir / "seed_scope.tsv").write_text(
        "identifier\tadded\treason\nNCBITaxon:562\t2026-01-01\ttest\n",
        encoding="utf-8",
    )
    (raw_dir / "ncbitaxon_taxa.tsv").write_text(
        "taxon_id\tlabel\trank\tparent_id\n"
        "NCBITaxon:2\tBacteria\tDOMAIN\t\n"
        "NCBITaxon:561\tEscherichia\tGENUS\tNCBITaxon:2\n"
        "NCBITaxon:562\tEscherichia coli\tSPECIES\tNCBITaxon:561\n"
        "NCBITaxon:83333\tEscherichia coli K-12\tSTRAIN\tNCBITaxon:562\n",
        encoding="utf-8",
    )
    (raw_dir / "bacdive_strains.tsv").write_text(
        "strain_id\tlabel\tdesignations\tculture_collection_ids\ttaxon_ids\t"
        "is_type_strain\tbacdive_id\tgenome_accessions\tbiosample_accessions\n"
        "kgmicrobe.strain:bacdive_155687\tEscherichia coli MG1655\tMG1655\t"
        "DSM:18039\tNCBITaxon:562\tfalse\tbacdive.strain:155687\t\t\n",
        encoding="utf-8",
    )
    overlay_readme = (REPO_ROOT / "curation" / "causal_graphs" / "README.md").read_text(
        encoding="utf-8"
    )
    match = re.search(r"```yaml\n(.*?)\n```", overlay_readme, flags=re.DOTALL)
    assert match is not None
    readme_doc = yaml.safe_load(match.group(1))
    for n in readme_doc["causal_graphs"][0]["nodes"]:
        if n.get("node_id") == "lacZ":
            n.pop("strain_id", None)
    (overlays_dir / "NCBITaxon_562.yaml").write_text(
        yaml.safe_dump(readme_doc, sort_keys=False),
        encoding="utf-8",
    )
    failures = mod.causal_graph_provenance_problems(synth_root)
    assert any(
        "node 'lacZ': GENE_OR_PROTEIN node missing required 'strain_id' for host taxon "
        "NCBITaxon:562 with subtree BacDive strain" in f
        for f in failures
    )


def test_cycle11_stage6_uniprot_sort_release_pin_and_causal_graph_chebi_go_homogeneity_gates(
    tmp_path: Path,
):
    """Enforce strict ascending uniprot_id row ordering and single uniform release_version
    pin in load_uniprot_proteins(), CHEBI_ID_PATTERN / GO_ID_PATTERN node grounding
    validation and non-empty optional description/snippet/notes validation in
    validate_causal_graph_structure(), and host-taxon TAXON node exclusivity plus
    within-graph GENE_OR_PROTEIN organism_taxon_id/strain_id homogeneity in
    causal_graph_provenance_problems() (#259, #256, #78)."""
    assert CHEBI_ID_PATTERN.match("CHEBI:17716")
    assert not CHEBI_ID_PATTERN.match("CHEBI:0")
    assert GO_ID_PATTERN.match("GO:0019513")
    assert not GO_ID_PATTERN.match("GO:19513")

    raw_lines = UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8").splitlines()
    header = raw_lines[0]
    row_p00722 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P00722\t"))
    row_p02920 = next(line for line in raw_lines[1:] if line.startswith("UniProtKB:P02920\t"))

    # 1a. Out-of-order uniprot_id row rejected
    unsorted_tsv = tmp_path / "unsorted.tsv"
    unsorted_tsv.write_text(
        header + "\n" + row_p02920 + "\n" + row_p00722 + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match=(
            r"out-of-order uniprot_id 'UniProtKB:P00722' after "
            r"'UniProtKB:P02920' \(must be sorted ascending\)"
        ),
    ):
        load_uniprot_proteins(unsorted_tsv)

    # 1b. Mixed release_version catalog pin rejected
    mixed_rel_tsv = tmp_path / "mixed_rel.tsv"
    mixed_rel_tsv.write_text(
        header + "\n" + row_p00722 + "\n" + row_p02920.replace("2026_02", "2026_03", 1) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        SystemExit,
        match="inconsistent release_version '2026_03' != catalog pin '2026_02' for 'UniProtKB:P02920'",
    ):
        load_uniprot_proteins(mixed_rel_tsv)

    # 2a. CHEMICAL node with non-CHEBI_ID_PATTERN grounding rejected
    bad_chem_grounding = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "chem_a",
                        "label": "lactose",
                        "node_type": "CHEMICAL",
                        "grounding": "GO:0005988",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "chem_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="CHEMICAL grounding 'GO:0005988' must match CHEBI_ID_PATTERN",
    ):
        validate_causal_graph_structure(bad_chem_grounding)

    # 2b. Non-CHEMICAL node using CHEBI: grounding rejected
    non_chem_chebi = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "CHEBI:17716",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match=r"non-CHEMICAL node \(BIOLOGICAL_PROCESS\) cannot use CHEBI: grounding 'CHEBI:17716'",
    ):
        validate_causal_graph_structure(non_chem_chebi)

    # 2c. BIOLOGICAL_PROCESS / MOLECULAR_FUNCTION node with non-GO_ID_PATTERN grounding rejected
    bad_go_grounding = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:15767",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="BIOLOGICAL_PROCESS grounding 'GO:15767' must match GO_ID_PATTERN",
    ):
        validate_causal_graph_structure(bad_go_grounding)

    # 2d. Empty/whitespace-only CausalGraph.description, CausalNode.description,
    # or EvidenceItem.snippet rejected
    empty_gdesc = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "description": "   ",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781"}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="requires non-empty string 'description' when present",
    ):
        validate_causal_graph_structure(empty_gdesc)

    empty_snippet = {
        "NCBITaxon:562": [
            {
                "graph_id": "g1",
                "title": "Test",
                "nodes": [
                    {
                        "node_id": "taxon",
                        "label": "Escherichia coli",
                        "node_type": "TAXON",
                        "grounding": "NCBITaxon:562",
                    },
                    {
                        "node_id": "proc_a",
                        "label": "lactose transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015767",
                    },
                ],
                "edges": [
                    {
                        "edge_id": "e1",
                        "subject": "taxon",
                        "predicate": "capable of",
                        "predicate_id": "RO:0002215",
                        "object": "proc_a",
                        "evidence": [{"reference": "PMID:7000781", "snippet": "   "}],
                    }
                ],
            }
        ]
    }
    with pytest.raises(
        SystemExit,
        match="evidence item requires non-empty string 'snippet' when present",
    ):
        validate_causal_graph_structure(empty_snippet)

    # 3. causal_graph_provenance_problems detects non-host TAXON grounding and
    # mixed GENE_OR_PROTEIN strain_id within the same CausalGraph
    script_path = REPO_ROOT / "scripts" / "check_provenance.py"
    spec = importlib.util.spec_from_file_location("check_provenance", script_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    synth_root = tmp_path / "synth_repo_c11"
    curation_dir = synth_root / "curation"
    overlays_dir = curation_dir / "causal_graphs"
    raw_dir = synth_root / "data" / "raw"
    overlays_dir.mkdir(parents=True)
    raw_dir.mkdir(parents=True)
    (curation_dir / "uniprot_proteins.tsv").write_text(
        UNIPROT_PROTEINS_PATH.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (curation_dir / "seed_scope.tsv").write_text(
        "identifier\tadded\treason\nNCBITaxon:562\t2026-01-01\ttest\n",
        encoding="utf-8",
    )
    (raw_dir / "ncbitaxon_taxa.tsv").write_text(
        "taxon_id\tlabel\trank\tparent_id\n"
        "NCBITaxon:2\tBacteria\tDOMAIN\t\n"
        "NCBITaxon:561\tEscherichia\tGENUS\tNCBITaxon:2\n"
        "NCBITaxon:562\tEscherichia coli\tSPECIES\tNCBITaxon:561\n"
        "NCBITaxon:83333\tEscherichia coli K-12\tSTRAIN\tNCBITaxon:562\n"
        "NCBITaxon:224308\tBacillus subtilis subsp. subtilis str. 168\tSTRAIN\tNCBITaxon:562\n"
        "NCBITaxon:208964\tPseudomonas aeruginosa PAO1\tSTRAIN\tNCBITaxon:562\n"
        "NCBITaxon:243232\tMethanocaldococcus jannaschii DSM 2661\tSTRAIN\tNCBITaxon:562\n"
        "NCBITaxon:294750\tCryptococcus deuterogattii R265\tSTRAIN\tNCBITaxon:562\n"
        "NCBITaxon:235443\tCryptococcus neoformans H99\tSTRAIN\tNCBITaxon:562\n"
        "NCBITaxon:283643\tCryptococcus deneoformans B-3501A\tSTRAIN\tNCBITaxon:562\n",
        encoding="utf-8",
    )
    (raw_dir / "bacdive_strains.tsv").write_text(
        "strain_id\tlabel\tdesignations\tculture_collection_ids\ttaxon_ids\t"
        "is_type_strain\tbacdive_id\tgenome_accessions\tbiosample_accessions\n"
        "kgmicrobe.strain:bacdive_155687\tEscherichia coli MG1655\tMG1655\t"
        "DSM:18039\tNCBITaxon:562\tfalse\tbacdive.strain:155687\t\t\n"
        "kgmicrobe.strain:bacdive_155688\tEscherichia coli K-12\tK-12\t"
        "DSM:498\tNCBITaxon:562\tfalse\tbacdive.strain:155688\t\t\n",
        encoding="utf-8",
    )
    ecoli_data = yaml.safe_load(
        (REPO_ROOT / "curation" / "causal_graphs" / "NCBITaxon_562.yaml").read_text(
            encoding="utf-8"
        )
    )
    graph0 = ecoli_data["causal_graphs"][0]
    graph0["nodes"].append(
        {
            "node_id": "extra_taxon",
            "label": "Escherichia coli K-12",
            "node_type": "TAXON",
            "grounding": "NCBITaxon:83333",
        }
    )
    graph0["edges"].append(
        {
            "edge_id": "extra_taxon_edge",
            "subject": "extra_taxon",
            "predicate": "capable of",
            "predicate_id": "RO:0002215",
            "object": "lactose_transport",
            "evidence": [
                {
                    "reference": "PMID:9278503",
                    "snippet": "Synthetic extra taxon edge for test.",
                }
            ],
        }
    )
    for n in graph0["nodes"]:
        if n.get("node_id") == "lacZ":
            n["strain_id"] = "kgmicrobe.strain:bacdive_155688"
    (overlays_dir / "NCBITaxon_562.yaml").write_text(
        yaml.safe_dump(ecoli_data, sort_keys=False),
        encoding="utf-8",
    )
    failures = mod.causal_graph_provenance_problems(synth_root)
    assert any(
        "node 'extra_taxon': TAXON grounding 'NCBITaxon:83333' != host taxon 'NCBITaxon:562'" in f
        for f in failures
    )
    assert any(
        "node 'lacZ': inconsistent GENE_OR_PROTEIN strain_id "
        "'kgmicrobe.strain:bacdive_155688' != 'kgmicrobe.strain:bacdive_155687'" in f
        for f in failures
    )


