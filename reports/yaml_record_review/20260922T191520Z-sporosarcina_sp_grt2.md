# YAML Record Review: Sporosarcina sp. GRT2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sporosarcina_sp_grt2.yaml`
- Started UTC: 2026-09-22T19:13:04Z
- Finished UTC: 2026-09-22T19:15:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004367` |
| Label | `Sporosarcina sp. GRT2` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2647733` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level record under the `unclassified Sporosarcina` no-rank parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/sporosarcina_sp_grt2.yaml` | Pass; `linkml-validate` exited 0 with no diagnostics. |
| `just validate-strict data/taxa/bacteria/sporosarcina_sp_grt2.yaml data/taxa/bacteria/variovorax_sp_hrt16.yaml data/taxa/bacteria/xanthomonas_sp_brt8.yaml data/taxa/bacteria/oxalobacteraceae_bacterium_hrt30.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004367` is the pinned NCBI row for `Sporosarcina sp. GRT2`, rank `SPECIES`, parent `NCBITaxon:2647733`, and genetic code `11`. The lineage follows NCBI through `Bacillota`, `Bacilli`, `Caryophanales`, `Caryophanaceae`, `Sporosarcina`, and `unclassified Sporosarcina`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004367`, label `Sporosarcina sp. GRT2`, rank `SPECIES`, parent `NCBITaxon:2647733`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | `curation/seed_scope.tsv` lists `NCBITaxon:1004367` as in scope by an `attested rule` with 1 source including NCBI. |

## Completeness

The omitted `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. Gitignore-independent `rg --no-ignore --hidden` scans over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found only the NCBI taxonomy row plus the scope and path entries for this exact NCBI ID and label.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004367`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-sporosarcina_sp_grt2.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
