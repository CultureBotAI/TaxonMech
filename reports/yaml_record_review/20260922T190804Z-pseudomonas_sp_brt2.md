# YAML Record Review: Pseudomonas sp. BRT2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_brt2.yaml`
- Started UTC: 2026-09-22T19:07:27Z
- Finished UTC: 2026-09-22T19:08:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004358` |
| Label | `Pseudomonas sp. BRT2` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:196821` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level record under the `unclassified Pseudomonas` no-rank parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_sp_brt2.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/pedobacter_sp_hrt7.yaml data/taxa/bacteria/pseudomonas_sp_brb6.yaml data/taxa/bacteria/pseudomonas_sp_brb7.yaml data/taxa/bacteria/pseudomonas_sp_brt2.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004358` is the pinned NCBI row for `Pseudomonas sp. BRT2`, rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, `Pseudomonas`, and `unclassified Pseudomonas`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004358`, label `Pseudomonas sp. BRT2`, rank `SPECIES`, parent `NCBITaxon:196821`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | The seed history lists the expected single source: `NCBITAXON`. |

## Completeness

The empty `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. Gitignore-independent `rg --no-ignore --hidden` scans over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found only the NCBI taxonomy row plus the scope and path entries for this exact NCBI ID.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004358`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_brt2.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
