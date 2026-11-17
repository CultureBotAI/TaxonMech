# YAML Record Review: Penicillium oxalicum

- File: `data/taxa/eukaryota/penicillium_oxalicum.yaml`
- Identifier: `NCBITaxon:69781`
- Label: `Penicillium oxalicum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9674 contains the matching current NCBI row for `NCBITaxon:69781`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53187 includes `NCBITaxon:69781` with reason `attested rule: Penicillium oxalicum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_oxalicum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_osmophilum.yaml data/taxa/eukaryota/penicillium_outeniquaense.yaml data/taxa/eukaryota/penicillium_oxalicum.yaml data/taxa/eukaryota/penicillium_oxalicum_114_2.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium asturianum`.
- The related synonyms in YAML exactly match the NCBI related synonyms: `Penicillium asturianum C. Ramirez & A.T. Martinez, 1981`, `Penicillium oxalicum Currie & Thom, 1915`, and `Penicillium sp. 16 XZ-2015`.
- `data/raw/ncbi_merged_ids.tsv` lines 18152 and 23536 map old ids `NCBITaxon:1506159` and `NCBITaxon:1661384` into `NCBITaxon:69781`. Exact anchored greps against `data/raw/ncbitaxon_taxa.tsv` found no retained rows for either old id, so no `replaces` entries are expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41545 has one aggregate GOLD row for `NCBITaxon:69781` with `organism_count: 4`, matching the GOLD source attestation and its direct-under-this-taxon note.
- Native GOLD contains four exact organisms for NCBI taxon `69781`: strains `HP7-1`, `SGAir0226`, `PM4501B`, and `M7025A`; the four joined projects are `Gp0235520`, `Gp0449653`, `Gp0702250`, and `Gp0702251`, and four joined analysis rows carry those project ids.
- `data/raw/ncbi_type_material.tsv` has 31 exact rows for `NCBITaxon:69781`: `CBS 173.81`, `CBS:173.81`, `ATCC 1126`, `ATCC-1126`, `ATCC1126`, `ATCC:1126`, `BCCM/MUCL 29047`, `BCCM/MUCL-29047`, `BCCM/MUCL29047`, `BCCM/MUCL:29047`, `CBS 219.30`, `CBS:219.30`, `CCF<CZE>:2315`, `FRR 787`, `FRR-787`, `FRR787`, `FRR:787`, `IBT 6566`, `IBT-6566`, `IBT6566`, `IBT:6566`, `MUCL 29047`, `MUCL:29047`, `NRRL 787`, `NRRL:787`, `QM 7606`, `QM-7606`, `QM7606`, `QM:7606`, `IMI 192332`, and `IMI:192332`.
- StrainInfo has 113 direct exact records and 163 deposits for NCBI taxon `69781`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:69781`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:69781`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `69781`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:69781`, inspect the regenerated `data/taxa/eukaryota/penicillium_oxalicum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_oxalicum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_oxalicum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_oxalicum.md`, so the absence check included gitignored reports.
