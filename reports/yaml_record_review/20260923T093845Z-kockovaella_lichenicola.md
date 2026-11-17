# YAML Record Review: Kockovaella lichenicola

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kockovaella_lichenicola.yaml
- Started UTC: 2026-09-23T09:38:45Z
- Finished UTC: 2026-09-23T09:38:45Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kockovaella_lichenicola.yaml` denotes the exact NCBI species `Kockovaella lichenicola` as `NCBITaxon:104678`, rank `SPECIES`, under genus `NCBITaxon:4998` (`Kockovaella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kockovaella_lichenicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kockovaella_lichenicola.yaml data/taxa/eukaryota/kockovaella_prillingeri.yaml data/taxa/eukaryota/kockovaella_sichuanensis.yaml data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:18709` carries `NCBITaxon:104678`, label `Kockovaella lichenicola`, rank `SPECIES`, parent `NCBITaxon:4998`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kockovaella`.
- `curation/seed_scope.tsv:53690` contains this identifier with reason `attested rule: Kockovaella lichenicola, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:688`, whose aggregate count is `5` for `NCBITaxon:104678`.
- The current native GOLD scan found 5 exact organisms for `Kockovaella lichenicola`: `Go0624915`, `Go0624916`, `Go0624917`, `Go0624918`, and `Go0624919`.
- Expanding those exact GOLD organisms found no native linked project or analysis rows.
- StrainInfo has 3 exact direct rows and 6 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 2 rows for `NCBITaxon:104678` at lines 3032-3033, covering `CBS 8315` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:104678`, `just validate data/taxa/eukaryota/kockovaella_lichenicola.yaml`, and `just validate-strict data/taxa/eukaryota/kockovaella_lichenicola.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kockovaella_lichenicola` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
