# YAML Record Review: Juglanconis oblonga

- Repository: TaxonMech
- Record: data/taxa/eukaryota/juglanconis_oblonga.yaml
- Started UTC: 2026-09-23T09:02:07Z
- Finished UTC: 2026-09-23T09:02:07Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/juglanconis_oblonga.yaml` denotes the exact NCBI species `Juglanconis oblonga` as `NCBITaxon:1940568`, rank `SPECIES`, under genus `NCBITaxon:1940564` (`Juglanconis`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/juglanconis_oblonga.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jaminaea_rosea.yaml data/taxa/eukaryota/jianyunia_sakaguchii.yaml data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml data/taxa/eukaryota/juglanconis_oblonga.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:497937` carries `NCBITaxon:1940568`, label `Juglanconis oblonga`, rank `SPECIES`, parent `NCBITaxon:1940564`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Juglanconis`.
- `curation/seed_scope.tsv:61693` contains this identifier with reason `attested rule: Juglanconis oblonga, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:1045752`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:17855`, whose aggregate count is `1` for `NCBITaxon:1940568`.
- The current native GOLD scan found exact organism `Go0449071` for `Juglanconis oblonga AR4414` and project `Gp0313473`.
- The native GOLD analysis scan found one exact linked analysis, `Juglanconis oblonga AR4414`, through project `Gp0313473`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:1940568`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1940568`, `just validate data/taxa/eukaryota/juglanconis_oblonga.yaml`, and `just validate-strict data/taxa/eukaryota/juglanconis_oblonga.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `juglanconis_oblonga` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
