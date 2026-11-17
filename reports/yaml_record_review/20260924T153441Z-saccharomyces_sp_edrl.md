# YAML Record Review: Saccharomyces sp. EDRL

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_sp_edrl.yaml`
- Identifier: `NCBITaxon:1343043`

## Target

Reviewed the complete 75-line YAML record for Saccharomyces sp. EDRL. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_sp_edrl.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_sp_edrl.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_pastorianus_cbs_6283.yaml data/taxa/eukaryota/saccharomyces_sp_edrl.yaml data/taxa/eukaryota/saccharomyces_sp_m14.yaml data/taxa/eukaryota/saccharomyces_uvarum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 322663 retains `NCBITaxon:1343043` as `Saccharomyces sp. EDRL`, rank `STRAIN`, parent `NCBITaxon:4932`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 59573, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 1 exact synonym, 0 related synonyms, and 0 broad synonyms; the YAML synonym block matches that source count.
- All 14 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- No rows in `data/raw/ncbi_merged_ids.tsv` map retired NCBI IDs into `NCBITaxon:1343043`, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:1343043` at line 8352 with `organism_count` 2, matching the YAML source assertion count.
- Native GOLD exact scans found 2 organism rows, 2 project rows, and 1 analysis row for NCBI 1343043.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:1343043`.
- Local BacDive evidence had 0 exact rows for NCBI 1343043.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 1343043.

## Completeness

- Generated raw strain tables had 0 exact rows across `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source scans had 0 exact rows across BactoTraits, GTDB mappings and species, LPSN, Madin, and MediaDive inputs.
- Generated StrainInfo overlay tables had 0 exact rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

All raw-source checks were run from the detached `/private/tmp/taxonmech-codex-review` worktree; only this ignored report was written in the primary checkout.
