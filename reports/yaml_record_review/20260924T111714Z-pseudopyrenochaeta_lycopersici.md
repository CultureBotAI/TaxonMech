# YAML Record Review: Pseudopyrenochaeta lycopersici

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudopyrenochaeta_lycopersici.yaml`
- Identifier: `NCBITaxon:285811`

## Target
Reviewed the complete 91-line YAML record for `Pseudopyrenochaeta lycopersici`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudopyrenochaeta_lycopersici`.

## Validation
- `just validate data/taxa/eukaryota/pseudopyrenochaeta_lycopersici.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudopyrenochaeta_lycopersici.yaml data/taxa/eukaryota/pseudorhypophila_mangenotii.yaml data/taxa/eukaryota/pseudorhypophila_marina.yaml data/taxa/eukaryota/pseudorhypophila_pilifera.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 58377 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:285811` as species `Pseudopyrenochaeta lycopersici`, with parent `NCBITaxon:2078564`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 1 exact synonym, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 54993: `attested rule: Pseudopyrenochaeta lycopersici, 2 sources incl. NCBI`.
- Seventeen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:285811`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:285811` at line 27750 with `organism_count=3`, matching the YAML GOLD source attestation.
- The native GOLD exports had 0 exact projects, 3 exact organism rows, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 5 exact rows for `NCBITaxon:285811`, lines 132983-132987: 3 culture-from-isotype rows and 2 culture-from-type-material rows.
- `data/straininfo/records.jsonl.gz` had 14 direct JSONL rows and 15 exact deposits for `NCBITaxon:285811`; the exact numeric-boundary JSONL check also counted 14 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:285811`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:285811`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:285811`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
