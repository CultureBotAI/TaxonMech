# YAML Record Review: Saccharomycopsis fodiens

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycopsis_fodiens.yaml`
- Identifier: `NCBITaxon:1305767`

## Target

Reviewed the complete 78-line YAML record for Saccharomycopsis fodiens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycopsis_fodiens.

## Validation

- `just validate data/taxa/eukaryota/saccharomycopsis_fodiens.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_crataegensis.yaml data/taxa/eukaryota/saccharomycopsis_fermentans.yaml data/taxa/eukaryota/saccharomycopsis_fibuligera.yaml data/taxa/eukaryota/saccharomycopsis_fodiens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 308582 retains `NCBITaxon:1305767` as `Saccharomycopsis fodiens`, rank `SPECIES`, parent `NCBITaxon:4943`, genetic code `12`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 59334, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 0 exact synonyms, 3 related synonyms, and 0 broad synonyms; the YAML synonym block matches those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:110554` to `NCBITaxon:1305767` at line 3554. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:110554`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:1305767` at line 7489 with `organism_count` 1, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 1 project row, and 0 analysis rows for NCBI 1305767.
- NCBI type-material evidence had 7 exact rows for `NCBITaxon:1305767` at `data/raw/ncbi_type_material.tsv` lines 21269-21275.
- Local BacDive evidence had 0 exact rows for NCBI 1305767.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 1305767.

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
