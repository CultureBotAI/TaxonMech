# YAML Record Review: Kirkomyces cordensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kirkomyces_cordensis.yaml
- Started UTC: 2026-09-23T09:19:22Z
- Finished UTC: 2026-09-23T09:19:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kirkomyces_cordensis.yaml` denotes the exact NCBI species `Kirkomyces cordensis` as `NCBITaxon:562975`, rank `SPECIES`, under genus `NCBITaxon:101139` (`Kirkomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kirkomyces_cordensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kickxella_alabastrina.yaml data/taxa/eukaryota/kiflimonium_junci.yaml data/taxa/eukaryota/kipferlia_bialata.yaml data/taxa/eukaryota/kirkomyces_cordensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:132120` carries `NCBITaxon:562975`, label `Kirkomyces cordensis`, rank `SPECIES`, parent `NCBITaxon:101139`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kirkomyces`.
- `curation/seed_scope.tsv:56042` contains this identifier with reason `attested rule: Kirkomyces cordensis, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:101140`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38876`, whose aggregate count is `1` for `NCBITaxon:562975`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:562975`.
- StrainInfo has 1 exact direct row and 5 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 2 culture-from-isotype rows for `NCBITaxon:562975`: `CBS 223.63` and `CBS:223.63`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:562975`, `just validate data/taxa/eukaryota/kirkomyces_cordensis.yaml`, and `just validate-strict data/taxa/eukaryota/kirkomyces_cordensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kirkomyces_cordensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
