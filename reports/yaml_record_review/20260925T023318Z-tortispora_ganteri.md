# YAML Record Review: Tortispora ganteri

- Verdict: pass
- Target: `data/taxa/eukaryota/tortispora_ganteri.yaml`
- Identifier: `NCBITaxon:1326887`

## Target

Reviewed the complete 75-line YAML record for Tortispora ganteri. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tortispora_ganteri.

## Validation

- `just validate data/taxa/eukaryota/tortispora_ganteri.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/torrubiella_hemipterigena.yaml data/taxa/eukaryota/tortispora_agaves.yaml data/taxa/eukaryota/tortispora_caseinolytica.yaml data/taxa/eukaryota/tortispora_ganteri.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The YAML keeps the current NCBI row from line 316537: `NCBITaxon:1326887`, `Tortispora ganteri`, rank `SPECIES`, parent `NCBITaxon:1540147`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table retained exactly one row for `NCBITaxon:1326887` at line 59483.
- NCBI synonym columns contained 0 exact synonyms, 0 broad synonyms, and 2 related synonyms, matching the two YAML synonym entries.
- The YAML lineage checked 13 ancestor rows against NCBI and had no missing ancestors or label/rank mismatches.
- The NCBI merged-ID table had one old ID, `NCBITaxon:1326889`, redirecting to `NCBITaxon:1326887`; the ignored-file-inclusive tab-bounded lookup found it only in `data/raw/ncbi_merged_ids.tsv`, not as a retained active row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The generated GOLD aggregate had one row at line 7955 with `organism_count` `1`, matching the YAML GOLD assertion count.
- Native GOLD tables contained 1 organism row, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` had nine exact type-material rows for `NCBITaxon:1326887`: `CBS 12581`, `CBS:12581`, `NRRL 17035`, `NRRL Y-17035`, `NRRL:17035`, `NRRL:Y-17035`, `NRRL:Y:17035`, `SUB 86-469.5`, and `SUB:86-469.5`.
- BacDive had 0 exact strain rows for `NCBITaxon:1326887`.
- StrainInfo JSONL had 0 direct strain rows and 0 exact deposit annotations for `NCBITaxon:1326887`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1326887`: BacDive strains, culture-collection strains, strain assemblies, strain genome records, and strain-related records were all empty for this target.
- Auxiliary source scans found no exact rows for `NCBITaxon:1326887` in BactoTraits, GTDB mappings, GTDB species, LPSN names, Madin, or MediaDive.
- Generated StrainInfo overlay tables had no rows for `NCBITaxon:1326887` in `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No seeded YAML was edited; this review only adds the ignored Markdown report.
