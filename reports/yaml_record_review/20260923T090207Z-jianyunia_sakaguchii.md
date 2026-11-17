# YAML Record Review: Jianyunia sakaguchii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jianyunia_sakaguchii.yaml
- Started UTC: 2026-09-23T09:02:07Z
- Finished UTC: 2026-09-23T09:02:07Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/jianyunia_sakaguchii.yaml` denotes the exact NCBI species `Jianyunia sakaguchii` as `NCBITaxon:109612`, rank `SPECIES`, under genus `NCBITaxon:1798856` (`Jianyunia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jianyunia_sakaguchii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jaminaea_rosea.yaml data/taxa/eukaryota/jianyunia_sakaguchii.yaml data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml data/taxa/eukaryota/juglanconis_oblonga.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:19686` carries `NCBITaxon:109612`, label `Jianyunia sakaguchii`, rank `SPECIES`, parent `NCBITaxon:1798856`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Jianyunia`.
- `curation/seed_scope.tsv:53742` contains this identifier with reason `attested rule: Jianyunia sakaguchii, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1813`, whose aggregate count is `1` for `NCBITaxon:109612`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:109612`.
- StrainInfo has 2 exact direct rows and 6 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 8 rows for `NCBITaxon:109612` at lines 6182-6189, covering `CBS 8464` cultures from type material plus `IGC 5505`, `JCM 10047`, and `OK255` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:109612`, `just validate data/taxa/eukaryota/jianyunia_sakaguchii.yaml`, and `just validate-strict data/taxa/eukaryota/jianyunia_sakaguchii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jianyunia_sakaguchii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
