# YAML Record Review: Pseudoinonotus dryadeus

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudoinonotus_dryadeus.yaml`
- Identifier: `NCBITaxon:167352`

## Target
Reviewed the complete 81-line YAML record for `Pseudoinonotus dryadeus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudoinonotus_dryadeus`.

## Validation
- `just validate data/taxa/eukaryota/pseudoinonotus_dryadeus.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudoinonotus_dryadeus.yaml data/taxa/eukaryota/pseudokeronopsis_carnea.yaml data/taxa/eukaryota/pseudokeronopsis_flava.yaml data/taxa/eukaryota/pseudoloma_neurophilia.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 34259 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:167352` as species `Pseudoinonotus dryadeus`, with parent `NCBITaxon:218108`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 2 exact synonyms, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 54231: `attested rule: Pseudoinonotus dryadeus, 2 sources incl. NCBI`.
- Thirteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:167352`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:167352` at line 14389 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 1 exact project, 1 exact organism row, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:167352`.
- `data/straininfo/records.jsonl.gz` had 6 direct JSONL rows and 7 exact deposits for `NCBITaxon:167352`; the exact numeric-boundary JSONL check also counted 6 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:167352`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:167352`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:167352`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
