# YAML Record Review: Pseudoperonospora humuli

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudoperonospora_humuli.yaml`
- Identifier: `NCBITaxon:162120`

## Target
Reviewed the complete 59-line YAML record for `Pseudoperonospora humuli`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudoperonospora_humuli`.

## Validation
- `just validate data/taxa/eukaryota/pseudoperonospora_humuli.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudoneurospora_amorphoporcata.yaml data/taxa/eukaryota/pseudopedinella_elastica.yaml data/taxa/eukaryota/pseudoperonospora_humuli.yaml data/taxa/eukaryota/pseudophaeomoniella_oleicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 33352 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:162120` as species `Pseudoperonospora humuli`, with parent `NCBITaxon:143452`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 0 exact synonyms, 0 related synonyms, and 0 broad synonyms, matching the absent YAML synonym block.
- The seed-scope table had exactly one target row at line 54189: `attested rule: Pseudoperonospora humuli, 2 sources incl. NCBI`.
- Ten lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:162120`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:162120` at line 13877 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 1 exact project, 1 exact organism row, and 1 exact analysis for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:162120`.
- `data/straininfo/records.jsonl.gz` had 0 direct JSONL rows and 0 exact deposits for `NCBITaxon:162120`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:162120`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:162120`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:162120`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
