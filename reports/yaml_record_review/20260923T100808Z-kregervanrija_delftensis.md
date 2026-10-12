# YAML Record Review: Kregervanrija delftensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kregervanrija_delftensis.yaml
- Started UTC: 2026-09-23T10:08:08Z
- Finished UTC: 2026-09-23T10:08:08Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kregervanrija_delftensis.yaml` denotes the exact NCBI species `Kregervanrija delftensis` as `NCBITaxon:324739`, rank `SPECIES`, under genus `NCBITaxon:324738` (`Kregervanrija`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kregervanrija_delftensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kregervanrija_delftensis.yaml data/taxa/eukaryota/kregervanrija_fluxuum.yaml data/taxa/eukaryota/kregervanrija_pseudodelftensis.yaml data/taxa/eukaryota/kretzschmaria_clavus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:66299` carries `NCBITaxon:324739`, label `Kregervanrija delftensis`, rank `SPECIES`, parent `NCBITaxon:324738`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kregervanrija`.
- `curation/seed_scope.tsv:55206` contains this identifier with reason `attested rule: Kregervanrija delftensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:85135` maps side-inventory old ID `NCBITaxon:53653` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32125`, whose aggregate count is `1` for `NCBITaxon:324739`.
- The current native GOLD scan found exact organism `Go0517047` for `Kregervanrija delftensis NRRL Y-7119`.
- Expanding that exact GOLD organism found project `Gp0441085` and the native linked analysis `Kregervanrija delftensis NRRL Y-7119` through `AP PROJECT GOLD IDS`.
- StrainInfo has 4 exact direct rows and 15 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 12 rows for `NCBITaxon:324739` at lines 177311-177322, covering `ATCC 22305`, `BCRC 22385`, `CBS 2614`, `CCRC 22385`, `IFO 10715`, and `NRRL Y-7119` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:324739`, `just validate data/taxa/eukaryota/kregervanrija_delftensis.yaml`, and `just validate-strict data/taxa/eukaryota/kregervanrija_delftensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kregervanrija_delftensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
