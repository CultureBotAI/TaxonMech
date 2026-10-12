# YAML Record Review: Penicillium repenticola

- File: `data/taxa/eukaryota/penicillium_repenticola.yaml`
- Identifier: `NCBITaxon:1699866`
- Label: `Penicillium repenticola`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 442283 contains the matching current NCBI row for `NCBITaxon:1699866`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 61073 includes `NCBITaxon:1699866` with reason `attested rule: Penicillium repenticola, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_repenticola.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_raperi.yaml data/taxa/eukaryota/penicillium_raphiae.yaml data/taxa/eukaryota/penicillium_repenticola.yaml data/taxa/eukaryota/penicillium_reticulisporum.yaml` exited successfully.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The two exact synonyms in YAML exactly match the pipe-delimited NCBI exact synonyms: `Penicillium repensicola` and `Penicillium repenticola Visagie & K. Jacobs, 2016`.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium sp. CMV-2015c` and `Penicillium sp. DTO 186-A8`; NCBI lists no broad synonyms for the target row.
- `data/raw/ncbi_merged_ids.tsv` line 23235 maps old `NCBITaxon:1651868` into `NCBITaxon:1699866`, but an exact retained-row search found no `NCBITaxon:1651868` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 14701 has one aggregate GOLD row for `NCBITaxon:1699866` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `1699866`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has ten exact rows for `NCBITaxon:1699866`: `CBS 139160`, `CBS:139160`, `CV 1495`, `CV:1495`, `DAOM 241080`, `DAOM:241080`, `DAOMC 241080`, `DAOMC:241080`, `DTO 183-B8`, and `DTO:183-B8`, all cultures from the holotype.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `1699866`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1699866`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1699866`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1699866`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1699866`, inspect the regenerated `data/taxa/eukaryota/penicillium_repenticola.yaml`, then run `just validate data/taxa/eukaryota/penicillium_repenticola.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_repenticola.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_repenticola.md`, so the absence check included gitignored reports.
