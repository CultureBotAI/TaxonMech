# YAML Record Review: Kalapuya brunnea

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kalapuya_brunnea.yaml
- Started UTC: 2026-09-23T09:04:40Z
- Finished UTC: 2026-09-23T09:04:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kalapuya_brunnea.yaml` denotes the exact NCBI species `Kalapuya brunnea` as `NCBITaxon:720594`, rank `SPECIES`, under genus `NCBITaxon:720593` (`Kalapuya`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kalapuya_brunnea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jugulospora_carbonaria.yaml data/taxa/eukaryota/jumillera_viridis.yaml data/taxa/eukaryota/kalaharituber_pfeilii.yaml data/taxa/eukaryota/kalapuya_brunnea.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:169545` carries `NCBITaxon:720594`, label `Kalapuya brunnea`, rank `SPECIES`, parent `NCBITaxon:720593`, genetic code `1`, and the NCBI synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kalapuya`.
- `curation/seed_scope.tsv:56558` contains this identifier with reason `attested rule: Kalapuya brunnea, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:41972`, whose aggregate count is `1` for `NCBITaxon:720594`.
- The current native GOLD scan found exact organism `Go0496713` for `Kalapuya brunnea GMNB 372`.
- Expanding that exact GOLD organism found projects `Gp0397259` and `Gp0543300`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 3 rows for `NCBITaxon:720594`: `OSC JT32730` as isotype and `OSC 131234` / `OSC:131234` as paratype.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:720594`, `just validate data/taxa/eukaryota/kalapuya_brunnea.yaml`, and `just validate-strict data/taxa/eukaryota/kalapuya_brunnea.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kalapuya_brunnea` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
