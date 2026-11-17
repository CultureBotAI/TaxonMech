# YAML Record Review: Kuraishia floccosa

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kuraishia_floccosa.yaml
- Started UTC: 2026-09-23T10:14:15Z
- Finished UTC: 2026-09-23T10:14:15Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kuraishia_floccosa.yaml` denotes the exact NCBI species `Kuraishia floccosa` as `NCBITaxon:181602`, rank `SPECIES`, under genus `NCBITaxon:317045` (`Kuraishia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kuraishia_floccosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kuraishia_borneana.yaml data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml data/taxa/eukaryota/kuraishia_cidri.yaml data/taxa/eukaryota/kuraishia_floccosa.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:36407` carries `NCBITaxon:181602`, label `Kuraishia floccosa`, rank `SPECIES`, parent `NCBITaxon:317045`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kuraishia`.
- `curation/seed_scope.tsv:54357` contains this identifier with reason `attested rule: Kuraishia floccosa, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:58835` maps side-inventory old ID `NCBITaxon:2963369` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:16086`, whose aggregate count is `1` for `NCBITaxon:181602`.
- The current native GOLD scan found exact organism `Go0705512` for `Kuraishia floccosa NRRL Y-27951`.
- Expanding that exact GOLD organism found project `Gp0831555`, with no native linked analysis rows.
- StrainInfo has 1 exact direct row and 3 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:181602` at lines 61980-61985, covering `CBS 10307`, `NCAIM Y.01581`, and `NRRL Y-27951` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:181602`, `just validate data/taxa/eukaryota/kuraishia_floccosa.yaml`, and `just validate-strict data/taxa/eukaryota/kuraishia_floccosa.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kuraishia_floccosa` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
