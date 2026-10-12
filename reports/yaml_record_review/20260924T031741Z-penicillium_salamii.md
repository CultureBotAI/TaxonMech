# YAML Record Review: Penicillium salamii

- File: `data/taxa/eukaryota/penicillium_salamii.yaml`
- Identifier: `NCBITaxon:1612424`
- Label: `Penicillium salamii`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 416409 contains the matching current NCBI row for `NCBITaxon:1612424`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 60572 includes `NCBITaxon:1612424` with reason `attested rule: Penicillium salamii, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_salamii.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_salamii.yaml data/taxa/eukaryota/penicillium_samsonianum.yaml data/taxa/eukaryota/penicillium_sanguifluum.yaml data/taxa/eukaryota/penicillium_sclerotigenum.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium salamii Perrone, Frisvad, Samson & Houbraken, 2015`; NCBI lists no broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium sp. AS-2013` and `Penicillium sp. GP-2014`.
- `data/raw/ncbi_merged_ids.tsv` lines 15008 and 19398 map old `NCBITaxon:1406945` and `NCBITaxon:1540422` into `NCBITaxon:1612424`, but an exact retained-row search found neither old ID in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 13080 has one aggregate GOLD row for `NCBITaxon:1612424` with `organism_count: 1`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `1612424`: 1 unique `data/gold/organisms.jsonl.gz` organism and 2 joined GOLD projects. No joined GOLD analyses were found, and no exact generated strain rows were emitted from GOLD.
- `data/raw/ncbi_type_material.tsv` has eight exact rows for `NCBITaxon:1612424`: `CBS 135391`, `CBS:135391`, `DTO 198-E1`, `DTO:198-E1`, `ITEM 15291`, and `ITEM:15291` are cultures from the holotype, and `CBS H-21341` and `CBS:H:21341` are holotypes.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `1612424`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1612424`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1612424`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1612424`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1612424`, inspect the regenerated `data/taxa/eukaryota/penicillium_salamii.yaml`, then run `just validate data/taxa/eukaryota/penicillium_salamii.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_salamii.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_salamii.md`, so the absence check included gitignored reports.
