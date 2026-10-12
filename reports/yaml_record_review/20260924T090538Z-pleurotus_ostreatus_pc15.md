# YAML Record Review: Pleurotus ostreatus PC15

- Verdict: pass
- Target: `data/taxa/eukaryota/pleurotus_ostreatus_pc15.yaml`
- Identifier: `NCBITaxon:1137138`

## Target

Reviewed the complete 74-line YAML record for `Pleurotus ostreatus PC15`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleurotus_ostreatus_pc15`.

## Validation

- `just validate data/taxa/eukaryota/pleurotus_ostreatus_pc15.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/pleurotus_ostreatoroseus.yaml data/taxa/eukaryota/pleurotus_ostreatus.yaml data/taxa/eukaryota/pleurotus_ostreatus_pc15.yaml data/taxa/eukaryota/pleurotus_platypus.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:247254` is the exact retained NCBITaxon row for `NCBITaxon:1137138`: label `Pleurotus ostreatus PC15`, rank `STRAIN`, parent `NCBITaxon:5322`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:57883` contains the seeded in-scope row for `NCBITaxon:1137138` with the reason `attested rule: Pleurotus ostreatus PC15, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1137138`.

## Evidence

- `data/raw/gold_organisms.tsv:2818` is the aggregate GOLD row for `NCBITaxon:1137138` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1137138`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1137138`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1137138`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The strain-level lineage adds `Pleurotus ostreatus` as the species ancestor, giving 15 checked lineage ancestors instead of the 14 present on the neighboring Pleurotus species records. The generated GOLD source attestation is consistent with the exact native GOLD organism and linked project for `Pleurotus ostreatus N001 PC15`.
