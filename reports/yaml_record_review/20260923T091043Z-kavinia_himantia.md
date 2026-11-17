# YAML Record Review: Kavinia himantia

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kavinia_himantia.yaml
- Started UTC: 2026-09-23T09:10:43Z
- Finished UTC: 2026-09-23T09:10:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kavinia_himantia.yaml` denotes the exact NCBI species `Kavinia himantia` as `NCBITaxon:234815`, rank `SPECIES`, under genus `NCBITaxon:80652` (`Kavinia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kavinia_himantia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/karlodinium_veneficum.yaml data/taxa/eukaryota/kavinia_alboviridis.yaml data/taxa/eukaryota/kavinia_himantia.yaml data/taxa/eukaryota/kazachstania_africana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:46227` carries `NCBITaxon:234815`, label `Kavinia himantia`, rank `SPECIES`, parent `NCBITaxon:80652`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kavinia`.
- `curation/seed_scope.tsv:54675` contains this identifier with reason `attested rule: Kavinia himantia, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:149341`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:21854`, whose aggregate count is `3` for `NCBITaxon:234815`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:234815`.
- StrainInfo has 1 exact direct row and 1 exact deposit row but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:234815`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:234815`, `just validate data/taxa/eukaryota/kavinia_himantia.yaml`, and `just validate-strict data/taxa/eukaryota/kavinia_himantia.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kavinia_himantia` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
