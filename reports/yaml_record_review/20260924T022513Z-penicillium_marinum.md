# YAML Record Review: Penicillium marinum

- File: `data/taxa/eukaryota/penicillium_marinum.yaml`
- Identifier: `NCBITaxon:293560`
- Label: `Penicillium marinum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 59954 contains the matching current NCBI row for `NCBITaxon:293560`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 55042 includes `NCBITaxon:293560` with reason `attested rule: Penicillium marinum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_marinum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_malmesburiense.yaml data/taxa/eukaryota/penicillium_malodoratum.yaml data/taxa/eukaryota/penicillium_marinum.yaml data/taxa/eukaryota/penicillium_mattheeae.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The one related synonym in YAML exactly matches the NCBI related synonym: `Penicillium marinum Frisvad & Samson, 2004`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:293560`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 28973 has one aggregate GOLD row for `NCBITaxon:293560` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `293560`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:293560`: `CBS 109550`, `CBS:109550`, `IBT 14360`, and `IBT:14360`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `293560`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:293560`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:293560`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `293560`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:293560`, inspect the regenerated `data/taxa/eukaryota/penicillium_marinum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_marinum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_marinum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_marinum.md`, so the absence check included gitignored reports.
