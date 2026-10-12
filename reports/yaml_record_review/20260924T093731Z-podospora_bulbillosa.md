# YAML Record Review: Podospora bulbillosa

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_bulbillosa.yaml`
- Identifier: `NCBITaxon:2587404`

## Target

Reviewed the complete 90-line YAML record for `Podospora bulbillosa`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_bulbillosa`.

## Validation

- `just validate data/taxa/eukaryota/podospora_bulbillosa.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_austrohemisphaerica.yaml data/taxa/eukaryota/podospora_bulbillosa.yaml data/taxa/eukaryota/podospora_conica.yaml data/taxa/eukaryota/podospora_cupiformis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:534327` is the exact retained NCBITaxon row for `NCBITaxon:2587404`: label `Podospora bulbillosa`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62860` contains the seeded in-scope row for `NCBITaxon:2587404` with the reason `attested rule: Podospora bulbillosa, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:585595` to `NCBITaxon:2587404`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:23676` is the aggregate GOLD row for `NCBITaxon:2587404` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, 31 linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has two exact type-material rows for `NCBITaxon:2587404`, both cultures from holotype filed under `Cladorrhinum bulbillosum`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 10 direct local JSONL records covering 11 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2587404`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2587404`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows are NCBI designations for `CBS 304.90` and `CBS:304.90` that do not appear as generated strain rows. The exact StrainInfo JSONL hits likewise have no corresponding BacDive or generated StrainInfo overlay rows.
