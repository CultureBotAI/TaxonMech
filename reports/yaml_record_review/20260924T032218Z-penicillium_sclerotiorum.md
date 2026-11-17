# YAML Record Review: Penicillium sclerotiorum

- File: `data/taxa/eukaryota/penicillium_sclerotiorum.yaml`
- Identifier: `NCBITaxon:69788`
- Label: `Penicillium sclerotiorum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9678 contains the matching current NCBI row for `NCBITaxon:69788`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53191 includes `NCBITaxon:69788` with reason `attested rule: Penicillium sclerotiorum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sclerotiorum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_sclerotiorum.yaml data/taxa/eukaryota/penicillium_scottii.yaml data/taxa/eukaryota/penicillium_senticosum.yaml data/taxa/eukaryota/penicillium_sexuale.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium sclerotiorum J.F.H. Beyma, 1937`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:69788`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41549 has one aggregate GOLD row for `NCBITaxon:69788` with `organism_count: 1`, matching the GOLD source attestation.
- Exact native GOLD source rows are present for NCBI taxon `69788`: 1 unique `data/gold/organisms.jsonl.gz` organism, 1 joined GOLD project, and 1 joined GOLD analysis. None of those native GOLD rows emitted exact generated strain rows because they did not join to a BacDive-derived local strain inventory entry.
- `data/raw/ncbi_type_material.tsv` has six exact rows for `NCBITaxon:69788`: `CBS 287.36`, `CBS:287.36`, `FRR 2074`, `FRR:2074`, `NRRL 2074`, and `NRRL:2074`, all cultures from the neotype.
- StrainInfo has 59 direct exact records and 104 deposits for NCBI taxon `69788`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:69788`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:69788`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `69788`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:69788`, inspect the regenerated `data/taxa/eukaryota/penicillium_sclerotiorum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_sclerotiorum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_sclerotiorum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_sclerotiorum.md`, so the absence check included gitignored reports.
