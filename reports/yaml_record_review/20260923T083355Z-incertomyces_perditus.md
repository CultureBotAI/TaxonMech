# YAML Record Review: Incertomyces perditus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/incertomyces_perditus.yaml
- Started UTC: 2026-09-23T08:33:55Z
- Finished UTC: 2026-09-23T08:34:02Z
- Verdict: pass

## Target

Generated species-level eukaryote record `data/taxa/eukaryota/incertomyces_perditus.yaml` denotes `Incertomyces perditus` as `NCBITaxon:1507824`, rank `SPECIES`, under parent `NCBITaxon:1664127` (`Incertomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/incertomyces_perditus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/immersiella_caudata.yaml data/taxa/eukaryota/imperator_rhodopurpureus.yaml data/taxa/eukaryota/incertomyces_perditus.yaml data/taxa/eukaryota/infundibulicybe_gibba.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:387247` carries `NCBITaxon:1507824`, label `Incertomyces perditus`, rank `SPECIES`, parent `NCBITaxon:1664127`, genetic code `1`, and the two related synonyms emitted in YAML.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks.
- `curation/seed_scope.tsv:60372` contains this identifier with reason `attested rule: Incertomyces perditus, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:11865`, whose aggregate count is `1` for `NCBITaxon:1507824`.
- The current native GOLD organism scan found exact organism `Go0583370` for `Incertomyces perditus CCFEE 5385`, with projects `Gp0587333` and `Gp0891536`; no native analysis row joined to those projects.
- Exact `data/raw/ncbi_type_material.tsv` rows record `CCFEE 5385` and `CCFEE:5385` as cultures from holotype, and `CBS 136105` and `CBS:136105` as holotype designations for this NCBI taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`, so the NCBI type-material strings do not have a local final BacDive strain surface to emit.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- StrainInfo has no exact direct or deposit rows for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, type-material, or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1507824`, `just validate data/taxa/eukaryota/incertomyces_perditus.yaml`, and `just validate-strict data/taxa/eukaryota/incertomyces_perditus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `incertomyces_perditus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
