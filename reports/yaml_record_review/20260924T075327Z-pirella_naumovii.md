# YAML Record Review: Pirella naumovii

- Verdict: pass
- Target: `data/taxa/eukaryota/pirella_naumovii.yaml`
- Identifier: `NCBITaxon:1196579`

## Target

Reviewed the complete 81-line YAML record for `Pirella naumovii`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pirella_naumovii`.

## Validation

- `just validate data/taxa/eukaryota/pirella_naumovii.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pirella_circinans.yaml data/taxa/eukaryota/pirella_naumovii.yaml data/taxa/eukaryota/pirella_reniformis.yaml data/taxa/eukaryota/piromyces_communis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:269157` is the exact retained NCBITaxon row for `NCBITaxon:1196579`: label `Pirella naumovii`, rank `SPECIES`, parent `NCBITaxon:142620`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:58301` contains the seeded in-scope row for `NCBITaxon:1196579` with the reason `attested rule: Pirella naumovii, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:1196579`.

## Evidence

- `data/raw/gold_organisms.tsv:4749` is the aggregate GOLD row for `NCBITaxon:1196579` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:13010` through `data/raw/ncbi_type_material.tsv:13020` contain the 11 exact NCBI type-material rows for `NCBITaxon:1196579`.
- StrainInfo has 1 direct exact JSONL row and 7 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1196579`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1196579`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
