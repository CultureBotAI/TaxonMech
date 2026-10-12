# YAML Record Review: Synechococcus sp. P2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/synechococcus_sp_p2.yaml
- Started UTC: 2026-10-02T12:39:56Z
- Finished UTC: 2026-10-02T12:39:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102121` |
| Label | `Synechococcus sp. P2` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2626047` |
| Parent label | `unclassified Synechococcus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| NCBI synonyms | 4 |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/synechococcus_sp_p2.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/synechococcus_sp_c9.yaml data/taxa/bacteria/synechococcus_sp_p1.yaml data/taxa/bacteria/synechococcus_sp_p2.yaml data/taxa/bacteria/chlorogloeopsis_fritschii_pcc_6718.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 69 lines, 11 lineage entries, 4 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Pass: found one seed row and one NCBI Taxonomy row; confirmed all 11 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102119\|102120\|102121\|102122)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to source rows, `PATHS.tsv`, `seed_scope.tsv`, and the generated YAMLs. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10517 maps `NCBITaxon:102121` to `synechococcus_sp_p2`.
- `curation/seed_scope.tsv` row 143502 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17814 names `NCBITaxon:102121` as `Synechococcus sp. P2`.
- The generated YAML line 1 preserves the NCBI identifier and line 59 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, genetic code, and four exact synonyms agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2626047` / `unclassified Synechococcus`.
- No source external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102121`.
- This review did not infer additional strain entries, top-level genome records, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/synechococcus_sp_p2.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/synechococcus_sp_p2.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10517 |
| `curation/seed_scope.tsv` | 143502 |
| `data/raw/ncbitaxon_taxa.tsv` | 17814 |
| `data/taxa/bacteria/synechococcus_sp_p2.yaml` | 1, 42, and 57 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/synechococcus_sp_p2.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/synechococcus_sp_p2.yaml` directly.
