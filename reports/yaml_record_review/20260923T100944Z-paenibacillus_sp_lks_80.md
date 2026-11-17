# YAML Record Review: Paenibacillus sp. LKS-80

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_lks_80.yaml
- Started UTC: 2026-09-23T10:08:24Z
- Finished UTC: 2026-09-23T10:09:44Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1008086 |
| Label | Paenibacillus sp. LKS-80 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:185978, unclassified Paenibacillus |
| Maintained status | Generated from the committed `data/raw/`, `data/atb/`, and `data/straininfo/` inventories |

This review covered the full generated YAML at `data/taxa/bacteria/paenibacillus_sp_lks_80.yaml`. The record carries one `NCBITAXON` source attestation and has no `synonyms`, `nomenclature`, `taxonomy_mappings`, `strains`, `strain_attestations`, `genome_records`, `genome_assemblies`, `culture_collection_ids`, or `causal_graphs` blocks to audit.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/paenibacillus_sp_lks_71.yaml data/taxa/bacteria/paenibacillus_sp_lks_76.yaml data/taxa/bacteria/paenibacillus_sp_lks_80.yaml data/taxa/bacteria/paenibacillus_sp_lks_85.yaml` | Passed: 4 files scanned, 0 files with errors |
| `just validate data/taxa/bacteria/paenibacillus_sp_lks_80.yaml` | Passed with `No issues found` |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenibacillus_sp_lks_80.md'` | No prior report found; this `find` search includes ignored reports |
| Exact `NCBITaxon:1008086` source search with `rg --no-ignore --hidden` | Found only `data/taxa/PATHS.tsv` and the matching `data/raw/ncbitaxon_taxa.tsv` row |
| Anchored `Paenibacillus sp. LKS-80` source search over `data/raw`, `data/atb`, and `data/straininfo` with `rg --no-ignore --hidden` | Found only the matching NCBI row |
| `just verify-corpus` | Skipped for this report batch: the reviews are read-only, only ignored Markdown reports were added, and an earlier full-corpus verification over 625,960 records was clean |
| `just validate-history` | Skipped: read-only YAML reviews do not add `history/` curation decisions |
| `just validate-products` | Not applicable: this record has no `causal_graphs` product identifiers |

## Identity and Grounding

The YAML identity is supported by the pinned local NCBI row:

| Source | ID | Label | Rank | Parent | Genetic code | Snapshot |
|---|---|---|---|---|---|---|
| `data/raw/ncbitaxon_taxa.tsv` | NCBITaxon:1008086 | Paenibacillus sp. LKS-80 | SPECIES | NCBITaxon:185978 | 11 | 2026-09-13 |

The record's `identifier`, `label`, `rank`, `parent_taxon`, `taxon_domain`, and `genetic_code` agree with that source row and the NCBI lineage carried in the generated YAML. `grounding_status: EXACT` is appropriate because the record is grounded directly to `NCBITaxon:1008086`, and `mapping_status: SEEDED` reflects the generated seed provenance.

## Evidence

The one `source_attestations` entry is narrow and source-backed:

| Claim | Evidence | Assessment |
|---|---|---|
| `NCBITAXON` attests `NCBITaxon:1008086` as `Paenibacillus sp. LKS-80` | Matching `data/raw/ncbitaxon_taxa.tsv` row from the 2026-09-13 snapshot | Supported |
| `assertion_count: 1` with `assertion_unit: NAME` | The record has one NCBI name-row attestation and no auxiliary ATB or StrainInfo row for this exact taxon | Supported |

No citation-bearing claims, synonyms, LPSN nomenclature entries, GTDB mappings, strain links, or genome links are present, so there are no unsupported or over-scoped source assertions to flag.

## Completeness

The empty optional sections are consistent with the pinned inventories inspected for this review. Exact `NCBITaxon:1008086` and anchored `Paenibacillus sp. LKS-80` searches with ignored files included found no same-taxon ATB or StrainInfo rows to project.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. If an upstream refresh later adds LPSN, GTDB, ATB, BacDive, or StrainInfo support for `NCBITaxon:1008086`, rerun `just seed`, `just seed-canary NCBITaxon:1008086`, the focused strict validator, and `just verify-corpus` before accepting the regenerated YAML.

## Additional Notes

Live authority pages were not used for this batch; the review used the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv` as the local source of truth.
