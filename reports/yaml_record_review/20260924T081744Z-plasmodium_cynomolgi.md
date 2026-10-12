# YAML Record Review: Plasmodium cynomolgi

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_cynomolgi.yaml`
- Identifier: `NCBITaxon:5827`

## Target

Reviewed the complete 67-line YAML record for `Plasmodium cynomolgi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_cynomolgi`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_cynomolgi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/plasmodium_cynomolgi.yaml data/taxa/eukaryota/plasmodium_cynomolgi_strain_b.yaml data/taxa/eukaryota/plasmodium_falciparum.yaml data/taxa/eukaryota/plasmodium_falciparum_nf54.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2589` is the exact retained NCBITaxon row for `NCBITaxon:5827`: label `Plasmodium cynomolgi`, rank `SPECIES`, parent `NCBITaxon:418103`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52091` contains the seeded in-scope row for `NCBITaxon:5827` with the reason `attested rule: Plasmodium cynomolgi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 11 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5827`.

## Evidence

- `data/raw/gold_organisms.tsv:39424` is the aggregate GOLD row for `NCBITaxon:5827` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5827`.
- `data/straininfo/records.jsonl.gz` has 11 exact direct StrainInfo rows for this NCBI taxon, each with an exact deposit row: lines 274727, 274733, 274744, 274765, 274898, 274902, 274915, 274918, 274922, 276187, and 276188.
- BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5827`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5827`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The GOLD source attestation is scoped to records filed directly under `NCBITaxon:5827`; descendant taxa are not gathered into the generated count. The exact StrainInfo JSONL rows do not emit overlay rows because StrainInfo overlays are limited to BacDive-derived local strains.
