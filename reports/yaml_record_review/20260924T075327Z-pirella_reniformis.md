# YAML Record Review: Pirella reniformis

- Verdict: pass
- Target: `data/taxa/eukaryota/pirella_reniformis.yaml`
- Identifier: `NCBITaxon:2184027`

## Target

Reviewed the complete 72-line YAML record for `Pirella reniformis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pirella_reniformis`.

## Validation

- `just validate data/taxa/eukaryota/pirella_reniformis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pirella_circinans.yaml data/taxa/eukaryota/pirella_naumovii.yaml data/taxa/eukaryota/pirella_reniformis.yaml data/taxa/eukaryota/piromyces_communis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:521114` is the exact retained NCBITaxon row for `NCBITaxon:2184027`: label `Pirella reniformis`, rank `SPECIES`, parent `NCBITaxon:142620`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62460` contains the seeded in-scope row for `NCBITaxon:2184027` with the reason `attested rule: Pirella reniformis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:2184027`.

## Evidence

- `data/raw/gold_organisms.tsv:20807` is the aggregate GOLD row for `NCBITaxon:2184027` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:291294`, one linked project row at `data/gold/projects.jsonl.gz:193642`, and no linked analysis rows for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:2184027`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2184027`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2184027`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
