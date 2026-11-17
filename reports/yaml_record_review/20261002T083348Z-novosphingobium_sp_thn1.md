# YAML Record Review: Novosphingobium sp. THN1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/novosphingobium_sp_thn1.yaml
- Started UTC: 2026-10-02T08:33:48Z
- Finished UTC: 2026-10-02T08:33:48Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1016987` |
| Label | `Novosphingobium sp. THN1` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2644732` |
| Parent label | `unclassified Novosphingobium` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Taxonomy mappings | `1` GTDB close match |
| Synonyms / xrefs | `1` / `1` from GTDB |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/novosphingobium_sp_thn1.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/novosphingobium_sp_thn1.yaml data/taxa/bacteria/moraxella_sp_16285.yaml data/taxa/bacteria/moraxella_sp_1967.yaml data/taxa/bacteria/moraxella_sp_2102.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 0 strains, 1 synonym, 1 xref, and 2 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/novosphingobium_sp_thn1.yaml` | Not applicable: the helper rejected the `ncbitaxon_taxa.tsv` row because the source column is `ncbitaxon\|gtdb`, not bare `ncbitaxon`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*novosphingobium_sp_thn1.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1016987)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, and this generated YAML. |
| `rg --no-ignore --hidden -n 'GTDB:s__Novosphingobium_sp003454795\|s__Novosphingobium_sp003454795' data curation` | Pass: the exact GTDB scan found the species row, three mapping rows, and three generated YAMLs carrying that GTDB species. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` maps `NCBITaxon:1016987` to `novosphingobium_sp_thn1`.
- `curation/seed_scope.tsv` row 65988 keeps this taxon in scope with an attested two-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218505 names `NCBITaxon:1016987` as `Novosphingobium sp. THN1` with source set `ncbitaxon|gtdb`.
- The YAML identifier, label, rank, parent taxon, and genetic code agree with that raw NCBI row.
- `data/raw/gtdb_species.tsv` row 128907 defines `GTDB:s__Novosphingobium_sp003454795` with 3 genomes.
- `data/raw/gtdb_mappings.tsv` row 1170 maps `GTDB:s__Novosphingobium_sp003454795` to `NCBITaxon:1016987` with `skos:closeMatch` and genome count 3.

## Evidence

- The sole NCBI source attestation is `NCBITAXON`, `source_id: NCBITaxon:1016987`, `source_label: Novosphingobium sp. THN1`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The GTDB source attestation is `GTDB`, `source_id: GTDB:s__Novosphingobium_sp003454795`, `mapping_predicate: skos:closeMatch`, `assertion_count: 3`, and `assertion_unit: GENOME`.
- The `taxonomy_mappings` block exactly mirrors the close-match row from `data/raw/gtdb_mappings.tsv`.
- The GTDB exact synonym `Novosphingobium sp003454795` is derived from the same GTDB species identifier.
- The `xrefs` list contains only `GTDB:s__Novosphingobium_sp003454795`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2644732` / `unclassified Novosphingobium`.

## Completeness

- The record is complete for the NCBI plus GTDB rows that generated this taxon.
- `strain_count: 0` is supported by the absence of BacDive and StrainInfo rows for `NCBITaxon:1016987`.
- No GOLD, LPSN, MADIN, MediaDive, BacDive, BactoTraits, or StrainInfo evidence is asserted.
- The same GTDB species also maps to `NCBITaxon:1874826` as `skos:broadMatch` at `data/raw/gtdb_mappings.tsv` row 73010 and to `NCBITaxon:2726186` as `skos:closeMatch` at row 210730.
- TaxonMech also materializes `GTDB:s__Novosphingobium_sp003454795` in `novosphingobium_sp.yaml` and `novosphingobium_sp_erw19.yaml`; this review only checks the direct `NCBITaxon:1016987` payload.
- No causal graph is expected for this generated taxon-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/novosphingobium_sp_thn1.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/novosphingobium_sp_thn1.yaml`.
- Re-run exact NCBI and GTDB scans after any refresh of `data/raw/` or `curation/seed_scope.tsv`.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The 2026-09-13 NCBI snapshot and the 2026-09-13 GTDB extraction are the sources named by the raw NCBI row.
- TaxonMech preserves the NCBI placement under `unclassified Novosphingobium`; this review does not infer a named species.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10169 |
| `curation/seed_scope.tsv` | 65988 |
| `data/raw/ncbitaxon_taxa.tsv` | 218505 |
| `data/raw/gtdb_species.tsv` | 128907 |
| `data/raw/gtdb_mappings.tsv` | 1170 |
| `data/taxa/bacteria/novosphingobium_sp_thn1.yaml` | 1, 38, 46, 51, 56, and 62 |

- GTDB context observed but not materialized directly on this YAML:

| Mapping row | Predicate | Target |
|---|---|---|
| 73010 | `skos:broadMatch` | `NCBITaxon:1874826` |
| 210730 | `skos:closeMatch` | `NCBITaxon:2726186` |

- The generated record has no top-level `nomenclature`, `strains`, or `causal_graphs` blocks.
- The review found no maintained upstream row that disagrees with this YAML payload.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/novosphingobium_sp_thn1.yaml` directly.
