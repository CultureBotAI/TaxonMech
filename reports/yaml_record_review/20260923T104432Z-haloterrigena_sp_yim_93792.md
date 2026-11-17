# YAML Record Review: Haloterrigena sp. YIM 93792

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/haloterrigena_sp_yim_93792.yaml
- Started UTC: 2026-09-23T10:42:10Z
- Finished UTC: 2026-09-23T10:44:32Z
- Verdict: pass

## Target

Reviewed `data/taxa/archaea/haloterrigena_sp_yim_93792.yaml`.

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1008154` |
| label | `Haloterrigena sp. YIM 93792` |
| rank | `SPECIES` |
| domain | `ARCHAEA` |
| parent | `NCBITaxon:2631942` / `unclassified Haloterrigena` |
| generated status | Seeded from pinned source inventories in `data/raw/`, `data/atb/`, and `data/straininfo/` |

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-haloterrigena_sp_yim_93792.md'` | Passed: no prior report for this stem; `find` inspected ignored report files. |
| `just validate-strict data/taxa/archaea/haloterrigena_sp_yim_93684.yaml data/taxa/archaea/haladaptatus_pallidirubidus.yaml data/taxa/archaea/halalkalicoccus_paucihalophilus.yaml data/taxa/archaea/haloterrigena_sp_yim_93792.yaml` | Passed: 4 files scanned, 0 files with errors, 0 total error rows. |
| `just validate data/taxa/archaea/haloterrigena_sp_yim_93792.yaml` | Passed: LinkML validation reported no issues. |

`just validate-products` was skipped because this taxon has no `causal_graphs`. `just validate-history` was skipped because this read-only review did not add a history decision. The full-corpus `just verify-corpus` gate was skipped for this individual review batch because these reports do not edit generated taxon YAML.

## Identity and Grounding

The record consistently denotes the NCBI species-level placeholder `NCBITaxon:1008154`, `Haloterrigena sp. YIM 93792`.

- The curated identifier, label, rank, `parent_taxon`, genetic code, and NCBI-only source attestation match the pinned row in `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1008154`, `Haloterrigena sp. YIM 93792`, `SPECIES`, parent `NCBITaxon:2631942`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.
- The lineage terminates at `NCBITaxon:2631942` / `unclassified Haloterrigena`, which agrees with the raw NCBI parent.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a seeded record whose identifier is the source NCBI taxon itself.
- The record has no synonyms, xrefs, nomenclature, taxonomy mappings, or strain block, matching the lack of same-taxon LPSN, GTDB, BacDive, GOLD, ATB, MediaDive, or StrainInfo rows in the exact local searches.

## Evidence

The only material biological assertion is the NCBI identity and placement. The exact `rg --no-ignore --hidden` searches for `NCBITaxon:1008154` and `Haloterrigena sp. YIM 93792` over `data/raw/`, `data/atb/`, and `data/straininfo/` found the NCBI source row and no auxiliary rows that should have produced extra generated sections.

No external live source pages were used; the pinned 2026-09-13 NCBI row is the reviewed source of truth for this generated record.

## Completeness

No consequential gaps were found.

- `strain_count: 0` is consistent with the absence of exact BacDive, GOLD, ATB, NCBI Assembly, GTDB genome, and StrainInfo rows for this NCBI ID.
- Empty optional nomenclature, mapping, synonym, xref, strain, and causal-graph sections are expected for this NCBI-only placeholder.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is needed. If the pinned NCBI snapshot changes, rerun the source seeding pipeline and the narrow validators used above.

## Additional Notes

This review was read-only. Future identity, lineage, attestation, or count changes for this generated taxon should be made in the source seed inputs or `src/taxonmech/seed.py`, not by hand-editing `data/taxa/archaea/haloterrigena_sp_yim_93792.yaml`.
