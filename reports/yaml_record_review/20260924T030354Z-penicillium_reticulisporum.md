# YAML Record Review: Penicillium reticulisporum

- File: `data/taxa/eukaryota/penicillium_reticulisporum.yaml`
- Identifier: `NCBITaxon:91637`
- Label: `Penicillium reticulisporum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 14832 contains the matching current NCBI row for `NCBITaxon:91637`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53521 includes `NCBITaxon:91637` with reason `attested rule: Penicillium reticulisporum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_reticulisporum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_raperi.yaml data/taxa/eukaryota/penicillium_raphiae.yaml data/taxa/eukaryota/penicillium_repenticola.yaml data/taxa/eukaryota/penicillium_reticulisporum.yaml` exited successfully.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The two exact synonyms in YAML exactly match the pipe-delimited NCBI exact synonyms: `Eupenicillium reticulisporum` and `Eupenicillium reticulosporum`.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium reticulisporum Udagawa, 1968`; NCBI lists no broad synonyms for the target row.
- `data/raw/ncbi_merged_ids.tsv` line 92954 maps old `NCBITaxon:70107` into `NCBITaxon:91637`, but an exact retained-row search found no `NCBITaxon:70107` row in `data/raw/ncbitaxon_taxa.tsv`; no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 44471 has one aggregate GOLD row for `NCBITaxon:91637` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `91637`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has 12 exact rows for `NCBITaxon:91637`: `ATCC 18566`, `ATCC:18566`, `CBS 122.68`, `CBS:122.68`, `IFO 9024`, `IFO:9024`, `IMI 136700`, `IMI:136700`, `NHL 6105`, `NHL:6105`, `NRRL 3447`, and `NRRL:3447`.
- StrainInfo has 3 direct exact records and 18 deposits for NCBI taxon `91637`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:91637`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:91637`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `91637`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:91637`, inspect the regenerated `data/taxa/eukaryota/penicillium_reticulisporum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_reticulisporum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_reticulisporum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_reticulisporum.md`, so the absence check included gitignored reports.
