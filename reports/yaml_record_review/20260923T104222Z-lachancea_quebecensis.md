# YAML Record Review: Lachancea quebecensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachancea_quebecensis.yaml
- Started UTC: 2026-09-23T10:42:22Z
- Finished UTC: 2026-09-23T10:42:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachancea_quebecensis.yaml` denotes the exact NCBI species `Lachancea quebecensis` as `NCBITaxon:1654605`, rank `SPECIES`, under genus `NCBITaxon:300275` (`Lachancea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachancea_quebecensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachancea_nothofagi.yaml data/taxa/eukaryota/lachancea_quebecensis.yaml data/taxa/eukaryota/lachancea_sp_fantastica.yaml data/taxa/eukaryota/lachancea_thermotolerans.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:432687` carries `NCBITaxon:1654605`, label `Lachancea quebecensis`, rank `SPECIES`, parent `NCBITaxon:300275`, genetic code `1`, exact synonym `Lachancea quebecensis K.C. Freel, G. Charron, J.B. Leducq, C.R. Landry & J. Schacherer, 2015`, and the related synonym `Lachancea sp. KF-2015`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachancea`.
- `curation/seed_scope.tsv:60989` contains this identifier with reason `attested rule: Lachancea quebecensis, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:14233`, whose aggregate count is `2` for `NCBITaxon:1654605`.
- The current native GOLD scan found exact organisms `Go0454953` and `Go0705719` for this NCBI taxon.
- Expanding those exact GOLD organisms found projects `Gp0323279` and `Gp0831774`, plus one native analysis row linked through `Gp0323279`.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 rows for `NCBITaxon:1654605` at lines 50094-50097, covering `CBS 14138` culture-from-holotype variants and `LL11_022` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1654605`, `just validate data/taxa/eukaryota/lachancea_quebecensis.yaml`, and `just validate-strict data/taxa/eukaryota/lachancea_quebecensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachancea_quebecensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
