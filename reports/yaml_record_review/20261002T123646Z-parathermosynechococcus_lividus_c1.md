# YAML Record Review: Parathermosynechococcus lividus C1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml
- Started UTC: 2026-10-02T12:36:46Z
- Finished UTC: 2026-10-02T12:36:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102118` |
| Label | `Parathermosynechococcus lividus C1` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:33070` |
| Parent label | `Parathermosynechococcus lividus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| NCBI synonyms | 3 |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/delta_proteobacterium_s2651.yaml data/taxa/bacteria/stanieria_cyanosphaera.yaml data/taxa/bacteria/oscillatoria_sancta.yaml data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 67 lines, 11 lineage entries, 3 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Pass: found one seed row and one NCBI Taxonomy row; confirmed all 11 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(102111\|102116\|102117\|102118)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to source rows, `PATHS.tsv`, `seed_scope.tsv`, and the generated YAMLs. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10514 maps `NCBITaxon:102118` to `parathermosynechococcus_lividus_c1`.
- `curation/seed_scope.tsv` row 143501 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17811 names `NCBITaxon:102118` as `Parathermosynechococcus lividus C1`.
- The generated YAML line 1 preserves the NCBI identifier and line 56 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, genetic code, and three exact synonyms agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:33070` / `Parathermosynechococcus lividus`.
- No source external xrefs, nested strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this strain.
- Nested `strains` are absent because the record itself is the strain-rank taxon and no BacDive, culture-collection, StrainInfo, ATB, or exact strain-related rows are present.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102118`.
- This review did not infer additional genome records, external taxonomy mappings, or causal graphs beyond the maintained inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10514 |
| `curation/seed_scope.tsv` | 143501 |
| `data/raw/ncbitaxon_taxa.tsv` | 17811 |
| `data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml` | 1, 42, and 56 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/parathermosynechococcus_lividus_c1.yaml` directly.
