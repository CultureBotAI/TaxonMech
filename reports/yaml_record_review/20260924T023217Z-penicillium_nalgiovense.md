# YAML Record Review: Penicillium nalgiovense

- File: `data/taxa/eukaryota/penicillium_nalgiovense.yaml`
- Identifier: `NCBITaxon:60175`
- Label: `Penicillium nalgiovense`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 7586 contains the matching current NCBI row for `NCBITaxon:60175`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53018 includes `NCBITaxon:60175` with reason `attested rule: Penicillium nalgiovense, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_nalgiovense.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_minnesotense.yaml data/taxa/eukaryota/penicillium_momoi.yaml data/taxa/eukaryota/penicillium_nalgiovense.yaml data/taxa/eukaryota/penicillium_nalgiovense_fm193.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The one related synonym in YAML exactly matches the NCBI related synonym: `Penicillium nalgiovense Laxa, 1932`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:60175`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 39776 has one aggregate GOLD row for `NCBITaxon:60175` with `organism_count: 2`, matching the GOLD source attestation and its direct-under-this-taxon note.
- Native GOLD contains two exact organisms for NCBI taxon `60175`: `Go0372915` for strain `IBT 13039` and `Go0583249` for strain `ITEM 18323`; joined projects were `Gp0219706`, `Gp0586833`, and `Gp0589694`, with one joined analysis row for `Gp0219706`.
- `data/raw/ncbi_type_material.tsv` has fifteen exact rows for `NCBITaxon:60175`: `CBS 352.48`, `CBS:352.48`, `CBS 101030`, `CBS:101030`, `IBT 21536`, `IBT 3800`, `IBT 3861`, `IBT:21536`, `IBT:3800`, `IBT:3861`, `ICMP:5611`, `MUCL 31194`, `MUCL:31194`, `NRRL 911`, and `NRRL:911`.
- StrainInfo has 50 direct exact records and 62 deposits for NCBI taxon `60175`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:60175`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:60175`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `60175`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:60175`, inspect the regenerated `data/taxa/eukaryota/penicillium_nalgiovense.yaml`, then run `just validate data/taxa/eukaryota/penicillium_nalgiovense.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_nalgiovense.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_nalgiovense.md`, so the absence check included gitignored reports.
