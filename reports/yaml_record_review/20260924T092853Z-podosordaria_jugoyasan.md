# YAML Record Review: Podosordaria jugoyasan

- Verdict: pass
- Target: `data/taxa/eukaryota/podosordaria_jugoyasan.yaml`
- Identifier: `NCBITaxon:323548`

## Target

Reviewed the complete 87-line YAML record for `Podosordaria jugoyasan`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podosordaria_jugoyasan`.

## Validation

- `just validate data/taxa/eukaryota/podosordaria_jugoyasan.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podila_verticillata.yaml data/taxa/eukaryota/podosira_stelligera.yaml data/taxa/eukaryota/podosordaria_jugoyasan.yaml data/taxa/eukaryota/podosphaera_macularis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:66159` is the exact retained NCBITaxon row for `NCBITaxon:323548`: label `Podosordaria jugoyasan`, rank `SPECIES`, parent `NCBITaxon:281918`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55200` contains the seeded in-scope row for `NCBITaxon:323548` with the reason `attested rule: Podosordaria jugoyasan, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:323548`.

## Evidence

- `data/raw/gold_organisms.tsv:32068` is the aggregate GOLD row for `NCBITaxon:323548` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:323548`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has two exact strain records covering six exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:323548`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:323548`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Podosordaria jugoyasan CBS 670.77`.
