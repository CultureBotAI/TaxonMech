# YAML Record Review: Trichoderma harzianum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_harzianum.yaml`
- Identifier: `NCBITaxon:5544`

## Target

Reviewed the complete 84-line YAML record for Trichoderma harzianum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_harzianum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_harzianum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_gliocladium.yaml data/taxa/eukaryota/trichoderma_gracile.yaml data/taxa/eukaryota/trichoderma_guizhouense.yaml data/taxa/eukaryota/trichoderma_harzianum.yaml` scanned all four batch files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:2465` keeps `NCBITaxon:5544` as `Trichoderma harzianum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The NCBI row carries 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- The seed-scope scan found exactly 1 row for `NCBITaxon:5544`, with the sampled row at line 52031.
- All 16 lineage entries in the YAML were checked against the retained NCBI lineage; 0 ancestors were missing and 0 lineage values mismatched.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:1082954`, `NCBITaxon:194532`, `NCBITaxon:64503`, and `NCBITaxon:929689` forward to `NCBITaxon:5544`; none of the obsolete IDs were retained by the YAML record.

## Evidence

- `data/gold/gold_taxon_summary.tsv` has exactly 1 aggregate row for `NCBITaxon:5544` at line 38687, with `organism_count` 12.
- Native GOLD rows were present for this target: 11 organism rows, 45 project rows, and 10 analysis rows.
- `data/raw/ncbi_type_material.tsv` has 6 exact type-material rows for `NCBITaxon:5544`.
- Local exact-citation scans found 0 BacDive rows, 316 StrainInfo direct taxon rows, and 393 StrainInfo deposit rows.
- The compressed StrainInfo JSONL had 322 records carrying exact `NCBITaxon:5544` values; 6 were non-direct taxon rows with exact target deposits.

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
