# YAML Record Review: Saccharomycodes ludwigii

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycodes_ludwigii.yaml`
- Identifier: `NCBITaxon:36035`

## Target

Reviewed the complete 102-line YAML record for Saccharomycodes ludwigii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycodes_ludwigii.

## Validation

- `just validate data/taxa/eukaryota/saccharomycodes_ludwigii.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycodes_ludwigii.yaml data/taxa/eukaryota/saccharomycopsis_amapae.yaml data/taxa/eukaryota/saccharomycopsis_babjevae.yaml data/taxa/eukaryota/saccharomycopsis_capsularis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 4045 retains `NCBITaxon:36035` as `Saccharomycodes ludwigii`, rank `SPECIES`, parent `NCBITaxon:36034`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 52313, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 2 exact synonyms, 9 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:2898213`, `NCBITaxon:2898214`, `NCBITaxon:2898215`, `NCBITaxon:3016114`, `NCBITaxon:3016115`, `NCBITaxon:3016116`, and `NCBITaxon:3016117` to `NCBITaxon:36035` at lines 56673-56675 and 60510-60513. Exact searches of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:36035` at line 33257 with `organism_count` 3, matching the YAML source assertion count.
- Native GOLD exact scans found 3 organism rows, 3 project rows, and 1 analysis row for NCBI 36035.
- NCBI type-material evidence had 16 exact rows for `NCBITaxon:36035` at `data/raw/ncbi_type_material.tsv` lines 193761-193776.
- Local BacDive evidence had 0 exact rows for NCBI 36035.
- Local StrainInfo evidence had 69 direct rows and 121 matching deposit designations for NCBI 36035.

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
