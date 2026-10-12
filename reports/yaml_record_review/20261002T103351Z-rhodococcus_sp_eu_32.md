# YAML Record Review: Rhodococcus sp. Eu-32

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rhodococcus_sp_eu_32.yaml
- Started UTC: 2026-10-02T10:33:51Z
- Finished UTC: 2026-10-02T10:33:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017319` |
| Label | `Rhodococcus sp. Eu-32` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:192944` |
| Parent label | `unclassified Rhodococcus (in: high G+C Gram-positive bacteria)` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/rhodococcus_sp_eu_32.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/paenibacillus_sp_nioc04.yaml data/taxa/bacteria/virgibacillus_sp_iegm_795.yaml data/taxa/bacteria/photobacterium_sp_dsm_24471.yaml data/taxa/bacteria/rhodococcus_sp_eu_32.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 1 GTDB taxonomy mapping, 1 synonym, 1 xref, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed, NCBI, GTDB, and exact GTDB species rows; confirmed all 10 lineage rows; and found no exact strain-related source rows for `NCBITaxon:1017319`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*-rhodococcus_sp_eu_32.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017319)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `seed_scope.tsv`, `gtdb_mappings.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10316 maps `NCBITaxon:1017319` to `rhodococcus_sp_eu_32`.
- `curation/seed_scope.tsv` row 65989 keeps this taxon in scope with an attested NCBI+GTDB rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218651 names `NCBITaxon:1017319` as `Rhodococcus sp. Eu-32`.
- `data/raw/gtdb_mappings.tsv` row 1182 maps `NCBITaxon:1017319` to `GTDB:s__Rhodococcoides_kyotonensis_B` with `skos:closeMatch` and 34 genomes.
- `data/raw/gtdb_species.tsv` row 154034 preserves `GTDB:s__Rhodococcoides_kyotonensis_B` under `GTDB:g__Rhodococcoides` with the same 34-genome count.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:192944` / `unclassified Rhodococcus (in: high G+C Gram-positive bacteria)`.
- GTDB contributes the single `skos:closeMatch` mapping, matching xref, exact synonym, and 34-genome source attestation.
- No NCBI synonyms, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI and GTDB rows currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- The GTDB mapping predicate, species identifier, species label, and genome count match the raw `gtdb_mappings.tsv` and `gtdb_species.tsv` rows.
- This review does not infer a named-species placement for the unclassified Rhodococcus parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/rhodococcus_sp_eu_32.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/rhodococcus_sp_eu_32.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10316 |
| `curation/seed_scope.tsv` | 65989 |
| `data/raw/gtdb_mappings.tsv` | 1182 |
| `data/raw/gtdb_species.tsv` | 154034 |
| `data/raw/ncbitaxon_taxa.tsv` | 218651 |
| `data/taxa/bacteria/rhodococcus_sp_eu_32.yaml` | 1, 39, 45, 50, 54, and 61 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/rhodococcus_sp_eu_32.yaml`.
- The generated record has no top-level `nomenclature`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/rhodococcus_sp_eu_32.yaml` directly.
