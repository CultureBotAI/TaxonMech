# YAML Record Review: Saccharomyces cerevisiae x Saccharomyces eubayanus x Saccharomyces kudriavzevii x Saccharomyces uvarum

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_cerevisiae_x_saccharomyces_eubayanus_x_saccharomyces_kudri.yaml`
- Identifier: `NCBITaxon:2528333`

## Target

Reviewed the complete 75-line YAML record for Saccharomyces cerevisiae x Saccharomyces eubayanus x Saccharomyces kudriavzevii x Saccharomyces uvarum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_cerevisiae_x_saccharomyces_eubayanus_x_saccharomyces_kudri.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_cerevisiae_x_saccharomyces_eubayanus_x_saccharomyces_kudri.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_cerevisiae_x_saccharomyces_eubayanus_x_saccharomyces_kudri.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_x_saccharomyces_kudriavzevii_x_saccharomyces_uv.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_x_saccharomyces_paradoxus.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_yb210.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 529424 retains `NCBITaxon:2528333` as `Saccharomyces cerevisiae x Saccharomyces eubayanus x Saccharomyces kudriavzevii x Saccharomyces uvarum`, rank `SPECIES`, parent `NCBITaxon:3735051`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 62765, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 0 exact synonyms, 0 related synonyms, and 0 broad synonyms; the YAML absence of synonym blocks matches those source counts.
- All 14 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- No rows in `data/raw/ncbi_merged_ids.tsv` map retired NCBI IDs into `NCBITaxon:2528333`, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:2528333` at line 23028 with `organism_count` 4, matching the YAML source assertion count.
- Native GOLD exact scans found 0 organism rows, 0 project rows, and 0 analysis rows for NCBI 2528333.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:2528333`.
- Local BacDive evidence had 0 exact rows for NCBI 2528333.
- Local StrainInfo evidence had 0 direct rows and 0 matching deposit designations for NCBI 2528333.

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
