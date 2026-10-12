# YAML Record Review: Plasmodium gonderi

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_gonderi.yaml`
- Identifier: `NCBITaxon:77519`

## Target

Reviewed the complete 62-line YAML record for `Plasmodium gonderi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_gonderi`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_gonderi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_fragile.yaml data/taxa/eukaryota/plasmodium_gaboni.yaml data/taxa/eukaryota/plasmodium_gallinaceum.yaml data/taxa/eukaryota/plasmodium_gonderi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11267` is the exact retained NCBITaxon row for `NCBITaxon:77519`: label `Plasmodium gonderi`, rank `SPECIES`, parent `NCBITaxon:418103`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53310` contains the seeded in-scope row for `NCBITaxon:77519` with the reason `attested rule: Plasmodium gonderi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:77519`.

## Evidence

- `data/raw/gold_organisms.tsv:42685` is the aggregate GOLD row for `NCBITaxon:77519` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:77519`.
- `data/straininfo/records.jsonl.gz:274732` contains one exact direct StrainInfo row and one exact StrainInfo deposit row for this NCBI taxon.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:77519`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:77519`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL row does not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
