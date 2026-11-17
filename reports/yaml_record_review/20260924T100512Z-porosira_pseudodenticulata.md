# YAML Record Review: Porosira pseudodenticulata

- Verdict: pass
- Target: `data/taxa/eukaryota/porosira_pseudodenticulata.yaml`
- Identifier: `NCBITaxon:263736`

## Target

Reviewed the complete 81-line YAML record for `Porosira pseudodenticulata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `porosira_pseudodenticulata`.

## Validation

- `just validate data/taxa/eukaryota/porosira_pseudodenticulata.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/porodaedalea_pini.yaml data/taxa/eukaryota/poronia_punctata.yaml data/taxa/eukaryota/porosira_glacialis.yaml data/taxa/eukaryota/porosira_pseudodenticulata.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:53905` is the exact retained NCBITaxon row for `NCBITaxon:263736`: label `Porosira pseudodenticulata`, rank `SPECIES`, parent `NCBITaxon:49259`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54850` contains the seeded in-scope row for `NCBITaxon:263736` with the reason `attested rule: Porosira pseudodenticulata, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 3 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:265538` to `NCBITaxon:263736`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:24206` is the aggregate GOLD row for `NCBITaxon:263736` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target in the local native GOLD tables.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:263736`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found five direct local JSONL records covering five exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:263736`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:263736`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation uses the aggregate GOLD row; the local native GOLD tables have no exact organism rows for `NCBITaxon:263736`. The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows.
