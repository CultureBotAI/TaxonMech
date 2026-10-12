# YAML Record Review: Lepidosphaeria nicotiae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml
- Started UTC: 2026-09-23T12:00:38Z
- Finished UTC: 2026-09-23T12:00:38Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml` denotes the exact NCBI species `Lepidosphaeria nicotiae` as `NCBITaxon:372061`, rank `SPECIES`, under genus `NCBITaxon:372051` (`Lepidosphaeria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lenzites_betulinus_141.yaml data/taxa/eukaryota/leotia_sp.yaml data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml data/taxa/eukaryota/lepista_sp.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:78122` carries `NCBITaxon:372061`, label `Lepidosphaeria nicotiae`, rank `SPECIES`, parent `NCBITaxon:372051`, genetic code `1`, related synonym `Lepidosphaeria nicotiae Parguey-Leduc, 1970`, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lepidosphaeria` genus.
- `curation/seed_scope.tsv:55394` contains this identifier with reason `attested rule: Lepidosphaeria nicotiae, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:372061`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33618`, whose aggregate count is `2` for `NCBITaxon:372061`.
- The current native GOLD scan found no exact organism, project, or analysis rows for this NCBI ID.
- Exact StrainInfo scans found four direct strains and seven deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:197407` and `:197408` contain isotype spellings `CBS 559.71` and `CBS:559.71` for `NCBITaxon:372061`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:372061`, `just validate data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml`, and `just validate-strict data/taxa/eukaryota/lepidosphaeria_nicotiae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lepidosphaeria_nicotiae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
