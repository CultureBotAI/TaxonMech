# YAML Record Review: Pseudopedinella elastica

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudopedinella_elastica.yaml`
- Identifier: `NCBITaxon:35684`

## Target
Reviewed the complete 60-line YAML record for `Pseudopedinella elastica`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudopedinella_elastica`.

## Validation
- `just validate data/taxa/eukaryota/pseudopedinella_elastica.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudoneurospora_amorphoporcata.yaml data/taxa/eukaryota/pseudopedinella_elastica.yaml data/taxa/eukaryota/pseudoperonospora_humuli.yaml data/taxa/eukaryota/pseudophaeomoniella_oleicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 3923 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:35684` as species `Pseudopedinella elastica`, with parent `NCBITaxon:35683`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 0 exact synonyms, 1 related synonym, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 52292: `attested rule: Pseudopedinella elastica, 2 sources incl. NCBI`.
- Nine lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:35684`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:35684` at line 33108 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 0 exact projects, 1 exact organism row, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:35684`.
- `data/straininfo/records.jsonl.gz` had 2 direct JSONL rows and 3 exact deposits for `NCBITaxon:35684`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:35684`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:35684`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:35684`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
