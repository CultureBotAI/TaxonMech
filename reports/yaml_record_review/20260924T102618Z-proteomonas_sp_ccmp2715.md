# YAML Record Review: Proteomonas sp. CCMP2715

- Verdict: pass
- Target: `data/taxa/eukaryota/proteomonas_sp_ccmp2715.yaml`
- Identifier: `NCBITaxon:3055148`

## Target

Reviewed the complete 57-line YAML record for `Proteomonas sp. CCMP2715`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `proteomonas_sp_ccmp2715`.

## Validation

- `just validate data/taxa/eukaryota/proteomonas_sp_ccmp2715.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/prorocentrum_lima.yaml data/taxa/eukaryota/prorocentrum_micans.yaml data/taxa/eukaryota/prorocentrum_minimum.yaml data/taxa/eukaryota/proteomonas_sp_ccmp2715.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:590844` is the exact retained NCBITaxon row for `NCBITaxon:3055148`: label `Proteomonas sp. CCMP2715`, rank `SPECIES`, parent `NCBITaxon:2633161`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63520` contains the seeded in-scope row for `NCBITaxon:3055148` with the reason `attested rule: Proteomonas sp. CCMP2715, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 8 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:30682` is the aggregate GOLD row for `NCBITaxon:3055148` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism rows, linked project rows, or linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:3055148`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:3055148`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:3055148`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is backed by the aggregate GOLD row; exact native GOLD organism, project, and analysis scans returned 0 rows for `NCBITaxon:3055148`.
