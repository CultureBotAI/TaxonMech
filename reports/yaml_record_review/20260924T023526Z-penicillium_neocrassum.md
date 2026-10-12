# YAML Record Review: Penicillium neocrassum

- File: `data/taxa/eukaryota/penicillium_neocrassum.yaml`
- Identifier: `NCBITaxon:1167569`
- Label: `Penicillium neocrassum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 257893 contains the matching current NCBI row for `NCBITaxon:1167569`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 58096 includes `NCBITaxon:1167569` with reason `attested rule: Penicillium neocrassum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_neocrassum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_neocrassum.yaml data/taxa/eukaryota/penicillium_neoechinulatum.yaml data/taxa/eukaryota/penicillium_neoherquei.yaml data/taxa/eukaryota/penicillium_nodulum.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The two related synonyms in YAML exactly match the pipe-delimited NCBI related synonyms: `Penicillium neocrassum R. Serra & S.W. Peterson, 2007` and `Penicillium sp. NRRL 35639`.
- `data/raw/ncbi_merged_ids.tsv` line 75125 maps old id `NCBITaxon:391093` into `NCBITaxon:1167569`. An exact anchored grep against `data/raw/ncbitaxon_taxa.tsv` found no retained row for `NCBITaxon:391093`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 3564 has one aggregate GOLD row for `NCBITaxon:1167569` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `1167569`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:1167569`: `NRRL 35639`, `NRRL:35639`, `BPI 872161`, and `BPI:872161`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `1167569`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1167569`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1167569`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1167569`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1167569`, inspect the regenerated `data/taxa/eukaryota/penicillium_neocrassum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_neocrassum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_neocrassum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_neocrassum.md`, so the absence check included gitignored reports.
