# YAML Record Review: Piptocephalis brijmohanii

- Verdict: pass
- Target: `data/taxa/eukaryota/piptocephalis_brijmohanii.yaml`
- Identifier: `NCBITaxon:2486754`

## Target

Reviewed the complete 69-line YAML record for `Piptocephalis brijmohanii`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piptocephalis_brijmohanii`.

## Validation

- `just validate data/taxa/eukaryota/piptocephalis_brijmohanii.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pinibarrenia_chlamydospora.yaml data/taxa/eukaryota/pinnaticoemansia_coronantispora.yaml data/taxa/eukaryota/piptocephalis_brijmohanii.yaml data/taxa/eukaryota/piptocephalis_cylindrospora.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:526304` is the exact retained NCBITaxon row for `NCBITaxon:2486754`: label `Piptocephalis brijmohanii`, rank `SPECIES`, parent `NCBITaxon:78916`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62591` contains the seeded in-scope row for `NCBITaxon:2486754` with the reason `attested rule: Piptocephalis brijmohanii, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:2486754`.

## Evidence

- `data/raw/gold_organisms.tsv:22358` is the aggregate GOLD row for `NCBITaxon:2486754` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:372467`, one linked project row at `data/gold/projects.jsonl.gz:326116`, and no linked analysis rows for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:2486754`.
- StrainInfo has 6 direct exact JSONL rows and 10 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2486754`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2486754`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
