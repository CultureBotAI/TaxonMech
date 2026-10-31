# Curated Causal-Graph Overlays (`curation/causal_graphs/`)

This directory holds maintained YAML overlay files (`*.yaml`) that attach
evidence-backed `causal_graphs` (and optional curation `history` events) to
in-scope `TaxonRecord` entries during `just seed-apply` (`src/taxonmech/seed.py`)
and `scripts/verify_corpus.py` (#78, `taxonmech-infra-0001`).

## Overlay File Contract

Each `*.yaml` file in `curation/causal_graphs/` defines overlays for a single
NCBI taxon record using the `TaxonRecord` slot names (`identifier`,
`causal_graphs`, and optional `curation_history`):

```yaml
identifier: NCBITaxon:562
causal_graphs:
  - graph_id: lac-operon-lactose-catabolism
    title: E. coli K-12 lacZYA lactose transport and hydrolysis pathway
    description: >-
      Beta-galactosidase (LacZ) and lactose permease (LacY) mediate lactose
      uptake and hydrolysis into D-glucose and D-galactose in Escherichia coli.
    nodes:
      - node_id: lacZ
        label: beta-galactosidase LacZ
        node_type: GENE_OR_PROTEIN
        grounding: UniProtKB:P00722
        xrefs:
          - EC:3.2.1.23
        organism_taxon_id: NCBITaxon:83333
        proteome_id: UP:UP000000625
        gene_symbol: lacZ
        locus_tag: b0344
        sequence_length: 1024
        sequence_crc64: 9D295EF4CEF90B08
        sequence_version: 2
        entry_status: SWISS_PROT
      - node_id: lactose-hydrolysis
        label: lactose catabolic process via hydrolase
        node_type: BIOLOGICAL_PROCESS
        grounding: GO:0019513
    edges:
      - edge_id: lacz-capable-of-lactose-hydrolysis
        subject: lacZ
        predicate: capable of
        predicate_id: RO:0002215
        object: lactose-hydrolysis
        evidence:
          - reference: PMID:13426092
            snippet: >-
              Classical genetic and biochemical characterization of the
              Escherichia coli beta-galactosidase (lacZ) system.
```

## Validation Gates

1. **LinkML schema validation (`src/taxonmech/schema/taxonmech.yaml`)**:
   Every merged `TaxonRecord` is validated through
   `taxonmech.validation.write_validated.write_validated_taxon` before write.
2. **Ontology ID↔label correspondence (`conf/id_label_targets.yaml`)**:
   `CausalNode.grounding` + `CausalNode.label` and `CausalEdge.predicate_id` +
   `CausalEdge.predicate_label` are checked by
   `scripts/validate_id_label_correspondence.py`. Ontology-backed prefixes
   (`NCBITaxon`, `ENVO`, `UBERON`, `FOODON`, `CHEBI`, `GO`, `MONDO`, `HP`,
   `PATO`, `RO`, `BFO`, `cob`) are resolved via OAK adapters; curated identifier
   prefixes (`UniProtKB`, `EC`, `METPO`, `OMP`, `UP`, `traitmech`, `habitatmech`)
   are registered in `src/taxonmech/schema/taxonmech.yaml` and
   `conf/id_label_targets.yaml`.
3. **Causal-graph structural referential integrity (`src/taxonmech/seed.py`)**:
   `load_causal_graphs()` invokes `validate_causal_graph_structure()` to verify
   `node_id` and `edge_id` syntax (`EDGE_ID_PATTERN`) and uniqueness within
   every graph, `CausalNodeTypeEnum` membership (`CAUSAL_NODE_TYPES`), isolation
   of protein-only slots (`PROTEIN_ONLY_NODE_SLOTS`) exclusively to
   `GENE_OR_PROTEIN` nodes, `CURIE_PATTERN` syntax and non-duplication for
   `grounding`, `xrefs`, and `predicate_id` (plus `NCBITaxon:` prefix enforcement
   for `TAXON` nodes), referential integrity of `edge.subject` and `edge.object`
   against `graph.nodes`, absence of self-loop edges (`subject != object`) and
   duplicate parallel `(subject, predicate_id or predicate, object)` edges, and
   non-empty, non-duplicate `evidence[].reference` citations matching
   `EVIDENCE_REFERENCE_PATTERN` (`PMID:`, `PMC:PMC`, `DOI:10.`, or `http(s)://`)
   on every edge (#189).
4. **Offline UniProtKB reference, NCBI Taxonomy lineage, and BacDive strain validation (`curation/uniprot_proteins.tsv`, `conf/sources.yaml`, & `src/taxonmech/seed.py`)**:
   `load_uniprot_proteins()`, `load_causal_graphs()`, `load_inventory()`, and
   `scripts/check_provenance.py` enforce required descriptive metadata
   (`entry_name`, `protein_name`, `organism_label`, `release_version`),
   `gene_symbol` or `locus_tag` presence, and `EC_NUMBER_PATTERN` (`EC:<digits>`)
   syntax/uniqueness on `curation/uniprot_proteins.tsv`; verify every
   `GENE_OR_PROTEIN` node against the pinned reference catalog (`entry_status`,
   `organism_taxon_id`, `proteome_id`, `gene_symbol`, `locus_tag`, `ec_numbers`,
   `sequence_length`, `sequence_crc64`, `sequence_version`); verify `TAXON` node
   `grounding` presence and lineage compatibility against `ncbitaxon_taxa.tsv`;
   and verify any declared `strain_id` (`kgmicrobe.strain:bacdive_*`) against
   `data/raw/bacdive_strains.tsv` and the host record/organism lineage so
   species/strain records cannot bind cross-species or mismatched protein/strain
   entries (#189).
5. **Byte-exact corpus reproducibility (`scripts/verify_corpus.py`)**:
   `scripts/verify_corpus.py` loads `curation/causal_graphs/` through
   `build_corpus()` and compares every `data/taxa/<domain>/<slug>.yaml` against
   `emit_taxon_yaml(build_document(concept, corpus.inventory))`.
