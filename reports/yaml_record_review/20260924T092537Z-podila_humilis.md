# YAML Record Review: Podila humilis

- Verdict: pass
- Target: `data/taxa/eukaryota/podila_humilis.yaml`
- Identifier: `NCBITaxon:64523`

## Target

Reviewed the complete 74-line YAML record for `Podila humilis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podila_humilis`.

## Validation

- `just validate data/taxa/eukaryota/podila_humilis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podila_epigama.yaml data/taxa/eukaryota/podila_horticola.yaml data/taxa/eukaryota/podila_humilis.yaml data/taxa/eukaryota/podila_minutissima.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8181` is the exact retained NCBITaxon row for `NCBITaxon:64523`: label `Podila humilis`, rank `SPECIES`, parent `NCBITaxon:2779937`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53091` contains the seeded in-scope row for `NCBITaxon:64523` with the reason `attested rule: Podila humilis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:64523`.

## Evidence

- `data/raw/gold_organisms.tsv:40324` is the aggregate GOLD row for `NCBITaxon:64523` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has two exact culture-from-syntype rows for `NCBITaxon:64523`, both filed under `Mortierella humilis`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 12 exact local JSONL records covering 14 deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:64523`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:64523`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows are NCBI designations that do not appear as generated strain rows, and the exact StrainInfo JSONL hits likewise have no corresponding BacDive or generated StrainInfo overlay rows. The two exact native GOLD organism rows match the aggregate GOLD `organism_count=2` attestation.
