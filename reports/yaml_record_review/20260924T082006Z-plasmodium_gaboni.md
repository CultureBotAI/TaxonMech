# YAML Record Review: Plasmodium gaboni

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_gaboni.yaml`
- Identifier: `NCBITaxon:647221`

## Target

Reviewed the complete 66-line YAML record for `Plasmodium gaboni`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_gaboni`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_gaboni.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_fragile.yaml data/taxa/eukaryota/plasmodium_gaboni.yaml data/taxa/eukaryota/plasmodium_gallinaceum.yaml data/taxa/eukaryota/plasmodium_gonderi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:149398` is the exact retained NCBITaxon row for `NCBITaxon:647221`: label `Plasmodium gaboni`, rank `SPECIES`, parent `NCBITaxon:418107`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56232` contains the seeded in-scope row for `NCBITaxon:647221` with the reason `attested rule: Plasmodium gaboni, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 0 related synonyms, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:647221`.

## Evidence

- `data/raw/gold_organisms.tsv:40385` is the aggregate GOLD row for `NCBITaxon:647221` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, three linked project rows, and three linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:647221`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:647221`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:647221`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
