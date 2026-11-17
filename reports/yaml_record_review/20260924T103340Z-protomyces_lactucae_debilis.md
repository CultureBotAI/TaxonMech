# YAML Record Review: Protomyces lactucae-debilis

- Verdict: pass
- Target: `data/taxa/eukaryota/protomyces_lactucae_debilis.yaml`
- Identifier: `NCBITaxon:2754530`

## Target

Reviewed the complete 69-line YAML record for `Protomyces lactucae-debilis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protomyces_lactucae_debilis`.

## Validation

- `just validate data/taxa/eukaryota/protomyces_lactucae_debilis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/protocruzia_adhaerens.yaml data/taxa/eukaryota/protomyces_lactucae_debilis.yaml data/taxa/eukaryota/protomycocladus_faisalabadensis.yaml data/taxa/eukaryota/protostelium_mycophagum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:551199` is the exact retained NCBITaxon row for `NCBITaxon:2754530`: label `Protomyces lactucae-debilis`, rank `SPECIES`, parent `NCBITaxon:27331`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63192` contains the seeded in-scope row for `NCBITaxon:2754530` with the reason `attested rule: Protomyces lactucae-debilis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:56484` to `NCBITaxon:2754530`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:25953` is the aggregate GOLD row for `NCBITaxon:2754530` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has three exact `type material` rows for `NCBITaxon:2754530`, all variants of `NRRL YB-4353`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found two direct local JSONL records covering four exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2754530`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2754530`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

`NCBITaxon:56484` appears only as a retired old ID in `data/raw/ncbi_merged_ids.tsv` and not as a retained row in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of a generated `replaces` value.
