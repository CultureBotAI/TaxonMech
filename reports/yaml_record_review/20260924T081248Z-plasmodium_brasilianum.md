# YAML Record Review: Plasmodium brasilianum

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_brasilianum.yaml`
- Identifier: `NCBITaxon:5824`

## Target

Reviewed the complete 66-line YAML record for `Plasmodium brasilianum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_brasilianum`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_brasilianum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_berghei.yaml data/taxa/eukaryota/plasmodium_billcollinsi.yaml data/taxa/eukaryota/plasmodium_blacklocki_nom_inval.yaml data/taxa/eukaryota/plasmodium_brasilianum.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2586` is the exact retained NCBITaxon row for `NCBITaxon:5824`: label `Plasmodium brasilianum`, rank `SPECIES`, parent `NCBITaxon:418103`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52088` contains the seeded in-scope row for `NCBITaxon:5824` with the reason `attested rule: Plasmodium brasilianum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5824`.

## Evidence

- `data/raw/gold_organisms.tsv:39402` is the aggregate GOLD row for `NCBITaxon:5824` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5824`.
- `data/straininfo/records.jsonl.gz:274767` and `data/straininfo/records.jsonl.gz:276375` contain the 2 exact direct StrainInfo rows for this NCBI taxon, each with an exact deposit row.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5824`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5824`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
