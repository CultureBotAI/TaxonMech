# YAML Record Review: Penicillium oxalicum YT02

- File: `data/taxa/eukaryota/penicillium_oxalicum_yt02.yaml`
- Identifier: `NCBITaxon:858480`
- Label: `Penicillium oxalicum YT02`
- Verdict: pass

## Target

- The seeded record is a strain-level `EUKARYOTA` record under `NCBITaxon:69781` (`Penicillium oxalicum`).
- `data/raw/ncbitaxon_taxa.tsv` line 180527 contains the matching current NCBI row for `NCBITaxon:858480`: rank `STRAIN`, parent `NCBITaxon:69781`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 56734 includes `NCBITaxon:858480` with reason `attested rule: Penicillium oxalicum YT02, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_oxalicum_yt02.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_oxalicum_ju_a10_s.yaml data/taxa/eukaryota/penicillium_oxalicum_ju_a10_t.yaml data/taxa/eukaryota/penicillium_oxalicum_yt02.yaml data/taxa/eukaryota/penicillium_pagulum.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 16 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI strain identifier match.
- The lineage includes the expected species parent, `NCBITaxon:69781` (`Penicillium oxalicum`), between genus `NCBITaxon:5073` and the target strain.
- NCBI lists no exact, broad, or related synonyms for the target row, and the YAML correctly omits a `synonyms` block.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:858480`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 43302 has one aggregate GOLD row for `NCBITaxon:858480` with `organism_count: 1`, matching the GOLD source attestation.
- Native GOLD contains one exact organism for NCBI taxon `858480`, `Go0007270`; that organism, project `Gp0007270`, and the joined analysis row are named `Penicillium expansum YT02` while still carrying the same NCBI taxon id.
- `data/raw/ncbi_type_material.tsv` has zero exact rows for `NCBITaxon:858480`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `858480`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:858480`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:858480`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `858480`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:858480`, inspect the regenerated `data/taxa/eukaryota/penicillium_oxalicum_yt02.yaml`, then run `just validate data/taxa/eukaryota/penicillium_oxalicum_yt02.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_oxalicum_yt02.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_oxalicum_yt02.md`, so the absence check included gitignored reports.
