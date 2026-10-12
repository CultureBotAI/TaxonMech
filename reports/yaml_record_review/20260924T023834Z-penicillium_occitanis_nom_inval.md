# YAML Record Review: Penicillium occitanis (nom. inval.)

- File: `data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml`
- Identifier: `NCBITaxon:290292`
- Label: `Penicillium occitanis (nom. inval.)`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:2593313` (`unclassified Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 59120 contains the matching current NCBI row for `NCBITaxon:290292`: rank `SPECIES`, parent `NCBITaxon:2593313`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 55013 includes `NCBITaxon:290292` with reason `attested rule: Penicillium occitanis (nom. inval.), 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_nordicum.yaml data/taxa/eukaryota/penicillium_novae_zeelandiae.yaml data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml data/taxa/eukaryota/penicillium_onobense.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 16 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The lineage includes `NCBITaxon:2593313` (`unclassified Penicillium`) as the target's immediate `NO_RANK` parent under genus `NCBITaxon:5073`, matching the NCBI row.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium occitanis`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:290292`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 28330 has one aggregate GOLD row for `NCBITaxon:290292` with `organism_count: 2`, matching the GOLD source attestation.
- Native GOLD contains two exact organisms for NCBI taxon `290292`: `Go0455072` / `Gp0323398` for strain `CT1`, and `Go0455073` / `Gp0323399` for strain `CL100`; two joined analysis rows carry those project ids.
- `data/raw/ncbi_type_material.tsv` has zero exact rows for `NCBITaxon:290292`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `290292`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:290292`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:290292`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `290292`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:290292`, inspect the regenerated `data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml`, then run `just validate data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_occitanis_nom_inval.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_occitanis_nom_inval.md`, so the absence check included gitignored reports.
