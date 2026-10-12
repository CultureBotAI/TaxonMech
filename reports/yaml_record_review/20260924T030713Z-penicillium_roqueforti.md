# YAML Record Review: Penicillium roqueforti

- File: `data/taxa/eukaryota/penicillium_roqueforti.yaml`
- Identifier: `NCBITaxon:5082`
- Label: `Penicillium roqueforti`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 2223 contains the matching current NCBI row for `NCBITaxon:5082`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 51932 includes `NCBITaxon:5082` with reason `attested rule: Penicillium roqueforti, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_roqueforti.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_ribium.yaml data/taxa/eukaryota/penicillium_robsamsonii.yaml data/taxa/eukaryota/penicillium_rolfsii.yaml data/taxa/eukaryota/penicillium_roqueforti.yaml` exited successfully.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium roqueforti Sopp, 1912`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:5082`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 37457 has one aggregate GOLD row for `NCBITaxon:5082` with `organism_count: 6`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `5082`: 6 unique `data/gold/organisms.jsonl.gz` organisms, 8 joined GOLD projects, and 4 joined GOLD analyses. None of those native GOLD rows emitted exact generated strain rows because they did not join to a BacDive-derived local strain inventory entry.
- `data/raw/ncbi_type_material.tsv` has 12 exact rows for `NCBITaxon:5082`: `CBS 221.30` and `CBS:221.30` are cultures from the neotype; `ATCC 10110`, `ATCC:10110`, `CECT 2905`, `CECT:2905`, `NRRL 849`, `NRRL:849`, `QM 1937`, and `QM:1937` are cultures from type material; and `IMI 24313` and `IMI:24313` are type material.
- StrainInfo has 132 direct exact records and 174 deposits for NCBI taxon `5082`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:5082`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:5082`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `5082`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:5082`, inspect the regenerated `data/taxa/eukaryota/penicillium_roqueforti.yaml`, then run `just validate data/taxa/eukaryota/penicillium_roqueforti.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_roqueforti.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_roqueforti.md`, so the absence check included gitignored reports.
