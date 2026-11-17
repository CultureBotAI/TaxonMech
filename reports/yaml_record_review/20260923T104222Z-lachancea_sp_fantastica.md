# YAML Record Review: Lachancea sp. 'fantastica'

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachancea_sp_fantastica.yaml
- Started UTC: 2026-09-23T10:42:22Z
- Finished UTC: 2026-09-23T10:42:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachancea_sp_fantastica.yaml` denotes the exact NCBI species `Lachancea sp. 'fantastica'` as `NCBITaxon:1230904`, rank `SPECIES`, under `NCBITaxon:2619250` (`unclassified Lachancea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachancea_sp_fantastica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachancea_nothofagi.yaml data/taxa/eukaryota/lachancea_quebecensis.yaml data/taxa/eukaryota/lachancea_sp_fantastica.yaml data/taxa/eukaryota/lachancea_thermotolerans.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:281038` carries `NCBITaxon:1230904`, label `Lachancea sp. 'fantastica'`, rank `SPECIES`, parent `NCBITaxon:2619250`, genetic code `1`, and the related synonym `Lachancea sp. CBS 6924`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, passing through `unclassified Lachancea` under genus `Lachancea`.
- `curation/seed_scope.tsv:58584` contains this identifier with reason `attested rule: Lachancea sp. 'fantastica', 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:77551` maps side-inventory old ID `NCBITaxon:433476` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5522`, whose aggregate count is `2` for `NCBITaxon:1230904`.
- The current native GOLD scan found exact organisms `Go0039232` and `Go0372903` for `Lachancea sp. 'fantastica' CBS 6924`.
- Expanding those exact GOLD organisms found projects `Gp0039232` and `Gp0219694`, plus one native analysis row linked through `Gp0219694`.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1230904` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1230904`, `just validate data/taxa/eukaryota/lachancea_sp_fantastica.yaml`, and `just validate-strict data/taxa/eukaryota/lachancea_sp_fantastica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachancea_sp_fantastica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
