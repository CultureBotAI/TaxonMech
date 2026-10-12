# YAML Record Review: Poriella subacida

- Verdict: pass
- Target: `data/taxa/eukaryota/poriella_subacida.yaml`
- Identifier: `NCBITaxon:2872513`

## Target

Reviewed the complete 99-line YAML record for `Poriella subacida`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `poriella_subacida`.

## Validation

- `just validate data/taxa/eukaryota/poriella_subacida.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/porcisia_hertigi.yaml data/taxa/eukaryota/poriella_subacida.yaml data/taxa/eukaryota/porodaedalea_chrysoloma.yaml data/taxa/eukaryota/porodaedalea_niemelaei.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:566459` is the exact retained NCBITaxon row for `NCBITaxon:2872513`: label `Poriella subacida`, rank `SPECIES`, parent `NCBITaxon:2872512`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63339` contains the seeded in-scope row for `NCBITaxon:2872513` with the reason `attested rule: Poriella subacida, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 4 exact synonyms, 6 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old IDs `NCBITaxon:1431285` and `NCBITaxon:81050` to `NCBITaxon:2872513`, and exact retained NCBITaxon scans found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:27919` is the aggregate GOLD row for `NCBITaxon:2872513` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact isotype rows for `NCBITaxon:2872513`, filed under `Polyporus subacidus`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact StrainInfo scan found 22 direct local JSONL records covering 37 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2872513`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2872513`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows cover four `MICH 11782` isotype spelling variants. The exact StrainInfo deposit count includes the `MUCL 39634` deposit embedded in a `Perenniporia fraxinea` direct row; that is not a direct target row and did not generate BacDive or StrainInfo overlay records.
