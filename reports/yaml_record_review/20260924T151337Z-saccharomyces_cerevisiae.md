# YAML Record Review: Saccharomyces cerevisiae

- Verdict: pass
- Target: `data/taxa/eukaryota/saccharomyces_cerevisiae.yaml`
- Identifier: `NCBITaxon:4932`

## Target

Reviewed the complete 122-line YAML record for Saccharomyces cerevisiae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for saccharomyces_cerevisiae.

## Validation

- `just validate data/taxa/eukaryota/saccharomyces_cerevisiae.yaml` exited successfully and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/saccharina_japonica.yaml data/taxa/eukaryota/saccharina_latissima.yaml data/taxa/eukaryota/saccharomyces_cerevisiae.yaml data/taxa/eukaryota/saccharomyces_cerevisiae_by4743.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- NCBI row 2152 retains `NCBITaxon:4932` as `Saccharomyces cerevisiae`, rank `SPECIES`, parent `NCBITaxon:4930`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The target appears once in `curation/seed_scope.tsv` at line 51886, which keeps it in scope for the seeded eukaryote review set.
- The NCBI row supplies 11 exact synonyms, 6 related synonyms, and 0 broad synonyms; the YAML synonym blocks match those source counts.
- All 13 lineage identifiers resolved to current NCBI rows, with no missing rows and no parent-label mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:252598`, `NCBITaxon:2898199`, and `NCBITaxon:41870` to `NCBITaxon:4932` at lines 43916, 56665, and 76803. Exact searches of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- The generated GOLD aggregate has one exact `data/raw/gold_organisms.tsv` row for `NCBITaxon:4932` at line 37165 with `organism_count` 884, matching the YAML source assertion count.
- Native GOLD exact scans found 849 organism rows, 1229 project rows, and 756 analysis rows for NCBI 4932.
- NCBI type-material evidence had 7 exact rows for `NCBITaxon:4932` at `data/raw/ncbi_type_material.tsv` lines 223391-223397; those rows cover the Mycoderma cerevisiae designations `ATCC 18824`, `ATCC:18824`, `CBS 1171`, `CBS:1171`, `NRRL Y-12632`, `NRRL:Y-12632`, and `NRRL:Y:12632`.
- Local BacDive evidence had 0 exact rows for NCBI 4932.
- Local StrainInfo evidence had 7783 direct rows and 9481 matching deposit designations for NCBI 4932; 66 JSONL rows had only a matching deposit without a direct strain taxon match.

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
