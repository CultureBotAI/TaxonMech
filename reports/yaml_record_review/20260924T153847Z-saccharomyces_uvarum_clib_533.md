# YAML Record Review: Saccharomyces uvarum CLIB 533

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_uvarum_clib_533.yaml`
- Identifier: `NCBITaxon:659244`

## Target

Reviewed the complete 84-line YAML record for Saccharomyces uvarum CLIB 533. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_uvarum_clib_533.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_uvarum_clib_533.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_uvarum_clib_533.yaml data/taxa/eukaryota/saccharomyces_x_bayanus.yaml data/taxa/eukaryota/saccharomyces_x_bayanus_cbs_1502.yaml data/taxa/eukaryota/saccharomyces_x_bayanus_cbs_1542.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 152474 retains `NCBITaxon:659244` as `Saccharomyces uvarum CLIB 533`, rank `STRAIN`, parent `NCBITaxon:230603`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 56296, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 4 exact synonyms, 0 related synonyms, and 0 broad synonyms; the YAML synonym block matches those source counts.
- All 14 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:226127` and `NCBITaxon:226231` to `NCBITaxon:659244` at lines 39772 and 39777. Exact searches of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:659244` at line 40640 with `organism_count` 2, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 2 project rows, and 2 analysis rows for NCBI 659244.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:659244`.
- Local BacDive evidence had 0 exact rows for NCBI 659244.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 659244.

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
