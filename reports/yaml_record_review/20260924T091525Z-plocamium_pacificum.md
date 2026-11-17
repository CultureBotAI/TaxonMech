# YAML Record Review: Plocamium pacificum

- Verdict: pass
- Target: `data/taxa/eukaryota/plocamium_pacificum.yaml`
- Identifier: `NCBITaxon:321259`

## Target

Reviewed the complete 60-line YAML record for `Plocamium pacificum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plocamium_pacificum`.

## Validation

- `just validate data/taxa/eukaryota/plocamium_pacificum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plocamium_pacificum.yaml data/taxa/eukaryota/pluteus_cervinus.yaml data/taxa/eukaryota/pneumocystis_canis.yaml data/taxa/eukaryota/pneumocystis_carinii.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:65759` is the exact retained NCBITaxon row for `NCBITaxon:321259`: label `Plocamium pacificum`, rank `SPECIES`, parent `NCBITaxon:31451`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55192` contains the seeded in-scope row for `NCBITaxon:321259` with the reason `attested rule: Plocamium pacificum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 9 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:321259`.

## Evidence

- `data/raw/gold_organisms.tsv:31981` is the aggregate GOLD row for `NCBITaxon:321259` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism, project, or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:321259`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:321259`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:321259`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The Rhodophyta lineage is shorter than the fungal records in the surrounding lexical neighborhood and still matched all exact retained NCBITaxon ancestor rows. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism, project, and analysis files have no exact rows for this NCBI taxon.
