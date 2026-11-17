# YAML Record Review: Penicillium nalgiovense FM193

- File: `data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml`
- Identifier: `NCBITaxon:1439352`
- Label: `Penicillium nalgiovense FM193`
- Verdict: pass

## Target

- The seeded record is a strain-level `EUKARYOTA` record under `NCBITaxon:60175` (`Penicillium nalgiovense`).
- `data/raw/ncbitaxon_taxa.tsv` line 360928 contains the matching current NCBI row for `NCBITaxon:1439352`: rank `STRAIN`, parent `NCBITaxon:60175`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 60139 includes `NCBITaxon:1439352` with reason `attested rule: Penicillium nalgiovense FM193, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_minnesotense.yaml data/taxa/eukaryota/penicillium_momoi.yaml data/taxa/eukaryota/penicillium_nalgiovense.yaml data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 16 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI strain identifier match.
- The lineage includes the expected species parent, `NCBITaxon:60175` (`Penicillium nalgiovense`), between genus `NCBITaxon:5073` and the target strain.
- NCBI lists no exact, broad, or related synonyms for the target row, and the YAML correctly omits a `synonyms` block.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:1439352`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 10480 has one aggregate GOLD row for `NCBITaxon:1439352` with `organism_count: 11`, matching the GOLD source attestation.
- Native GOLD contains twelve exact organisms for NCBI taxon `1439352`; the bounded sample includes `Go0101010` for strain `FM193`, and the exact project and analysis evidence link through `Gp0101010`.
- `data/raw/ncbi_type_material.tsv` has zero exact rows for `NCBITaxon:1439352`.
- StrainInfo has zero direct exact records and zero deposits for NCBI taxon `1439352`, and no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:1439352`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:1439352`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `1439352`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:1439352`, inspect the regenerated `data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml`, then run `just validate data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_nalgiovense_fm193.md`, so the absence check included gitignored reports.
