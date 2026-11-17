# YAML Record Review: Plasmodium berghei

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_berghei.yaml`
- Identifier: `NCBITaxon:5821`

## Target

Reviewed the complete 66-line YAML record for `Plasmodium berghei`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_berghei`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_berghei.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_berghei.yaml data/taxa/eukaryota/plasmodium_billcollinsi.yaml data/taxa/eukaryota/plasmodium_blacklocki_nom_inval.yaml data/taxa/eukaryota/plasmodium_brasilianum.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2585` is the exact retained NCBITaxon row for `NCBITaxon:5821`: label `Plasmodium berghei`, rank `SPECIES`, parent `NCBITaxon:418101`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52087` contains the seeded in-scope row for `NCBITaxon:5821` with the reason `attested rule: Plasmodium berghei, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5821`.

## Evidence

- `data/raw/gold_organisms.tsv:39401` is the aggregate GOLD row for `NCBITaxon:5821` and reports `organism_count=5`, matching the YAML GOLD source attestation.
- Native GOLD has 5 exact organism rows, 5 linked project rows, and 5 linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5821`.
- `data/straininfo/records.jsonl.gz` has 6 exact direct StrainInfo rows for this NCBI taxon, each with an exact deposit row: lines 274755, 275630, 275632, 275635, 276210, and 276263.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5821`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5821`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
