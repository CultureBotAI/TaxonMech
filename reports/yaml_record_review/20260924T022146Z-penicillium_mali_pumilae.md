# YAML Record Review: Penicillium mali-pumilae

- File: `data/taxa/eukaryota/penicillium_mali_pumilae.yaml`
- Identifier: `NCBITaxon:2607994`
- Label: `Penicillium mali-pumilae`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 536490 contains the matching current NCBI row for `NCBITaxon:2607994`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 62902 includes `NCBITaxon:2607994` with reason `attested rule: Penicillium mali-pumilae, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_mali_pumilae.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_magnielliptisporum.yaml data/taxa/eukaryota/penicillium_majusculum.yaml data/taxa/eukaryota/penicillium_malachiteum.yaml data/taxa/eukaryota/penicillium_mali_pumilae.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium mali-pumilae Hyang B. Lee, T.T.T. Nguyen & Houbraken, 2019` and `Penicillium sp. HBL-2015b`.
- `data/raw/ncbi_merged_ids.tsv` line 23362 maps old id `NCBITaxon:1656272` into `NCBITaxon:2607994`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:1656272`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 24046 has one aggregate GOLD row for `NCBITaxon:2607994` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `2607994`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has two exact rows for `NCBITaxon:2607994`: `CBS H-22503` and `CBS:H-22503`.
- StrainInfo has four direct exact records and four deposits for NCBI taxon `2607994`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:2607994`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:2607994`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `2607994`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:2607994`, inspect the regenerated `data/taxa/eukaryota/penicillium_mali_pumilae.yaml`, then run `just validate data/taxa/eukaryota/penicillium_mali_pumilae.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_mali_pumilae.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_mali_pumilae.md`, so the absence check included gitignored reports.
