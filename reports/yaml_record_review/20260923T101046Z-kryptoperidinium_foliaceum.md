# YAML Record Review: Kryptoperidinium foliaceum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml
- Started UTC: 2026-09-23T10:10:46Z
- Finished UTC: 2026-09-23T10:10:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml` denotes the exact NCBI species `Kryptoperidinium foliaceum` as `NCBITaxon:160619`, rank `SPECIES`, under genus `NCBITaxon:160618` (`Kryptoperidinium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kretzschmaria_hedjaroudei.yaml data/taxa/eukaryota/kretzschmaria_zonata.yaml data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:33118` carries `NCBITaxon:160619`, label `Kryptoperidinium foliaceum`, rank `SPECIES`, parent `NCBITaxon:160618`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 9 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kryptoperidinium`.
- `curation/seed_scope.tsv:54179` contains this identifier with reason `attested rule: Kryptoperidinium foliaceum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:77126` maps side-inventory old ID `NCBITaxon:425802` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12992`, whose aggregate count is `2` for `NCBITaxon:160619`.
- The current native GOLD scan found exact organisms `Go0368715` for `Kryptoperidinium foliaceum CCAP 1116/3` and `Go0368716` for `Kryptoperidinium foliaceum CCMP 1326`.
- Expanding those exact GOLD organisms found no native linked project or analysis rows.
- StrainInfo has 3 exact direct rows and 3 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:160619`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:160619`, `just validate data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml`, and `just validate-strict data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kryptoperidinium_foliaceum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
