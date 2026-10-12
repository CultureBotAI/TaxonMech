# YAML Record Review: Podospora anserina

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_anserina.yaml`
- Identifier: `NCBITaxon:2587412`

## Target

Reviewed the complete 96-line YAML record for `Podospora anserina`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_anserina`.

## Validation

- `just validate data/taxa/eukaryota/podospora_anserina.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_anserina.yaml data/taxa/eukaryota/podospora_appendiculata.yaml data/taxa/eukaryota/podospora_australis.yaml data/taxa/eukaryota/podospora_austroamericana.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:534330` is the exact retained NCBITaxon row for `NCBITaxon:2587412`: label `Podospora anserina`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62863` contains the seeded in-scope row for `NCBITaxon:2587412` with the reason `attested rule: Podospora anserina, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 4 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:5145` to `NCBITaxon:2587412`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:23679` is the aggregate GOLD row for `NCBITaxon:2587412` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, 22 linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has one exact type-material row for `NCBITaxon:2587412`, a culture from epitype filed under `Malinvernia anserina`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact StrainInfo scan found 22 direct local JSONL records covering 25 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2587412`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2587412`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material row is an NCBI designation that does not appear as a generated strain row. The StrainInfo exact-deposit count includes two deposits embedded in `Podospora pauciseta` strain rows; those are not direct target rows and did not generate BacDive or StrainInfo overlay rows.
