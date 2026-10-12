# YAML Record Review: Penicillium polonicum

- File: `data/taxa/eukaryota/penicillium_polonicum.yaml`
- Identifier: `NCBITaxon:60169`
- Label: `Penicillium polonicum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 7581 contains the matching current NCBI row for `NCBITaxon:60169`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53013 includes `NCBITaxon:60169` with reason `attested rule: Penicillium polonicum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_polonicum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_polonicum.yaml data/taxa/eukaryota/penicillium_psychrotrophicum.yaml` scanned 2 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The two exact synonyms in YAML exactly match the pipe-delimited NCBI exact synonyms: `Penicillium aurantiogriseum var. polonicum` and `Penicillium polonicum K.M. Zalessky, 1927`.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium aurantiogriseum var. polonicum (W.Zalessky) Frisvad & Filt`; NCBI lists no broad synonyms for the target row.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:60169`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 39771 has one aggregate GOLD row for `NCBITaxon:60169` with `organism_count: 7`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `60169`: 7 unique `data/gold/organisms.jsonl.gz` organisms, 9 joined GOLD projects, and 5 joined GOLD analyses. None of those native GOLD rows emitted exact generated strain rows because they did not join to a BacDive-derived local strain inventory entry.
- `data/raw/ncbi_type_material.tsv` has ten exact rows for `NCBITaxon:60169`: `CBS 222.28`, `CBS:222.28`, `IBT 12821`, `IBT:12821`, `IMI 291194`, `IMI:291194`, `MUCL 29204`, `MUCL:29204`, `NRRL 995`, and `NRRL:995`.
- StrainInfo has 41 direct exact records and 58 deposits for NCBI taxon `60169`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:60169`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:60169`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `60169`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:60169`, inspect the regenerated `data/taxa/eukaryota/penicillium_polonicum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_polonicum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_polonicum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_polonicum.md`, so the absence check included gitignored reports.
