# YAML Record Review: Lactifluus subvellereus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactifluus_subvellereus.yaml
- Started UTC: 2026-09-23T11:09:43Z
- Finished UTC: 2026-09-23T11:09:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactifluus_subvellereus.yaml` denotes the exact NCBI species `Lactifluus subvellereus` as `NCBITaxon:1837270`, rank `SPECIES`, under genus `NCBITaxon:596919` (`Lactifluus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactifluus_subvellereus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactifluus_subvellereus.yaml data/taxa/eukaryota/lactifluus_volemus.yaml data/taxa/eukaryota/laetiporus_sulphureus.yaml data/taxa/eukaryota/lagenidium_giganteum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:479105` carries `NCBITaxon:1837270`, label `Lactifluus subvellereus`, rank `SPECIES`, parent `NCBITaxon:596919`, genetic code `1`, exact synonym `Lactarius subvellereus`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactifluus`.
- `curation/seed_scope.tsv:61343` contains this identifier with reason `attested rule: Lactifluus subvellereus, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:1837270`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:16292`, whose aggregate count is `1` for `NCBITaxon:1837270`.
- The current native GOLD scan found exact organism `Go0146565` for `Lactifluus subvellereus BPL653`.
- Expanding that exact GOLD organism found projects `Gp0155237` and `Gp0197032` and no native analysis rows.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1837270` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1837270`, `just validate data/taxa/eukaryota/lactifluus_subvellereus.yaml`, and `just validate-strict data/taxa/eukaryota/lactifluus_subvellereus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactifluus_subvellereus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
