# YAML Record Review: Isabelozyma gotoi

- Repository: TaxonMech
- Record: data/taxa/eukaryota/isabelozyma_gotoi.yaml
- Started UTC: 2026-09-23T08:47:24Z
- Finished UTC: 2026-09-23T08:47:24Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/isabelozyma_gotoi.yaml` denotes `Isabelozyma gotoi` as `NCBITaxon:87895`, rank `SPECIES`, under parent `NCBITaxon:3312684` (`Isabelozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/isabelozyma_gotoi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/irpex_rosettiformis.yaml data/taxa/eukaryota/isabelozyma_gotoi.yaml data/taxa/eukaryota/isabelozyma_heimii.yaml data/taxa/eukaryota/isabelozyma_pseudorhagii.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13863` carries `NCBITaxon:87895`, label `Isabelozyma gotoi`, rank `SPECIES`, parent `NCBITaxon:3312684`, genetic code `12`, exact synonyms `Candida gotoi|Hyphopichia gotoi`, and the three related synonyms emitted in YAML.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:53463` contains this identifier with reason `attested rule: Isabelozyma gotoi, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:43718`, whose aggregate count is `1` for `NCBITaxon:87895`.
- The current native GOLD organism scan found exact organism `Go0517043` for `Hyphopichia gotoi NRRL Y-27225`, with project `Gp0441081` and analysis `Hyphopichia gotoi NRRL Y-27225` joined through `AP PROJECT GOLD IDS=Gp0441081`.
- Exact `data/raw/ncbi_type_material.tsv` rows 270396-270401 record 6 `Candida gotoi` culture-from-type-material designations for `CBS 8531`, `JCM 10145`, and `NRRL Y-27225` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material and exact StrainInfo deposit strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has one exact direct SI record and seven exact deposits, but no final assembly, exclusion, or related-record rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:87895`, `just validate data/taxa/eukaryota/isabelozyma_gotoi.yaml`, and `just validate-strict data/taxa/eukaryota/isabelozyma_gotoi.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `isabelozyma_gotoi` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
