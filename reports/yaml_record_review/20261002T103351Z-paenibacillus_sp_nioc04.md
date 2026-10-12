# YAML Record Review: Paenibacillus sp. NIOC04

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_nioc04.yaml
- Started UTC: 2026-10-02T10:33:51Z
- Finished UTC: 2026-10-02T10:33:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017279` |
| Label | `Paenibacillus sp. NIOC04` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:185978` |
| Parent label | `unclassified Paenibacillus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/paenibacillus_sp_nioc04.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/paenibacillus_sp_nioc04.yaml data/taxa/bacteria/virgibacillus_sp_iegm_795.yaml data/taxa/bacteria/photobacterium_sp_dsm_24471.yaml data/taxa/bacteria/rhodococcus_sp_eu_32.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 54 lines, 10 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed and NCBI rows; confirmed all 10 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*-paenibacillus_sp_nioc04.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017279)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10313 maps `NCBITaxon:1017279` to `paenibacillus_sp_nioc04`.
- `curation/seed_scope.tsv` row 319186 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218647 names `NCBITaxon:1017279` as `Paenibacillus sp. NIOC04`.
- The generated YAML line 1 preserves the NCBI identifier and line 43 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:185978` / `unclassified Paenibacillus`.
- No source synonyms, external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:1017279`.
- This review does not infer a named-species placement for the unclassified Paenibacillus parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/paenibacillus_sp_nioc04.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/paenibacillus_sp_nioc04.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10313 |
| `curation/seed_scope.tsv` | 319186 |
| `data/raw/ncbitaxon_taxa.tsv` | 218647 |
| `data/taxa/bacteria/paenibacillus_sp_nioc04.yaml` | 1 and 43 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/paenibacillus_sp_nioc04.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/paenibacillus_sp_nioc04.yaml` directly.
