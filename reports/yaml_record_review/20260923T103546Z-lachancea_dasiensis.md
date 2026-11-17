# YAML Record Review: Lachancea dasiensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachancea_dasiensis.yaml
- Started UTC: 2026-09-23T10:35:46Z
- Finished UTC: 2026-09-23T10:35:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachancea_dasiensis.yaml` denotes the exact NCBI species `Lachancea dasiensis` as `NCBITaxon:1072105`, rank `SPECIES`, under genus `NCBITaxon:300275` (`Lachancea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachancea_dasiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/laccaria_trichodermophora.yaml data/taxa/eukaryota/lachancea_cidri.yaml data/taxa/eukaryota/lachancea_dasiensis.yaml data/taxa/eukaryota/lachancea_fermentati.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:229718` carries `NCBITaxon:1072105`, label `Lachancea dasiensis`, rank `SPECIES`, parent `NCBITaxon:300275`, genetic code `1`, exact synonym `Lachancea dasiensis C.F. Lee, 2009`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachancea`.
- `curation/seed_scope.tsv:57482` contains this identifier with reason `attested rule: Lachancea dasiensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps five side-inventory old IDs into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1239`, whose aggregate count is `2` for `NCBITaxon:1072105`.
- The current native GOLD scan found exact organisms `Go0039201` and `Go0372907` for `Lachancea dasiensis CBS 10888`.
- Expanding those exact GOLD organisms found projects `Gp0039201`, `Gp0219698`, and `Gp0780232`, plus two native analysis rows linked through the latter two project IDs.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 7 rows for `NCBITaxon:1072105` at lines 4611-4617, covering `ATCC MYA-4748`, `CBS 10888`, and `SC5L02` culture-from-holotype or holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1072105`, `just validate data/taxa/eukaryota/lachancea_dasiensis.yaml`, and `just validate-strict data/taxa/eukaryota/lachancea_dasiensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachancea_dasiensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The NCBI merged-ID side rows were at lines 10189, 82865, 82979, 86364, and 86365 of `data/raw/ncbi_merged_ids.tsv`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
