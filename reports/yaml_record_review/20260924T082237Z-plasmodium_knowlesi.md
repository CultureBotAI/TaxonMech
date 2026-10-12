# YAML Record Review: Plasmodium knowlesi

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_knowlesi.yaml`
- Identifier: `NCBITaxon:5850`

## Target

Reviewed the complete 63-line YAML record for `Plasmodium knowlesi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_knowlesi`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_knowlesi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_knowlesi.yaml data/taxa/eukaryota/plasmodium_knowlesi_strain_h.yaml data/taxa/eukaryota/plasmodium_malariae.yaml data/taxa/eukaryota/plasmodium_ovale.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2593` is the exact retained NCBITaxon row for `NCBITaxon:5850`: label `Plasmodium knowlesi`, rank `SPECIES`, parent `NCBITaxon:418103`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52095` contains the seeded in-scope row for `NCBITaxon:5850` with the reason `attested rule: Plasmodium knowlesi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5850`.

## Evidence

- `data/raw/gold_organisms.tsv:39463` is the aggregate GOLD row for `NCBITaxon:5850` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5850`.
- `data/straininfo/records.jsonl.gz` has 4 exact direct StrainInfo rows for this NCBI taxon, each with an exact deposit row: lines 274921, 275074, 275075, and 276190.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5850`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5850`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The GOLD source attestation is scoped to records filed directly under `NCBITaxon:5850`; descendant taxa are not gathered into the generated count. The exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
