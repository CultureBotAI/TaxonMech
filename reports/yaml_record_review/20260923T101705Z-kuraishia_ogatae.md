# YAML Record Review: Kuraishia ogatae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kuraishia_ogatae.yaml
- Started UTC: 2026-09-23T10:17:05Z
- Finished UTC: 2026-09-23T10:17:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kuraishia_ogatae.yaml` denotes the exact NCBI species `Kuraishia ogatae` as `NCBITaxon:537810`, rank `SPECIES`, under genus `NCBITaxon:317045` (`Kuraishia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kuraishia_ogatae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kuraishia_hungarica.yaml data/taxa/eukaryota/kuraishia_molischiana.yaml data/taxa/eukaryota/kuraishia_ogatae.yaml data/taxa/eukaryota/kuraishia_piskuri.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:123880` carries `NCBITaxon:537810`, label `Kuraishia ogatae`, rank `SPECIES`, parent `NCBITaxon:317045`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kuraishia`.
- `curation/seed_scope.tsv:55933` contains this identifier with reason `attested rule: Kuraishia ogatae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:85176` maps side-inventory old ID `NCBITaxon:537811` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38236`, whose aggregate count is `1` for `NCBITaxon:537810`.
- The current native GOLD scan found exact organism `Go0517116` for `Kuraishia ogatae NRRL Y-48474`.
- Expanding that exact GOLD organism found project `Gp0441154` and the native linked analysis `Kuraishia ogatae NRRL Y-48474` through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:537810` at lines 230875-230880, covering `CBS 10924`, `NCAIM Y.01845`, and `NRRL Y-48474` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:537810`, `just validate data/taxa/eukaryota/kuraishia_ogatae.yaml`, and `just validate-strict data/taxa/eukaryota/kuraishia_ogatae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kuraishia_ogatae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
