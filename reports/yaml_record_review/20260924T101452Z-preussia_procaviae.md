# YAML Record Review: Sporormiella procaviae

- Verdict: pass
- Target: `data/taxa/eukaryota/preussia_procaviae.yaml`
- Identifier: `NCBITaxon:2781211`

## Target

Reviewed the complete 90-line YAML record for `Sporormiella procaviae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `preussia_procaviae`.

## Validation

- `just validate data/taxa/eukaryota/preussia_procaviae.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/powellomyces_hirtus.yaml data/taxa/eukaryota/preussia_procaviae.yaml data/taxa/eukaryota/priceomyces_carsonii.yaml data/taxa/eukaryota/priceomyces_castillae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:554614` is the exact retained NCBITaxon row for `NCBITaxon:2781211`: label `Sporormiella procaviae`, rank `SPECIES`, parent `NCBITaxon:718228`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63230` contains the seeded in-scope row for `NCBITaxon:2781211` with the reason `attested rule: Preussia procaviae, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:26490` is the aggregate GOLD row for `NCBITaxon:2781211` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has two exact `culture from holotype` rows for `NCBITaxon:2781211`, covering `CBS 146827` and `CBS:146827`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2781211`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2781211`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The YAML label follows the retained 2026-09-13 NCBITaxon row while keeping `Preussia procaviae` as an exact synonym, so the original `preussia_procaviae` file stem and seed rule still resolve to `NCBITaxon:2781211`.
