# YAML Record Review: Penicillium malodoratum

- File: `data/taxa/eukaryota/penicillium_malodoratum.yaml`
- Identifier: `NCBITaxon:69805`
- Label: `Penicillium malodoratum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9683 contains the matching current NCBI row for `NCBITaxon:69805`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53196 includes `NCBITaxon:69805` with reason `attested rule: Penicillium malodoratum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_malodoratum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_malmesburiense.yaml data/taxa/eukaryota/penicillium_malodoratum.yaml data/taxa/eukaryota/penicillium_marinum.yaml data/taxa/eukaryota/penicillium_mattheeae.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- The exact synonym in YAML exactly matches the NCBI exact synonym: `Aspergillus malodoratus`.
- The related synonyms in YAML exactly match the NCBI related synonyms: `Aspergillus malodoratus Kwon-Chung & Fennell, 1965` and `Penicillium malodoratum (Kwon-Chung & Fennell) Samson, Houbraken, Visagie & Frisvad, 2015`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:69805`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41555 has one aggregate GOLD row for `NCBITaxon:69805` with `organism_count: 1`, matching the GOLD source attestation.
- Native GOLD contains one exact organism for NCBI taxon `69805`: `Go0446104`, strain `CBS 490.65`; the joined project is `Gp0312201`, and no joined analysis rows were found.
- `data/raw/ncbi_type_material.tsv` has eight exact rows for `NCBITaxon:69805`: `ATCC 16834`, `ATCC:16834`, `CBS 490.65`, `CBS:490.65`, `NRRL 5083`, `NRRL:5083`, `IMI 172289`, and `IMI:172289`.
- StrainInfo has two direct exact records and seven deposits for NCBI taxon `69805`, but no exact rows were emitted in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:69805`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:69805`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `69805`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:69805`, inspect the regenerated `data/taxa/eukaryota/penicillium_malodoratum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_malodoratum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_malodoratum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_malodoratum.md`, so the absence check included gitignored reports.
