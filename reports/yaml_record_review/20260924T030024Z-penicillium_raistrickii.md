# YAML Record Review: Penicillium raistrickii

- File: `data/taxa/eukaryota/penicillium_raistrickii.yaml`
- Identifier: `NCBITaxon:69783`
- Label: `Penicillium raistrickii`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9675 contains the matching current NCBI row for `NCBITaxon:69783`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53188 includes `NCBITaxon:69783` with reason `attested rule: Penicillium raistrickii, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_raistrickii.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_raciborskii.yaml data/taxa/eukaryota/penicillium_radicicola.yaml data/taxa/eukaryota/penicillium_raistrickii.yaml data/taxa/eukaryota/penicillium_ranomafanaense.yaml` exited successfully.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium raistrickii G. Smith, 1933`.
- `data/raw/ncbi_merged_ids.tsv` line 7274 maps old `NCBITaxon:1196404` into `NCBITaxon:69783`, but an exact retained-row search found no `NCBITaxon:1196404` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41546 has one aggregate GOLD row for `NCBITaxon:69783` with `organism_count: 1`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `69783`: 1 unique `data/gold/organisms.jsonl.gz` organism, 3 joined GOLD projects, and 1 joined GOLD analysis. None of those native GOLD rows emitted exact generated strain rows because they did not join to a BacDive-derived local strain inventory entry.
- `data/raw/ncbi_type_material.tsv` has eight exact rows for `NCBITaxon:69783`: `FRR 1044` and `FRR:1044` are cultures from the neotype, and `CBS 272.83`, `CBS:272.83`, `CECT 2735`, `CECT:2735`, `IMI 255795`, and `IMI:255795` are type material.
- StrainInfo has 34 direct exact records and 61 deposits for NCBI taxon `69783`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:69783`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:69783`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `69783`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:69783`, inspect the regenerated `data/taxa/eukaryota/penicillium_raistrickii.yaml`, then run `just validate data/taxa/eukaryota/penicillium_raistrickii.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_raistrickii.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_raistrickii.md`, so the absence check included gitignored reports.
