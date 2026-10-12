# YAML Record Review: Penicillium paxilli

- File: `data/taxa/eukaryota/penicillium_paxilli.yaml`
- Identifier: `NCBITaxon:70109`
- Label: `Penicillium paxilli`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9777 contains the matching current NCBI row for `NCBITaxon:70109`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53207 includes `NCBITaxon:70109` with reason `attested rule: Penicillium paxilli, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_paxilli.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_paxilli.yaml data/taxa/eukaryota/penicillium_penarojense.yaml data/taxa/eukaryota/penicillium_persicinum.yaml data/taxa/eukaryota/penicillium_pole_evansii.yaml` exited successfully.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium paxilli Bainier, 1907`.
- `data/raw/ncbi_merged_ids.tsv` line 21962 maps old `NCBITaxon:1618006` into `NCBITaxon:70109`, but an exact retained-row search found no `NCBITaxon:1618006` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41627 has one aggregate GOLD row for `NCBITaxon:70109` with `organism_count: 2`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `70109`: 1 unique `data/gold/organisms.jsonl.gz` organism and 1 joined GOLD project. No joined GOLD analyses were found, and the native GOLD rows did not emit exact generated strain rows.
- `data/raw/ncbi_type_material.tsv` has two exact rows for `NCBITaxon:70109`: `CBS 360.48` and `CBS:360.48`, both cultures from the neotype.
- StrainInfo has 46 direct exact records and 67 deposits for NCBI taxon `70109`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:70109`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:70109`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `70109`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:70109`, inspect the regenerated `data/taxa/eukaryota/penicillium_paxilli.yaml`, then run `just validate data/taxa/eukaryota/penicillium_paxilli.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_paxilli.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_paxilli.md`, so the absence check included gitignored reports.
