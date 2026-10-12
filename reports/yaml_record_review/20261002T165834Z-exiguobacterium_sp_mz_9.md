# YAML Record Review: Exiguobacterium sp. MZ_9

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml
- Started UTC: 2026-10-02T16:58:34Z
- Finished UTC: 2026-10-02T16:58:34Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1026870` |
| Label | `Exiguobacterium sp. MZ_9` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2644629` |
| Parent label | `unclassified Exiguobacterium` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml data/taxa/bacteria/knoellia_sp_mz_16.yaml data/taxa/bacteria/kocuria_sp_mz_10.yaml data/taxa/bacteria/pantoea_sp_mz_11.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 57 lines, 11 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row and one first-column NCBI Taxonomy row; confirmed all 11 first-column lineage rows; and found no GTDB, GOLD aggregate, or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:1026870` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10917 maps `NCBITaxon:1026870` to `exiguobacterium_sp_mz_9`.
- `curation/seed_scope.tsv` row 319293 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218762 names `NCBITaxon:1026870` as `Exiguobacterium sp. MZ_9`, under `NCBITaxon:2644629` / `unclassified Exiguobacterium`.
- The generated YAML line 1 preserves the NCBI identifier and line 46 preserves the sole NCBI source ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The NCBI row supplies no synonyms, matching the absence of a `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2644629` / `unclassified Exiguobacterium`.

## Completeness

- The record is complete for the exact NCBI row currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GTDB, exact GOLD, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:1026870`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10917, `curation/seed_scope.tsv` row 319293, `data/raw/ncbitaxon_taxa.tsv` row 218762, and YAML lines 1 and 46.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/exiguobacterium_sp_mz_9.yaml` directly.
