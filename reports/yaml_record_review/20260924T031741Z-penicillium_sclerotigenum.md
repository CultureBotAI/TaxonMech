# YAML Record Review: Penicillium sclerotigenum

- File: `data/taxa/eukaryota/penicillium_sclerotigenum.yaml`
- Identifier: `NCBITaxon:69787`
- Label: `Penicillium sclerotigenum`
- Verdict: pass

## Target

- The seeded record is a species-level `EUKARYOTA` record under `NCBITaxon:5073` (`Penicillium`).
- `data/raw/ncbitaxon_taxa.tsv` line 9677 contains the matching current NCBI row for `NCBITaxon:69787`: rank `SPECIES`, parent `NCBITaxon:5073`, genetic code `1`, no retired target, and `attested_by: gold`.
- `curation/seed_scope.tsv` line 53190 includes `NCBITaxon:69787` with reason `attested rule: Penicillium sclerotigenum, 2 sources incl. NCBI`.
- The seeded label, rank, parent, genetic code, and NCBI source attestation match the raw NCBI row.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sclerotigenum.yaml` passed with no LinkML issues.
- `just validate-strict data/taxa/eukaryota/penicillium_salamii.yaml data/taxa/eukaryota/penicillium_samsonianum.yaml data/taxa/eukaryota/penicillium_sanguifluum.yaml data/taxa/eukaryota/penicillium_sclerotigenum.yaml` scanned 4 files and reported 0 files with `ERROR`.
- The bounded source scan rechecked 15 lineage entries against `data/raw/ncbitaxon_taxa.tsv`; no lineage rows were missing and no label or rank mismatches were found.

## Identity and Grounding

- `grounding_status: EXACT` and `mapping_status: SEEDED` are consistent with the direct NCBI identifier match.
- NCBI lists no exact or broad synonyms for the target row.
- The related synonym in YAML exactly matches the NCBI related synonym: `Penicillium sclerotigenum W. Yamamoto, 1955`.
- `data/raw/ncbi_merged_ids.tsv` has no rows whose `current_taxon_id` is `NCBITaxon:69787`, so no `replaces` entry is expected.

## Evidence

- `data/raw/gold_organisms.tsv` line 41548 has one aggregate GOLD row for `NCBITaxon:69787` with `organism_count: 1`, matching the GOLD source attestation.
- No exact native `data/gold/organisms.jsonl.gz` rows, joined GOLD projects, or joined GOLD analyses were found for NCBI taxon `69787`; no generated raw strain row is expected from GOLD.
- `data/raw/ncbi_type_material.tsv` has 16 exact rows for `NCBITaxon:69787`: `ATCC 18488`, `ATCC:18488`, `CBS 101033`, `CBS 343.59`, `CBS:101033`, `CBS:343.59`, `IBT 14346`, `IBT 21544`, `IBT:14346`, `IBT:21544`, `IFO 6167`, `IFO:6167`, `IMI 68616`, `IMI:68616`, `NRRL 3461`, and `NRRL:3461`.
- StrainInfo has 7 direct exact records and 22 deposits for NCBI taxon `69787`, but emitted no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; the zero `strain_count` is therefore consistent with generated strain TSV evidence.

## Completeness

- The generated raw target tables had zero exact rows for `NCBITaxon:69787`: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- The auxiliary source tables had zero exact rows for `NCBITaxon:69787`: `data/raw/lpsn_names.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- `data/bacdive/records.jsonl.gz` had zero exact BacDive records for numeric taxon id `69787`.

## Findings

None.

## Recommended Edits

None.

## Follow-up Checks

- If a future source refresh changes this taxon, run `just seed-canary NCBITaxon:69787`, inspect the regenerated `data/taxa/eukaryota/penicillium_sclerotigenum.yaml`, then run `just validate data/taxa/eukaryota/penicillium_sclerotigenum.yaml`, `just validate-strict data/taxa/eukaryota/penicillium_sclerotigenum.yaml`, and `just verify-corpus`.
- If future curation adds ontology-backed graph content, run `just validate-products`.

## Additional Notes

- The report was written from detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report file was created in the primary checkout.
- Before writing, an exact `find` over the ignored `reports/yaml_record_review` directory found no existing `*-penicillium_sclerotigenum.md`, so the absence check included gitignored reports.
