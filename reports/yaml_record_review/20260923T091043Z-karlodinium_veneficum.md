# YAML Record Review: Karlodinium veneficum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/karlodinium_veneficum.yaml
- Started UTC: 2026-09-23T09:10:43Z
- Finished UTC: 2026-09-23T09:10:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/karlodinium_veneficum.yaml` denotes the exact NCBI species `Karlodinium veneficum` as `NCBITaxon:407301`, rank `SPECIES`, under genus `NCBITaxon:157684` (`Karlodinium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/karlodinium_veneficum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/karlodinium_veneficum.yaml data/taxa/eukaryota/kavinia_alboviridis.yaml data/taxa/eukaryota/kavinia_himantia.yaml data/taxa/eukaryota/kazachstania_africana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:88044` carries `NCBITaxon:407301`, label `Karlodinium veneficum`, rank `SPECIES`, parent `NCBITaxon:157684`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 9 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Karlodinium`.
- `curation/seed_scope.tsv:55538` contains this identifier with reason `attested rule: Karlodinium veneficum, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:157685`, `NCBITaxon:160608`, `NCBITaxon:188904`, `NCBITaxon:2956`, and `NCBITaxon:342587`, but none are present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:34653`, whose aggregate count is `2` for `NCBITaxon:407301`.
- The current native GOLD scan found exact organisms `Go0002352` for `Karlodinium micrum` and `Go0368714` for `Karlodinium veneficum CCMP 2283`.
- Expanding those exact GOLD organisms found project `Gp0002352`, with no native linked analysis rows.
- StrainInfo has 9 exact direct rows and 9 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:407301`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:407301`, `just validate data/taxa/eukaryota/karlodinium_veneficum.yaml`, and `just validate-strict data/taxa/eukaryota/karlodinium_veneficum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `karlodinium_veneficum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
