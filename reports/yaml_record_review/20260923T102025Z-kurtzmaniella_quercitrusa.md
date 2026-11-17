# YAML Record Review: Kurtzmaniella quercitrusa

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml
- Started UTC: 2026-09-23T10:20:25Z
- Finished UTC: 2026-09-23T10:20:25Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml` denotes the exact NCBI species `Kurtzmaniella quercitrusa` as `NCBITaxon:2763128`, rank `SPECIES`, under genus `NCBITaxon:549703` (`Kurtzmaniella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kurtia_argillacea.yaml data/taxa/eukaryota/kurtzmaniella_cleridarum.yaml data/taxa/eukaryota/kurtzmaniella_natalensis.yaml data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:552058` carries `NCBITaxon:2763128`, label `Kurtzmaniella quercitrusa`, rank `SPECIES`, parent `NCBITaxon:549703`, genetic code `12`, exact synonyms `Candida parapsilosis var. quercus` and `Candida quercitrusa`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kurtzmaniella`.
- `curation/seed_scope.tsv:63211` contains this identifier with reason `attested rule: Kurtzmaniella quercitrusa, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:79026` maps side-inventory old ID `NCBITaxon:45578` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:26168`, whose aggregate count is `1` for `NCBITaxon:2763128`.
- The current native GOLD scan found exact organism `Go0705574` for `Kurtzmaniella quercitrusa NRRL Y-5392`.
- Expanding that exact GOLD organism found project `Gp0831618`, with no native linked analysis rows.
- Exact StrainInfo scans found 15 direct strains and 29 deposits for this taxon; exact BacDive and generated raw strain-table scans found no corresponding local BacDive-derived strain rows to overlay.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 16 rows for `NCBITaxon:2763128` at lines 119339-119354, covering `ATCC 56466`, `BCRC 21497`, `CBS 4412`, `CCRC 21497`, `IFO 1022`, `IGC 2703`, `JCM 9832`, and `NRRL Y-5392` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2763128`, `just validate data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml`, and `just validate-strict data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kurtzmaniella_quercitrusa` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
