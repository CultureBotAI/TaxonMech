# YAML Record Review: Kurtzmaniella sp. PG3605

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml
- Started UTC: 2026-09-23T10:23:23Z
- Finished UTC: 2026-09-23T10:23:23Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml` denotes the exact NCBI species-level placeholder `Kurtzmaniella sp. PG3605` as `NCBITaxon:2940388`, rank `SPECIES`, under `NCBITaxon:2649086` (`unclassified Kurtzmaniella`) within genus `NCBITaxon:549703` (`Kurtzmaniella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml data/taxa/eukaryota/kurtzmaniella_sp_r2202.yaml data/taxa/eukaryota/kurtzmanomyces_insolitus.yaml data/taxa/eukaryota/kwoniella_botswanensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:574602` carries `NCBITaxon:2940388`, label `Kurtzmaniella sp. PG3605`, rank `SPECIES`, parent `NCBITaxon:2649086`, genetic code `12`, exact synonym `Aspergillus sp. PG3605`, and the NCBI synonym set retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected no-rank `unclassified Kurtzmaniella` node.
- `curation/seed_scope.tsv:63459` contains this identifier with reason `attested rule: Kurtzmaniella sp. PG3605, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:29130`, whose aggregate count is `1` for `NCBITaxon:2940388`.
- The current native GOLD scan found exact organism `Go0657566` for `Aspergillus sp. PG3605 2NP920`.
- Expanding that exact GOLD organism found project `Gp0701834` and one native analysis row linked through that project ID.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:2940388`, matching the absence of type-material derived strain assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2940388`, `just validate data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml`, and `just validate-strict data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kurtzmaniella_sp_pg3605` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
