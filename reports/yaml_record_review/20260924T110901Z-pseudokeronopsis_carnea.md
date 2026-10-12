# YAML Record Review: Pseudokeronopsis carnea

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudokeronopsis_carnea.yaml`
- Identifier: `NCBITaxon:385029`

## Target
Reviewed the complete 72-line YAML record for `Pseudokeronopsis carnea`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudokeronopsis_carnea`.

## Validation
- `just validate data/taxa/eukaryota/pseudokeronopsis_carnea.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudoinonotus_dryadeus.yaml data/taxa/eukaryota/pseudokeronopsis_carnea.yaml data/taxa/eukaryota/pseudokeronopsis_flava.yaml data/taxa/eukaryota/pseudoloma_neurophilia.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 80976 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:385029` as species `Pseudokeronopsis carnea`, with parent `NCBITaxon:311385`, genetic code `6`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 1 exact synonym, 1 related synonym, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 55458: `attested rule: Pseudokeronopsis carnea, 2 sources incl. NCBI`.
- Twelve lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had one exact current-ID row: line 64034 maps old ID `NCBITaxon:311386` into `NCBITaxon:385029`; the exact two-file grep matched only `data/raw/ncbi_merged_ids.tsv`, so `NCBITaxon:311386` is not retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:385029` at line 33996 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 1 exact project, 1 exact organism row, and 1 exact analysis for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:385029`.
- `data/straininfo/records.jsonl.gz` had 0 direct JSONL rows and 0 exact deposits for `NCBITaxon:385029`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:385029`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:385029`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:385029`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
