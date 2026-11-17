# YAML Record Review: Candidatus Magnispira bakii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_magnispira_bakii.yaml
- Started UTC: 2026-10-03T02:13:54Z
- Finished UTC: 2026-10-03T02:14:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102970` |
| Label | `Candidatus Magnispira bakii` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:102926` |
| Parent label | `Candidatus Magnispira` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_magnispira_bakii.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/uncultured_bacterium_bs4.yaml ... data/taxa/bacteria/psychrilyobacter_sp_stab703.yaml` | Pass: the strict ten-file NCBI placeholder batch scanned 10 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 67 lines, 11 lineage entries, 3 NCBI synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 11 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found only `ncbitaxon_taxa.tsv` and `seed_scope.tsv` rows for `NCBITaxon:102970`, with no exact auxiliary source rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 12269 maps `NCBITaxon:102970` to `candidatus_magnispira_bakii`.
- `curation/seed_scope.tsv` row 143886 keeps this taxon in scope with an NCBI rule.
- `data/raw/ncbitaxon_taxa.tsv` row 18225 names `NCBITaxon:102970` as `Candidatus Magnispira bakii`, under `NCBITaxon:102926` / `Candidatus Magnispira`.
- The generated YAML line 1 preserves the NCBI identifier, and line 56 preserves the NCBI source ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The NCBI row supplies two exact synonyms and one related synonym, matching the three-entry `synonyms` block on lines 42-51.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:102926` / `Candidatus Magnispira`.

## Completeness

- The record is complete for the exact NCBI row currently present for `Candidatus Magnispira bakii`.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:102970`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/candidatus_magnispira_bakii.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/candidatus_magnispira_bakii.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 12269, `curation/seed_scope.tsv` row 143886, `data/raw/ncbitaxon_taxa.tsv` row 18225, and YAML lines 1 and 56.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/candidatus_magnispira_bakii.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/candidatus_magnispira_bakii.yaml` directly.
