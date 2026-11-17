# YAML Record Review: Jimgerdemannia flammicorona

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml
- Started UTC: 2026-09-23T09:02:07Z
- Finished UTC: 2026-09-23T09:02:07Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml` denotes the exact NCBI species `Jimgerdemannia flammicorona` as `NCBITaxon:994334`, rank `SPECIES`, under genus `NCBITaxon:2052799` (`Jimgerdemannia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jaminaea_rosea.yaml data/taxa/eukaryota/jianyunia_sakaguchii.yaml data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml data/taxa/eukaryota/juglanconis_oblonga.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:207033` carries `NCBITaxon:994334`, label `Jimgerdemannia flammicorona`, rank `SPECIES`, parent `NCBITaxon:2052799`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Jimgerdemannia`.
- `curation/seed_scope.tsv:57115` contains this identifier with reason `attested rule: Jimgerdemannia flammicorona, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:45448`, whose aggregate count is `2` for `NCBITaxon:994334`.
- The current native GOLD scan found exact organisms `Go0141628` for `Jimgerdemannia flammicorona GMNB39` and `Go0141630` for `Jimgerdemannia flammicorona AD002`.
- Expanding those exact GOLD organisms found projects `Gp0147020` and `Gp0147022`.
- The native GOLD analysis scan found linked analyses for `Jimgerdemannia flammicorona GMNB39 Standard Draft` through `Gp0147020` and `Jimgerdemannia flammicorona AD002 Standard Draft` through `Gp0147022`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 isotype rows for `NCBITaxon:994334` at lines 276877-276880, all `MICH 13760` spelling variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:994334`, `just validate data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml`, and `just validate-strict data/taxa/eukaryota/jimgerdemannia_flammicorona.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jimgerdemannia_flammicorona` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
