# YAML Record Review: Pisolithus orientalis

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_orientalis.yaml`
- Identifier: `NCBITaxon:936130`

## Target

Reviewed the complete 78-line YAML record for `Pisolithus orientalis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_orientalis`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_orientalis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pisolithus_orientalis.yaml data/taxa/eukaryota/pisolithus_sp.yaml data/taxa/eukaryota/pisolithus_thermaeus.yaml data/taxa/eukaryota/pisolithus_tinctorius.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:198182` is the exact retained NCBITaxon row for `NCBITaxon:936130`: label `Pisolithus orientalis`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56957` contains the seeded in-scope row for `NCBITaxon:936130` with the reason `attested rule: Pisolithus orientalis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:936130`.

## Evidence

- `data/raw/gold_organisms.tsv:44813` is the aggregate GOLD row for `NCBITaxon:936130` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, three linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:274273` through `data/raw/ncbi_type_material.tsv:274277` contain the 5 exact NCBI type-material rows for `NCBITaxon:936130`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:936130`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:936130`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The five NCBI type-material rows are equivalent holotype designations and do not imply generated strain rows.
