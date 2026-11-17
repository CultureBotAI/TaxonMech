# YAML Record Review: Kuraishia molischiana

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kuraishia_molischiana.yaml
- Started UTC: 2026-09-23T10:17:05Z
- Finished UTC: 2026-09-23T10:17:05Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kuraishia_molischiana.yaml` denotes the exact NCBI species `Kuraishia molischiana` as `NCBITaxon:317048`, rank `SPECIES`, under genus `NCBITaxon:317045` (`Kuraishia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kuraishia_molischiana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kuraishia_hungarica.yaml data/taxa/eukaryota/kuraishia_molischiana.yaml data/taxa/eukaryota/kuraishia_ogatae.yaml data/taxa/eukaryota/kuraishia_piskuri.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:65144` carries `NCBITaxon:317048`, label `Kuraishia molischiana`, rank `SPECIES`, parent `NCBITaxon:317045`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kuraishia`.
- `curation/seed_scope.tsv:55168` contains this identifier with reason `attested rule: Kuraishia molischiana, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:31859`, whose aggregate count is `1` for `NCBITaxon:317048`.
- The current native GOLD scan found exact organism `Go0517115` for `Kuraishia molischiana NRRL Y-27899`.
- Expanding that exact GOLD organism found project `Gp0441153` and the native linked analysis `Kuraishia molischiana NRRL Y-27899` through `AP PROJECT GOLD IDS`.
- StrainInfo has 8 exact direct rows and 30 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:317048` at lines 174240-174245, covering `CBS 9993`, `NCAIM Y.01725`, and `NRRL Y-27899` culture-from-type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:317048`, `just validate data/taxa/eukaryota/kuraishia_molischiana.yaml`, and `just validate-strict data/taxa/eukaryota/kuraishia_molischiana.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kuraishia_molischiana` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
