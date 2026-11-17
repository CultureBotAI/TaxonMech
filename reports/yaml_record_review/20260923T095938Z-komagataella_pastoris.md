# YAML Record Review: Komagataella pastoris

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_pastoris.yaml
- Started UTC: 2026-09-23T09:59:38Z
- Finished UTC: 2026-09-23T09:59:38Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataella_pastoris.yaml` denotes the exact NCBI species `Komagataella pastoris` as `NCBITaxon:4922`, rank `SPECIES`, under genus `NCBITaxon:460517` (`Komagataella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_pastoris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_kurtzmanii.yaml data/taxa/eukaryota/komagataella_mondaviorum.yaml data/taxa/eukaryota/komagataella_pastoris.yaml data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2143` carries `NCBITaxon:4922`, label `Komagataella pastoris`, rank `SPECIES`, parent `NCBITaxon:460517`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataella`.
- `curation/seed_scope.tsv:51878` contains this identifier with reason `attested rule: Komagataella pastoris, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:2898212` and `NCBITaxon:460518` into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37137`, whose aggregate count is `39` for `NCBITaxon:4922`.
- The current native GOLD scan found 40 exact organism rows: one strainless base organism, 31 JPS strain rows, and 8 named-strain rows including `Go0350720` for `ATCC 28485`, `Go0608177` for `CBS 704`, and `Go0608180` for `NRRL Y-1603`.
- Expanding those exact GOLD organisms found 36 projects and 34 native linked analysis rows through `AP PROJECT GOLD IDS`.
- StrainInfo has 151 exact direct rows and 205 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 16 rows for `NCBITaxon:4922` at lines 223108-223123, covering `CBS 704` and `NRRL Y-1603` culture-from-type-material variants plus `ATCC 28485`, `BCRC 21531`, `CCRC 21531`, `DSM 70382`, `JCM 3650`, and `NCYC 175` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:4922`, `just validate data/taxa/eukaryota/komagataella_pastoris.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_pastoris.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_pastoris` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The generated assertion count follows `data/raw/gold_organisms.tsv`; the current native exact scan contains one additional strainless base GOLD organism row.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
