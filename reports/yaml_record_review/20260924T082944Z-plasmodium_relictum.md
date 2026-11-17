# YAML Record Review: Plasmodium relictum

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_relictum.yaml`
- Identifier: `NCBITaxon:85471`

## Target

Reviewed the complete 72-line YAML record for `Plasmodium relictum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_relictum`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_relictum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_relictum.yaml data/taxa/eukaryota/plasmodium_vinckei.yaml data/taxa/eukaryota/plasmodium_vinckei_brucechwatti.yaml data/taxa/eukaryota/plasmodium_vinckei_lentum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13190` is the exact retained NCBITaxon row for `NCBITaxon:85471`: label `Plasmodium relictum`, rank `SPECIES`, parent `NCBITaxon:418104`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53417` contains the seeded in-scope row for `NCBITaxon:85471` with the reason `attested rule: Plasmodium relictum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:85471`.

## Evidence

- `data/raw/gold_organisms.tsv:43246` is the aggregate GOLD row for `NCBITaxon:85471` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:85471`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one exact local JSONL record, `siID 350440`, carrying the `ATCC 30141` deposit.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:85471`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:85471`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hit has no corresponding BacDive or generated StrainInfo overlay row, so the generated YAML correctly remains a GOLD- and NCBITaxon-attested zero-strain record.
