# YAML Record Review: Penicillium rubefaciens

- File: `data/taxa/eukaryota/penicillium_rubefaciens.yaml`
- Identifier: `NCBITaxon:1167576`
- Label: `Penicillium rubefaciens`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 257895 contains the matching current NCBI row for `NCBITaxon:1167576`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 58098 includes `NCBITaxon:1167576` with reason `attested rule: Penicillium rubefaciens, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_rubefaciens.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_roseoviride.yaml data/taxa/eukaryota/penicillium_rubefaciens.yaml data/taxa/eukaryota/penicillium_rubens.yaml data/taxa/eukaryota/penicillium_rubens_wisconsin_54_1255.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium rubefaciens Quintan., 1982` and `Penicillium sp. CBS 145.83`.
- `data/raw/ncbi_merged_ids.tsv` line 23234 maps old `NCBITaxon:1651867` into `NCBITaxon:1167576`, but an exact retained-row search found no `NCBITaxon:1651867` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 3566 has one aggregate GOLD row for `NCBITaxon:1167576` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `1167576`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:1167576`: `CBS 145.83`, `CBS:145.83`, `CECT 2752`, and `CECT:2752`, all cultures from the neotype.
- StrainInfo has 6 direct exact records and 8 deposits for NCBI taxon `1167576`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1167576`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1167576`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1167576`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1167576`, inspect the regenerated `data/taxa/eukaryota/penicillium_rubefaciens.yaml`, then run `just validate data/taxa/eukaryota/penicillium_rubefaciens.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_rubefaciens.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_rubefaciens.md`, so the absence check included gitignored reports.
