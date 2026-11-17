# YAML Record Review: Saccharomyces pastorianus CBS 1513

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_pastorianus_cbs_1513.yaml`
- Identifier: `NCBITaxon:1073566`

## Target

Reviewed the complete 78-line YAML record for Saccharomyces pastorianus CBS 1513. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_pastorianus_cbs_1513.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_pastorianus_cbs_1513.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_paradoxus_nrrl_y_17217.yaml data/taxa/eukaryota/saccharomyces_pastorianus.yaml data/taxa/eukaryota/saccharomyces_pastorianus_cbs_1503.yaml data/taxa/eukaryota/saccharomyces_pastorianus_cbs_1513.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 230064 retains `NCBITaxon:1073566` as `Saccharomyces pastorianus CBS 1513`, rank `STRAIN`, parent `NCBITaxon:27292`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 57509, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 2 exact synonyms, 0 related synonyms, and 0 broad synonyms; the YAML synonym block matches those source counts.
- All 14 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:1428316` to `NCBITaxon:1073566` at line 15616. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:1428316`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:1073566` at line 1287 with `organism_count` 2, matching the YAML source assertion count.
- Native GOLD exact scans found 3 organism rows, 5 project rows, and 3 analysis rows for NCBI 1073566.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:1073566`.
- Local BacDive evidence had 0 exact rows for NCBI 1073566.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 1073566.

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
