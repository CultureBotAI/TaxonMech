# YAML Record Review: Lactiplantibacillus pentosus MP-10

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml
- Started UTC: 2026-10-02T20:01:33Z
- Finished UTC: 2026-10-02T20:01:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1028490` |
| Label | `Lactiplantibacillus pentosus MP-10` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1589` |
| Parent label | `Lactiplantibacillus pentosus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/psychrobacter_sp_dab_alk66.yaml data/taxa/bacteria/psychrobacter_sp_dab_alk97.yaml data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml data/taxa/bacteria/nocardiopsis_sp_sd7.yaml data/taxa/bacteria/bacillus_sp_bhd.yaml data/taxa/bacteria/arthrobacter_sp_gtc2.yaml` | Pass: the strict six-file batch scanned 6 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 86 lines, 10 lineage entries, 2 synonyms, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 4 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, one GTDB mapping row, one GOLD aggregate row, one MADIN aggregate row, one legacy page row, all 10 first-column lineage rows, and no auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `madin_taxa.tsv`, `legacy_page_paths.tsv`, and `seed_scope.tsv` rows for `NCBITaxon:1028490`, with no exact `data/straininfo` or `data/atb` rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11319 maps `NCBITaxon:1028490` to `lactiplantibacillus_pentosus_mp_10`.
- `curation/seed_scope.tsv` row 26050 keeps this taxon in scope with an NCBI plus GTDB plus GOLD plus MADIN rule.
- `data/raw/ncbitaxon_taxa.tsv` row 219154 names `NCBITaxon:1028490` as `Lactiplantibacillus pentosus MP-10`, under `NCBITaxon:1589` / `Lactiplantibacillus pentosus`, and supplies the exact synonym `Lactobacillus pentosus MP-10`.
- `data/raw/gtdb_mappings.tsv` row 1228 maps `GTDB:s__Lactiplantibacillus_pentosus` to `NCBITaxon:1028490` with `skos:closeMatch` and 143 genomes.
- `data/raw/gold_organisms.tsv` row 343 contributes one GOLD organism, `data/raw/madin_taxa.tsv` row 521 contributes one MADIN trait assertion, and `curation/legacy_page_paths.tsv` row 661 records the generated page route.
- The generated YAML line 1 preserves the NCBI identifier; lines 39, 49, 52, and 54 preserve the mapping, synonym sources, and xref; and lines 59, 65, 71, and 76 preserve the source IDs.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The GTDB `skos:closeMatch` row is reflected in both `taxonomy_mappings` and `xrefs`, and the GTDB plus NCBI synonyms are preserved in the YAML synonym block.
- GOLD and MADIN each contribute the expected aggregate source attestation without any explicit strain or assembly rows.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:1589` / `Lactiplantibacillus pentosus`.

## Completeness

- The record is complete for the exact NCBI, GTDB, GOLD, and MADIN rows currently present for this strain taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- No explicit genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11319, `curation/seed_scope.tsv` row 26050, `data/raw/ncbitaxon_taxa.tsv` row 219154, `data/raw/gtdb_mappings.tsv` row 1228, `data/raw/gold_organisms.tsv` row 343, `data/raw/madin_taxa.tsv` row 521, `curation/legacy_page_paths.tsv` row 661, and YAML lines 1, 39, 49, 52, 54, 59, 65, 71, and 76.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/lactiplantibacillus_pentosus_mp_10.yaml` directly.
