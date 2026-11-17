# YAML Record Review: Kazachstania taianensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kazachstania_taianensis.yaml
- Started UTC: 2026-09-23T09:13:34Z
- Finished UTC: 2026-09-23T09:13:34Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kazachstania_taianensis.yaml` denotes the exact NCBI species `Kazachstania taianensis` as `NCBITaxon:655095`, rank `SPECIES`, under genus `NCBITaxon:71245` (`Kazachstania`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kazachstania_taianensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kazachstania_kunashirensis.yaml data/taxa/eukaryota/kazachstania_martiniae.yaml data/taxa/eukaryota/kazachstania_psychrophila.yaml data/taxa/eukaryota/kazachstania_taianensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:151485` carries `NCBITaxon:655095`, label `Kazachstania taianensis`, rank `SPECIES`, parent `NCBITaxon:71245`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kazachstania`.
- `curation/seed_scope.tsv:56251` contains this identifier with reason `attested rule: Kazachstania taianensis, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:40536`, whose aggregate count is `1` for `NCBITaxon:655095`.
- The current native GOLD scan found exact organism `Go0517021` for `Kazachstania taianensis NRRL Y-48846` and project `Gp0441059`.
- The native GOLD analysis scan found one exact linked analysis, `Kazachstania taianensis NRRL Y-48846`, through project `Gp0441059`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 7 culture-from-type-material rows for `NCBITaxon:655095` at lines 245749-245755, covering `AS 2.4160`, `CBS 11405`, `CGMCC 2.4160`, and `NRRL Y-48846` spelling variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:655095`, `just validate data/taxa/eukaryota/kazachstania_taianensis.yaml`, and `just validate-strict data/taxa/eukaryota/kazachstania_taianensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kazachstania_taianensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
