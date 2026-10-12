# YAML Record Review: Plasmodium vinckei vinckei

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_vinckei_vinckei.yaml`
- Identifier: `NCBITaxon:54757`

## Target

Reviewed the complete 69-line YAML record for `Plasmodium vinckei vinckei`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_vinckei_vinckei`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_vinckei_vinckei.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_vinckei_petteri.yaml data/taxa/eukaryota/plasmodium_vinckei_vinckei.yaml data/taxa/eukaryota/plasmodium_vivax.yaml data/taxa/eukaryota/plasmodium_vivax_sal_1.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6953` is the exact retained NCBITaxon row for `NCBITaxon:54757`: label `Plasmodium vinckei vinckei`, rank `SUBSPECIES`, parent `NCBITaxon:5860`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52937` contains the seeded in-scope row for `NCBITaxon:54757` with the reason `attested rule: Plasmodium vinckei vinckei, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 0 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:54757`.

## Evidence

- `data/raw/gold_organisms.tsv:38481` is the aggregate GOLD row for `NCBITaxon:54757` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:54757`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has one exact local JSONL record, `siID 350285`, carrying the `ATCC 30091` deposit.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:54757`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:54757`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 1 organism, while the local native GOLD organism JSONL has 2 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row. The exact StrainInfo JSONL hit has no corresponding BacDive or generated StrainInfo overlay row, so the generated YAML correctly remains a zero-strain record.
