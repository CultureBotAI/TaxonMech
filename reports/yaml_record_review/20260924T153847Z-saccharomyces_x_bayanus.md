# YAML Record Review: Saccharomyces x bayanus

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_x_bayanus.yaml`
- Identifier: `NCBITaxon:4931`

## Target

Reviewed the complete 79-line YAML record for Saccharomyces x bayanus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_x_bayanus.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_x_bayanus.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_uvarum_clib_533.yaml data/taxa/eukaryota/saccharomyces_x_bayanus.yaml data/taxa/eukaryota/saccharomyces_x_bayanus_cbs_1502.yaml data/taxa/eukaryota/saccharomyces_x_bayanus_cbs_1542.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 2151 retains `NCBITaxon:4931` as `Saccharomyces x bayanus`, rank `SPECIES`, parent `NCBITaxon:3735051`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 51885, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 1 exact synonym, 1 related synonym, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 14 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- No rows in `data/raw/ncbi_merged_ids.tsv` map retired NCBI IDs into `NCBITaxon:4931`, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:4931` at line 37163 with `organism_count` 15, matching the YAML source assertion count.
- Native GOLD exact scans found 14 organism rows, 9 project rows, and 5 analysis rows for NCBI 4931.
- NCBI type-material evidence had 30 exact rows for `NCBITaxon:4931` at `data/raw/ncbi_type_material.tsv` lines 223341-223370.
- Local BacDive evidence had 0 exact rows for NCBI 4931.
- Local StrainInfo evidence had 204 direct rows and 368 matching deposit designations for NCBI 4931; 22 JSONL rows had only a matching deposit without a direct strain taxon match.

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
