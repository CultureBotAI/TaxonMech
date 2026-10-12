# YAML Record Review: Pilobolus umbonatus

- Verdict: pass
- Target: `data/taxa/eukaryota/pilobolus_umbonatus.yaml`
- Identifier: `NCBITaxon:101123`

## Target

Reviewed the complete 72-line YAML record for `Pilobolus umbonatus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pilobolus_umbonatus`.

## Validation

- `just validate data/taxa/eukaryota/pilobolus_umbonatus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pilaira_moreaui_var_caucasica.yaml data/taxa/eukaryota/pilasporangium_apinafurcum.yaml data/taxa/eukaryota/pilatotrama_ljubarskyi.yaml data/taxa/eukaryota/pilobolus_umbonatus.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:17437` is the exact retained NCBITaxon row for `NCBITaxon:101123`: label `Pilobolus umbonatus`, rank `SPECIES`, parent `NCBITaxon:81945`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53644` contains the seeded in-scope row for `NCBITaxon:101123` with the reason `attested rule: Pilobolus umbonatus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:101123`.

## Evidence

- `data/raw/gold_organisms.tsv:255` is the aggregate GOLD row for `NCBITaxon:101123` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:75061`, two linked project rows starting at `data/gold/projects.jsonl.gz:84381`, and no linked analysis rows for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:101123`.
- StrainInfo has 9 direct exact JSONL rows and 11 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:101123`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:101123`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
