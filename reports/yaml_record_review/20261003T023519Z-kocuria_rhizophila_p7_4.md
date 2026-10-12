# YAML Record Review: Kocuria rhizophila P7-4

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/kocuria_rhizophila_p7_4.yaml
- Started UTC: 2026-10-03T02:35:21Z
- Finished UTC: 2026-10-03T02:35:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1029824` |
| Label | `Kocuria rhizophila P7-4` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:72000` |
| Parent label | `Kocuria rhizophila` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/kocuria_rhizophila_p7_4.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/acinetobacter_sp_p8_3_8.yaml ... data/taxa/bacteria/arthrobacter_sp_dab_ata187.yaml` | Pass: the strict mixed ten-file batch scanned 10 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 84 lines, 10 lineage entries, 3 synonyms, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 3 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 10 first-column lineage rows, one GTDB closeMatch, one MADIN row, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found the expected NCBI, GTDB, MADIN, seed-scope, and legacy page-path rows for `NCBITaxon:1029824`, with no exact GOLD or auxiliary source rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 12319 maps `NCBITaxon:1029824` to `kocuria_rhizophila_p7_4`.
- `curation/seed_scope.tsv` row 36109 keeps this taxon in scope with NCBI, GTDB, and MADIN evidence.
- `data/raw/ncbitaxon_taxa.tsv` row 220086 names `NCBITaxon:1029824` as `Kocuria rhizophila P7-4`, under `NCBITaxon:72000` / `Kocuria rhizophila`.
- The generated YAML line 1 preserves the NCBI identifier; lines 61, 67, and 73 preserve the NCBI, GTDB, and MADIN source IDs.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13, a GTDB `skos:closeMatch` with 52 genomes, and a MADIN row with 4 trait assertions.
- The two NCBI strain spellings and the GTDB `Kocuria rhizophila` synonym match the three-entry `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:72000` / `Kocuria rhizophila`.

## Completeness

- The record is complete for the exact NCBI, GTDB, and MADIN rows currently present for this strain.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, GOLD, and exact strain-related source rows.
- The external GTDB taxonomy mapping is represented as both `taxonomy_mappings` and `xrefs`.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/kocuria_rhizophila_p7_4.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/kocuria_rhizophila_p7_4.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 12319, `curation/seed_scope.tsv` row 36109, `data/raw/ncbitaxon_taxa.tsv` row 220086, `data/raw/gtdb_mappings.tsv` row 1263, `data/raw/madin_taxa.tsv` row 557, and YAML lines 1, 61, 67, and 73.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/kocuria_rhizophila_p7_4.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/kocuria_rhizophila_p7_4.yaml` directly.
