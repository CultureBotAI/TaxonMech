# YAML Record Review: Saccharomyces jurei

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_jurei.yaml`
- Identifier: `NCBITaxon:1987369`

## Target

Reviewed the complete 79-line YAML record for Saccharomyces jurei. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_jurei.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_jurei.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_eubayanus.yaml data/taxa/eukaryota/saccharomyces_jurei.yaml data/taxa/eukaryota/saccharomyces_kudriavzevii.yaml data/taxa/eukaryota/saccharomyces_paradoxus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 508561 retains `NCBITaxon:1987369` as `Saccharomyces jurei`, rank `SPECIES`, parent `NCBITaxon:4930`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 61825, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 0 exact synonyms, 3 related synonyms, and 0 broad synonyms; the YAML synonym block matches those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:1423350` to `NCBITaxon:1987369` at line 15494. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:1423350`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:1987369` at line 18406 with `organism_count` 1, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 1 project row, and 1 analysis row for NCBI 1987369.
- NCBI type-material evidence had 8 exact rows for `NCBITaxon:1987369` at `data/raw/ncbi_type_material.tsv` lines 76697-76704.
- Local BacDive evidence had 0 exact rows for NCBI 1987369.
- Local StrainInfo evidence had 2 direct rows and 2 matching deposit designations for NCBI 1987369.

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
