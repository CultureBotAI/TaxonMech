# YAML Record Review: Plasmodium coatneyi

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_coatneyi.yaml`
- Identifier: `NCBITaxon:208452`

## Target

Reviewed the complete 66-line YAML record for `Plasmodium coatneyi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_coatneyi`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_coatneyi.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_chabaudi.yaml data/taxa/eukaryota/plasmodium_chabaudi_adami.yaml data/taxa/eukaryota/plasmodium_chabaudi_chabaudi.yaml data/taxa/eukaryota/plasmodium_coatneyi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:41126` is the exact retained NCBITaxon row for `NCBITaxon:208452`: label `Plasmodium coatneyi`, rank `SPECIES`, parent `NCBITaxon:3699347`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54505` contains the seeded in-scope row for `NCBITaxon:208452` with the reason `attested rule: Plasmodium coatneyi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:208452`.

## Evidence

- `data/raw/gold_organisms.tsv:19957` is the aggregate GOLD row for `NCBITaxon:208452` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:208452`.
- `data/straininfo/records.jsonl.gz:274901` contains one exact direct StrainInfo row and one exact StrainInfo deposit row for this NCBI taxon.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:208452`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:208452`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The aggregate GOLD inventory reports 1 organism, while the local native GOLD organism JSONL has 2 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row. The exact StrainInfo JSONL row does not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
