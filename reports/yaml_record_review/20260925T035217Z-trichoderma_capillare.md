# YAML Record Review: Trichoderma capillare

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_capillare.yaml`
- Identifier: `NCBITaxon:1115737`

## Target

Reviewed the complete 81-line YAML record for Trichoderma capillare. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_capillare.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_capillare.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_camerunense.yaml data/taxa/eukaryota/trichoderma_capillare.yaml data/taxa/eukaryota/trichoderma_catoptron.yaml data/taxa/eukaryota/trichoderma_ceciliae.yaml` scanned all four batch files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:240281` keeps `NCBITaxon:1115737` as `Trichoderma capillare`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The NCBI row carries 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope scan found exactly 1 row for `NCBITaxon:1115737`, with the sampled row at line 57700.
- All 16 lineage entries in the YAML were checked against the retained NCBI lineage; 0 ancestors were missing and 0 lineage values mismatched.
- The NCBI merged-ID scan found 0 old IDs mapped to this target.

## Evidence

- `data/gold/gold_taxon_summary.tsv` has exactly 1 aggregate row for `NCBITaxon:1115737` at line 2061, with `organism_count` 1.
- Native GOLD rows matched that aggregate: 1 organism row, 2 project rows, and 0 analysis rows.
- `data/raw/ncbi_type_material.tsv` has 9 exact type-material rows for `NCBITaxon:1115737`.
- Local exact-citation scans found 0 BacDive rows, 2 StrainInfo direct taxon rows, and 2 StrainInfo deposit rows.

## Completeness

- Generated raw strain tables had 0 exact rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 exact rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

This review was read-only for the seeded YAML and source evidence files. It created only this ignored report.
