# YAML Record Review: Priceomyces haplophilus

- Verdict: pass
- Target: `data/taxa/eukaryota/priceomyces_haplophilus.yaml`
- Identifier: `NCBITaxon:45502`

## Target

Reviewed the complete 81-line YAML record for `Priceomyces haplophilus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `priceomyces_haplophilus`.

## Validation

- `just validate data/taxa/eukaryota/priceomyces_haplophilus.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/priceomyces_fermenticarens.yaml data/taxa/eukaryota/priceomyces_haplophilus.yaml data/taxa/eukaryota/priceomyces_medius.yaml data/taxa/eukaryota/priceomyces_melissophilus.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5574` is the exact retained NCBITaxon row for `NCBITaxon:45502`: label `Priceomyces haplophilus`, rank `SPECIES`, parent `NCBITaxon:766759`, genetic code `12`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52620` contains the seeded in-scope row for `NCBITaxon:45502` with the reason `attested rule: Priceomyces haplophilus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:36017` is the aggregate GOLD row for `NCBITaxon:45502` and reports `organism_count=12`, matching the YAML GOLD source attestation.
- Native GOLD has 12 exact organism rows, two linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv:214555` through `data/raw/ncbi_type_material.tsv:214574` provide 20 exact type-material aliases under `Pichia haplophila`, split between seven `culture from type material` rows and 13 `type material` rows.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found six direct local JSONL records covering 35 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:45502`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:45502`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with both the aggregate GOLD row and the 12 unique native GOLD organism rows for this target. The exact StrainInfo JSONL evidence has no corresponding BacDive or generated StrainInfo overlay rows.
