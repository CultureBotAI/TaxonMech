# YAML Record Review: Lodderomyces orthopsilosis AY2

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml
- Started UTC: 2026-09-23T13:34:22Z
- Finished UTC: 2026-09-23T13:34:22Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml` denotes the exact NCBI strain `Lodderomyces orthopsilosis AY2` as `NCBITaxon:1213353`, rank `STRAIN`, under species `NCBITaxon:273371` (`Lodderomyces orthopsilosis`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml data/taxa/eukaryota/lodderomyces_orthopsilosis_co_90_125.yaml data/taxa/eukaryota/lodderomyces_oxycetoniae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:274433` carries `NCBITaxon:1213353`, label `Lodderomyces orthopsilosis AY2`, rank `STRAIN`, parent `NCBITaxon:273371`, genetic code `12`, no synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lodderomyces orthopsilosis` species.
- `curation/seed_scope.tsv:58423` contains this identifier with reason `attested rule: Lodderomyces orthopsilosis AY2, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:1213353`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5075`, whose aggregate count is `1` for `NCBITaxon:1213353`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0039261`, and one linked project, `Gp0039261`.
- The native GOLD analyses scan found one row linked through `Gp0039261`.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The exact NCBI type-material scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:1213353`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1213353`, `just validate data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml`, and `just validate-strict data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lodderomyces_orthopsilosis_ay2` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
