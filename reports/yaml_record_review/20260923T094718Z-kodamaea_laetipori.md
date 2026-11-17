# YAML Record Review: Kodamaea laetipori

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_laetipori.yaml
- Started UTC: 2026-09-23T09:47:18Z
- Finished UTC: 2026-09-23T09:47:18Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_laetipori.yaml` denotes the exact NCBI species `Kodamaea laetipori` as `NCBITaxon:271274`, rank `SPECIES`, under genus `NCBITaxon:77850` (`Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_laetipori.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kodamaea_kaohsiungensis_nom_inval.yaml data/taxa/eukaryota/kodamaea_laetipori.yaml data/taxa/eukaryota/kodamaea_leandrae.yaml data/taxa/eukaryota/kodamaea_lidongshanica_nom_inval.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56027` carries `NCBITaxon:271274`, label `Kodamaea laetipori`, rank `SPECIES`, parent `NCBITaxon:77850`, genetic code `12`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kodamaea`.
- `curation/seed_scope.tsv:54918` contains this identifier with reason `attested rule: Kodamaea laetipori, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:271276`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:25126`, whose aggregate count is `1` for `NCBITaxon:271274`.
- The current native GOLD scan found exact organism `Go0517157` for `Kodamaea laetipori NRRL Y-27713`.
- Expanding that exact GOLD organism found projects `Gp0441195` and `Gp0780267`; native linked analysis expansion found two rows for `Kodamaea laetipori NRRL Y-27713` through those projects.
- StrainInfo has 3 exact direct rows and 4 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:271274` at lines 112537-112542, covering `BG 02-5-27-4-2-2`, `CBS 9884`, and `NRRL Y-27713` culture-from-type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:271274`, `just validate data/taxa/eukaryota/kodamaea_laetipori.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_laetipori.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_laetipori` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
