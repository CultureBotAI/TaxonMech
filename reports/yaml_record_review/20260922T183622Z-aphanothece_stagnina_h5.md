# YAML Record Review: Aphanothece stagnina H5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aphanothece_stagnina_h5.yaml`
- Started UTC: 2026-09-22T18:35:04Z
- Finished UTC: 2026-09-22T18:36:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004306` |
| Label | `Aphanothece stagnina H5` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1004305` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI strain-level record under `Aphanothece stagnina`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/aphanothece_stagnina_h5.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/hydrotalea_sandarakina.yaml data/taxa/bacteria/aphanothece_stagnina.yaml data/taxa/bacteria/aphanothece_stagnina_h5.yaml data/taxa/bacteria/nostoc_sp_r5.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004306` is the pinned NCBI row for `Aphanothece stagnina H5`, rank `STRAIN`, parent `NCBITaxon:1004305`, and genetic code `11`. The lineage follows NCBI through `Cyanobacteriota`, `Cyanophyceae`, `Oscillatoriophycideae`, `Chroococcales`, `Aphanothecaceae`, `Aphanothece`, and `Aphanothece stagnina`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004306`, label `Aphanothece stagnina H5`, rank `STRAIN`, parent `NCBITaxon:1004305`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | The seed history lists the expected single source: `NCBITAXON`. |

## Completeness

The empty `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. A gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1004306`, `Aphanothece stagnina H5`, and `aphanothece_stagnina_h5` found only the NCBI taxonomy row plus the `PATHS.tsv` entry for this target.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004306`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-aphanothece_stagnina_h5.md'` check found no prior ignored local report before this one was written. The live NCBI lookup was unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
