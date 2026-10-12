# YAML Record Review: Piskurozyma capsuligena

- Verdict: pass
- Target: `data/taxa/eukaryota/piskurozyma_capsuligena.yaml`
- Identifier: `NCBITaxon:5211`

## Target

Reviewed the complete 83-line YAML record for `Piskurozyma capsuligena`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piskurozyma_capsuligena`.

## Validation

- `just validate data/taxa/eukaryota/piskurozyma_capsuligena.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piromyces_sp_ok2_1.yaml data/taxa/eukaryota/pirum_gemmata.yaml data/taxa/eukaryota/piskurozyma_capsuligena.yaml data/taxa/eukaryota/piskurozyma_fildesensis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2292` is the exact retained NCBITaxon row for `NCBITaxon:5211`: label `Piskurozyma capsuligena`, rank `SPECIES`, parent `NCBITaxon:1851566`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:51953` contains the seeded in-scope row for `NCBITaxon:5211` with the reason `attested rule: Piskurozyma capsuligena, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:5211`.

## Evidence

- `data/raw/gold_organisms.tsv:37803` is the aggregate GOLD row for `NCBITaxon:5211` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files have no exact rows for this target.
- `data/raw/ncbi_type_material.tsv:227621` through `data/raw/ncbi_type_material.tsv:227642` contain the 22 exact NCBI type-material rows for `NCBITaxon:5211`.
- StrainInfo has 23 direct exact JSONL rows and 70 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5211`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5211`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
