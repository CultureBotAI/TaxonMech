# YAML Record Review: Penicillium mattheeae

- File: `data/taxa/eukaryota/penicillium_mattheeae.yaml`
- Identifier: `NCBITaxon:3078878`
- Label: `Penicillium mattheeae`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 595232 contains the matching current NCBI row for `NCBITaxon:3078878`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 63539 includes `NCBITaxon:3078878` with reason `attested rule: Penicillium mattheeae, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_mattheeae.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_malmesburiense.yaml data/taxa/eukaryota/penicillium_malodoratum.yaml data/taxa/eukaryota/penicillium_marinum.yaml data/taxa/eukaryota/penicillium_mattheeae.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium mattheeae Visagie & Yilmaz, 2022` and `Penicillium sp. CMV-2020m`.
- `data/raw/ncbi_merged_ids.tsv` line 52139 maps old id `NCBITaxon:2794329` into `NCBITaxon:3078878`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:2794329`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 31189 has one aggregate GOLD row for `NCBITaxon:3078878` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `3078878`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has thirteen exact rows for `NCBITaxon:3078878`: `CBS 147415`, `CBS-147415`, `CBS147415`, `CBS:147415`, `CMW 56388`, `CMW-56388`, `CMW56388`, `CMW:56388`, `CN014C5`, `PREM 63219`, `PREM-63219`, `PREM63219`, and `PREM:63219`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `3078878`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:3078878`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:3078878`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `3078878`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:3078878`, inspect the regenerated `data/taxa/eukaryota/penicillium_mattheeae.yaml`, then run `just validate data/taxa/eukaryota/penicillium_mattheeae.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_mattheeae.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_mattheeae.md`, so the absence check included gitignored reports.
