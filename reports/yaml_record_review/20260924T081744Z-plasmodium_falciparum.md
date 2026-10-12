# YAML Record Review: Plasmodium falciparum

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_falciparum.yaml`
- Identifier: `NCBITaxon:5833`

## Target

Reviewed the complete 73-line YAML record for `Plasmodium falciparum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_falciparum`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_falciparum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_cynomolgi.yaml data/taxa/eukaryota/plasmodium_cynomolgi_strain_b.yaml data/taxa/eukaryota/plasmodium_falciparum.yaml data/taxa/eukaryota/plasmodium_falciparum_nf54.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2590` is the exact retained NCBITaxon row for `NCBITaxon:5833`: label `Plasmodium falciparum`, rank `SPECIES`, parent `NCBITaxon:418107`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52092` contains the seeded in-scope row for `NCBITaxon:5833` with the reason `attested rule: Plasmodium falciparum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5833`.

## Evidence

- `data/raw/gold_organisms.tsv:39437` is the aggregate GOLD row for `NCBITaxon:5833` and reports `organism_count=61`, matching the YAML GOLD source attestation.
- Native GOLD has 62 exact organism rows, 71 linked project rows, and 11 linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5833`.
- `data/straininfo/records.jsonl.gz` has 15 exact direct StrainInfo rows for this NCBI taxon, each with an exact deposit row: lines 274746, 274914, 274977, 274979, 275130, 275218, 275225, 275226, 275228, 275290, 275307, 275548, 275550, 276109, and 276172.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5833`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5833`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The GOLD source attestation is scoped to records filed directly under `NCBITaxon:5833`; descendant taxa are not gathered into the generated count. The aggregate GOLD inventory reports 61 organisms, while the local native GOLD organism JSONL has 62 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row. The exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
