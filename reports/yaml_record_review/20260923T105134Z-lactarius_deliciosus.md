# YAML Record Review: Lactarius deliciosus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_deliciosus.yaml
- Started UTC: 2026-09-23T10:51:34Z
- Finished UTC: 2026-09-23T10:51:34Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_deliciosus.yaml` denotes the exact NCBI species `Lactarius deliciosus` as `NCBITaxon:55514`, rank `SPECIES`, under genus `NCBITaxon:34444` (`Lactarius`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_deliciosus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachnum_pygmaeum.yaml data/taxa/eukaryota/lactarius_akahatsu.yaml data/taxa/eukaryota/lactarius_controversus.yaml data/taxa/eukaryota/lactarius_deliciosus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7021` carries `NCBITaxon:55514`, label `Lactarius deliciosus`, rank `SPECIES`, parent `NCBITaxon:34444`, genetic code `1`, exact synonym `Agaricus deliciosus`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactarius`.
- `curation/seed_scope.tsv:52947` contains this identifier with reason `attested rule: Lactarius deliciosus, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38704`, whose aggregate count is `2` for `NCBITaxon:55514`.
- The current native GOLD scan found exact organisms `Go0411490` and `Go0518064` for `Lactarius deliciosus` strains `48` and `MG9`.
- Expanding those exact GOLD organisms found projects `Gp0305063`, `Gp0306811`, and `Gp0442133`, plus two native analysis rows linked through `Gp0305063` and `Gp0442133`.
- Exact StrainInfo scans found 17 direct strains and 26 deposits for this taxon; exact BacDive and generated StrainInfo overlay scans found no corresponding local BacDive-derived rows to emit.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:55514` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:55514`, `just validate data/taxa/eukaryota/lactarius_deliciosus.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_deliciosus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_deliciosus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
