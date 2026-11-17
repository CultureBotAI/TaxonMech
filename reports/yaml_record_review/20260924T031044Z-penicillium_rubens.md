# YAML Record Review: Penicillium rubens

- File: `data/taxa/eukaryota/penicillium_rubens.yaml`
- Identifier: `NCBITaxon:1108849`
- Label: `Penicillium rubens`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under the no-rank `NCBITaxon:254878` (`Penicillium chrysogenum species complex`) parent within `Penicillium`.
- `data/raw/ncbitaxon_taxa.tsv` line 237696 contains the matching current NCBI row for `NCBITaxon:1108849`: rank `SPECIES`, parent `NCBITaxon:254878`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 57662 includes `NCBITaxon:1108849` with reason `attested rule: Penicillium rubens, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_rubens.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_roseoviride.yaml data/taxa/eukaryota/penicillium_rubefaciens.yaml data/taxa/eukaryota/penicillium_rubens.yaml data/taxa/eukaryota/penicillium_rubens_wisconsin_54_1255.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 16 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium rubens Biourge, 1923`; NCBI lists no broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium sp. YAP1`.
- `data/raw/ncbi_merged_ids.tsv` line 59083 maps old `NCBITaxon:2971041` into `NCBITaxon:1108849`, but an exact retained-row search found no `NCBITaxon:2971041` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 1972 has one aggregate GOLD row for `NCBITaxon:1108849` with `organism_count: 4`, matching the direct-taxon GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `1108849`: 3 unique `data/gold/organisms.jsonl.gz` organisms, 3 joined GOLD projects, and 3 joined GOLD analyses. None of those native GOLD rows emitted exact generated strain rows because they did not join to a BacDive-derived local strain inventory entry.
- `data/raw/ncbi_type_material.tsv` has 24 exact rows for `NCBITaxon:1108849`, spanning lines 6651-6674: 16 culture-from-lectotype spellings of `ATCC 9783`, `ATCC-9783`, `ATCC9783`, `ATCC:9783`, `CBS 129667`, `CBS-129667`, `CBS129667`, `CBS:129667`, `IBT 30129`, `IBT-30129`, `IBT30129`, `IBT:30129`, `NRRL 792`, `NRRL-792`, `NRRL792`, and `NRRL:792`, plus 8 lectotype spellings of `CBS H-20595`, `CBS H20595`, `CBS-H-20595`, `CBS-H20595`, `CBS:H-20595`, `CBS:H20595`, `CBSH-20595`, and `CBSH20595`.
- StrainInfo has 46 direct exact records and 61 deposits for NCBI taxon `1108849`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1108849`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1108849`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1108849`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1108849`, inspect the regenerated `data/taxa/eukaryota/penicillium_rubens.yaml`, then run `just validate data/taxa/eukaryota/penicillium_rubens.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_rubens.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_rubens.md`, so the absence check included gitignored reports.
