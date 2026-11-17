# YAML Record Review: Lenzites betulinus 141

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lenzites_betulinus_141.yaml
- Started UTC: 2026-09-23T12:00:38Z
- Finished UTC: 2026-09-23T12:00:38Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/lenzites_betulinus_141.yaml` denotes the exact NCBI strain `Lenzites betulinus 141` as `NCBITaxon:1142160`, rank `STRAIN`, under species `NCBITaxon:5632` (`Lenzites betulinus`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lenzites_betulinus_141.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lenzites_betulinus_141.yaml data/taxa/eukaryota/leotia_sp.yaml data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml data/taxa/eukaryota/lepista_sp.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:248333` carries `NCBITaxon:1142160`, label `Lenzites betulinus 141`, rank `STRAIN`, parent `NCBITaxon:5632`, genetic code `1`, exact synonyms `Lenzites betulina 141` and `Trametes betulina 141`, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lenzites betulinus` species.
- `curation/seed_scope.tsv:57916` contains this identifier with reason `attested rule: Lenzites betulinus 141, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:1142160`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:2945`, whose aggregate count is `1` for `NCBITaxon:1142160`.
- The current native GOLD scan found exact organism `Go0017033` for `Lenzites betulina 141` and no exact native project or analysis rows for this NCBI ID.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1142160` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1142160`, `just validate data/taxa/eukaryota/lenzites_betulinus_141.yaml`, and `just validate-strict data/taxa/eukaryota/lenzites_betulinus_141.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lenzites_betulinus_141` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
