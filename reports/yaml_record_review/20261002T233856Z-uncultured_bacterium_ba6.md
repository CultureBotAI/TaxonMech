# YAML Record Review: uncultured bacterium BA6

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_bacterium_ba6.yaml
- Started UTC: 2026-10-02T23:38:56Z
- Finished UTC: 2026-10-02T23:38:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102929` |
| Label | `uncultured bacterium BA6` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:50742` |
| Parent label | `environmental samples` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/uncultured_bacterium_ba6.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_stfrb240.yaml ... data/taxa/bacteria/pseudomonas_sp_stfrb248.yaml` | Pass: the strict ten-file Pseudomonas/uncultured-bacterium batch scanned 10 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 48 lines, 8 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 8 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found only `ncbitaxon_taxa.tsv` and `seed_scope.tsv` rows for `NCBITaxon:102929`, with no exact auxiliary source rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11875 maps `NCBITaxon:102929` to `uncultured_bacterium_ba6`.
- `curation/seed_scope.tsv` row 143845 keeps this taxon in scope with an NCBI rule.
- `data/raw/ncbitaxon_taxa.tsv` row 18184 names `NCBITaxon:102929` as `uncultured bacterium BA6`, under `NCBITaxon:50742` / `environmental samples`.
- The generated YAML line 1 preserves the NCBI identifier, and line 37 preserves the NCBI source ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The NCBI row supplies no synonyms, matching the absence of a `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:50742` / `environmental samples`.

## Completeness

- The record is complete for the exact NCBI row currently present for this Bacteroidota environmental species placeholder.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:102929`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/uncultured_bacterium_ba6.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/uncultured_bacterium_ba6.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11875, `curation/seed_scope.tsv` row 143845, `data/raw/ncbitaxon_taxa.tsv` row 18184, and YAML lines 1 and 37.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/uncultured_bacterium_ba6.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/uncultured_bacterium_ba6.yaml` directly.
