# YAML Record Review: Powellomyces hirtus

- Verdict: pass
- Target: `data/taxa/eukaryota/powellomyces_hirtus.yaml`
- Identifier: `NCBITaxon:109895`

## Target

Reviewed the complete 72-line YAML record for `Powellomyces hirtus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `powellomyces_hirtus`.

## Validation

- `just validate data/taxa/eukaryota/powellomyces_hirtus.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/powellomyces_hirtus.yaml data/taxa/eukaryota/preussia_procaviae.yaml data/taxa/eukaryota/priceomyces_carsonii.yaml data/taxa/eukaryota/priceomyces_castillae.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:19734` is the exact retained NCBITaxon row for `NCBITaxon:109895`: label `Powellomyces hirtus`, rank `SPECIES`, parent `NCBITaxon:109893`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53750` contains the seeded in-scope row for `NCBITaxon:109895` with the reason `attested rule: Powellomyces hirtus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:1837` is the aggregate GOLD row for `NCBITaxon:109895` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, three linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:6287` through `data/raw/ncbi_type_material.tsv:6297` provide 11 exact `type material` aliases for `Powellomyces hirtus`.
- BacDive has no exact local JSONL records for this NCBI taxon; StrainInfo has no direct exact local JSONL records and one exact deposit, `ATCC 22196` on siID `167951`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:109895`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:109895`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with the aggregate GOLD row and the two native GOLD organism rows for strains `BR81` and `CBS 809.83`. NCBI type-material aliases and the non-direct StrainInfo deposit are evidence-only here and do not create rows in the generated strain overlays.
