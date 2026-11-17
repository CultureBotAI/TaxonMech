# YAML Record Review: Leptomonas seymouri BHU1095

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml
- Started UTC: 2026-09-23T12:06:23Z
- Finished UTC: 2026-09-23T12:06:23Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml` denotes the exact NCBI strain `Leptomonas seymouri BHU1095` as `NCBITaxon:1263718`, rank `STRAIN`, under species `NCBITaxon:5684` (`Leptomonas seymouri`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leptographium_lundbergii.yaml data/taxa/eukaryota/leptomonas_pyrrhocoris.yaml data/taxa/eukaryota/leptomonas_seymouri.yaml data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:292591` carries `NCBITaxon:1263718`, label `Leptomonas seymouri BHU1095`, rank `STRAIN`, parent `NCBITaxon:5684`, genetic code `1`, exact synonyms `Leishmania donovani BHU 1095` and `Leishmania donovani Ld BHU 1095`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leptomonas seymouri` species.
- `curation/seed_scope.tsv:58799` contains this identifier with reason `attested rule: Leptomonas seymouri BHU1095, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:6214`, whose aggregate count is `1` for `NCBITaxon:1263718`.
- The current native GOLD scan found exact organism `Go0038935` for `Leptomonas seymouri BHU 1095`, project `Gp0038935`, and one native analysis row linked through `AP PROJECT GOLD IDS` to `Gp0038935`.
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

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1263718`, `just validate data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml`, and `just validate-strict data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leptomonas_seymouri_bhu1095` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
