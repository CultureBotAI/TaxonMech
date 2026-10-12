# YAML Record Review: Pleurotus ostreatus

- Verdict: pass
- Target: `data/taxa/eukaryota/pleurotus_ostreatus.yaml`
- Identifier: `NCBITaxon:5322`

## Target

Reviewed the complete 88-line YAML record for `Pleurotus ostreatus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pleurotus_ostreatus`.

## Validation

- `just validate data/taxa/eukaryota/pleurotus_ostreatus.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pleurotus_ostreatoroseus.yaml data/taxa/eukaryota/pleurotus_ostreatus.yaml data/taxa/eukaryota/pleurotus_ostreatus_pc15.yaml data/taxa/eukaryota/pleurotus_platypus.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2349` is the exact retained NCBITaxon row for `NCBITaxon:5322`: label `Pleurotus ostreatus`, rank `SPECIES`, parent `NCBITaxon:5320`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:51967` contains the seeded in-scope row for `NCBITaxon:5322` with the reason `attested rule: Pleurotus ostreatus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 4 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5322`.

## Evidence

- `data/raw/gold_organisms.tsv:38041` is the aggregate GOLD row for `NCBITaxon:5322` and reports `organism_count=88`, matching the YAML GOLD source attestation.
- Native GOLD has seven exact organism rows, 47 linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has two exact epitype rows for `NCBITaxon:5322`, both filed under `Agaricus ostreatus`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has 331 exact strain records covering 382 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5322`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5322`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

One additional StrainInfo JSONL row has a `Pleurotus columbinus` strain with two `Pleurotus ostreatus` deposits; it was counted only in the exact-deposit total. The generated GOLD source attestation uses the aggregate GOLD row rather than the smaller local native GOLD organism row count.
