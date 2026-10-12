# YAML Record Review: Leucogyrophana mollusca

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leucogyrophana_mollusca.yaml
- Started UTC: 2026-09-23T12:14:05Z
- Finished UTC: 2026-09-23T12:14:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leucogyrophana_mollusca.yaml` denotes the exact NCBI species `Leucogyrophana mollusca` as `NCBITaxon:85980`, rank `SPECIES`, under genus `NCBITaxon:85978` (`Leucogyrophana`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leucogyrophana_mollusca.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml data/taxa/eukaryota/leucocoprinus_leucothites.yaml data/taxa/eukaryota/leucocoprinus_nympharum.yaml data/taxa/eukaryota/leucogyrophana_mollusca.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13288` carries `NCBITaxon:85980`, label `Leucogyrophana mollusca`, rank `SPECIES`, parent `NCBITaxon:85978`, genetic code `1`, exact synonym `Merulius molluscus`, two related synonyms, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leucogyrophana` genus.
- `curation/seed_scope.tsv:53428` contains this identifier with reason `attested rule: Leucogyrophana mollusca, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:43336`, whose aggregate count is `3` for `NCBITaxon:85980`.
- The current native GOLD expansion found exact organisms `Go0036250` and `Go0527218`, 8 exact projects, and one native analysis row linked through `AP PROJECT GOLD IDS` to `Gp0036250`.
- Exact StrainInfo scans found 9 direct strains and 11 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

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

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:85980`, `just validate data/taxa/eukaryota/leucogyrophana_mollusca.yaml`, and `just validate-strict data/taxa/eukaryota/leucogyrophana_mollusca.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leucogyrophana_mollusca` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
