# Curated Causal-Graph Overlays (`curation/causal_graphs/`)

This directory holds maintained YAML overlay files (`*.yaml`) that attach
evidence-backed `causal_graphs` and required curation `curation_history` events to
in-scope `TaxonRecord` entries during `just seed-apply` (`src/taxonmech/seed.py`)
and `scripts/verify_corpus.py` (#78, `taxonmech-infra-0001`).

## Overlay File Contract

Each `*.yaml` file in `curation/causal_graphs/` defines overlays for a single
NCBI taxon record using the `TaxonRecord` slot names (`identifier`,
`causal_graphs`, and required non-empty `curation_history`):

```yaml
identifier: NCBITaxon:562
causal_graphs:
  - graph_id: lac-operon-lactose-catabolism
    title: E. coli K-12 lacZYA lactose transport and hydrolysis pathway
    description: >-
      Beta-galactosidase (LacZ) and lactose permease (LacY) mediate lactose
      uptake and hydrolysis into D-glucose and D-galactose in Escherichia coli.
    nodes:
      - node_id: taxon
        label: Escherichia coli
        node_type: TAXON
        grounding: NCBITaxon:562
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
      - edge_id: taxon-capable-of-lactose-hydrolysis
        subject: taxon
        predicate: capable of
        predicate_id: RO:0002215
        object: lactose-hydrolysis
        evidence:
          - reference: PMID:13426092
            snippet: >-
              Escherichia coli catabolizes lactose via beta-galactosidase
              hydrolysis.
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
curation_history:
  - timestamp: "2026-10-22T08:00:00Z"
    curator: curator
    action: CURATED
    changes: Curated E. coli K-12 lacZYA lactose catabolism causal graph (#78).
    llm_assisted: false
```

## Pinned UniProtKB Protein Catalog (`curation/uniprot_proteins.tsv`) and `strain_id` Binding

Every `GENE_OR_PROTEIN` node in `curation/causal_graphs/*.yaml` must resolve
offline against a row in `curation/uniprot_proteins.tsv` (registered in
`conf/sources.yaml`). `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines
302–347) enforces the exact 14-column header tuple `UNIPROT_PROTEIN_FIELDS`
(`src/taxonmech/seed.py` lines 62–77):

| Column (`UNIPROT_PROTEIN_FIELDS`) | Required? | Format / Validation Contract (`load_uniprot_proteins` & `validate_causal_graph_proteins`) |
|---|---|---|
| `uniprot_id` | Required (PK) | Unique `UniProtKB:<accession>` CURIE matching `UNIPROT_ID_PATTERN` and `CausalNode.grounding` |
| `entry_name` | Required | Non-empty UniProtKB entry mnemonic (e.g. `BGAL_ECOLI`) |
| `entry_status` | Required | `UniProtEntryStatusEnum` value (`SWISS_PROT` or `TREMBL`); must match `CausalNode.entry_status` |
| `protein_name` | Required | Non-empty recommended or submitted protein name from UniProtKB |
| `organism_taxon_id` | Required | Source organism `NCBITaxon:<id>` CURIE matching `NCBITAXON_ID_PATTERN`; must match `CausalNode.organism_taxon_id`, resolve to a species-or-below taxon (`_taxon_is_species_or_below`), and be lineage-compatible with the host `TaxonRecord.identifier` in `data/raw/ncbitaxon_taxa.tsv` |
| `organism_label` | Required | Non-empty source organism scientific name from UniProtKB |
| `proteome_id` | Optional | UniProt Proteome `UP:UP<9 digits>` CURIE matching `PROTEOME_ID_PATTERN` when present; must match `CausalNode.proteome_id` |
| `gene_symbol` | Conditional | Primary gene symbol (at least one of `gene_symbol` or `locus_tag` must be non-empty); must match `CausalNode.gene_symbol` (or allow ORF fallback when `gene_symbol` is empty in TSV) |
| `locus_tag` | Conditional | Ordered locus / ORF tag (at least one of `gene_symbol` or `locus_tag` must be non-empty); must match `CausalNode.locus_tag` |
| `ec_numbers` | Optional | Pipe-delimited (`\|`) unique `EC:` CURIEs matching `EC_NUMBER_PATTERN` (`^EC:[1-7]\.(?:[0-9]+\|-)\.(?:[0-9]+\|-)\.(?:n?[0-9]+\|-)$`); any `EC:` CURIE in `CausalNode.xrefs` must appear here |
| `sequence_length` | Required | Positive integer canonical amino-acid length (`> 0`); must equal `CausalNode.sequence_length` |
| `sequence_crc64` | Required | 16-character uppercase hex digest matching `CRC64_PATTERN` (`^[0-9A-F]{16}$`); must equal `CausalNode.sequence_crc64` |
| `sequence_version` | Required | Positive integer sequence version (`> 0`); must equal `CausalNode.sequence_version` |
| `release_version` | Required | Non-empty UniProtKB release pin (e.g. `2026_02`) |

### Species vs. Strain `strain_id` Binding Rule

`CausalNode.strain_id` is an optional `GENE_OR_PROTEIN`-only slot validated by
`validate_causal_graph_proteins()` (`src/taxonmech/seed.py` lines 555–560,
653–670):

- When present, `strain_id` must match `BACDIVE_STRAIN_ID_PATTERN`
  (`^kgmicrobe\.strain:bacdive_[1-9][0-9]*$`), exist in
  `data/raw/bacdive_strains.tsv`, and appear on the host `TaxonRecord.strains[]`
  list.
- At least one taxon `s_tid` linked to `strain_id` in `data/raw/bacdive_strains.tsv`
  must sit within the host `TaxonRecord.identifier` subtree (`s_tid == tid or tid in _taxon_lineage(taxa, s_tid)`)
  and be lineage-compatible (`_taxa_lineage_compatible`) with the node's
  `organism_taxon_id` in `data/raw/ncbitaxon_taxa.tsv` (#208).
- Across the 15 maintained overlays (86 `GENE_OR_PROTEIN` nodes), **5 overlays
  (38 nodes) populate `strain_id`** because the target `TaxonRecord.strains[]`
  contains that BacDive strain record: `NCBITaxon_562.yaml` (*Escherichia coli*,
  `kgmicrobe.strain:bacdive_155687`), `NCBITaxon_1423.yaml` (*Bacillus subtilis*,
  `kgmicrobe.strain:bacdive_1156`), `NCBITaxon_287.yaml` (*Pseudomonas
  aeruginosa*, `kgmicrobe.strain:bacdive_12795`), and both
  `NCBITaxon_2190.yaml` (*Methanocaldococcus jannaschii*) and
  `NCBITaxon_243232.yaml` (*Methanocaldococcus jannaschii DSM 2661*)
  (`kgmicrobe.strain:bacdive_6981`, which is directly assigned to
  `NCBITaxon:243232` in `data/raw/bacdive_strains.tsv` and aggregated into
  `NCBITaxon:2190` via subtree rollup).
- **10 overlays (48 nodes) omit `strain_id`** while retaining strain-specific
  `organism_taxon_id` and `proteome_id` because the host `TaxonRecord` has
  `strains: []`: the 4 bacterial strain overlays whose BacDive strain row in
  `data/raw/bacdive_strains.tsv` is keyed to the parent species rather than the
  infraspecific TaxID (`NCBITaxon:83333` *Escherichia coli* K-12,
  `NCBITaxon:511145` *Escherichia coli* str. K-12 substr. MG1655,
  `NCBITaxon:224308` *Bacillus subtilis* subsp. *subtilis* str. 168, and
  `NCBITaxon:208964` *Pseudomonas aeruginosa* PAO1) and the 6 eukaryotic
  *Cryptococcus* species and strain overlays outside BacDive's prokaryotic
  scope (`NCBITaxon:5207` *Cryptococcus neoformans*, `NCBITaxon:235443`
  *Cryptococcus neoformans* H99, `NCBITaxon:40410` *Cryptococcus deneoformans*,
  `NCBITaxon:283643` *Cryptococcus deneoformans* B-3501A, `NCBITaxon:1859096`
  *Cryptococcus deuterogattii*, and `NCBITaxon:294750` *Cryptococcus
  deuterogattii* R265).

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
3. **Causal-graph structural referential integrity and closed-key schema validation (`src/taxonmech/seed.py`)**:
   `load_causal_graphs()` enforces required non-empty `title`, `nodes`, and
   `edges` on every loaded `CausalGraph`, invokes
   `validate_causal_graph_events()` to verify closed-key `CurationEvent`
   dictionaries (`CURATION_EVENT_KEYS`: `timestamp`, `curator`, `action`,
   `changes`, `llm_assisted`), ISO-8601 UTC `timestamp` syntax
   (`ISO_UTC_TIMESTAMP_PATTERN`), non-decreasing chronological order, non-empty
   `curator`/`action`/`changes`, and boolean `llm_assisted`, and invokes
   `validate_causal_graph_structure()` to verify closed-key object schemas
   (`CAUSAL_GRAPH_KEYS`, `CAUSAL_NODE_KEYS`, `CAUSAL_EDGE_KEYS`, and
   `EVIDENCE_ITEM_KEYS`), `NCBITAXON_ID_PATTERN` syntax
   on the host `identifier`, `graph_id`, `node_id`, and `edge_id` syntax
   (`EDGE_ID_PATTERN`) and uniqueness within every taxon/graph,
   `CausalNodeTypeEnum` membership (`CAUSAL_NODE_TYPES`), isolation of
   protein-only slots (`PROTEIN_ONLY_NODE_SLOTS`) exclusively to
   `GENE_OR_PROTEIN` nodes, `CURIE_PATTERN` syntax and non-duplication for
   `grounding`, `xrefs`, and `predicate_id` (plus required `NCBITAXON_ID_PATTERN`
   `grounding` for `TAXON` nodes), referential integrity of `edge.subject` and
   `edge.object` against `graph.nodes`, full node connectivity (no disconnected
   `node_id`s left unreferenced by any `edge`), absence of self-loop edges
   (`subject != object`) and duplicate parallel
   `(subject, predicate_id or predicate, object)` edges, and non-empty,
   non-duplicate `evidence[].reference` citations matching
   `EVIDENCE_REFERENCE_PATTERN` (`PMID:`, `PMC:PMC`, `DOI:10.`, or `http(s)://`)
   on every edge (#189, #199, #208, #216).
4. **Offline UniProtKB reference, NCBI Taxonomy lineage, and BacDive strain validation (`curation/uniprot_proteins.tsv`, `conf/sources.yaml`, `src/taxonmech/seed.py`, & `scripts/check_provenance.py`)**:
   `load_uniprot_proteins()`, `load_causal_graphs()`, `load_inventory()`, and
   `scripts/check_provenance.py` (`causal_graph_provenance_problems()`) enforce
   `UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, and `PROTEOME_ID_PATTERN`
   syntax, species-or-below scope (`_taxon_is_species_or_below`), required
   descriptive metadata (`entry_name`, `protein_name`, `organism_label`,
   `release_version`), `gene_symbol` or `locus_tag` presence, and
   `EC_NUMBER_PATTERN` (`^EC:[1-7]\.(?:[0-9]+|-)\.(?:[0-9]+|-)\.(?:n?[0-9]+|-)$`) syntax/uniqueness on
   `curation/uniprot_proteins.tsv`; verify every `GENE_OR_PROTEIN` node against
   the pinned reference catalog (`entry_status`, `organism_taxon_id`,
   `proteome_id`, `gene_symbol`, `locus_tag`, `ec_numbers`, `sequence_length`,
   `sequence_crc64`, `sequence_version`), reject duplicate `GENE_OR_PROTEIN`
   `grounding` (`UniProtKB:<accession>`) within the same `CausalGraph`, require
   all full 4-part (non-wildcard) `EC:` numbers from `curation/uniprot_proteins.tsv`
   to appear in `CausalNode.xrefs`, and verify that every `uniprot_id` in
   `curation/uniprot_proteins.tsv` is referenced by at least one
   `GENE_OR_PROTEIN` node across `curation/causal_graphs/*.yaml`; verify `TAXON`
   node `grounding` presence and lineage compatibility against
   `ncbitaxon_taxa.tsv` and require every `CausalGraph` to include a `TAXON`
   node grounded to the host `TaxonRecord.identifier`; require every
   `CausalEdge.evidence[]` item to carry non-empty `notes` or `snippet`; verify
   any declared `strain_id`
   (`kgmicrobe.strain:bacdive_*`) against `data/raw/bacdive_strains.tsv`, the
   host taxon subtree (`s_tid == tid or tid in _taxon_lineage(taxa, s_tid)`),
   and `organism_taxon_id` lineage; and verify that every overlay file in
   `curation/causal_graphs/*.yaml` matches its `identifier` filename stem, is
   included in `curation/seed_scope.tsv`, and carries a non-empty, schema-valid
   `curation_history` list (#189, #199, #208, #216).
5. **Byte-exact corpus reproducibility (`scripts/verify_corpus.py`)**:
   `scripts/verify_corpus.py` loads `curation/causal_graphs/` through
   `build_corpus()` and compares every `data/taxa/<domain>/<slug>.yaml` against
   `emit_taxon_yaml(build_document(concept, corpus.inventory))`.
