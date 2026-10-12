# YAML Record Review: Pseudo-nitzschia delicatissima

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudo_nitzschia_delicatissima.yaml`
- Identifier: `NCBITaxon:44447`

## Target

Reviewed the complete 81-line YAML record for `Pseudo-nitzschia delicatissima`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudo_nitzschia_delicatissima`.

## Validation

- `just validate data/taxa/eukaryota/pseudo_nitzschia_delicatissima.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudo_nitzschia_australis.yaml data/taxa/eukaryota/pseudo_nitzschia_delicatissima.yaml data/taxa/eukaryota/pseudo_nitzschia_fraudulenta.yaml data/taxa/eukaryota/pseudo_nitzschia_heimii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5394` is the exact retained NCBITaxon row for `NCBITaxon:44447`: label `Pseudo-nitzschia delicatissima`, rank `SPECIES`, parent `NCBITaxon:41953`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52590` contains the seeded in-scope row for `NCBITaxon:44447` with the reason `attested rule: Pseudo-nitzschia delicatissima, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:35681` is the aggregate GOLD row for `NCBITaxon:44447` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, no linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:44447`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:44447`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:44447`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the two native GOLD organism rows for strains `B596` and `UNC1205`.
