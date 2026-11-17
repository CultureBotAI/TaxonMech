# YAML Record Review: Kazachstania psychrophila

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kazachstania_psychrophila.yaml
- Started UTC: 2026-09-23T09:13:34Z
- Finished UTC: 2026-09-23T09:13:34Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kazachstania_psychrophila.yaml` denotes the exact NCBI species `Kazachstania psychrophila` as `NCBITaxon:1337065`, rank `SPECIES`, under genus `NCBITaxon:71245` (`Kazachstania`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kazachstania_psychrophila.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kazachstania_kunashirensis.yaml data/taxa/eukaryota/kazachstania_martiniae.yaml data/taxa/eukaryota/kazachstania_psychrophila.yaml data/taxa/eukaryota/kazachstania_taianensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:320406` carries `NCBITaxon:1337065`, label `Kazachstania psychrophila`, rank `SPECIES`, parent `NCBITaxon:71245`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kazachstania`.
- `curation/seed_scope.tsv:59536` contains this identifier with reason `attested rule: Kazachstania psychrophila, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8176`, whose aggregate count is `3` for `NCBITaxon:1337065`.
- The current native GOLD scan found exact organisms `Go0615381`, `Go0615382`, and `Go0615383` for strains `H433`, `DSM 26230`, and `CBS 12689`.
- Expanding those exact GOLD organisms found project `Gp0831082`, with no native linked analysis rows.
- StrainInfo has 1 exact direct row and 1 exact deposit row but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 type-material rows for `NCBITaxon:1337065`: `CBS 12689`, `CBS:12689`, `DSM 26230`, and `DSM:26230`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1337065`, `just validate data/taxa/eukaryota/kazachstania_psychrophila.yaml`, and `just validate-strict data/taxa/eukaryota/kazachstania_psychrophila.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kazachstania_psychrophila` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
