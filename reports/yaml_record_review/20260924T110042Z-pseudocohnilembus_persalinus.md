# YAML Record Review: Pseudocohnilembus persalinus

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudocohnilembus_persalinus.yaml`
- Identifier: `NCBITaxon:266149`

## Target
Reviewed the complete 69-line YAML record for `Pseudocohnilembus persalinus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudocohnilembus_persalinus`.

## Validation
- `just validate data/taxa/eukaryota/pseudocohnilembus_persalinus.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudocercospora_vitis.yaml data/taxa/eukaryota/pseudocohnilembus_persalinus.yaml data/taxa/eukaryota/pseudocosmospora_vilior.yaml data/taxa/eukaryota/pseudoechria_curvicolla.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 54607 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:266149` as species `Pseudocohnilembus persalinus`, with parent `NCBITaxon:35103`, genetic code `6`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 0 exact synonyms, 1 related synonym, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 54892: `attested rule: Pseudocohnilembus persalinus, 2 sources incl. NCBI`.
- Twelve lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:266149`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:266149` at line 24417 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 1 exact project, 1 exact organism row, and 1 exact analysis for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:266149`.
- `data/straininfo/records.jsonl.gz` had 0 direct JSONL rows and 0 exact deposits for `NCBITaxon:266149`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:266149`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:266149`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:266149`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
