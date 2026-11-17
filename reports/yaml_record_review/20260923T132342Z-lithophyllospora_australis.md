# YAML Record Review: Lithophyllospora australis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lithophyllospora_australis.yaml
- Started UTC: 2026-09-23T13:23:42Z
- Finished UTC: 2026-09-23T13:23:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lithophyllospora_australis.yaml` denotes the exact NCBI species `Lithophyllospora australis` as `NCBITaxon:3016174`, rank `SPECIES`, under genus `NCBITaxon:3421014` (`Lithophyllospora`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lithophyllospora_australis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lithophyllospora_australis.yaml data/taxa/eukaryota/litonotus_pictus.yaml data/taxa/eukaryota/lizanozyma_gosingica.yaml data/taxa/eukaryota/lizanozyma_spartinae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:585513` carries `NCBITaxon:3016174`, label `Lithophyllospora australis`, rank `SPECIES`, parent `NCBITaxon:3421014`, genetic code `1`, three related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lithophyllospora` genus.
- The record preserves the `Chaetothyriales sp. CC-2022a`, `Knufia sp. CC-2022a`, and authorship-bearing `Lithophyllospora australis` related synonyms from NCBI.
- `curation/seed_scope.tsv:63489` contains this identifier with reason `attested rule: Lithophyllospora australis, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:2998318` for `NCBITaxon:3016174`, but it was not present as a retained retired row in `data/raw/ncbitaxon_taxa.tsv`; this matches the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:30176`, whose aggregate count is `1` for `NCBITaxon:3016174`.
- The current native GOLD scan found no exact organism, project, or analysis rows in the compressed GOLD files for this NCBI ID.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:155292` through `155296` contain five holotype spellings for `Lithophyllospora australis`: `MNA-CCFEE 6417`, hyphenated/compacted/colon variants, and `MUT 6702`. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:3016174`, `just validate data/taxa/eukaryota/lithophyllospora_australis.yaml`, and `just validate-strict data/taxa/eukaryota/lithophyllospora_australis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lithophyllospora_australis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
