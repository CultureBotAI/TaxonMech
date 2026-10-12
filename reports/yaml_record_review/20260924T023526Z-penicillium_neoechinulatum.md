# YAML Record Review: Penicillium neoechinulatum

- File: `data/taxa/eukaryota/penicillium_neoechinulatum.yaml`
- Identifier: `NCBITaxon:133748`
- Label: `Penicillium neoechinulatum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 26125 contains the matching current NCBI row for `NCBITaxon:133748`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53958 includes `NCBITaxon:133748` with reason `attested rule: Penicillium neoechinulatum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_neoechinulatum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_neocrassum.yaml data/taxa/eukaryota/penicillium_neoechinulatum.yaml data/taxa/eukaryota/penicillium_neoherquei.yaml data/taxa/eukaryota/penicillium_nodulum.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium aurantiogriseum var. neoechinulatum`.
- The related synonyms in YAML exactly match the NCBI related synonyms: `Penicillium aurantiogriseum var. neoechinulatum Frisvad, Filt. & Wicklow, 1987` and `Penicillium neoechinulatum (Frisvad, Filt. & Wicklow) Frisvad & Samson, 2004`.
- `data/raw/ncbi_merged_ids.tsv` line 88399 maps old id `NCBITaxon:60173` into `NCBITaxon:133748`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:60173`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 8185 has one aggregate GOLD row for `NCBITaxon:133748` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `133748`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has thirteen exact rows for `NCBITaxon:133748`: `CBS 169.87`, `CBS:169.87`, `IBT 21537`, `IBT 3493`, `IBT:21537`, `IBT:3493`, `IMI 296937`, `IMI:296937`, `NRRL 13486`, `NRRL A-27178`, `NRRL:13486`, `NRRL:A:27178`, and `NRRL:MOLD:A-27178`.
- StrainInfo has 19 direct exact records and 28 deposits for NCBI taxon `133748`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:133748`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:133748`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `133748`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:133748`, inspect the regenerated `data/taxa/eukaryota/penicillium_neoechinulatum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_neoechinulatum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_neoechinulatum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_neoechinulatum.md`, so the absence check included gitignored reports.
