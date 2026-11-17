# YAML Record Review: Psychrobacter sp. DAB_AL62B

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml
- Started UTC: 2026-10-02T19:59:26Z
- Finished UTC: 2026-10-02T19:59:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1028420` |
| Label | `Psychrobacter sp. DAB_AL62B` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:196806` |
| Parent label | `unclassified Psychrobacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/psychrobacter_sp_dab_al49.yaml data/taxa/bacteria/psychrobacter_sp_dab_al6.yaml data/taxa/bacteria/psychrobacter_sp_dab_al60.yaml data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 1 synonym, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, one GTDB mapping row, all 10 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found only `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, and `seed_scope.tsv` rows for `NCBITaxon:1028420`, with no exact `data/straininfo` or `data/atb` rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11315 maps `NCBITaxon:1028420` to `psychrobacter_sp_dab_al62b`.
- `curation/seed_scope.tsv` row 65996 keeps this taxon in scope with an NCBI plus GTDB rule.
- `data/raw/ncbitaxon_taxa.tsv` row 219148 names `NCBITaxon:1028420` as `Psychrobacter sp. DAB_AL62B`, under `NCBITaxon:196806` / `unclassified Psychrobacter`.
- `data/raw/gtdb_mappings.tsv` row 1227 maps `GTDB:s__Psychrobacter_sp900168255` to `NCBITaxon:1028420` with `skos:closeMatch` and three genomes.
- The generated YAML line 1 preserves the NCBI identifier; lines 39, 49, and 51 preserve the GTDB mapping, synonym, and xref; and lines 56 and 62 preserve the two source IDs.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The GTDB `skos:closeMatch` row is reflected in both `taxonomy_mappings` and `xrefs`, and the GTDB species label is normalized into one exact synonym.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:196806` / `unclassified Psychrobacter`.

## Completeness

- The record is complete for the exact NCBI and GTDB rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- No explicit genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11315, `curation/seed_scope.tsv` row 65996, `data/raw/ncbitaxon_taxa.tsv` row 219148, `data/raw/gtdb_mappings.tsv` row 1227, and YAML lines 1, 39, 49, 51, 56, and 62.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/psychrobacter_sp_dab_al62b.yaml` directly.
