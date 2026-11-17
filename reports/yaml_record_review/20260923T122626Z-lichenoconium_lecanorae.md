# YAML Record Review: Lichenoconium lecanorae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lichenoconium_lecanorae.yaml
- Started UTC: 2026-09-23T12:26:26Z
- Finished UTC: 2026-09-23T12:26:26Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lichenoconium_lecanorae.yaml` denotes the exact NCBI species `Lichenoconium lecanorae` as `NCBITaxon:977788`, rank `SPECIES`, under genus `NCBITaxon:977787` (`Lichenoconium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lichenoconium_lecanorae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lichenoconium_lecanorae.yaml data/taxa/eukaryota/lichenostigmatales_sp.yaml data/taxa/eukaryota/lichtheimia_blakesleeana.yaml data/taxa/eukaryota/lichtheimia_corymbifera.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:203959` carries `NCBITaxon:977788`, label `Lichenoconium lecanorae`, rank `SPECIES`, parent `NCBITaxon:977787`, genetic code `1`, exact synonym `Coniosporium lecanorae`, two related synonyms, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lichenoconium` genus.
- `curation/seed_scope.tsv:57032` contains this identifier with reason `attested rule: Lichenoconium lecanorae, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:45164`, whose aggregate count is `1` for `NCBITaxon:977788`.
- The current native GOLD scan found no exact organism, project, or analysis rows for this NCBI ID.
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

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:977788`, `just validate data/taxa/eukaryota/lichenoconium_lecanorae.yaml`, and `just validate-strict data/taxa/eukaryota/lichenoconium_lecanorae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lichenoconium_lecanorae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
