# YAML Record Review: Penicillium penarojense

- File: `data/taxa/eukaryota/penicillium_penarojense.yaml`
- Identifier: `NCBITaxon:1506156`
- Label: `Penicillium penarojense`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 386764 contains the matching current NCBI row for `NCBITaxon:1506156`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 60355 includes `NCBITaxon:1506156` with reason `attested rule: Penicillium penarojense, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_penarojense.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_paxilli.yaml data/taxa/eukaryota/penicillium_penarojense.yaml data/taxa/eukaryota/penicillium_persicinum.yaml data/taxa/eukaryota/penicillium_pole_evansii.yaml` exited successfully.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Penicillium penajorense`; NCBI lists no broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium penarojense Houbraken, C. Lopez, Frisvad & Samson, 2011` and `Penicillium sp. 3 JH-2010`.
- `data/raw/ncbi_merged_ids.tsv` line 94659 maps old `NCBITaxon:756465` into `NCBITaxon:1506156`, but an exact retained-row search found no `NCBITaxon:756465` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 11829 has one aggregate GOLD row for `NCBITaxon:1506156` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `1506156`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:1506156`: `CBS 113178` and `CBS:113178` are cultures from the holotype, and `IBT 23262` and `IBT:23262` are cultures from type material.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `1506156`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1506156`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1506156`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1506156`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1506156`, inspect the regenerated `data/taxa/eukaryota/penicillium_penarojense.yaml`, then run `just validate data/taxa/eukaryota/penicillium_penarojense.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_penarojense.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_penarojense.md`, so the absence check included gitignored reports.
