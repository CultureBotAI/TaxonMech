# YAML Record Review: Liangdongia dendrica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/liangdongia_dendrica.yaml
- Started UTC: 2026-09-23T12:23:01Z
- Finished UTC: 2026-09-23T12:23:01Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/liangdongia_dendrica.yaml` denotes the exact NCBI species `Liangdongia dendrica` as `NCBITaxon:49324`, rank `SPECIES`, under genus `NCBITaxon:3712556` (`Liangdongia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/liangdongia_dendrica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/liangdongia_dendrica.yaml data/taxa/eukaryota/liangdongia_dryadoides.yaml data/taxa/eukaryota/liangdongia_quercuum.yaml data/taxa/eukaryota/libkindia_masarykiana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6275` carries `NCBITaxon:49324`, label `Liangdongia dendrica`, rank `SPECIES`, parent `NCBITaxon:3712556`, genetic code `1`, exact synonyms `Candida dendrica` and `Torulopsis dendrica`, three related synonyms, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Liangdongia` genus.
- `curation/seed_scope.tsv:52799` contains this identifier with reason `attested rule: Liangdongia dendrica, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37168`, whose aggregate count is `1` for `NCBITaxon:49324`.
- The current native GOLD scan found exact organism `Go0705643` for `Candida dendrica NRRL Y-7775`, project `Gp0831691`, and no exact native analysis rows for this NCBI ID.
- Exact StrainInfo scans found 3 direct strains and 13 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:223456` through `223473` contain 18 holotype or culture-from-holotype spellings for `Torulopsis dendrica`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:49324`, `just validate data/taxa/eukaryota/liangdongia_dendrica.yaml`, and `just validate-strict data/taxa/eukaryota/liangdongia_dendrica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `liangdongia_dendrica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
