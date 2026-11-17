# YAML Record Review: Haloterrigena sp. tarium 17-2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/archaea/haloterrigena_sp_tarium_17_2.yaml`
- Started UTC: 2026-09-22T18:32:40Z
- Finished UTC: 2026-09-22T18:34:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004298` |
| Label | `Haloterrigena sp. tarium 17-2` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2631942` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level archaeal record under the `unclassified Haloterrigena` no-rank parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/haloterrigena_sp_tarium_17_2.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/stanieria_sp_ue7a.yaml data/taxa/bacteria/stanieria_sp_ue7d.yaml data/taxa/archaea/haloterrigena_sp_tarium_17_2.yaml data/taxa/archaea/haloterrigena_sp_tarium_161_1.yaml` | Pass; the strict batch exited 0. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004298` is the pinned NCBI row for `Haloterrigena sp. tarium 17-2`, rank `SPECIES`, parent `NCBITaxon:2631942`, and genetic code `11`. The lineage follows NCBI through `Methanobacteriati`, `Methanobacteriota`, `Stenosarchaea group`, `Halobacteria`, `Halobacteriales`, `Natrialbaceae`, `Haloterrigena`, and `unclassified Haloterrigena`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004298`, label `Haloterrigena sp. tarium 17-2`, rank `SPECIES`, parent `NCBITaxon:2631942`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | The seed history lists the expected single source: `NCBITAXON`. |

## Completeness

The empty `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. A gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1004298`, `Haloterrigena sp. tarium 17-2`, and `haloterrigena_sp_tarium_17_2` found only the NCBI taxonomy row plus the `PATHS.tsv` entry for this target.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004298`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-haloterrigena_sp_tarium_17_2.md'` check found no prior ignored local report before this one was written. The live NCBI lookup was unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
