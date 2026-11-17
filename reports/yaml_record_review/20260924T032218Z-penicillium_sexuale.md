# YAML Record Review: Penicillium sexuale

- File: `data/taxa/eukaryota/penicillium_sexuale.yaml`
- Identifier: `NCBITaxon:2834232`
- Label: `Penicillium sexuale`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 562133 contains the matching current NCBI row for `NCBITaxon:2834232`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 63303 includes `NCBITaxon:2834232` with reason `attested rule: Penicillium sexuale, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sexuale.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_sclerotiorum.yaml data/taxa/eukaryota/penicillium_scottii.yaml data/taxa/eukaryota/penicillium_senticosum.yaml data/taxa/eukaryota/penicillium_sexuale.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium sp. ERA-2019d`; NCBI lists no broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium sexuale Rodr.-Andr., Cano & Stchigel, 2021`.
- `data/raw/ncbi_merged_ids.tsv` line 45689 maps old `NCBITaxon:2593317` into `NCBITaxon:2834232`, but an exact retained-row search found no `NCBITaxon:2593317` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 27424 has one aggregate GOLD row for `NCBITaxon:2834232` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `2834232`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has two exact rows for `NCBITaxon:2834232`: `FMR 17380` and `FMR:17380`, both cultures from the holotype.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `2834232`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:2834232`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:2834232`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `2834232`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:2834232`, inspect the regenerated `data/taxa/eukaryota/penicillium_sexuale.yaml`, then run `just validate data/taxa/eukaryota/penicillium_sexuale.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_sexuale.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_sexuale.md`, so the absence check included gitignored reports.
