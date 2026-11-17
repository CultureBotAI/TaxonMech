# YAML Record Review: Kodamaea plutei

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_plutei.yaml
- Started UTC: 2026-09-23T09:50:03Z
- Finished UTC: 2026-09-23T09:50:03Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_plutei.yaml` denotes the exact NCBI species `Kodamaea plutei` as `NCBITaxon:271264`, rank `SPECIES`, under genus `NCBITaxon:77850` (`Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_plutei.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kodamaea_neixiangensis.yaml data/taxa/eukaryota/kodamaea_nitidulidarum.yaml data/taxa/eukaryota/kodamaea_ohmeri.yaml data/taxa/eukaryota/kodamaea_plutei.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56026` carries `NCBITaxon:271264`, label `Kodamaea plutei`, rank `SPECIES`, parent `NCBITaxon:77850`, genetic code `12`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kodamaea`.
- `curation/seed_scope.tsv:54917` contains this identifier with reason `attested rule: Kodamaea plutei, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:25125`, whose aggregate count is `1` for `NCBITaxon:271264`.
- The current native GOLD scan found exact organism `Go0705483` for `Kodamaea plutei NRRL Y-27715`.
- Expanding that exact GOLD organism found project `Gp0831526`, with no native linked analysis rows.
- StrainInfo has 1 exact direct row and 2 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 10 rows for `NCBITaxon:271264` at lines 112521-112530, covering `ATCC MYA-4329`, `BG02-5-27-3-2-1`, `CBS 9885`, and `NRRL Y-27715` culture-from-type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:271264`, `just validate data/taxa/eukaryota/kodamaea_plutei.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_plutei.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_plutei` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
