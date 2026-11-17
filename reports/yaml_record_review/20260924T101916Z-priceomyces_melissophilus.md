# YAML Record Review: Priceomyces melissophilus

- Verdict: pass
- Target: `data/taxa/eukaryota/priceomyces_melissophilus.yaml`
- Identifier: `NCBITaxon:27298`

## Target

Reviewed the complete 86-line YAML record for `Priceomyces melissophilus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `priceomyces_melissophilus`.

## Validation

- `just validate data/taxa/eukaryota/priceomyces_melissophilus.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/priceomyces_fermenticarens.yaml data/taxa/eukaryota/priceomyces_haplophilus.yaml data/taxa/eukaryota/priceomyces_medius.yaml data/taxa/eukaryota/priceomyces_melissophilus.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2714` is the exact retained NCBITaxon row for `NCBITaxon:27298`: label `Priceomyces melissophilus`, rank `SPECIES`, parent `NCBITaxon:766759`, genetic code `12`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52138` contains the seeded in-scope row for `NCBITaxon:27298` with the reason `attested rule: Priceomyces melissophilus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:25415` is the aggregate GOLD row for `NCBITaxon:27298` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:114666` through `data/raw/ncbi_type_material.tsv:114678` provide 13 exact `type material` aliases under `Pichia melissophila`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found six direct local JSONL records covering 25 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:27298`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:27298`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the single native GOLD organism row for `NRRL Y-7585`. The anchored source scans found exact type-material and StrainInfo evidence only, with no generated raw strain or StrainInfo overlay rows.
