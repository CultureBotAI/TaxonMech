# YAML Record Review: Kluyveromyces marxianus var. marxianus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kluyveromyces_marxianus_var_marxianus.yaml
- Started UTC: 2026-09-23T09:26:19Z
- Finished UTC: 2026-09-23T09:26:19Z
- Verdict: pass

## Target

Generated eukaryote varietas record `data/taxa/eukaryota/kluyveromyces_marxianus_var_marxianus.yaml` denotes the exact NCBI variety `Kluyveromyces marxianus var. marxianus` as `NCBITaxon:374272`, rank `VARIETAS`, under species `NCBITaxon:4911` (`Kluyveromyces marxianus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kluyveromyces_marxianus_var_marxianus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_marxianus_var_marxianus.yaml data/taxa/eukaryota/kluyveromyces_nonfermentans.yaml data/taxa/eukaryota/kluyveromyces_siamensis.yaml data/taxa/eukaryota/kluyveromyces_starmeri.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:78473` carries `NCBITaxon:374272`, label `Kluyveromyces marxianus var. marxianus`, rank `VARIETAS`, parent `NCBITaxon:4911`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the parent species `Kluyveromyces marxianus`.
- `curation/seed_scope.tsv:55399` contains this identifier with reason `attested rule: Kluyveromyces marxianus var. marxianus, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:1162310` and `NCBITaxon:1608288`, but neither old ID is present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33671`, whose aggregate count is `1` for `NCBITaxon:374272`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:374272`.
- StrainInfo has 59 exact direct rows and 152 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 18 rows for `NCBITaxon:374272` at lines 197936-197953, covering `CBS 712` and `NRRL Y-8281` cultures from type material plus `BCRC 21499`, `CCRC 21499`, `DBVPG 6165`, `IFO 10005`, `IGC 3886`, `MUCL 46196`, and `UCD 55-82` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:374272`, `just validate data/taxa/eukaryota/kluyveromyces_marxianus_var_marxianus.yaml`, and `just validate-strict data/taxa/eukaryota/kluyveromyces_marxianus_var_marxianus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kluyveromyces_marxianus_var_marxianus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
