# YAML Record Review: Halogeometricum sp. YIM 93541

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halogeometricum_sp_yim_93541.yaml
- Started UTC: 2026-09-23T10:39:15Z
- Finished UTC: 2026-09-23T10:40:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1008149 |
| Label | Halogeometricum sp. YIM 93541 |
| Rank | SPECIES |
| Domain | ARCHAEA |
| Parent | NCBITaxon:2628593, unclassified Halogeometricum |
| Maintained status | Generated from the committed `data/raw/`, `data/atb/`, and `data/straininfo/` inventories |

This review covered the full generated YAML at `data/taxa/archaea/halogeometricum_sp_yim_93541.yaml`. The record carries one `NCBITAXON` source attestation, one NCBI exact synonym, and has no `nomenclature`, `taxonomy_mappings`, `strains`, `strain_attestations`, `genome_records`, `genome_assemblies`, `culture_collection_ids`, or `causal_graphs` blocks to audit.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/archaea/haloterrigena_sp_yim_93596.yaml data/taxa/archaea/haloterrigena_sp_yim_93593.yaml data/taxa/archaea/haloterrigena_sp_yim_93641.yaml data/taxa/archaea/halogeometricum_sp_yim_93541.yaml` | Passed: 4 files scanned, 0 files with errors |
| `just validate data/taxa/archaea/halogeometricum_sp_yim_93541.yaml` | Passed with `No issues found` |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halogeometricum_sp_yim_93541.md'` | No prior report found; this `find` search includes ignored reports |
| Exact `NCBITaxon:1008149` source search with `rg --no-ignore --hidden` | Found only `data/taxa/PATHS.tsv` and the matching `data/raw/ncbitaxon_taxa.tsv` row |
| Anchored `Halogeometricum sp. YIM 93541` and `Halosarcina sp. YIM 93541` source search over `data/raw`, `data/atb`, and `data/straininfo` with `rg --no-ignore --hidden` | Found only the matching NCBI row |
| `just verify-corpus` | Skipped for this report batch: the reviews are read-only, only ignored Markdown reports were added, and an earlier full-corpus verification over 625,960 records was clean |
| `just validate-history` | Skipped: read-only YAML reviews do not add `history/` curation decisions |
| `just validate-products` | Not applicable: this record has no `causal_graphs` product identifiers |

## Identity and Grounding

The YAML identity is supported by the pinned local NCBI row:

| Source | ID | Label | Rank | Parent | Genetic code | Snapshot |
|---|---|---|---|---|---|---|
| `data/raw/ncbitaxon_taxa.tsv` | NCBITaxon:1008149 | Halogeometricum sp. YIM 93541 | SPECIES | NCBITaxon:2628593 | 11 | 2026-09-13 |

The record's `identifier`, `label`, `rank`, `parent_taxon`, `taxon_domain`, and `genetic_code` agree with that source row and the NCBI lineage carried in the generated YAML: `Halogeometricum` under `Halobacteriales` and `Haloferacaceae` via `unclassified Halogeometricum`. `grounding_status: EXACT` is appropriate because the record is grounded directly to `NCBITaxon:1008149`, and `mapping_status: SEEDED` reflects the generated seed provenance.

## Evidence

The NCBI-sourced claims are narrow and source-backed:

| Claim | Evidence | Assessment |
|---|---|---|
| `NCBITAXON` attests `NCBITaxon:1008149` as `Halogeometricum sp. YIM 93541` | Matching `data/raw/ncbitaxon_taxa.tsv` row from the 2026-09-13 snapshot | Supported |
| `Halosarcina sp. YIM 93541` is an `EXACT_SYNONYM` from `NCBITaxon` | The same row has `Halosarcina sp. YIM 93541` in the synonym field | Supported |
| `assertion_count: 1` with `assertion_unit: NAME` | The record has one NCBI name-row attestation and no auxiliary ATB or StrainInfo row for this exact taxon | Supported |

No citation-bearing claims, LPSN nomenclature entries, GTDB mappings, strain links, or genome links are present, so there are no unsupported or over-scoped source assertions to flag.

## Completeness

The empty optional sections are consistent with the pinned inventories inspected for this review. Exact `NCBITaxon:1008149` and anchored `Halogeometricum sp. YIM 93541`/`Halosarcina sp. YIM 93541` searches with ignored files included found no same-taxon ATB or StrainInfo rows to project.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. If an upstream refresh later adds LPSN, GTDB, ATB, BacDive, or StrainInfo support for `NCBITaxon:1008149`, rerun `just seed`, `just seed-canary NCBITaxon:1008149`, the focused strict validator, and `just verify-corpus` before accepting the regenerated YAML.

## Additional Notes

Live authority pages were not used for this batch; the review used the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv` as the local source of truth.
