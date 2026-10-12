# YAML Record Review: Saccharomyces cerevisiae FostersO

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_cerevisiae_fosterso.yaml`
- Identifier: `NCBITaxon:764101`

## Target

Reviewed the complete 71-line YAML record for Saccharomyces cerevisiae FostersO. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_cerevisiae_fosterso.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_cerevisiae_fosterso.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_cerevisiae_cbs_1585.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_fostersb.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_fosterso.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_pe_2.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 177375 retains `NCBITaxon:764101` as `Saccharomyces cerevisiae FostersO`, rank `STRAIN`, parent `NCBITaxon:4932`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 56677, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 0 exact synonyms, 0 related synonyms, and 0 broad synonyms; the YAML absence of synonym blocks matches those source counts.
- All 14 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- No rows in `data/raw/ncbi_merged_ids.tsv` map retired NCBI IDs into `NCBITaxon:764101`, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:764101` at line 42519 with `organism_count` 1, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 1 project row, and 1 analysis row for NCBI 764101.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:764101`.
- Local BacDive evidence had 0 exact rows for NCBI 764101.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 764101.

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
