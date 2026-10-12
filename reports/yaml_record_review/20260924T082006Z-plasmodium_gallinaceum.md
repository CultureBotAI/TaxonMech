# YAML Record Review: Plasmodium gallinaceum

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_gallinaceum.yaml`
- Identifier: `NCBITaxon:5849`

## Target

Reviewed the complete 62-line YAML record for `Plasmodium gallinaceum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_gallinaceum`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_gallinaceum.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_fragile.yaml data/taxa/eukaryota/plasmodium_gaboni.yaml data/taxa/eukaryota/plasmodium_gallinaceum.yaml data/taxa/eukaryota/plasmodium_gonderi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2592` is the exact retained NCBITaxon row for `NCBITaxon:5849`: label `Plasmodium gallinaceum`, rank `SPECIES`, parent `NCBITaxon:418104`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52094` contains the seeded in-scope row for `NCBITaxon:5849` with the reason `attested rule: Plasmodium gallinaceum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5849`.

## Evidence

- `data/raw/gold_organisms.tsv:39461` is the aggregate GOLD row for `NCBITaxon:5849` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5849`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5849`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5849`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 1 organism, while the local native GOLD organism JSONL has 2 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
