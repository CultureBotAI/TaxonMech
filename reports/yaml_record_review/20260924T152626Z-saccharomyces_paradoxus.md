# YAML Record Review: Saccharomyces paradoxus

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_paradoxus.yaml`
- Identifier: `NCBITaxon:27291`

## Target

Reviewed the complete 73-line YAML record for Saccharomyces paradoxus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_paradoxus.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_paradoxus.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharomyces_eubayanus.yaml data/taxa/eukaryota/saccharomyces_jurei.yaml data/taxa/eukaryota/saccharomyces_kudriavzevii.yaml data/taxa/eukaryota/saccharomyces_paradoxus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 2707 retains `NCBITaxon:27291` as `Saccharomyces paradoxus`, rank `SPECIES`, parent `NCBITaxon:4930`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 52131, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 0 exact synonyms, 1 related synonym, and 0 broad synonyms; the YAML synonym block matches that source count.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- No rows in `data/raw/ncbi_merged_ids.tsv` map retired NCBI IDs into `NCBITaxon:27291`, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:27291` at line 25384 with `organism_count` 35, matching the YAML source assertion count.
- Native GOLD exact scans found 35 organism rows, 38 project rows, and 4 analysis rows for NCBI 27291.
- NCBI type-material evidence had 49 exact rows for `NCBITaxon:27291` at `data/raw/ncbi_type_material.tsv` lines 114353-114401.
- Local BacDive evidence had 0 exact rows for NCBI 27291.
- Local StrainInfo evidence had 84 direct rows and 138 matching deposit designations for NCBI 27291; 3 JSONL rows had only a matching deposit without a direct strain taxon match.

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
