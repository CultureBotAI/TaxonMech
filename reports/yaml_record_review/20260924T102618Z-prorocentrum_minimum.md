# YAML Record Review: Prorocentrum minimum

- Verdict: pass
- Target: `data/taxa/eukaryota/prorocentrum_minimum.yaml`
- Identifier: `NCBITaxon:39449`

## Target

Reviewed the complete 66-line YAML record for `Prorocentrum minimum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `prorocentrum_minimum`.

## Validation

- `just validate data/taxa/eukaryota/prorocentrum_minimum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/prorocentrum_lima.yaml data/taxa/eukaryota/prorocentrum_micans.yaml data/taxa/eukaryota/prorocentrum_minimum.yaml data/taxa/eukaryota/proteomonas_sp_ccmp2715.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4450` is the exact retained NCBITaxon row for `NCBITaxon:39449`: label `Prorocentrum minimum`, rank `SPECIES`, parent `NCBITaxon:2944`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52408` contains the seeded in-scope row for `NCBITaxon:39449` with the reason `attested rule: Prorocentrum minimum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:34245` is the aggregate GOLD row for `NCBITaxon:39449` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:39449`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 15 direct local JSONL records covering 17 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:39449`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:39449`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the three native GOLD organism rows. Only strain `D-127` has linked native GOLD project and analysis rows in the exact local scan.
