# YAML Record Review: Kuraishia capsulata CBS 1993

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml
- Started UTC: 2026-09-23T10:14:15Z
- Finished UTC: 2026-09-23T10:14:15Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml` denotes the exact NCBI strain `Kuraishia capsulata CBS 1993` as `NCBITaxon:1382522`, rank `STRAIN`, under species `NCBITaxon:317047` (`Kuraishia capsulata`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kuraishia_borneana.yaml data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml data/taxa/eukaryota/kuraishia_cidri.yaml data/taxa/eukaryota/kuraishia_floccosa.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:337703` carries `NCBITaxon:1382522`, label `Kuraishia capsulata CBS 1993`, rank `STRAIN`, parent `NCBITaxon:317047`, genetic code `1`, and exact synonym `Kuraishia capsulata CBS1993` as retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected species `Kuraishia capsulata`.
- `curation/seed_scope.tsv:59733` contains this identifier with reason `attested rule: Kuraishia capsulata CBS 1993, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8978`, whose aggregate count is `8` for `NCBITaxon:1382522`.
- The current native GOLD scan found 9 exact organism rows, including `Go0100965` for `Kuraishia capsulata CBS 1993` and eight additional `Kuraishia capsulata` strain rows from `ATCC 24204` through `UCD 50-340`.
- Expanding those exact GOLD organisms found projects `Gp0100965` and `Gp0831405`, with one native linked analysis for `Kuraishia capsulata CBS 1993` through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:1382522`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1382522`, `just validate data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml`, and `just validate-strict data/taxa/eukaryota/kuraishia_capsulata_cbs_1993.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kuraishia_capsulata_cbs_1993` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The generated assertion count follows `data/raw/gold_organisms.tsv`; the current native exact GOLD JSONL scan contains one additional exact organism row for this NCBI ID.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
