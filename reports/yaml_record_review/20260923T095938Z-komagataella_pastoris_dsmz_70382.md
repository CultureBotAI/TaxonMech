# YAML Record Review: Komagataella pastoris DSMZ 70382

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml
- Started UTC: 2026-09-23T09:59:38Z
- Finished UTC: 2026-09-23T09:59:38Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml` denotes the exact NCBI strain `Komagataella pastoris DSMZ 70382` as `NCBITaxon:638632`, rank `STRAIN`, under species `NCBITaxon:4922` (`Komagataella pastoris`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_kurtzmanii.yaml data/taxa/eukaryota/komagataella_mondaviorum.yaml data/taxa/eukaryota/komagataella_pastoris.yaml data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:147079` carries `NCBITaxon:638632`, label `Komagataella pastoris DSMZ 70382`, rank `STRAIN`, parent `NCBITaxon:4922`, genetic code `1`, and exact synonym `Pichia pastoris DSMZ 70382` as retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected species `Komagataella pastoris`.
- `curation/seed_scope.tsv:56194` contains this identifier with reason `attested rule: Komagataella pastoris DSMZ 70382, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:40173`, whose aggregate count is `1` for `NCBITaxon:638632`.
- The current native GOLD scan found exact organism `Go0005122` for `Komagataella pastoris DSM 70382`.
- Expanding that exact GOLD organism found project `Gp0005122` and the native linked analysis `Komagataella pastoris DSM 70382` through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:638632`; the species-level `Komagataella pastoris` type-material rows carry `DSM 70382`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:638632`, `just validate data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_pastoris_dsmz_70382` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
