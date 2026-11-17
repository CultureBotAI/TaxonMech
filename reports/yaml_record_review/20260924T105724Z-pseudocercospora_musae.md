# YAML Record Review: Pseudocercospora musae

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudocercospora_musae.yaml`
- Identifier: `NCBITaxon:113226`

## Target
Reviewed the complete 93-line YAML record for `Pseudocercospora musae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudocercospora_musae`.

## Validation
- `just validate data/taxa/eukaryota/pseudocercospora_musae.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudocercospora_fijiensis_cirad86.yaml data/taxa/eukaryota/pseudocercospora_fuligena.yaml data/taxa/eukaryota/pseudocercospora_musae.yaml data/taxa/eukaryota/pseudocercospora_ulei.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 20592 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:113226` as species `Pseudocercospora musae`, with parent `NCBITaxon:131324`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 2 exact synonyms, 3 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 53790: `attested rule: Pseudocercospora musae, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:113226`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:113226` at line 2694 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 1 exact project, 1 exact organism row, and 1 exact analysis for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:113226`.
- `data/straininfo/records.jsonl.gz` had 7 direct JSONL rows and 9 exact deposits for `NCBITaxon:113226`; the exact numeric-boundary JSONL check also counted 7 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:113226`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:113226`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:113226`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
