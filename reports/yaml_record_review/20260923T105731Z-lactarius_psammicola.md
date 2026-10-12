# YAML Record Review: Lactarius psammicola

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_psammicola.yaml
- Started UTC: 2026-09-23T10:57:31Z
- Finished UTC: 2026-09-23T10:57:31Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_psammicola.yaml` denotes the exact NCBI species `Lactarius psammicola` as `NCBITaxon:1907521`, rank `SPECIES`, under genus `NCBITaxon:34444` (`Lactarius`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_psammicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactarius_lignyotus.yaml data/taxa/eukaryota/lactarius_psammicola.yaml data/taxa/eukaryota/lactarius_pseudohatsudake.yaml data/taxa/eukaryota/lactarius_quietus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:493033` carries `NCBITaxon:1907521`, label `Lactarius psammicola`, rank `SPECIES`, parent `NCBITaxon:34444`, genetic code `1`, and related synonym `Lactarius psammicola A.H. Sm., 1941`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactarius`.
- `curation/seed_scope.tsv:61534` contains this identifier with reason `attested rule: Lactarius psammicola, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:17261`, whose aggregate count is `1` for `NCBITaxon:1907521`.
- The current native GOLD scan found exact organism `Go0120390` for `Lactarius psammicola BPL869`.
- Expanding that exact GOLD organism found projects `Gp0128271` and `Gp0196969`, plus one native analysis row linked through `Gp0128271`.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 holotype rows for `NCBITaxon:1907521` at lines 69625-69628, covering `MICH 11190` variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1907521`, `just validate data/taxa/eukaryota/lactarius_psammicola.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_psammicola.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_psammicola` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
