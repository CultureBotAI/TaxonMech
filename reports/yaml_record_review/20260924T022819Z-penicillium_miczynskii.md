# YAML Record Review: Penicillium miczynskii

- File: `data/taxa/eukaryota/penicillium_miczynskii.yaml`
- Identifier: `NCBITaxon:36645`
- Label: `Penicillium miczynskii`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 4084 contains the matching current NCBI row for `NCBITaxon:36645`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 52341 includes `NCBITaxon:36645` with reason `attested rule: Penicillium miczynskii, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_miczynskii.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_mediterraneum.yaml data/taxa/eukaryota/penicillium_melanoconidium.yaml data/taxa/eukaryota/penicillium_mexicanum.yaml data/taxa/eukaryota/penicillium_miczynskii.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium miczynskii K.M. Zalessky, 1927` and `Penicillium miczynskii K.W. Zaleski, 1927`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:36645`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 33426 has one aggregate GOLD row for `NCBITaxon:36645` with `organism_count: 10`, matching the GOLD source attestation.
- Native GOLD contains ten exact organisms for NCBI taxon `36645`, including `Go0607936` through `Go0607940` in the bounded sample, and zero joined GOLD projects or analyses.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:36645`: `CBS 220.28`, `CBS:220.28`, `FRR 1077`, and `FRR:1077`.
- StrainInfo has 37 direct exact records and 78 deposits for NCBI taxon `36645`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:36645`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:36645`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `36645`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:36645`, inspect the regenerated `data/taxa/eukaryota/penicillium_miczynskii.yaml`, then run `just validate data/taxa/eukaryota/penicillium_miczynskii.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_miczynskii.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_miczynskii.md`, so the absence check included gitignored reports.
