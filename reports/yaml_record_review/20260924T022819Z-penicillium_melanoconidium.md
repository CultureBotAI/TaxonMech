# YAML Record Review: Penicillium melanoconidium

- File: `data/taxa/eukaryota/penicillium_melanoconidium.yaml`
- Identifier: `NCBITaxon:60168`
- Label: `Penicillium melanoconidium`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 7580 contains the matching current NCBI row for `NCBITaxon:60168`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53012 includes `NCBITaxon:60168` with reason `attested rule: Penicillium melanoconidium, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_melanoconidium.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_mediterraneum.yaml data/taxa/eukaryota/penicillium_melanoconidium.yaml data/taxa/eukaryota/penicillium_mexicanum.yaml data/taxa/eukaryota/penicillium_miczynskii.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium aurantiogriseum var. melanoconidium`.
- The related synonyms in YAML exactly match the NCBI related synonyms: `Penicillium aurantiogriseum var. melanoconidium Frisvad`, `Penicillium aurantiogriseum var. melanoconidium Frisvad, 1990`, and `Penicillium melanoconidium (Frisvad) Frisvad & Samson, 2004`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:60168`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 39770 has one aggregate GOLD row for `NCBITaxon:60168` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `60168`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has six exact rows for `NCBITaxon:60168`: `CBS 115506`, `CBS:115506`, `IBT 3444`, `IBT:3444`, `IMI 321503`, and `IMI:321503`.
- StrainInfo has 19 direct exact records and 27 deposits for NCBI taxon `60168`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:60168`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:60168`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `60168`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:60168`, inspect the regenerated `data/taxa/eukaryota/penicillium_melanoconidium.yaml`, then run `just validate data/taxa/eukaryota/penicillium_melanoconidium.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_melanoconidium.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_melanoconidium.md`, so the absence check included gitignored reports.
