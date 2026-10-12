# YAML Record Review: Helicobacter pylori R29

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_r29.yaml
- Started UTC: 2026-10-02T16:12:23Z
- Finished UTC: 2026-10-02T16:12:23Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102604` |
| Label | `Helicobacter pylori R29` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:210` |
| Parent label | `Helicobacter pylori` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_r29.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/helicobacter_pylori_r29.yaml data/taxa/bacteria/helicobacter_pylori_97_42.yaml data/taxa/bacteria/helicobacter_pylori_88_39.yaml data/taxa/bacteria/helicobacter_pylori_88_28.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 58 lines, 10 lineage entries, 1 synonym, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row and one first-column NCBI Taxonomy row; confirmed all 10 first-column lineage rows; and found no GOLD aggregate row or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102604` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10816 maps `NCBITaxon:102604` to `helicobacter_pylori_r29`.
- `curation/seed_scope.tsv` row 143788 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 18114 names `NCBITaxon:102604` as the strain `Helicobacter pylori R29`.
- The generated YAML line 1 preserves the NCBI identifier and line 45 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, strain rank, label, parent species, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The single NCBI synonym is `Helicobacter pylori (strain R29)`, as supplied by `data/raw/ncbitaxon_taxa.tsv` row 18114.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:210` / `Helicobacter pylori`.

## Completeness

- The record is complete for the exact NCBI row currently present for this strain taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GTDB, exact GOLD, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102604`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/helicobacter_pylori_r29.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/helicobacter_pylori_r29.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10816, `curation/seed_scope.tsv` row 143788, `data/raw/ncbitaxon_taxa.tsv` row 18114, and YAML lines 1 and 45.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/helicobacter_pylori_r29.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/helicobacter_pylori_r29.yaml` directly.
