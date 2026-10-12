# YAML Record Review: Penicillium osmophilum

- File: `data/taxa/eukaryota/penicillium_osmophilum.yaml`
- Identifier: `NCBITaxon:91636`
- Label: `Penicillium osmophilum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 14831 contains the matching current NCBI row for `NCBITaxon:91636`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53520 includes `NCBITaxon:91636` with reason `attested rule: Penicillium osmophilum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_osmophilum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_osmophilum.yaml data/taxa/eukaryota/penicillium_outeniquaense.yaml data/taxa/eukaryota/penicillium_oxalicum.yaml data/taxa/eukaryota/penicillium_oxalicum_114_2.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Eupenicillium osmophilum`.
- The one related synonym in YAML exactly matches the NCBI related synonym: `Penicillium osmophilum Stolk & Veenbaas-Rijks, 1974`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:91636`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 44470 has one aggregate GOLD row for `NCBITaxon:91636` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `91636`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has six exact rows for `NCBITaxon:91636`: `NRRL 5922`, `NRRL:5922`, `CBS 462.72`, `CBS:462.72`, `IBT 14679`, and `IBT:14679`.
- StrainInfo has two direct exact records and nine deposits for NCBI taxon `91636`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:91636`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:91636`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `91636`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:91636`, inspect the regenerated `data/taxa/eukaryota/penicillium_osmophilum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_osmophilum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_osmophilum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_osmophilum.md`, so the absence check included gitignored reports.
