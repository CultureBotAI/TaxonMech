# YAML Record Review: Piskurozyma fildesensis

- Verdict: pass
- Target: `data/taxa/eukaryota/piskurozyma_fildesensis.yaml`
- Identifier: `NCBITaxon:1834862`

## Target

Reviewed the complete 81-line YAML record for `Piskurozyma fildesensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piskurozyma_fildesensis`.

## Validation

- `just validate data/taxa/eukaryota/piskurozyma_fildesensis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piromyces_sp_ok2_1.yaml data/taxa/eukaryota/pirum_gemmata.yaml data/taxa/eukaryota/piskurozyma_capsuligena.yaml data/taxa/eukaryota/piskurozyma_fildesensis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:478373` is the exact retained NCBITaxon row for `NCBITaxon:1834862`: label `Piskurozyma fildesensis`, rank `SPECIES`, parent `NCBITaxon:1851566`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:61337` contains the seeded in-scope row for `NCBITaxon:1834862` with the reason `attested rule: Piskurozyma fildesensis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 4 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:12711` and `data/raw/ncbi_merged_ids.tsv:12712` map old IDs `NCBITaxon:1338684` and `NCBITaxon:1338685` into `NCBITaxon:1834862`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:16262` is the aggregate GOLD row for `NCBITaxon:1834862` and reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows and no linked project or analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:63134` through `data/raw/ncbi_type_material.tsv:63139` contain the 6 exact NCBI type-material rows for `NCBITaxon:1834862`.
- StrainInfo has 2 direct exact JSONL rows and 2 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1834862`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1834862`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The two merged old IDs are merge metadata only for this generated record. Because neither old ID is present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected.
