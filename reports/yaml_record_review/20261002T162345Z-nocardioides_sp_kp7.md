# YAML Record Review: Nocardioides sp. KP7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/nocardioides_sp_kp7.yaml
- Started UTC: 2026-10-02T16:23:45Z
- Finished UTC: 2026-10-02T16:23:45Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102632` |
| Label | `Nocardioides sp. KP7` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2615069` |
| Parent label | `unclassified Nocardioides` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/nocardioides_sp_kp7.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_b7t.yaml data/taxa/bacteria/ralstonia_sp_b15.yaml data/taxa/bacteria/nocardioides_sp_kp7.yaml data/taxa/bacteria/alcaligenes_sp_rds8.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 57 lines, 10 lineage entries, 1 synonym, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row and one first-column NCBI Taxonomy row; confirmed all 10 first-column lineage rows; and found no GTDB, GOLD aggregate, or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102632` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10838 maps `NCBITaxon:102632` to `nocardioides_sp_kp7`.
- `curation/seed_scope.tsv` row 143804 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 18136 names `NCBITaxon:102632` as `Nocardioides sp. KP7`, under `NCBITaxon:2615069` / `unclassified Nocardioides`.
- The generated YAML line 1 preserves the NCBI identifier and line 47 preserves the sole NCBI source ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The single NCBI synonym is `Nocardioides sp. (strain KP7)`, as supplied by `data/raw/ncbitaxon_taxa.tsv` row 18136.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2615069` / `unclassified Nocardioides`.

## Completeness

- The record is complete for the exact NCBI row currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GTDB, exact GOLD, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102632`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/nocardioides_sp_kp7.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/nocardioides_sp_kp7.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10838, `curation/seed_scope.tsv` row 143804, `data/raw/ncbitaxon_taxa.tsv` row 18136, and YAML lines 1 and 47.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/nocardioides_sp_kp7.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/nocardioides_sp_kp7.yaml` directly.
