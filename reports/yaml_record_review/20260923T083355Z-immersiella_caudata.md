# YAML Record Review: Immersiella caudata

- Repository: TaxonMech
- Record: data/taxa/eukaryota/immersiella_caudata.yaml
- Started UTC: 2026-09-23T08:33:55Z
- Finished UTC: 2026-09-23T08:34:02Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/immersiella_caudata.yaml` denotes `Immersiella caudata` as `NCBITaxon:314043`, rank `SPECIES`, under parent `NCBITaxon:260662` (`Immersiella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/immersiella_caudata.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/immersiella_caudata.yaml data/taxa/eukaryota/imperator_rhodopurpureus.yaml data/taxa/eukaryota/incertomyces_perditus.yaml data/taxa/eukaryota/infundibulicybe_gibba.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:64231` carries `NCBITaxon:314043`, label `Immersiella caudata`, rank `SPECIES`, parent `NCBITaxon:260662`, genetic code `1`, exact synonyms `Cercophora caudata|Sordaria caudata`, and the three related authority-bearing synonyms emitted in YAML.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:55152` contains this identifier with reason `attested rule: Immersiella caudata, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:46194` has side old ID `NCBITaxon:260663 -> NCBITaxon:314043`, but no retained retired `ncbitaxon_taxa` row exists, so omitting `replaces` is expected.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:31716`, whose aggregate count is `1` for `NCBITaxon:314043`.
- The current native GOLD organism scan also found exact organism `Go0358423` for `Cercophora caudata CBS 606.72`, with projects `Gp0197091` and `Gp0251478`; no native analysis row joined to those projects.
- StrainInfo has exact direct SI rows for `SI-ID168559`/`CBS 606.72` and `SI-ID268056`/`ICMP 21805`, but there are no exact BacDive-derived final strain rows for this taxon, so the empty `strains`, `genome_assemblies`, and `related_records` surfaces are consistent with the local seeding rules.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:314043`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, StrainInfo, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:314043`, `just validate data/taxa/eukaryota/immersiella_caudata.yaml`, and `just validate-strict data/taxa/eukaryota/immersiella_caudata.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `immersiella_caudata` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
