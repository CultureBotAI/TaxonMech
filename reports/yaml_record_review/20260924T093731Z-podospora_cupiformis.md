# YAML Record Review: Podospora cupiformis

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_cupiformis.yaml`
- Identifier: `NCBITaxon:330528`

## Target

Reviewed the complete 81-line YAML record for `Podospora cupiformis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_cupiformis`.

## Validation

- `just validate data/taxa/eukaryota/podospora_cupiformis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_austrohemisphaerica.yaml data/taxa/eukaryota/podospora_bulbillosa.yaml data/taxa/eukaryota/podospora_conica.yaml data/taxa/eukaryota/podospora_cupiformis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:67554` is the exact retained NCBITaxon row for `NCBITaxon:330528`: label `Podospora cupiformis`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55248` contains the seeded in-scope row for `NCBITaxon:330528` with the reason `attested rule: Podospora cupiformis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:32290` is the aggregate GOLD row for `NCBITaxon:330528` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact type-material rows for `NCBITaxon:330528`, filed under `Podospora cupiformis`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found one direct local JSONL record covering two exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:330528`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:330528`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows cover NCBI designations for `CBS 246.71`, `CBS:246.71`, `ATCC 22448`, and `ATCC:22448`, while the exact StrainInfo row carries the `CBS 246.71` and `ATCC 22448` deposits. None of those rows generated BacDive or StrainInfo overlay records.
