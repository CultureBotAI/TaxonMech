# YAML Record Review: Penicillium outeniquaense

- File: `data/taxa/eukaryota/penicillium_outeniquaense.yaml`
- Identifier: `NCBITaxon:3078879`
- Label: `Penicillium outeniquaense`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 595233 contains the matching current NCBI row for `NCBITaxon:3078879`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 63540 includes `NCBITaxon:3078879` with reason `attested rule: Penicillium outeniquaense, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_outeniquaense.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_osmophilum.yaml data/taxa/eukaryota/penicillium_outeniquaense.yaml data/taxa/eukaryota/penicillium_oxalicum.yaml data/taxa/eukaryota/penicillium_oxalicum_114_2.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium outeniquaense Visagie & Yilmaz, 2022` and `Penicillium sp. CMV-2020l`.
- `data/raw/ncbi_merged_ids.tsv` line 52274 maps old id `NCBITaxon:2796923` into `NCBITaxon:3078879`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:2796923`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 31190 has one aggregate GOLD row for `NCBITaxon:3078879` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `3078879`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has thirteen exact rows for `NCBITaxon:3078879`: `CBS 147414`, `CBS-147414`, `CBS147414`, `CBS:147414`, `CMW 56387`, `CMW-56387`, `CMW56387`, `CMW:56387`, `CN014C2`, `PREM 63218`, `PREM-63218`, `PREM63218`, and `PREM:63218`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `3078879`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:3078879`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:3078879`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `3078879`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:3078879`, inspect the regenerated `data/taxa/eukaryota/penicillium_outeniquaense.yaml`, then run `just validate data/taxa/eukaryota/penicillium_outeniquaense.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_outeniquaense.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_outeniquaense.md`, so the absence check included gitignored reports.
