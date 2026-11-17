# YAML Record Review: Kockovaella sichuanensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kockovaella_sichuanensis.yaml
- Started UTC: 2026-09-23T09:38:45Z
- Finished UTC: 2026-09-23T09:38:45Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kockovaella_sichuanensis.yaml` denotes the exact NCBI species `Kockovaella sichuanensis` as `NCBITaxon:104679`, rank `SPECIES`, under genus `NCBITaxon:4998` (`Kockovaella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kockovaella_sichuanensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kockovaella_lichenicola.yaml data/taxa/eukaryota/kockovaella_prillingeri.yaml data/taxa/eukaryota/kockovaella_sichuanensis.yaml data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:18710` carries `NCBITaxon:104679`, label `Kockovaella sichuanensis`, rank `SPECIES`, parent `NCBITaxon:4998`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kockovaella`.
- `curation/seed_scope.tsv:53691` contains this identifier with reason `attested rule: Kockovaella sichuanensis, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:689`, whose aggregate count is `6` for `NCBITaxon:104679`.
- Complete exact native GOLD expansion found 6 organisms for `Kockovaella sichuanensis`: `Go0624920`, `Go0624921`, `Go0624922`, `Go0624923`, `Go0624924`, and `Go0624925`.
- Expanding those exact GOLD organisms found no native linked project or analysis rows.
- StrainInfo has 4 exact direct rows and 7 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 rows for `NCBITaxon:104679` at lines 3034-3037, covering `CBS 8318` culture-from-type-material variants and `HB 40` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:104679`, `just validate data/taxa/eukaryota/kockovaella_sichuanensis.yaml`, and `just validate-strict data/taxa/eukaryota/kockovaella_sichuanensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kockovaella_sichuanensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
