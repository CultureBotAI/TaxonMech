# YAML Record Review: Plasmodium ovale curtisi

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_ovale_curtisi.yaml`
- Identifier: `NCBITaxon:864141`

## Target

Reviewed the complete 75-line YAML record for `Plasmodium ovale curtisi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_ovale_curtisi`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_ovale_curtisi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_ovale_curtisi.yaml data/taxa/eukaryota/plasmodium_ovale_wallikeri.yaml data/taxa/eukaryota/plasmodium_praefalciparum_nom_ined.yaml data/taxa/eukaryota/plasmodium_reichenowi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:181865` is the exact retained NCBITaxon row for `NCBITaxon:864141`: label `Plasmodium ovale curtisi`, rank `SUBSPECIES`, parent `NCBITaxon:36330`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56792` contains the seeded in-scope row for `NCBITaxon:864141` with the reason `attested rule: Plasmodium ovale curtisi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:86965` maps old ID `NCBITaxon:573885` into `NCBITaxon:864141`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:43461` is the aggregate GOLD row for `NCBITaxon:864141` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:864141`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:864141`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:864141`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The merged old ID is merge metadata only for this generated record. Because that old ID is not present in the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
