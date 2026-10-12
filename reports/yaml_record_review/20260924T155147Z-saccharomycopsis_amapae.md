# YAML Record Review: Saccharomycopsis amapae

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycopsis_amapae.yaml`
- Identifier: `NCBITaxon:51913`

## Target

Reviewed the complete 83-line YAML record for Saccharomycopsis amapae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycopsis_amapae.

## Validation

- `just validate data/taxa/eukaryota/saccharomycopsis_amapae.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycodes_ludwigii.yaml data/taxa/eukaryota/saccharomycopsis_amapae.yaml data/taxa/eukaryota/saccharomycopsis_babjevae.yaml data/taxa/eukaryota/saccharomycopsis_capsularis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 6523 retains `NCBITaxon:51913` as `Saccharomycopsis amapae`, rank `SPECIES`, parent `NCBITaxon:4943`, genetic code `12`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 52840, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 1 exact synonym, 3 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:1470811` to `NCBITaxon:51913` at line 16975. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:1470811`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:51913` at line 37681 with `organism_count` 1, matching the YAML source assertion count.
- Native GOLD exact scans found 1 organism row, 1 project row, and 0 analysis rows for NCBI 51913.
- NCBI type-material evidence had 15 exact rows for `NCBITaxon:51913` at `data/raw/ncbi_type_material.tsv` lines 227105-227119.
- Local BacDive evidence had 0 exact rows for NCBI 51913.
- Local StrainInfo evidence had 2 direct rows and 9 matching deposit designations for NCBI 51913.

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
