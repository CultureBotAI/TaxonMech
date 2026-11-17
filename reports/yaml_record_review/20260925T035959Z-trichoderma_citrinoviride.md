# YAML Record Review: Trichoderma citrinoviride

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_citrinoviride.yaml`
- Identifier: `NCBITaxon:58853`

## Target

Reviewed the complete 96-line YAML record for Trichoderma citrinoviride. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_citrinoviride.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_citrinoviride.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_christiani.yaml data/taxa/eukaryota/trichoderma_citrinoviride.yaml data/taxa/eukaryota/trichoderma_citrinum.yaml data/taxa/eukaryota/trichoderma_compactum.yaml` scanned all four batch files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:7440` keeps `NCBITaxon:58853` as `Trichoderma citrinoviride`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The NCBI row carries 2 exact synonyms, 0 broad synonyms, and 4 related synonyms.
- The seed-scope scan found exactly 1 row for `NCBITaxon:58853`, with the sampled row at line 52996.
- All 16 lineage entries in the YAML were checked against the retained NCBI lineage; 0 ancestors were missing and 0 lineage values mismatched.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:226009`, `NCBITaxon:36924`, `NCBITaxon:399280`, and `NCBITaxon:64610` forward to `NCBITaxon:58853`; none of the obsolete IDs were retained by the YAML record.

## Evidence

- `data/gold/gold_taxon_summary.tsv` has exactly 1 aggregate row for `NCBITaxon:58853` at line 39549, with `organism_count` 2.
- Native GOLD rows were present for this target: 1 organism row, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` has 4 exact type-material rows for `NCBITaxon:58853`.
- Local exact-citation scans found 0 BacDive rows, 79 StrainInfo direct taxon rows, and 105 StrainInfo deposit rows.
- The compressed StrainInfo JSONL had 83 records carrying exact `NCBITaxon:58853` values; 4 were non-direct taxon rows with exact target deposits.

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
