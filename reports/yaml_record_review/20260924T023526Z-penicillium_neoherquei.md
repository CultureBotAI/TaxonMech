# YAML Record Review: Penicillium neoherquei

- File: `data/taxa/eukaryota/penicillium_neoherquei.yaml`
- Identifier: `NCBITaxon:2972955`
- Label: `Penicillium neoherquei`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 580409 contains the matching current NCBI row for `NCBITaxon:2972955`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 63483 includes `NCBITaxon:2972955` with reason `attested rule: Penicillium neoherquei, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_neoherquei.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/penicillium_neocrassum.yaml data/taxa/eukaryota/penicillium_neoechinulatum.yaml data/taxa/eukaryota/penicillium_neoherquei.yaml data/taxa/eukaryota/penicillium_nodulum.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The one related synonym in YAML exactly matches the NCBI related synonym: `Penicillium neoherquei Labuda, Kubatova, Nebesarova, Oberlies & Raja, 2022`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:2972955`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 29681 has one aggregate GOLD row for `NCBITaxon:2972955` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `2972955`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has fifteen exact rows for `NCBITaxon:2972955`: `CBS 148692`, `CBS-148692`, `CBS148692`, `CBS:148692`, `CCF 6604`, `CCF:6604`, `CCF<CZE> 6604`, `CCF<CZE>-6604`, `CCF<CZE>6604`, `CCF<CZE>:6604`, `G1071`, `PRM 956035`, `PRM-956035`, `PRM956035`, and `PRM:956035`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `2972955`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:2972955`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:2972955`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `2972955`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:2972955`, inspect the regenerated `data/taxa/eukaryota/penicillium_neoherquei.yaml`, then run `just validate data/taxa/eukaryota/penicillium_neoherquei.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_neoherquei.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_neoherquei.md`, so the absence check included gitignored reports.
