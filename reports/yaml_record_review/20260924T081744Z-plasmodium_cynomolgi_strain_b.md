# YAML Record Review: Plasmodium cynomolgi strain B

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmodium_cynomolgi_strain_b.yaml`
- Identifier: `NCBITaxon:1120755`

## Target

Reviewed the complete 69-line YAML record for `Plasmodium cynomolgi strain B`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmodium_cynomolgi_strain_b`.

## Validation

- `just validate data/taxa/eukaryota/plasmodium_cynomolgi_strain_b.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmodium_cynomolgi.yaml data/taxa/eukaryota/plasmodium_cynomolgi_strain_b.yaml data/taxa/eukaryota/plasmodium_falciparum.yaml data/taxa/eukaryota/plasmodium_falciparum_nf54.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:241891` is the exact retained NCBITaxon row for `NCBITaxon:1120755`: label `Plasmodium cynomolgi strain B`, rank `STRAIN`, parent `NCBITaxon:5827`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:57739` contains the seeded in-scope row for `NCBITaxon:1120755` with the reason `attested rule: Plasmodium cynomolgi strain B, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 0 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1120755`.

## Evidence

- `data/raw/gold_organisms.tsv:2156` is the aggregate GOLD row for `NCBITaxon:1120755` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1120755`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1120755`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1120755`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
