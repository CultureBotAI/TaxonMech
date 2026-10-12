# YAML Record Review: Podospora didyma

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_didyma.yaml`
- Identifier: `NCBITaxon:330526`

## Target

Reviewed the complete 81-line YAML record for `Podospora didyma`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_didyma`.

## Validation

- `just validate data/taxa/eukaryota/podospora_didyma.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_didyma.yaml data/taxa/eukaryota/podospora_fibrinocaudata.yaml data/taxa/eukaryota/podospora_fimiseda.yaml data/taxa/eukaryota/podospora_inflatula.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:67552` is the exact retained NCBITaxon row for `NCBITaxon:330526`: label `Podospora didyma`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55246` contains the seeded in-scope row for `NCBITaxon:330526` with the reason `attested rule: Podospora didyma, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:32288` is the aggregate GOLD row for `NCBITaxon:330526` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:330526`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found one direct local JSONL record covering one exact deposit.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:330526`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:330526`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hit has no corresponding BacDive or generated StrainInfo overlay row. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Podospora didyma CBS 232.78`.
