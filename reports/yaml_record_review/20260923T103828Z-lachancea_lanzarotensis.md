# YAML Record Review: Lachancea lanzarotensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachancea_lanzarotensis.yaml
- Started UTC: 2026-09-23T10:38:28Z
- Finished UTC: 2026-09-23T10:38:28Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachancea_lanzarotensis.yaml` denotes the exact NCBI species `Lachancea lanzarotensis` as `NCBITaxon:1245769`, rank `SPECIES`, under genus `NCBITaxon:300275` (`Lachancea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachancea_lanzarotensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachancea_kluyveri.yaml data/taxa/eukaryota/lachancea_lanzarotensis.yaml data/taxa/eukaryota/lachancea_meyersii.yaml data/taxa/eukaryota/lachancea_mirantina.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:286472` carries `NCBITaxon:1245769`, label `Lachancea lanzarotensis`, rank `SPECIES`, parent `NCBITaxon:300275`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachancea`.
- `curation/seed_scope.tsv:58659` contains this identifier with reason `attested rule: Lachancea lanzarotensis, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5918`, whose aggregate count is `1` for `NCBITaxon:1245769`.
- The current native GOLD scan found exact organism `Go0117706` for `Lachancea lanzarotensis CBS 12615`.
- Expanding that exact GOLD organism found projects `Gp0122660` and `Gp0780233`, plus two native analysis rows linked through those project IDs.
- Exact StrainInfo scans found seven direct strains and 14 deposits for this taxon; exact BacDive and generated raw strain-table scans found no corresponding local BacDive-derived strain rows to overlay.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:1245769` at lines 16582-16587, covering `CBS 12615`, `CECT 13066`, and `L2C-15` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1245769`, `just validate data/taxa/eukaryota/lachancea_lanzarotensis.yaml`, and `just validate-strict data/taxa/eukaryota/lachancea_lanzarotensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachancea_lanzarotensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
