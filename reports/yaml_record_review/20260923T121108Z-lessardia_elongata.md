# YAML Record Review: Lessardia elongata

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lessardia_elongata.yaml
- Started UTC: 2026-09-23T12:11:08Z
- Finished UTC: 2026-09-23T12:11:08Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lessardia_elongata.yaml` denotes the exact NCBI species `Lessardia elongata` as `NCBITaxon:210733`, rank `SPECIES`, under genus `NCBITaxon:210732` (`Lessardia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lessardia_elongata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leratiomyces_ceres.yaml data/taxa/eukaryota/leratiomyces_erythrocephalus.yaml data/taxa/eukaryota/lessardia_elongata.yaml data/taxa/eukaryota/leucangium_carthusianum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:41540` carries `NCBITaxon:210733`, label `Lessardia elongata`, rank `SPECIES`, parent `NCBITaxon:210732`, genetic code `1`, related synonym `Lessardia elongata Saldarriaga & F.J.R.Taylor, 2003`, and snapshot `2026-09-13`.
- The 9 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lessardia` genus.
- `curation/seed_scope.tsv:54522` contains this identifier with reason `attested rule: Lessardia elongata, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:20134`, whose aggregate count is `1` for `NCBITaxon:210733`.
- The current native GOLD scan found exact organism `Go0368721` for `Lessardia elongata SPMC 104` and no exact native projects or analysis rows for this NCBI ID.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The NCBI type-material scan found 0 rows for this taxon, matching the absence of type-material-specific output in the generated record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:210733`, `just validate data/taxa/eukaryota/lessardia_elongata.yaml`, and `just validate-strict data/taxa/eukaryota/lessardia_elongata.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lessardia_elongata` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
