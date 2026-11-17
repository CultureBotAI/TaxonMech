# YAML Record Review: Plasmopara muralis

- Verdict: pass
- Target: `data/taxa/eukaryota/plasmopara_muralis.yaml`
- Identifier: `NCBITaxon:1196443`

## Target

Reviewed the complete 66-line YAML record for `Plasmopara muralis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plasmopara_muralis`.

## Validation

- `just validate data/taxa/eukaryota/plasmopara_muralis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmopara_muralis.yaml data/taxa/eukaryota/plasmopara_obducens.yaml data/taxa/eukaryota/plasmopara_viticola.yaml data/taxa/eukaryota/platygloea_disciformis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:269145` is the exact retained NCBITaxon row for `NCBITaxon:1196443`: label `Plasmopara muralis`, rank `SPECIES`, parent `NCBITaxon:4780`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:58289` contains the seeded in-scope row for `NCBITaxon:1196443` with the reason `attested rule: Plasmopara muralis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:89310` maps old ID `NCBITaxon:622443` into `NCBITaxon:1196443`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:4737` is the aggregate GOLD row for `NCBITaxon:1196443` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1196443`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1196443`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1196443`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The merged old ID is merge metadata only for this generated record. Because that old ID is not present in the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
