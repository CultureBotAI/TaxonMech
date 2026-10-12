# YAML Record Review: Podospora appendiculata

- Verdict: pass
- Target: `data/taxa/eukaryota/podospora_appendiculata.yaml`
- Identifier: `NCBITaxon:314037`

## Target

Reviewed the complete 87-line YAML record for `Podospora appendiculata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podospora_appendiculata`.

## Validation

- `just validate data/taxa/eukaryota/podospora_appendiculata.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podospora_anserina.yaml data/taxa/eukaryota/podospora_appendiculata.yaml data/taxa/eukaryota/podospora_australis.yaml data/taxa/eukaryota/podospora_austroamericana.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:64228` is the exact retained NCBITaxon row for `NCBITaxon:314037`: label `Podospora appendiculata`, rank `SPECIES`, parent `NCBITaxon:5144`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55149` contains the seeded in-scope row for `NCBITaxon:314037` with the reason `attested rule: Podospora appendiculata, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:31713` is the aggregate GOLD row for `NCBITaxon:314037` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:314037`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found six direct local JSONL records covering eight exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:314037`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:314037`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation uses the aggregate GOLD row, which is consistent with the single native GOLD organism row for `Podospora appendiculata CBS 314.62`.
