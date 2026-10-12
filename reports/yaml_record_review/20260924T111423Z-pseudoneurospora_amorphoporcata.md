# YAML Record Review: Pseudoneurospora amorphoporcata

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudoneurospora_amorphoporcata.yaml`
- Identifier: `NCBITaxon:241081`

## Target
Reviewed the complete 88-line YAML record for `Pseudoneurospora amorphoporcata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudoneurospora_amorphoporcata`.

## Validation
- `just validate data/taxa/eukaryota/pseudoneurospora_amorphoporcata.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudoneurospora_amorphoporcata.yaml data/taxa/eukaryota/pseudopedinella_elastica.yaml data/taxa/eukaryota/pseudoperonospora_humuli.yaml data/taxa/eukaryota/pseudophaeomoniella_oleicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 47349 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:241081` as species `Pseudoneurospora amorphoporcata`, with parent `NCBITaxon:241080`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 1 exact synonym, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 54708: `attested rule: Pseudoneurospora amorphoporcata, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:241081`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:241081` at line 22002 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 1 exact organism row, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:241081`.
- `data/straininfo/records.jsonl.gz` had 1 direct JSONL row and 1 exact deposit for `NCBITaxon:241081`: siID 176818 at line 128947 with deposit `CBS 626.80`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:241081`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:241081`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:241081`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
