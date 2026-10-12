# YAML Record Review: Pilatotrama ljubarskyi

- Verdict: pass
- Target: `data/taxa/eukaryota/pilatotrama_ljubarskyi.yaml`
- Identifier: `NCBITaxon:2735509`

## Target

Reviewed the complete 78-line YAML record for `Pilatotrama ljubarskyi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pilatotrama_ljubarskyi`.

## Validation

- `just validate data/taxa/eukaryota/pilatotrama_ljubarskyi.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pilaira_moreaui_var_caucasica.yaml data/taxa/eukaryota/pilasporangium_apinafurcum.yaml data/taxa/eukaryota/pilatotrama_ljubarskyi.yaml data/taxa/eukaryota/pilobolus_umbonatus.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:548631` is the exact retained NCBITaxon row for `NCBITaxon:2735509`: label `Pilatotrama ljubarskyi`, rank `SPECIES`, parent `NCBITaxon:2735506`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:63007` contains the seeded in-scope row for `NCBITaxon:2735509` with the reason `attested rule: Pilatotrama ljubarskyi, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:4967` and `data/raw/ncbi_merged_ids.tsv:61187` map old IDs `NCBITaxon:1140396` and `NCBITaxon:303693` into `NCBITaxon:2735509`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:25515` is the aggregate GOLD row for `NCBITaxon:2735509` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, 25 linked project rows, and one linked analysis row for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:2735509`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2735509`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2735509`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The two merged old IDs are merge metadata only for this generated record. Because neither old ID is present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected.
