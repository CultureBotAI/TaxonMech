# YAML Record Review: Chroococcidiopsis sp. CCMP1991

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml
- Started UTC: 2026-10-02T18:46:18Z
- Finished UTC: 2026-10-02T18:46:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027986` |
| Label | `Chroococcidiopsis sp. CCMP1991` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2646205` |
| Parent label | `unclassified Chroococcidiopsis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Synonyms | `1` |
| Source attestations | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/chroococcidiopsis_sp_pcc_8201.yaml data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml data/taxa/bacteria/chroococcidiopsis_sp_ccmp2116.yaml data/taxa/bacteria/chroococcidiopsis_sp_ccmp2623.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 66 lines, 11 lineage entries, 1 synonym, 0 xrefs, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, and one exact GOLD aggregate row; confirmed all 11 first-column lineage rows; and found no auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:1027986` trace only to PATHS, the seed row, the legacy page path, the NCBI Taxonomy row, the GOLD aggregate row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11158 maps `NCBITaxon:1027986` to `chroococcidiopsis_sp_ccmp1991`.
- `curation/seed_scope.tsv` row 57221 keeps this taxon in scope with an attested NCBI-plus-GOLD rule.
- `curation/legacy_page_paths.tsv` row 651 preserves the older page path for this identifier.
- `data/raw/ncbitaxon_taxa.tsv` row 218989 names `NCBITaxon:1027986` as `Chroococcidiopsis sp. CCMP1991`, under `NCBITaxon:2646205` / `unclassified Chroococcidiopsis`.
- `data/raw/gold_organisms.tsv` row 335 contributes one exact organism count for this taxon.
- The generated YAML line 1 preserves the NCBI identifier; lines 50 and 56 preserve the NCBI and GOLD source IDs.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13 plus the exact GOLD aggregate.
- The NCBI row supplies the exact synonym `Chroococcidiopsis sp. A9402`, matching the sole `synonyms` entry.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2646205` / `unclassified Chroococcidiopsis`.

## Completeness

- The record is complete for the exact NCBI and GOLD aggregate rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:1027986`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11158, `curation/seed_scope.tsv` row 57221, `curation/legacy_page_paths.tsv` row 651, `data/raw/ncbitaxon_taxa.tsv` row 218989, `data/raw/gold_organisms.tsv` row 335, and YAML lines 1, 50, and 56.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/chroococcidiopsis_sp_ccmp1991.yaml` directly.
