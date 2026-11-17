# YAML Record Review: Plasmodium ovale wallikeri

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_ovale_wallikeri.yaml`
- Identifier: `NCBITaxon:864142`

## Target

Reviewed the complete 72-line YAML record for `Plasmodium ovale wallikeri`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_ovale_wallikeri`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_ovale_wallikeri.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_ovale_curtisi.yaml data/taxa/eukaryota/plasmodium_ovale_wallikeri.yaml data/taxa/eukaryota/plasmodium_praefalciparum_nom_ined.yaml data/taxa/eukaryota/plasmodium_reichenowi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:181866` is the exact retained NCBITaxon row for `NCBITaxon:864142`: label `Plasmodium ovale wallikeri`, rank `SUBSPECIES`, parent `NCBITaxon:36330`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56793` contains the seeded in-scope row for `NCBITaxon:864142` with the reason `attested rule: Plasmodium ovale wallikeri, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:864142`.

## Evidence

- `data/raw/gold_organisms.tsv:43462` is the aggregate GOLD row for `NCBITaxon:864142` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:864142`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:864142`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:864142`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
