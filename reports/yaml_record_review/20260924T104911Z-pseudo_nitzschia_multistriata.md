# YAML Record Review: Pseudo-nitzschia multistriata

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudo_nitzschia_multistriata.yaml`
- Identifier: `NCBITaxon:183589`

## Target

Reviewed the complete 78-line YAML record for `Pseudo-nitzschia multistriata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudo_nitzschia_multistriata`.

## Validation

- `just validate data/taxa/eukaryota/pseudo_nitzschia_multistriata.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudo_nitzschia_multiseries.yaml data/taxa/eukaryota/pseudo_nitzschia_multistriata.yaml data/taxa/eukaryota/pseudo_nitzschia_pungens.yaml data/taxa/eukaryota/pseudocenococcum_floridanum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36586` is the exact retained NCBITaxon row for `NCBITaxon:183589`: label `Pseudo-nitzschia multistriata`, rank `SPECIES`, parent `NCBITaxon:41953`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54374` contains the seeded in-scope row for `NCBITaxon:183589` with the reason `attested rule: Pseudo-nitzschia multistriata, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:16272` is the aggregate GOLD row for `NCBITaxon:183589` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, seven linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:183589`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:183589`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:183589`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the three exact native GOLD organism rows for `VF2.3`, `VF2.5`, and `B856`.
