# YAML Record Review: Kodamaea kakaduensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_kakaduensis.yaml
- Started UTC: 2026-09-23T09:44:22Z
- Finished UTC: 2026-09-23T09:44:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_kakaduensis.yaml` denotes the exact NCBI species `Kodamaea kakaduensis` as `NCBITaxon:85574`, rank `SPECIES`, under genus `NCBITaxon:77850` (`Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_kakaduensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kodamaea_fungicola.yaml data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml data/taxa/eukaryota/kodamaea_jinghongensis.yaml data/taxa/eukaryota/kodamaea_kakaduensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13208` carries `NCBITaxon:85574`, label `Kodamaea kakaduensis`, rank `SPECIES`, parent `NCBITaxon:77850`, genetic code `12`, and the NCBI synonym retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kodamaea`.
- `curation/seed_scope.tsv:53419` contains this identifier with reason `attested rule: Kodamaea kakaduensis, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:43251`, whose aggregate count is `1` for `NCBITaxon:85574`.
- The current native GOLD scan found exact organism `Go0705152` for `Kodamaea kakaduensis CBS 8611`.
- Expanding that exact GOLD organism found project `Gp0831175`, with no native linked analysis rows.
- StrainInfo has 3 exact direct rows and 5 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 3 rows for `NCBITaxon:85574` at lines 268150-268152, covering `CBS 8611` and `UWO(PS) 98-119.2` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:85574`, `just validate data/taxa/eukaryota/kodamaea_kakaduensis.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_kakaduensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_kakaduensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
