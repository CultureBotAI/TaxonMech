# YAML Record Review: Leptoxyphium fumago

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leptoxyphium_fumago.yaml
- Started UTC: 2026-09-23T12:08:34Z
- Finished UTC: 2026-09-23T12:08:34Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leptoxyphium_fumago.yaml` denotes the exact NCBI species `Leptoxyphium fumago` as `NCBITaxon:5474`, rank `SPECIES`, under genus `NCBITaxon:5473` (`Leptoxyphium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leptoxyphium_fumago.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leptoporus_mollis.yaml data/taxa/eukaryota/leptosphaeria_microscopica.yaml data/taxa/eukaryota/leptosphaerulina_australis.yaml data/taxa/eukaryota/leptoxyphium_fumago.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2424` carries `NCBITaxon:5474`, label `Leptoxyphium fumago`, rank `SPECIES`, parent `NCBITaxon:5473`, genetic code `1`, exact synonym `Caldariomyces fumago`, two related synonyms, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leptoxyphium` genus.
- `curation/seed_scope.tsv:52002` contains this identifier with reason `attested rule: Leptoxyphium fumago, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38476`, whose aggregate count is `1` for `NCBITaxon:5474`.
- The current native GOLD scan found exact organism `Go0384551` for `Leptoxyphium fumago SC3815`, project `Gp0235660`, and one native analysis row linked through `AP PROJECT GOLD IDS` to `Gp0235660`.
- Exact StrainInfo scans found 7 direct strains and 17 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The NCBI type-material scan found 0 rows for this taxon, matching the absence of type-material-specific output in the generated record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:5474`, `just validate data/taxa/eukaryota/leptoxyphium_fumago.yaml`, and `just validate-strict data/taxa/eukaryota/leptoxyphium_fumago.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leptoxyphium_fumago` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
