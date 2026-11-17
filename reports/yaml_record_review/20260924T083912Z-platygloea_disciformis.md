# YAML Record Review: Platygloea disciformis

- Verdict: pass
- Target: `data/taxa/eukaryota/platygloea_disciformis.yaml`
- Identifier: `NCBITaxon:255209`

## Target

Reviewed the complete 75-line YAML record for `Platygloea disciformis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `platygloea_disciformis`.

## Validation

- `just validate data/taxa/eukaryota/platygloea_disciformis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plasmopara_muralis.yaml data/taxa/eukaryota/plasmopara_obducens.yaml data/taxa/eukaryota/plasmopara_viticola.yaml data/taxa/eukaryota/platygloea_disciformis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:51836` is the exact retained NCBITaxon row for `NCBITaxon:255209`: label `Platygloea disciformis`, rank `SPECIES`, parent `NCBITaxon:105991`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54788` contains the seeded in-scope row for `NCBITaxon:255209` with the reason `attested rule: Platygloea disciformis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:255209`.

## Evidence

- `data/raw/gold_organisms.tsv:23199` is the aggregate GOLD row for `NCBITaxon:255209` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has no exact organism, project, or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact reference-material rows for `NCBITaxon:255209`: `AFTOL-ID 710`, `AFTOL-ID:710`, `IFO 32431`, and `IFO:32431`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found three exact local JSONL records covering five deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:255209`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:255209`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The generated GOLD source attestation uses the aggregate GOLD row even though the local native GOLD organism, project, and analysis files have no exact rows for this NCBI taxon.
