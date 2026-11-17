# YAML Record Review: Penicillium malachiteum

- File: `data/taxa/eukaryota/penicillium_malachiteum.yaml`
- Identifier: `NCBITaxon:1324776`
- Label: `Penicillium malachiteum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 315963 contains the matching current NCBI row for `NCBITaxon:1324776`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 59463 includes `NCBITaxon:1324776` with reason `attested rule: Penicillium malachiteum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_malachiteum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_magnielliptisporum.yaml data/taxa/eukaryota/penicillium_majusculum.yaml data/taxa/eukaryota/penicillium_malachiteum.yaml data/taxa/eukaryota/penicillium_mali_pumilae.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonyms in YAML exactly match the NCBI exact synonyms: `Chromocleista malachitea` and `Geosmithia malachitea`.
- The related synonyms in YAML exactly match the NCBI related synonyms: `Chromocleista malachitea Yaguchi & Udagawa, 1993`, `Geosmithia malachitea Yaguchi & Udagawa, 1993`, and `Penicillium malachiteum (Yaguchi & Udagawa) Houbraken & Samson 2011`.
- `data/raw/ncbi_merged_ids.tsv` line 92318 maps old id `NCBITaxon:68831` into `NCBITaxon:1324776`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:68831`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 7900 has one aggregate GOLD row for `NCBITaxon:1324776` with `organism_count: 2`, matching the GOLD source attestation.
- Native GOLD contains two exact organisms for NCBI taxon `1324776`: `Go0679387` / `Gp0781375` for strain `IBT 13176`, and `Go0679388` / `Gp0781376` for strain `IBT 17514`; two joined analysis rows carry those project ids.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:1324776`: `CBS 647.95`, `CBS:647.95`, `IBT 17515`, and `IBT:17515`.
- StrainInfo has three direct exact records and four deposits for NCBI taxon `1324776`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1324776`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1324776`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1324776`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1324776`, inspect the regenerated `data/taxa/eukaryota/penicillium_malachiteum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_malachiteum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_malachiteum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_malachiteum.md`, so the absence check included gitignored reports.
