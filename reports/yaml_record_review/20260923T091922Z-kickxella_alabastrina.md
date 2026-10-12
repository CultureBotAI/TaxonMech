# YAML Record Review: Kickxella alabastrina

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kickxella_alabastrina.yaml
- Started UTC: 2026-09-23T09:19:22Z
- Finished UTC: 2026-09-23T09:19:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kickxella_alabastrina.yaml` denotes the exact NCBI species `Kickxella alabastrina` as `NCBITaxon:61397`, rank `SPECIES`, under genus `NCBITaxon:61396` (`Kickxella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kickxella_alabastrina.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kickxella_alabastrina.yaml data/taxa/eukaryota/kiflimonium_junci.yaml data/taxa/eukaryota/kipferlia_bialata.yaml data/taxa/eukaryota/kirkomyces_cordensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7779` carries `NCBITaxon:61397`, label `Kickxella alabastrina`, rank `SPECIES`, parent `NCBITaxon:61396`, genetic code `1`, and the NCBI synonym retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kickxella`.
- `curation/seed_scope.tsv:53037` contains this identifier with reason `attested rule: Kickxella alabastrina, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39866`, whose aggregate count is `3` for `NCBITaxon:61397`.
- The current native GOLD scan found exact organisms `Go0302456` for `Kickxella alabastrina RSA 675` and `Go0515181` for `Kickxella alabastrina RSA 2140`.
- Expanding those exact GOLD organisms found projects `Gp0156927`, `Gp0215030`, and `Gp0435949`, with no native linked analysis rows.
- StrainInfo has 5 exact direct rows and 11 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:61397`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:61397`, `just validate data/taxa/eukaryota/kickxella_alabastrina.yaml`, and `just validate-strict data/taxa/eukaryota/kickxella_alabastrina.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kickxella_alabastrina` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
