# YAML Record Review: Lactarius quietus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_quietus.yaml
- Started UTC: 2026-09-23T10:57:31Z
- Finished UTC: 2026-09-23T10:57:31Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_quietus.yaml` denotes the exact NCBI species `Lactarius quietus` as `NCBITaxon:111141`, rank `SPECIES`, under genus `NCBITaxon:34444` (`Lactarius`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_quietus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactarius_lignyotus.yaml data/taxa/eukaryota/lactarius_psammicola.yaml data/taxa/eukaryota/lactarius_pseudohatsudake.yaml data/taxa/eukaryota/lactarius_quietus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:20150` carries `NCBITaxon:111141`, label `Lactarius quietus`, rank `SPECIES`, parent `NCBITaxon:34444`, genetic code `1`, exact synonym `Agaricus quietus`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactarius`.
- `curation/seed_scope.tsv:53775` contains this identifier with reason `attested rule: Lactarius quietus, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:2008`, whose aggregate count is `2` for `NCBITaxon:111141`.
- The current native GOLD scan found exact organisms `Go0010105` and `Go0010106` for `Lactarius quietus` strains `SC23` and `S23C`.
- Expanding those exact GOLD organisms found eight projects: `Gp0010105`, `Gp0010106`, and `Gp0333599` through `Gp0333604`, with no native analysis rows linked through those project IDs.
- Exact StrainInfo scans found 3 direct strains and 3 deposits for this taxon; exact BacDive and generated StrainInfo overlay scans found no corresponding local BacDive-derived rows to emit.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:111141` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:111141`, `just validate data/taxa/eukaryota/lactarius_quietus.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_quietus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_quietus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
