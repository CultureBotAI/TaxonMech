# YAML Record Review: Priceomyces carsonii

- Verdict: pass
- Target: `data/taxa/eukaryota/priceomyces_carsonii.yaml`
- Identifier: `NCBITaxon:28549`

## Target

Reviewed the complete 84-line YAML record for `Priceomyces carsonii`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `priceomyces_carsonii`.

## Validation

- `just validate data/taxa/eukaryota/priceomyces_carsonii.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/powellomyces_hirtus.yaml data/taxa/eukaryota/preussia_procaviae.yaml data/taxa/eukaryota/priceomyces_carsonii.yaml data/taxa/eukaryota/priceomyces_castillae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2964` is the exact retained NCBITaxon row for `NCBITaxon:28549`: label `Priceomyces carsonii`, rank `SPECIES`, parent `NCBITaxon:766759`, genetic code `12`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52174` contains the seeded in-scope row for `NCBITaxon:28549` with the reason `attested rule: Priceomyces carsonii, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:2898216` to `NCBITaxon:28549`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:27691` is the aggregate GOLD row for `NCBITaxon:28549` and reports `organism_count=7`, matching the YAML GOLD source attestation.
- Native GOLD has seven exact organism rows, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv:132237` through `data/raw/ncbi_type_material.tsv:132252` provide 16 exact `type material` aliases under `Pichia carsonii`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 33 direct local JSONL records covering 84 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:28549`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:28549`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

`NCBITaxon:2898216` appears only as a retired old ID in `data/raw/ncbi_merged_ids.tsv` and not as a retained row in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of a generated `replaces` value. The direct StrainInfo JSONL evidence is not materialized in BacDive or generated StrainInfo overlay tables.
