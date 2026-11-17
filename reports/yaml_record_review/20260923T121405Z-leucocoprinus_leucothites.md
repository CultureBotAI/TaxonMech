# YAML Record Review: Leucocoprinus leucothites

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leucocoprinus_leucothites.yaml
- Started UTC: 2026-09-23T12:14:05Z
- Finished UTC: 2026-09-23T12:14:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leucocoprinus_leucothites.yaml` denotes the exact NCBI species `Leucocoprinus leucothites` as `NCBITaxon:201217`, rank `SPECIES`, under genus `NCBITaxon:34431` (`Leucocoprinus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leucocoprinus_leucothites.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leucocoprinus_gongylophorus.yaml data/taxa/eukaryota/leucocoprinus_leucothites.yaml data/taxa/eukaryota/leucocoprinus_nympharum.yaml data/taxa/eukaryota/leucogyrophana_mollusca.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:39780` carries `NCBITaxon:201217`, label `Leucocoprinus leucothites`, rank `SPECIES`, parent `NCBITaxon:34431`, genetic code `1`, four exact synonyms, three related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leucocoprinus` genus.
- `curation/seed_scope.tsv:54453` contains this identifier with reason `attested rule: Leucocoprinus leucothites, 2 sources incl. NCBI`.
- The side NCBI merge scan found old ID `NCBITaxon:2364573` retired into `NCBITaxon:201217`; an ignored-inclusive `rg --no-ignore --hidden` search found no retained row for that old ID in `data/raw/ncbitaxon_taxa.tsv`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:18581`, whose aggregate count is `1` for `NCBITaxon:201217`.
- The current native GOLD scan found exact organism `Go0631693` for `Leucoagaricus leucothites CBS 146.42`, project `Gp0645255`, and one native analysis row linked through `AP PROJECT GOLD IDS` to `Gp0645255`.
- Exact StrainInfo scans found 6 direct strains and 6 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

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

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:201217`, `just validate data/taxa/eukaryota/leucocoprinus_leucothites.yaml`, and `just validate-strict data/taxa/eukaryota/leucocoprinus_leucothites.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leucocoprinus_leucothites` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
