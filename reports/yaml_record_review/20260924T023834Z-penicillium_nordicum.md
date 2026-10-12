# YAML Record Review: Penicillium nordicum

- File: `data/taxa/eukaryota/penicillium_nordicum.yaml`
- Identifier: `NCBITaxon:229535`
- Label: `Penicillium nordicum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 44996 contains the matching current NCBI row for `NCBITaxon:229535`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 54637 includes `NCBITaxon:229535` with reason `attested rule: Penicillium nordicum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_nordicum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_nordicum.yaml data/taxa/eukaryota/penicillium_novae_zeelandiae.yaml data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml data/taxa/eukaryota/penicillium_onobense.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The one related synonym in YAML exactly matches the NCBI related synonym: `Penicillium nordicum Dragoni & Cantoni ex C. Ramirez, 1985`.
- `data/raw/ncbi_merged_ids.tsv` line 34648 maps old id `NCBITaxon:2006377` into `NCBITaxon:229535`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:2006377`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 21548 has one aggregate GOLD row for `NCBITaxon:229535` with `organism_count: 2`, matching the GOLD source attestation.
- Native GOLD contains two exact organisms for NCBI taxon `229535`: `Go0090030` / `Gp0090030` for strain `BFE487`, and `Go0140093` / `Gp0145191` for strain `DAOMC 185683`; two joined analysis rows carry those project ids.
- `data/raw/ncbi_type_material.tsv` has eight exact rows for `NCBITaxon:229535`: `ATCC 44219`, `ATCC-44219`, `ATCC44219`, `ATCC:44219`, `IBT 13307`, `IBT-13307`, `IBT13307`, and `IBT:13307`.
- StrainInfo has ten direct exact records and twelve deposits for NCBI taxon `229535`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:229535`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:229535`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `229535`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:229535`, inspect the regenerated `data/taxa/eukaryota/penicillium_nordicum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_nordicum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_nordicum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_nordicum.md`, so the absence check included gitignored reports.
