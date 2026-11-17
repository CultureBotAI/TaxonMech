# YAML Record Review: Saccharina japonica

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharina_japonica.yaml`
- Identifier: `NCBITaxon:88149`

## Target

Reviewed the complete 75-line YAML record for Saccharina japonica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharina_japonica.

## Validation

- `just validate data/taxa/eukaryota/saccharina_japonica.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharina_japonica.yaml data/taxa/eukaryota/saccharina_latissima.yaml data/taxa/eukaryota/saccharomyces_cerevisiae.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_by4743.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 13933 retains `NCBITaxon:88149` as `Saccharina japonica`, rank `SPECIES`, parent `NCBITaxon:309357`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 53464, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 1 exact synonym, 3 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 11 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:3020498` to `NCBITaxon:88149` at line 60613. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:3020498`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:88149` at line 43765 with `organism_count` 1, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 1 project row, and 1 analysis row for NCBI 88149.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:88149`.
- Local BacDive evidence had 0 exact rows for NCBI 88149.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 88149.

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
