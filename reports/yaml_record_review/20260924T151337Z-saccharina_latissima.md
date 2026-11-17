# YAML Record Review: Saccharina latissima

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharina_latissima.yaml`
- Identifier: `NCBITaxon:309358`

## Target

Reviewed the complete 79-line YAML record for Saccharina latissima. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharina_latissima.

## Validation

- `just validate data/taxa/eukaryota/saccharina_latissima.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharina_japonica.yaml data/taxa/eukaryota/saccharina_latissima.yaml data/taxa/eukaryota/saccharomyces_cerevisiae.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_by4743.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 63286 retains `NCBITaxon:309358` as `Saccharina latissima`, rank `SPECIES`, parent `NCBITaxon:309357`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 55120, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 3 exact synonyms, 2 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 11 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:33638` to `NCBITaxon:309358` at line 68613. An exact search of `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:33638`, so no `replaces` entry is expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:309358` at line 31260 with `organism_count` 2, matching the YAML source assertion count.
- Native GOLD exact scans found 0 organism rows, 0 project rows, and 0 analysis rows for NCBI 309358.
- NCBI type-material evidence had 0 exact rows for `NCBITaxon:309358`.
- Local BacDive evidence had 0 exact rows for NCBI 309358.
- Local StrainInfo evidence had 1 direct row and 1 matching deposit designation for NCBI 309358; both resolve to SI-ID 345011 at JSONL line 270843, DOI `10.60712/SI-ID345011.1`, and deposit `CCAP 1321/3`.

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
