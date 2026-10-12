# YAML Record Review: Sporosarcina sp. LKS-72

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/sporosarcina_sp_lks_72.yaml
- Started UTC: 2026-09-23T10:20:00Z
- Finished UTC: 2026-09-23T10:21:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1008105 |
| Label | Sporosarcina sp. LKS-72 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2647733, unclassified Sporosarcina |
| Maintained status | Generated from the committed `data/raw/`, `data/atb/`, and `data/straininfo/` inventories |

This review covered the full generated YAML at `data/taxa/bacteria/sporosarcina_sp_lks_72.yaml`. The record carries one `NCBITAXON` source attestation and has no `synonyms`, `nomenclature`, `taxonomy_mappings`, `strains`, `strain_attestations`, `genome_records`, `genome_assemblies`, `culture_collection_ids`, or `causal_graphs` blocks to audit.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/sporosarcina_sp_lks_66.yaml data/taxa/bacteria/sporosarcina_sp_lks_72.yaml data/taxa/bacteria/staphylococcus_sp_lks_197.yaml data/taxa/bacteria/staphylococcus_sp_lks_198.yaml` | Passed |
| `just validate data/taxa/bacteria/sporosarcina_sp_lks_72.yaml` | Passed with `No issues found` |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-sporosarcina_sp_lks_72.md'` | No prior report found; this `find` search includes ignored reports |
| Exact `NCBITaxon:1008105` source search with `rg --no-ignore --hidden` | Found only `data/taxa/PATHS.tsv` and the matching `data/raw/ncbitaxon_taxa.tsv` row |
| Anchored `Sporosarcina sp. LKS-72` source search over `data/raw`, `data/atb`, and `data/straininfo` with `rg --no-ignore --hidden` | Found only the matching NCBI row |
| `just verify-corpus` | Skipped for this report batch: the reviews are read-only, only ignored Markdown reports were added, and an earlier full-corpus verification over 625,960 records was clean |
| `just validate-history` | Skipped: read-only YAML reviews do not add `history/` curation decisions |
| `just validate-products` | Not applicable: this record has no `causal_graphs` product identifiers |

## Identity and Grounding

The YAML identity is supported by the pinned local NCBI row:

| Source | ID | Label | Rank | Parent | Genetic code | Snapshot |
|---|---|---|---|---|---|---|
| `data/raw/ncbitaxon_taxa.tsv` | NCBITaxon:1008105 | Sporosarcina sp. LKS-72 | SPECIES | NCBITaxon:2647733 | 11 | 2026-09-13 |

The record's `identifier`, `label`, `rank`, `parent_taxon`, `taxon_domain`, and `genetic_code` agree with that source row and the NCBI lineage carried in the generated YAML: `Sporosarcina` under `Caryophanaceae` via `unclassified Sporosarcina`. `grounding_status: EXACT` is appropriate because the record is grounded directly to `NCBITaxon:1008105`, and `mapping_status: SEEDED` reflects the generated seed provenance.

## Evidence

The one `source_attestations` entry is narrow and source-backed:

| Claim | Evidence | Assessment |
|---|---|---|
| `NCBITAXON` attests `NCBITaxon:1008105` as `Sporosarcina sp. LKS-72` | Matching `data/raw/ncbitaxon_taxa.tsv` row from the 2026-09-13 snapshot | Supported |
| `assertion_count: 1` with `assertion_unit: NAME` | The record has one NCBI name-row attestation and no auxiliary ATB or StrainInfo row for this exact taxon | Supported |

No citation-bearing claims, synonyms, LPSN nomenclature entries, GTDB mappings, strain links, or genome links are present, so there are no unsupported or over-scoped source assertions to flag.

## Completeness

The empty optional sections are consistent with the pinned inventories inspected for this review. Exact `NCBITaxon:1008105` and anchored `Sporosarcina sp. LKS-72` searches with ignored files included found no same-taxon ATB or StrainInfo rows to project.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. If an upstream refresh later adds LPSN, GTDB, ATB, BacDive, or StrainInfo support for `NCBITaxon:1008105`, rerun `just seed`, `just seed-canary NCBITaxon:1008105`, the focused strict validator, and `just verify-corpus` before accepting the regenerated YAML.

## Additional Notes

Live authority pages were not used for this batch; the review used the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv` as the local source of truth.
