# YAML Record Review: Podila epicladia

- Verdict: pass
- Target: `data/taxa/eukaryota/podila_epicladia.yaml`
- Identifier: `NCBITaxon:979697`

## Target

Reviewed the complete 75-line YAML record for `Podila epicladia`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podila_epicladia`.

## Validation

- `just validate data/taxa/eukaryota/podila_epicladia.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/poaceascoma_sp.yaml data/taxa/eukaryota/pochonia_chlamydosporia.yaml data/taxa/eukaryota/podila_clonocystis.yaml data/taxa/eukaryota/podila_epicladia.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:204254` is the exact retained NCBITaxon row for `NCBITaxon:979697`: label `Podila epicladia`, rank `SPECIES`, parent `NCBITaxon:2779937`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:57045` contains the seeded in-scope row for `NCBITaxon:979697` with the reason `attested rule: Podila epicladia, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:979697`.

## Evidence

- `data/raw/gold_organisms.tsv:45184` is the aggregate GOLD row for `NCBITaxon:979697` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, three linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact type-material rows for `NCBITaxon:979697`, all filed under `Mortierella epicladia`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has four exact strain records covering four exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:979697`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:979697`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows are NCBI designations that do not appear as generated strain rows, and the exact StrainInfo JSONL hits likewise have no corresponding BacDive or generated StrainInfo overlay rows. The three exact native GOLD organism rows match the aggregate GOLD `organism_count=3` attestation.
