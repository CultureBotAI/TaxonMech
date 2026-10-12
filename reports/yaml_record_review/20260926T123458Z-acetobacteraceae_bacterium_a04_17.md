# YAML Record Review: Acetobacteraceae bacterium A04_17

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacteraceae_bacterium_a04_17.yaml`
- Started UTC: 2026-09-26T12:34:58Z
- Finished UTC: 2026-09-26T12:34:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1510838` |
| Label | `Acetobacteraceae bacterium A04_17` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:41293` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained status | Generated under `data/taxa/`; owned by the source inventories plus `curation/seed_scope.tsv` |

## Validation

| Check | Result |
|---|---|
| Read the full 51-line YAML | Pass |
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_a04_17.yaml` | Pass; LinkML reported `No issues found` |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium_a04_17.yaml data/taxa/bacteria/acetobacteraceae_bacterium_a05_col5cp2.yaml data/taxa/bacteria/acetobacteraceae_bacterium_a06_16.yaml data/taxa/bacteria/acetobacteraceae_bacterium_a07_7_27f_1072978_063.yaml` | Pass; 4 files scanned, 0 files with `ERROR` |
| `/private/tmp/taxonmech_yaml_summary.py` batch summary | Pass; confirmed one `NCBITAXON`/`NAME` source attestation, 9 lineage entries, 0 strains, 0 synonyms, 0 nomenclature entries, 0 GTDB mappings, 0 genome links, 0 related records, 0 xrefs, and 0 causal graphs |
| `/private/tmp/taxonmech_bounded_scan.py data/taxa/bacteria/acetobacteraceae_bacterium_a04_17.yaml` | Pass; matched the target row, checked all 9 lineage entries, found 1 scope row, and found no exact auxiliary source rows |
| `rg --no-ignore --hidden` over source, scope, catalog, history, and ignored report trees for this ID and label | Pass; found only the expected `curation/seed_scope.tsv` row and `data/raw/ncbitaxon_taxa.tsv` row |

Full-corpus `just verify-corpus` was not run for this read-only report batch.
The narrow schema and strict validators were run on the target, and the source
inventory checks above covered the rows that can seed this compact
NCBI-only record.

## Identity and Grounding

The record's identifier, label, rank, parent, genetic code, source, and
snapshot all agree with the pinned NCBI inventory row at
`data/raw/ncbitaxon_taxa.tsv:388796`:

| Field | YAML | Raw NCBI row |
|---|---|---|
| Identifier | `NCBITaxon:1510838` | `NCBITaxon:1510838` |
| Label | `Acetobacteraceae bacterium A04_17` | `Acetobacteraceae bacterium A04_17` |
| Rank | `SPECIES` | `SPECIES` |
| Parent | `NCBITaxon:41293` | `NCBITaxon:41293` |
| Genetic code | `11` | `11` |
| Source | `NCBITAXON` | `ncbitaxon` |
| Snapshot | `2026-09-13` | `2026-09-13` |

The root-first lineage has 9 entries and the bounded scan found no missing
ancestor rows or label/rank mismatches against `data/raw/ncbitaxon_taxa.tsv`.
`grounding_status: EXACT` is appropriate because the record is identified by
the NCBI Taxonomy CURIE itself. `taxon_domain: BACTERIA` is consistent with
the NCBI lineage through `NCBITaxon:2` `Bacteria`.

The record is in scope through `curation/seed_scope.tsv:458638`, whose reason
is `attested rule: Acetobacteraceae bacterium A04_17, 1 sources incl. NCBI`.

## Evidence

The only material biological/source assertion is the NCBI Taxonomy
attestation:

| Claim | Evidence | Status |
|---|---|---|
| `NCBITaxon:1510838` labels a species-level taxon named `Acetobacteraceae bacterium A04_17` under `NCBITaxon:41293` | `data/raw/ncbitaxon_taxa.tsv:388796` | Supported |
| The record has one upstream NCBI name assertion and no LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, BV-BRC, SeqCode, or StrainInfo attachment | Exact ignored-inclusive ID/label search plus bounded scans of the auxiliary inventories | Supported |
| `strain_count: 0` | Bounded scans found no BacDive, StrainInfo, culture collection, strain assembly, strain genome, strain related-record, native GOLD organism/project/analysis, or type-material rows for `1510838` | Supported |

No citation snippets are present, so there are no quotation boundaries to
verify. No synonym, nomenclature, taxonomy mapping, strain, genome, related
record, evidence, discussion, or causal-graph block is present.

## Completeness

No consequential gap was found. The empty optional slots are justified by the
source scans:

| Slot | Scan result |
|---|---|
| `synonyms` | NCBI `exact_synonyms`, `broad_synonyms`, and `related_synonyms` are empty; LPSN and GTDB target scans found 0 rows |
| `nomenclature` | `data/raw/lpsn_names.tsv` found 0 exact target rows |
| `taxonomy_mappings` | `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv` found 0 exact target rows |
| `strains`, `genome_assemblies`, `genome_records`, `related_records` | BacDive, culture-collection, genome-link, GOLD, StrainInfo, and ATB target scans found 0 exact rows |
| `causal_graphs` | No curator-authored mechanism graph is expected for a generated NCBI-only seed |

The absence checks used `find` for ignored reports and `rg --no-ignore
--hidden` or bounded scans over committed and compressed source inventories, so
gitignored report files and compressed native catalogs were not skipped.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None beyond the usual next regeneration gate. If NCBI or kg-microbe later
changes the ID, label, lineage, rank, or source attestations for this taxon,
rerun `just seed`, `just seed-canary NCBITaxon:1510838`, and
`just verify-corpus` after updating the maintained inventory or scope input.

## Additional Notes

This report is intentionally read-only. Any future change to generated fields
in `data/taxa/bacteria/acetobacteraceae_bacterium_a04_17.yaml` should be made
in the extractor, seeder, upstream source inventory, or `curation/seed_scope.tsv`
instead of hand-editing the YAML.
