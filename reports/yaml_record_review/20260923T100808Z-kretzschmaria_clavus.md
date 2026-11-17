# YAML Record Review: Kretzschmaria clavus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kretzschmaria_clavus.yaml
- Started UTC: 2026-09-23T10:08:08Z
- Finished UTC: 2026-09-23T10:08:08Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kretzschmaria_clavus.yaml` denotes the exact NCBI species `Kretzschmaria clavus` as `NCBITaxon:110527`, rank `SPECIES`, under genus `NCBITaxon:110525` (`Kretzschmaria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kretzschmaria_clavus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kregervanrija_delftensis.yaml data/taxa/eukaryota/kregervanrija_fluxuum.yaml data/taxa/eukaryota/kregervanrija_pseudodelftensis.yaml data/taxa/eukaryota/kretzschmaria_clavus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:19910` carries `NCBITaxon:110527`, label `Kretzschmaria clavus`, rank `SPECIES`, parent `NCBITaxon:110525`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kretzschmaria`.
- `curation/seed_scope.tsv:53763` contains this identifier with reason `attested rule: Kretzschmaria clavus, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1948`, whose aggregate count is `1` for `NCBITaxon:110527`.
- The current native GOLD JSONL exact scan found no organism, project, or analysis rows for this NCBI ID.
- StrainInfo has 1 exact direct row and 2 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.
- Exact BacDive scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:110527`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:110527`, `just validate data/taxa/eukaryota/kretzschmaria_clavus.yaml`, and `just validate-strict data/taxa/eukaryota/kretzschmaria_clavus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kretzschmaria_clavus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The generated assertion count follows `data/raw/gold_organisms.tsv`; the current native exact GOLD JSONL scan does not contain rows for this NCBI ID.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
