# YAML Record Review: Penicillium paneum

- File: `data/taxa/eukaryota/penicillium_paneum.yaml`
- Identifier: `NCBITaxon:68879`
- Label: `Penicillium paneum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9429 contains the matching current NCBI row for `NCBITaxon:68879`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53173 includes `NCBITaxon:68879` with reason `attested rule: Penicillium paneum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_paneum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_palitans.yaml data/taxa/eukaryota/penicillium_pancosmium.yaml data/taxa/eukaryota/penicillium_paneum.yaml data/taxa/eukaryota/penicillium_paraherquei.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The 12 related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium paneum Frisvad, 1996`, `Penicillium paneum JCM 28552`, `Penicillium paneum JCM 28570`, `Penicillium sp. JCM 28094`, `Penicillium sp. JCM 28111`, `Penicillium sp. JCM 28398`, `Penicillium sp. JCM 28410`, `Penicillium sp. JCM 28488`, `Penicillium sp. JCM 28508`, `Penicillium sp. JCM 28552`, `Penicillium sp. JCM 28570`, and `fungal sp. JCM 28412`.
- `data/raw/ncbi_merged_ids.tsv` maps nine old IDs into `NCBITaxon:68879` at lines 29071, 29072, 29074, 29077, 29080, 29083, 29084, 29085, and 33516, but an exact retained-row search found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41373 has one aggregate GOLD row for `NCBITaxon:68879` with `organism_count: 10`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `68879`: 10 unique `data/gold/organisms.jsonl.gz` organisms, 13 joined GOLD projects, and 8 joined GOLD analyses. None of those native GOLD rows emitted exact generated strain rows because they did not join to a BacDive-derived local strain inventory entry.
- `data/raw/ncbi_type_material.tsv` has six exact rows for `NCBITaxon:68879`: `CBS 101032`, `CBS:101032`, `IBT 12407`, `IBT 21541`, `IBT:12407`, and `IBT:21541`.
- StrainInfo has 27 direct exact records and 31 deposits for NCBI taxon `68879`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:68879`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:68879`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `68879`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:68879`, inspect the regenerated `data/taxa/eukaryota/penicillium_paneum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_paneum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_paneum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_paneum.md`, so the absence check included gitignored reports.
