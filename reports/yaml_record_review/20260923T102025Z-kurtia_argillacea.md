# YAML Record Review: Kurtia argillacea

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kurtia_argillacea.yaml
- Started UTC: 2026-09-23T10:20:25Z
- Finished UTC: 2026-09-23T10:20:25Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kurtia_argillacea.yaml` denotes the exact NCBI species `Kurtia argillacea` as `NCBITaxon:1882863`, rank `SPECIES`, under genus `NCBITaxon:1882866` (`Kurtia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kurtia_argillacea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kurtia_argillacea.yaml data/taxa/eukaryota/kurtzmaniella_cleridarum.yaml data/taxa/eukaryota/kurtzmaniella_natalensis.yaml data/taxa/eukaryota/kurtzmaniella_quercitrusa.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:490325` carries `NCBITaxon:1882863`, label `Kurtia argillacea`, rank `SPECIES`, parent `NCBITaxon:1882866`, genetic code `1`, exact synonym `Corticium argillaceum`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kurtia`.
- `curation/seed_scope.tsv:61434` contains this identifier with reason `attested rule: Kurtia argillacea, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:16919`, whose aggregate count is `1` for `NCBITaxon:1882863`.
- The current native GOLD scan found exact organism `Go0496723` for `Kurtia argillacea OMC1749`.
- Expanding that exact GOLD organism found projects `Gp0397260` and `Gp0400803`, with no native linked analysis rows.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:1882863`, matching the absence of type-material derived strain assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1882863`, `just validate data/taxa/eukaryota/kurtia_argillacea.yaml`, and `just validate-strict data/taxa/eukaryota/kurtia_argillacea.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kurtia_argillacea` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
