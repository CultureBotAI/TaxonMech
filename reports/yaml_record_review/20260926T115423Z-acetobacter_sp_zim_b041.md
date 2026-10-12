# YAML Record Review: Acetobacter sp. ZIM B041

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_zim_b041.yaml
- Started UTC: 2026-09-26T11:50:42Z
- Finished UTC: 2026-09-26T11:54:23Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:85326 |
| Label | Acetobacter sp. ZIM B041 |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:2628570, unclassified Acetobacter |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Raw NCBI row | data/raw/ncbitaxon_taxa.tsv:13149 |
| Scope row | curation/seed_scope.tsv:139817 |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/acetobacter_sp_zim_b041.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_zim_b034.yaml data/taxa/bacteria/acetobacter_sp_zim_b040.yaml data/taxa/bacteria/acetobacter_sp_zim_b041.yaml data/taxa/bacteria/acetobacter_sp_zim_b043.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 54 lines, 10 lineage entries, 1 NCBITAXON/NAME attestation, 0 strains, 0 optional source blocks |
| Bounded source scan | Pass; exact NCBI and seed-scope rows found, no lineage mismatches, no merged IDs, no optional exact source rows |
| Exact ignored-aware source scan | Pass; the exhaustive `rg --no-ignore --hidden` search across raw, catalog, BacDive, GOLD, ATB, StrainInfo, curation, and history paths found only the expected NCBI and scope rows |

## Identity and Grounding

- `NCBITaxon:85326`, label `Acetobacter sp. ZIM B041`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source `ncbitaxon`, and snapshot `2026-09-13` match the exact source row in `data/raw/ncbitaxon_taxa.tsv:13149`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with the single matching `curation/seed_scope.tsv:139817` row.
- The bounded NCBI scan resolved all 10 root-first lineage entries and found no missing ancestors or label/rank mismatches.

## Evidence

- The sole `source_attestations` entry names `NCBITAXON`, `NCBITaxon:85326`, `Acetobacter sp. ZIM B041`, `assertion_count: 1`, and `assertion_unit: NAME`; those values are directly supported by the exact NCBI inventory row.
- The NCBI raw row has blank synonym fields and no retirement target, matching the absence of `synonyms` and retained old IDs.
- The bounded scan found no rows for this target in LPSN, GTDB, Madin, BactoTraits, MediaDive, BacDive, GOLD, StrainInfo, strain genome, strain assembly, strain related-record, or NCBI type-material inventories.

## Completeness

- `strain_count: 0` is complete for the committed inventories: exact BacDive, StrainInfo, GOLD, aggregate GOLD, strain assembly, strain genome, and related-record scans all returned zero rows for `NCBITaxon:85326`.
- No nomenclature, taxonomy mappings, synonyms, xrefs, genome links, related records, definitions, or causal graphs are warranted by the scanned source rows.
- No additional source or history references were found by the ignored-file exact scan, so there is no local evidence for an omitted optional block.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future source refreshes should re-run the same exact NCBI, seed-scope, optional-source, schema, and strict validation checks before changing maintained inputs.

## Additional Notes

- Duplicate preflight used `find reports/yaml_record_review -maxdepth 1 -name '*-acetobacter_sp_zim_b041.md' -print`, which includes ignored report files, and found no existing report for this stem before this file was written.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
