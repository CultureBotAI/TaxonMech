# YAML Record Review: Kuraishia cidri

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kuraishia_cidri.yaml
- Started UTC: 2026-09-23T10:14:15Z
- Finished UTC: 2026-09-23T10:14:15Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kuraishia_cidri.yaml` denotes the exact NCBI species `Kuraishia cidri` as `NCBITaxon:1538149`, rank `SPECIES`, under genus `NCBITaxon:317045` (`Kuraishia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kuraishia_cidri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kuraishia_borneana.yaml data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml data/taxa/eukaryota/kuraishia_cidri.yaml data/taxa/eukaryota/kuraishia_floccosa.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:396302` carries `NCBITaxon:1538149`, label `Kuraishia cidri`, rank `SPECIES`, parent `NCBITaxon:317045`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kuraishia`.
- `curation/seed_scope.tsv:60419` contains this identifier with reason `attested rule: Kuraishia cidri, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:148632` and `NCBITaxon:155888` into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12224`, whose aggregate count is `1` for `NCBITaxon:1538149`.
- The current native GOLD scan found exact organism `Go0705389` for `Kuraishia cidri NRRL Y-27078`.
- Expanding that exact GOLD organism found project `Gp0831432`, with no native linked analysis rows.
- StrainInfo has 2 exact direct rows and 5 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 10 rows for `NCBITaxon:1538149` at lines 40539-40548, covering `CBS 4241`, `NCYC 3098`, and `NRRL Y-27078` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1538149`, `just validate data/taxa/eukaryota/kuraishia_cidri.yaml`, and `just validate-strict data/taxa/eukaryota/kuraishia_cidri.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kuraishia_cidri` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
