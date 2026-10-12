# YAML Record Review: Pinibarrenia chlamydospora

- Verdict: pass
- Target: `data/taxa/eukaryota/pinibarrenia_chlamydospora.yaml`
- Identifier: `NCBITaxon:3115591`

## Target

Reviewed the complete 84-line YAML record for `Pinibarrenia chlamydospora`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pinibarrenia_chlamydospora`.

## Validation

- `just validate data/taxa/eukaryota/pinibarrenia_chlamydospora.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pinibarrenia_chlamydospora.yaml data/taxa/eukaryota/pinnaticoemansia_coronantispora.yaml data/taxa/eukaryota/piptocephalis_brijmohanii.yaml data/taxa/eukaryota/piptocephalis_cylindrospora.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:600654` is the exact retained NCBITaxon row for `NCBITaxon:3115591`: label `Pinibarrenia chlamydospora`, rank `SPECIES`, parent `NCBITaxon:3232062`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63561` contains the seeded in-scope row for `NCBITaxon:3115591` with the reason `attested rule: Pinibarrenia chlamydospora, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:3115591`.

## Evidence

- `data/raw/gold_organisms.tsv:31451` is the aggregate GOLD row for `NCBITaxon:3115591` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files have no exact rows for this target.
- `data/raw/ncbi_type_material.tsv:168734` through `data/raw/ncbi_type_material.tsv:168743` contain the 10 exact NCBI type-material rows for `NCBITaxon:3115591`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:3115591`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:3115591`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The GOLD evidence for this record is present in the aggregate `data/raw/gold_organisms.tsv` inventory; the local native GOLD organism, project, and analysis JSONL scans have no exact rows for the target.
