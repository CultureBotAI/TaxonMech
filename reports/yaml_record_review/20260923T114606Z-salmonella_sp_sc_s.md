# YAML Record Review: Salmonella sp. sc-S

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_sp_sc_s.yaml`
- Started UTC: 2026-09-23T11:46:06Z
- Finished UTC: 2026-09-23T11:46:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/salmonella_sp_sc_s.yaml` |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1008303` |
| Label | `Salmonella sp. sc-S` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2614656` / `unclassified Salmonella` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |

This is a generated NCBI-only species placeholder under `unclassified Salmonella`.

## Validation

| Check | Result |
|---|---|
| Full target read | Passed; `sed -n '1,320p' data/taxa/bacteria/salmonella_sp_sc_s.yaml` covered all 53 lines. |
| Prior-report search | Passed; `find reports/yaml_record_review -maxdepth 1 -type f -name '*-salmonella_sp_sc_s.md'` found no prior report. `find` includes ignored report files. |
| Strict schema | Passed; `just validate-strict data/taxa/bacteria/streptomyces_sp_1004.yaml data/taxa/bacteria/streptomyces_sp_1055.yaml data/taxa/bacteria/streptomyces_sp_1209.yaml data/taxa/bacteria/salmonella_sp_sc_s.yaml` scanned 4 files with 0 error rows. |
| LinkML schema | Passed; `just validate data/taxa/bacteria/salmonella_sp_sc_s.yaml` returned `No issues found`. |
| Same-taxon source search | Passed; `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found this ID only in `PATHS.tsv` and the singleton NCBI source row. |
| Label search | Passed; a gitignore-independent fixed-string search for `Salmonella sp. sc-S` found only the exact NCBI source row. |
| History validation | Skipped; no `history/` decision record was added during this read-only review. |
| Corpus reproduction | Skipped; generated `data/taxa` YAML was not edited, and earlier full-corpus reproduction over the 625,960-record corpus was already clean. |
| Product ID/label validation | Skipped; this record has no `causal_graphs` or curator-added graph nodes. |

## Identity and Grounding

The YAML matches `data/raw/ncbitaxon_taxa.tsv:211309`: `NCBITaxon:1008303`, label `Salmonella sp. sc-S`, rank `SPECIES`, parent `NCBITaxon:2614656`, bacterial genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage is root-first through Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Enterobacteriaceae, `Salmonella`, then `unclassified Salmonella`. No auxiliary sources are projected onto this placeholder.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| Core NCBI identity fields | `data/raw/ncbitaxon_taxa.tsv:211309` | Supported exactly. |
| NCBI source attestation | One exact NCBI source row | Supported exactly. |
| Absent optional auxiliary sections | Gitignore-independent exact ID search across `data/raw`, `data/atb`, and `data/straininfo` | Supported by no same-taxon auxiliary rows. |

## Completeness

The record is complete for a singleton NCBI placeholder. The exact ignored-report search found no prior review for `salmonella_sp_sc_s`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run focused strict and LinkML validation after a source refresh.
- Repeat exact ID searches before projecting any auxiliary source rows.

## Additional Notes

No live NCBI lookup was available; the local pinned NCBI row was treated as the source of truth.
