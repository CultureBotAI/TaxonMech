# YAML Record Review: Porodaedalea chrysoloma

- Verdict: pass
- Target: `data/taxa/eukaryota/porodaedalea_chrysoloma.yaml`
- Identifier: `NCBITaxon:74615`

## Target

Reviewed the complete 81-line YAML record for `Porodaedalea chrysoloma`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `porodaedalea_chrysoloma`.

## Validation

- `just validate data/taxa/eukaryota/porodaedalea_chrysoloma.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/porcisia_hertigi.yaml data/taxa/eukaryota/poriella_subacida.yaml data/taxa/eukaryota/porodaedalea_chrysoloma.yaml data/taxa/eukaryota/porodaedalea_niemelaei.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:10619` is the exact retained NCBITaxon row for `NCBITaxon:74615`: label `Porodaedalea chrysoloma`, rank `SPECIES`, parent `NCBITaxon:175857`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53268` contains the seeded in-scope row for `NCBITaxon:74615` with the reason `attested rule: Porodaedalea chrysoloma, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:42216` is the aggregate GOLD row for `NCBITaxon:74615` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, four linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:74615`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 34 direct local JSONL records covering 35 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:74615`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:74615`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Porodaedalea chrysoloma FP-135951`.
