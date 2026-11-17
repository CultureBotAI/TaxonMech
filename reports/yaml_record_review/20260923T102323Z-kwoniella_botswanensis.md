# YAML Record Review: Kwoniella botswanensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kwoniella_botswanensis.yaml
- Started UTC: 2026-09-23T10:23:23Z
- Finished UTC: 2026-09-23T10:23:23Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kwoniella_botswanensis.yaml` denotes the exact NCBI species `Kwoniella botswanensis` as `NCBITaxon:1268659`, rank `SPECIES`, under genus `NCBITaxon:490731` (`Kwoniella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kwoniella_botswanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kurtzmaniella_sp_pg3605.yaml data/taxa/eukaryota/kurtzmaniella_sp_r2202.yaml data/taxa/eukaryota/kurtzmanomyces_insolitus.yaml data/taxa/eukaryota/kwoniella_botswanensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:294584` carries `NCBITaxon:1268659`, label `Kwoniella botswanensis`, rank `SPECIES`, parent `NCBITaxon:490731`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kwoniella`.
- `curation/seed_scope.tsv:58845` contains this identifier with reason `attested rule: Kwoniella botswanensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1247710`, `NCBITaxon:1295529`, `NCBITaxon:1295530`, and `NCBITaxon:1295536` into this current taxon, but no retained raw NCBI taxon row exists for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:6398`, whose aggregate count is `1` for `NCBITaxon:1268659`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:1268659`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 rows for `NCBITaxon:1268659` at lines 18220-18223, covering `CBS 12716` and `PYCC 6332` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1268659`, `just validate data/taxa/eukaryota/kwoniella_botswanensis.yaml`, and `just validate-strict data/taxa/eukaryota/kwoniella_botswanensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kwoniella_botswanensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact catalogs are side evidence only and can differ from the retained aggregate used to generate source attestations.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
