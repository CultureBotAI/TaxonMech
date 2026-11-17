# YAML Record Review: Thyridium curvatum

- Verdict: pass
- Target: `data/taxa/eukaryota/thyridium_curvatum.yaml`
- Identifier: `NCBITaxon:1093900`

## Target

Reviewed the complete 98-line YAML record for Thyridium curvatum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for thyridium_curvatum.

## Validation

- `just validate data/taxa/eukaryota/thyridium_curvatum.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/thoracosphaera_heimii.yaml data/taxa/eukaryota/thraustochytrium_sp.yaml data/taxa/eukaryota/thraustotheca_clavata.yaml data/taxa/eukaryota/thyridium_curvatum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 235274: `NCBITaxon:1093900`, `Thyridium curvatum`, rank `SPECIES`, parent `NCBITaxon:265082`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:1093900` at line 57590.
- NCBI synonym columns contained 2 exact synonyms, 0 broad synonyms, and 4 related synonyms, matching the six YAML synonym entries.
- The YAML lineage checked 16 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had two old IDs, `NCBITaxon:263893` and `NCBITaxon:700761`, redirecting to `NCBITaxon:1093900`; the ignored-file-inclusive tab-bounded lookup found both only in `data/raw/ncbi_merged_ids.tsv`, not as retained active rows in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 1710 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` had four exact type-material rows for `NCBITaxon:1093900`: `CBS 490.82`, `CBS:490.82`, `CDC 45-394-63`, and `CDC:45-394-63`.
- BacDive had 0 exact strain rows for `NCBITaxon:1093900`.
- StrainInfo JSONL had 16 direct strain rows and 24 exact deposit annotations for `NCBITaxon:1093900`; the exact JSONL grep confirmed 16 direct rows.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1093900`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:1093900` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:1093900` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
