# YAML Record Review: Priceomyces fermenticarens

- Verdict: pass
- Target: `data/taxa/eukaryota/priceomyces_fermenticarens.yaml`
- Identifier: `NCBITaxon:45549`

## Target

Reviewed the complete 83-line YAML record for `Priceomyces fermenticarens`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `priceomyces_fermenticarens`.

## Validation

- `just validate data/taxa/eukaryota/priceomyces_fermenticarens.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/priceomyces_fermenticarens.yaml data/taxa/eukaryota/priceomyces_haplophilus.yaml data/taxa/eukaryota/priceomyces_medius.yaml data/taxa/eukaryota/priceomyces_melissophilus.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5603` is the exact retained NCBITaxon row for `NCBITaxon:45549`: label `Priceomyces fermenticarens`, rank `SPECIES`, parent `NCBITaxon:766759`, genetic code `12`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52649` contains the seeded in-scope row for `NCBITaxon:45549` with the reason `attested rule: Priceomyces fermenticarens, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:36058` is the aggregate GOLD row for `NCBITaxon:45549` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:215116` through `data/raw/ncbi_type_material.tsv:215131` provide 16 exact `culture from type material` aliases under `Candida fermenticarens`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found one direct local JSONL record covering six exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:45549`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:45549`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the single native GOLD organism row for `NRRL Y-17321`. The type-material aliases also include `NRRL Y-17321`, but there are no generated raw strain rows to materialize into the zero-strain YAML.
