# YAML Record Review: Saccharomycopsis fibuligera

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomycopsis_fibuligera.yaml`
- Identifier: `NCBITaxon:4944`

## Target

Reviewed the complete 91-line YAML record for Saccharomycopsis fibuligera. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomycopsis_fibuligera.

## Validation

- `just validate data/taxa/eukaryota/saccharomycopsis_fibuligera.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomycopsis_crataegensis.yaml data/taxa/eukaryota/saccharomycopsis_fermentans.yaml data/taxa/eukaryota/saccharomycopsis_fibuligera.yaml data/taxa/eukaryota/saccharomycopsis_fodiens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 2155 retains `NCBITaxon:4944` as `Saccharomycopsis fibuligera`, rank `SPECIES`, parent `NCBITaxon:4943`, genetic code `12`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 51888, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 4 exact synonyms, 3 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:34354` and `NCBITaxon:56149` to `NCBITaxon:4944` at lines 70549 and 86392. Exact searches of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:4944` at line 37198 with `organism_count` 4, matching the YAML source assertion count.
- Native GOLD exact scans found 4 organism rows, 4 project rows, and 3 analysis rows for NCBI 4944.
- NCBI type-material evidence had 17 exact rows for `NCBITaxon:4944` at `data/raw/ncbi_type_material.tsv` lines 223878-223894.
- Local BacDive evidence had 0 exact rows for NCBI 4944.
- Local StrainInfo evidence had 77 direct rows and 188 matching deposit designations for NCBI 4944; 2 JSONL rows had only a matching deposit without a direct strain taxon match.

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
