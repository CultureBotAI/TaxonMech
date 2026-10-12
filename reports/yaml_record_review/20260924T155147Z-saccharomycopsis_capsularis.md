# YAML Record Review: Saccharomycopsis capsularis

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycopsis_capsularis.yaml`
- Identifier: `NCBITaxon:36036`

## Target

Reviewed the complete 72-line YAML record for Saccharomycopsis capsularis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycopsis_capsularis.

## Validation

- `just validate data/taxa/eukaryota/saccharomycopsis_capsularis.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycodes_ludwigii.yaml data/taxa/eukaryota/saccharomycopsis_amapae.yaml data/taxa/eukaryota/saccharomycopsis_babjevae.yaml data/taxa/eukaryota/saccharomycopsis_capsularis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 4046 retains `NCBITaxon:36036` as `Saccharomycopsis capsularis`, rank `SPECIES`, parent `NCBITaxon:4943`, genetic code `12`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 52314, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 0 exact synonyms, 1 related synonym, and 0 broad synonyms; the YAML synonym block matches that source count.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- No rows in `data/raw/ncbi_merged_ids.tsv` map retired NCBI IDs into `NCBITaxon:36036`, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:36036` at line 33258 with `organism_count` 1, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 1 project row, and 0 analysis rows for NCBI 36036.
- NCBI type-material evidence had 10 exact rows for `NCBITaxon:36036` at `data/raw/ncbi_type_material.tsv` lines 193777-193786.
- Local BacDive evidence had 0 exact rows for NCBI 36036.
- Local StrainInfo evidence had 15 direct rows and 51 matching deposit designations for NCBI 36036.

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
