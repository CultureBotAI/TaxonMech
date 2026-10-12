# YAML Record Review: Kryptoperidinium triquetrum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml
- Started UTC: 2026-09-23T10:10:46Z
- Finished UTC: 2026-09-23T10:10:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml` denotes the exact NCBI species `Kryptoperidinium triquetrum` as `NCBITaxon:66468`, rank `SPECIES`, under genus `NCBITaxon:160618` (`Kryptoperidinium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kretzschmaria_hedjaroudei.yaml data/taxa/eukaryota/kretzschmaria_zonata.yaml data/taxa/eukaryota/kryptoperidinium_foliaceum.yaml data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8693` carries `NCBITaxon:66468`, label `Kryptoperidinium triquetrum`, rank `SPECIES`, parent `NCBITaxon:160618`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 9 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kryptoperidinium`.
- `curation/seed_scope.tsv:53135` contains this identifier with reason `attested rule: Kryptoperidinium triquetrum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:55362` maps side-inventory old ID `NCBITaxon:2864184` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:40759`, whose aggregate count is `2` for `NCBITaxon:66468`.
- The current native GOLD scan found exact organisms `Go0002391` for `Heterocapsa triquetra` and `Go0368701` for `Heterocapsa triquetra CCMP 448`.
- Expanding those exact GOLD organisms found project `Gp0002391`, with no native linked analysis rows.
- StrainInfo has 5 exact direct rows and 5 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:66468`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:66468`, `just validate data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml`, and `just validate-strict data/taxa/eukaryota/kryptoperidinium_triquetrum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kryptoperidinium_triquetrum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Native GOLD still names the exact organisms `Heterocapsa triquetra`; the NCBI row and generated record use the current label `Kryptoperidinium triquetrum`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
