# YAML Record Review: Plasmodium chabaudi

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_chabaudi.yaml`
- Identifier: `NCBITaxon:5825`

## Target

Reviewed the complete 67-line YAML record for `Plasmodium chabaudi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_chabaudi`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_chabaudi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_chabaudi.yaml data/taxa/eukaryota/plasmodium_chabaudi_adami.yaml data/taxa/eukaryota/plasmodium_chabaudi_chabaudi.yaml data/taxa/eukaryota/plasmodium_coatneyi.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2587` is the exact retained NCBITaxon row for `NCBITaxon:5825`: label `Plasmodium chabaudi`, rank `SPECIES`, parent `NCBITaxon:418101`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52089` contains the seeded in-scope row for `NCBITaxon:5825` with the reason `attested rule: Plasmodium chabaudi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5825`.

## Evidence

- `data/raw/gold_organisms.tsv:39407` is the aggregate GOLD row for `NCBITaxon:5825` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5825`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5825`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5825`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The GOLD source attestation is scoped to records filed directly under `NCBITaxon:5825`; descendant taxa are not gathered into the generated count.
