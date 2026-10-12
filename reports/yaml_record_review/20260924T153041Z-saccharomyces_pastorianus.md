# YAML Record Review: Saccharomyces pastorianus

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_pastorianus.yaml`
- Identifier: `NCBITaxon:27292`

## Target

Reviewed the complete 91-line YAML record for Saccharomyces pastorianus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_pastorianus.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_pastorianus.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_paradoxus_nrrl_y_17217.yaml data/taxa/eukaryota/saccharomyces_pastorianus.yaml data/taxa/eukaryota/saccharomyces_pastorianus_cbs_1503.yaml data/taxa/eukaryota/saccharomyces_pastorianus_cbs_1513.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 2708 retains `NCBITaxon:27292` as `Saccharomyces pastorianus`, rank `SPECIES`, parent `NCBITaxon:4930`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 52132, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 3 exact synonyms, 4 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:55189` and `NCBITaxon:571644` to `NCBITaxon:27292` at lines 85828 and 86817. Exact searches of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:27292` at line 25395 with `organism_count` 14, matching the YAML source assertion count.
- Native GOLD exact scans found 14 organism rows, 17 project rows, and 16 analysis rows for NCBI 27292.
- NCBI type-material evidence had 39 exact rows for `NCBITaxon:27292` at `data/raw/ncbi_type_material.tsv` lines 114474-114512.
- Local BacDive evidence had 0 exact rows for NCBI 27292.
- Local StrainInfo evidence had 249 direct rows and 378 matching deposit designations for NCBI 27292; 25 JSONL rows had only a matching deposit without a direct strain taxon match.

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
