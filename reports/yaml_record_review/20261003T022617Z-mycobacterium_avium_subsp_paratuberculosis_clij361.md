# YAML Record Review: Mycobacterium avium subsp. paratuberculosis CLIJ361

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml
- Started UTC: 2026-10-03T02:26:17Z
- Finished UTC: 2026-10-03T02:26:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1029812` |
| Label | `Mycobacterium avium subsp. paratuberculosis CLIJ361` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1770` |
| Parent label | `Mycobacterium avium subsp. paratuberculosis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/citrobacter_sp_enrichment_culture_clone_br40.yaml ... data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml` | Pass: the strict mixed ten-file batch scanned 10 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 95 lines, 12 lineage entries, 3 synonyms, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 4 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 12 first-column lineage rows, one GTDB closeMatch, one GOLD organism row, one MADIN row, and no auxiliary exact strain-genome rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found the expected `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `madin_taxa.tsv`, and `seed_scope.tsv` rows for `NCBITaxon:1029812`, with no exact auxiliary source rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 12307 maps `NCBITaxon:1029812` to `mycobacterium_avium_subsp_paratuberculosis_clij361`.
- `curation/seed_scope.tsv` row 26054 keeps this taxon in scope with NCBI, GTDB, GOLD, and MADIN evidence.
- `data/raw/ncbitaxon_taxa.tsv` row 220074 names `NCBITaxon:1029812` as `Mycobacterium avium subsp. paratuberculosis CLIJ361`, under `NCBITaxon:1770` / `Mycobacterium avium subsp. paratuberculosis`.
- The generated YAML line 1 preserves the NCBI identifier; lines 68, 74, 80, and 85 preserve the NCBI, GTDB, GOLD, and MADIN source IDs.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13, a GTDB `skos:closeMatch` with 324 genomes, one GOLD organism row, and a MADIN row with 4 trait assertions.
- The two NCBI strain spellings and the GTDB `Mycobacterium avium` synonym match the three-entry `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:1770` / `Mycobacterium avium subsp. paratuberculosis`.

## Completeness

- The record is complete for the exact NCBI, GTDB, GOLD, and MADIN rows currently present for this strain.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- The external GTDB taxonomy mapping is represented as both `taxonomy_mappings` and `xrefs`.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 12307, `curation/seed_scope.tsv` row 26054, `data/raw/ncbitaxon_taxa.tsv` row 220074, `data/raw/gtdb_mappings.tsv` row 1251, `data/raw/gold_organisms.tsv` row 358, `data/raw/madin_taxa.tsv` row 545, and YAML lines 1, 68, 74, 80, and 85.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/mycobacterium_avium_subsp_paratuberculosis_clij361.yaml` directly.
