# YAML Record Review: Podospora tetraspora

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_tetraspora.yaml`
- Identifier: `NCBITaxon:343501`

## Target

Reviewed the complete 93-line YAML record for `Podospora tetraspora`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_tetraspora`.

## Validation

- `just validate data/taxa/eukaryota/podospora_tetraspora.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_striatispora.yaml data/taxa/eukaryota/podospora_tetraspora.yaml data/taxa/eukaryota/poitrasia_circinans.yaml data/taxa/eukaryota/polarella_glacialis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:70906` is the exact retained NCBITaxon row for `NCBITaxon:343501`: label `Podospora tetraspora`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55288` contains the seeded in-scope row for `NCBITaxon:343501` with the reason `attested rule: Podospora tetraspora, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:2981542` to `NCBITaxon:343501`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:32844` is the aggregate GOLD row for `NCBITaxon:343501` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:343501`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 11 direct local JSONL records covering 14 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:343501`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:343501`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Podospora tetraspora CBS 815.71`.
