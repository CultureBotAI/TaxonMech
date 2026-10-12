# YAML Record Review: Lachancea fermentati

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachancea_fermentati.yaml
- Started UTC: 2026-09-23T10:35:46Z
- Finished UTC: 2026-09-23T10:35:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachancea_fermentati.yaml` denotes the exact NCBI species `Lachancea fermentati` as `NCBITaxon:4955`, rank `SPECIES`, under genus `NCBITaxon:300275` (`Lachancea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachancea_fermentati.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/laccaria_trichodermophora.yaml data/taxa/eukaryota/lachancea_cidri.yaml data/taxa/eukaryota/lachancea_dasiensis.yaml data/taxa/eukaryota/lachancea_fermentati.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2162` carries `NCBITaxon:4955`, label `Lachancea fermentati`, rank `SPECIES`, parent `NCBITaxon:300275`, genetic code `1`, exact synonym `Zygosaccharomyces fermentati`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachancea`.
- `curation/seed_scope.tsv:51892` contains this identifier with reason `attested rule: Lachancea fermentati, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:56669` maps side-inventory old ID `NCBITaxon:2898203` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37209`, whose aggregate count is `3` for `NCBITaxon:4955`.
- The current native GOLD scan found exact organisms `Go0372906`, `Go0657876`, and `Go0705246` for this NCBI taxon.
- Expanding those exact GOLD organisms found projects `Gp0219697`, `Gp0702144`, and `Gp0831279`, plus two native analysis rows linked through the first two project IDs.
- Exact StrainInfo scans found 58 direct strains and 125 deposits for this taxon; exact BacDive and generated raw strain-table scans found no corresponding local BacDive-derived strain rows to overlay.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 16 rows for `NCBITaxon:4955` at lines 223977-223992, covering `ATCC 58446`, `BCRC 21760`, `CBS 707`, `CCRC 21760`, `CECT 11056`, `DBVPG 6297`, `IFO 0479`, and `NRRL Y-1559` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:4955`, `just validate data/taxa/eukaryota/lachancea_fermentati.yaml`, and `just validate-strict data/taxa/eukaryota/lachancea_fermentati.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachancea_fermentati` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
