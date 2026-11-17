# YAML Record Review: Lenzites betulinus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lenzites_betulinus.yaml
- Started UTC: 2026-09-23T11:58:29Z
- Finished UTC: 2026-09-23T11:58:29Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lenzites_betulinus.yaml` denotes the exact NCBI species `Lenzites betulinus` as `NCBITaxon:5632`, rank `SPECIES`, under genus `NCBITaxon:5631` (`Lenzites`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lenzites_betulinus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lentinus_polychrous.yaml data/taxa/eukaryota/lentinus_tigrinus.yaml data/taxa/eukaryota/lentithecium_fluviatile.yaml data/taxa/eukaryota/lenzites_betulinus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2505` carries `NCBITaxon:5632`, label `Lenzites betulinus`, rank `SPECIES`, parent `NCBITaxon:5631`, genetic code `1`, three exact synonyms, two related synonyms, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lenzites` genus.
- `curation/seed_scope.tsv:52049` contains this identifier with reason `attested rule: Lenzites betulinus, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5632`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38893`, whose aggregate count is `2` for `NCBITaxon:5632`; the generated attestation correctly notes that those are direct records under this taxon only.
- A complete current native GOLD pass found two exact organism rows, eight exact linked project rows, and one exact linked analysis row for this NCBI ID.
- Exact StrainInfo scans found one direct strain and one deposit row for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5632` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5632`, `just validate data/taxa/eukaryota/lenzites_betulinus.yaml`, and `just validate-strict data/taxa/eukaryota/lenzites_betulinus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lenzites_betulinus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
