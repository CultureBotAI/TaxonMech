# YAML Record Review: Pseudocercospora fijiensis CIRAD86

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudocercospora_fijiensis_cirad86.yaml`
- Identifier: `NCBITaxon:383855`

## Target
Reviewed the complete 87-line YAML record for `Pseudocercospora fijiensis CIRAD86`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudocercospora_fijiensis_cirad86`.

## Validation
- `just validate data/taxa/eukaryota/pseudocercospora_fijiensis_cirad86.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudocercospora_fijiensis_cirad86.yaml data/taxa/eukaryota/pseudocercospora_fuligena.yaml data/taxa/eukaryota/pseudocercospora_musae.yaml data/taxa/eukaryota/pseudocercospora_ulei.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 80597 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:383855` as strain `Pseudocercospora fijiensis CIRAD86`, with parent `NCBITaxon:1873960`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 2 exact synonyms, 0 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 55456: `attested rule: Pseudocercospora fijiensis CIRAD86, 2 sources incl. NCBI`.
- Seventeen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:383855`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:383855` at line 33974 with `organism_count=8`, matching the YAML GOLD source attestation.
- The native GOLD exports had 0 exact projects, 0 exact organism rows, and 0 exact analyses for this strain ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:383855`.
- `data/straininfo/records.jsonl.gz` had 0 direct JSONL rows and 0 exact deposits for `NCBITaxon:383855`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:383855`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:383855`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:383855`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
