# YAML Record Review: Lichtheimia ramosa B5792

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml
- Started UTC: 2026-09-23T12:31:10Z
- Finished UTC: 2026-09-23T12:31:10Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml` denotes the exact NCBI strain `Lichtheimia ramosa B5792` as `NCBITaxon:1357685`, rank `STRAIN`, under species `NCBITaxon:688394` (`Lichtheimia ramosa`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lichtheimia_hyalospora.yaml data/taxa/eukaryota/lichtheimia_ramosa.yaml data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml data/taxa/eukaryota/lichtheimia_sphaerocystis.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:328851` carries `NCBITaxon:1357685`, label `Lichtheimia ramosa B5792`, rank `STRAIN`, parent `NCBITaxon:688394`, genetic code `1`, no synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected parent species `Lichtheimia ramosa`.
- `curation/seed_scope.tsv:59653` contains this identifier with reason `attested rule: Lichtheimia ramosa B5792, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:1357685`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8677`, whose aggregate count is `1` for `NCBITaxon:1357685`.
- The current native GOLD expansion found one exact organism row, one exact project, and one native analysis row linked through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no rows for this strain NCBI ID, and the generated raw strain and StrainInfo overlay tables likewise have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no NCBI type-material rows for `NCBITaxon:1357685`, consistent with this being a strain-level child of `Lichtheimia ramosa`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1357685`, `just validate data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml`, and `just validate-strict data/taxa/eukaryota/lichtheimia_ramosa_b5792.yaml` on the regenerated record.

## Additional Notes

- The exact native GOLD row maps `NCBITaxon:1357685` to strain `B5792`, although its preserved organism and project name strings still use `Lichtheimia corymbifera B5792`; the generated record follows the current NCBI label and parent.
- No prior exact report for `lichtheimia_ramosa_b5792` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
