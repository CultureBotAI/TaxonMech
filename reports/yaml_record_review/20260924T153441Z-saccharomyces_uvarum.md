# YAML Record Review: Saccharomyces uvarum

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_uvarum.yaml`
- Identifier: `NCBITaxon:230603`

## Target

Reviewed the complete 91-line YAML record for Saccharomyces uvarum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_uvarum.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_uvarum.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_pastorianus_cbs_6283.yaml data/taxa/eukaryota/saccharomyces_sp_edrl.yaml data/taxa/eukaryota/saccharomyces_sp_m14.yaml data/taxa/eukaryota/saccharomyces_uvarum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 45312 retains `NCBITaxon:230603` as `Saccharomyces uvarum`, rank `SPECIES`, parent `NCBITaxon:4930`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 54643, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 4 exact synonyms, 3 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:27290` to `NCBITaxon:230603` at line 49642. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:27290`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:230603` at line 21622 with `organism_count` 22, matching the YAML source assertion count.
- Native GOLD exact scans found 22 organism rows, 22 project rows, and 22 analysis rows for NCBI 230603.
- NCBI type-material evidence had 65 exact rows for `NCBITaxon:230603` at `data/raw/ncbi_type_material.tsv` lines 92215-92279.
- Local BacDive evidence had 0 exact rows for NCBI 230603.
- Local StrainInfo evidence had 146 direct rows and 172 matching deposit designations for NCBI 230603; 9 JSONL rows had only a matching deposit without a direct strain taxon match.

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
