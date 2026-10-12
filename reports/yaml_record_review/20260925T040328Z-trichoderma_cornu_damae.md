# YAML Record Review: Trichoderma cornu-damae

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_cornu_damae.yaml`
- Identifier: `NCBITaxon:654480`

## Target

Reviewed the complete 93-line YAML record for Trichoderma cornu-damae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_cornu_damae.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_cornu_damae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_composticola.yaml data/taxa/eukaryota/trichoderma_corneum.yaml data/taxa/eukaryota/trichoderma_cornu_damae.yaml data/taxa/eukaryota/trichoderma_crassum.yaml` scanned all four batch files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:151288` keeps `NCBITaxon:654480` as `Trichoderma cornu-damae`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The NCBI row carries 2 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- The seed-scope scan found exactly 1 row for `NCBITaxon:654480`, with the sampled row at line 56249.
- All 16 lineage entries in the YAML were checked against the retained NCBI lineage; 0 ancestors were missing and 0 lineage values mismatched.
- The NCBI merged-ID scan found 0 old IDs mapped to this target.

## Evidence

- `data/gold/gold_taxon_summary.tsv` has exactly 1 aggregate row for `NCBITaxon:654480` at line 40524, with `organism_count` 1.
- Native GOLD rows were present for this target: 1 organism row, 1 project row, and 1 analysis row.
- `data/raw/ncbi_type_material.tsv` has 11 exact type-material rows for `NCBITaxon:654480`.
- Local exact-citation scans found 0 BacDive rows, 1 StrainInfo direct taxon row, and 2 StrainInfo deposit rows.

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
