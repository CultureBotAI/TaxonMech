# YAML Record Review: Pleurotus pulmonarius

- Verdict: pass
- Target: `data/taxa/eukaryota/pleurotus_pulmonarius.yaml`
- Identifier: `NCBITaxon:28995`

## Target

Reviewed the complete 90-line YAML record for `Pleurotus pulmonarius`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleurotus_pulmonarius`.

## Validation

- `just validate data/taxa/eukaryota/pleurotus_pulmonarius.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/pleurotus_pulmonarius.yaml data/taxa/eukaryota/pleurotus_purpureo_olivaceus.yaml data/taxa/eukaryota/pleurotus_salmoneostramineus.yaml data/taxa/eukaryota/pleurotus_smithii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:3000` is the exact retained NCBITaxon row for `NCBITaxon:28995`: label `Pleurotus pulmonarius`, rank `SPECIES`, parent `NCBITaxon:5320`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52188` contains the seeded in-scope row for `NCBITaxon:28995` with the reason `attested rule: Pleurotus pulmonarius, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 4 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:28995`.

## Evidence

- `data/raw/gold_organisms.tsv:28280` is the aggregate GOLD row for `NCBITaxon:28995` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, three linked project rows, and three linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:28995`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has 103 exact strain records covering 114 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:28995`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:28995`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

One additional StrainInfo JSONL row has a genus-level `Pleurotus` strain with a single `Pleurotus pulmonarius` deposit; it was counted only in the exact-deposit total. The three exact native GOLD organism rows match the aggregate GOLD `organism_count=3` attestation.
