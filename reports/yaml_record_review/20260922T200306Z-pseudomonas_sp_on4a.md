# YAML Record Review: Pseudomonas sp. ON4a

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_on4a.yaml`
- Started UTC: 2026-09-22T20:01:39Z
- Finished UTC: 2026-09-22T20:03:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:100476` |
| Label | `Pseudomonas sp. ON4a` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:196821` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level record under the `unclassified Pseudomonas` no-rank parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_sp_on4a.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_on4a.yaml data/taxa/bacteria/aphanothece_stagnina_h7.yaml data/taxa/bacteria/phoenix_dactylifera_lethal_yellowing_phytoplasma.yaml data/taxa/bacteria/sabal_palmetto_lethal_yellowing_phytoplasma.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:100476` is the pinned NCBI row for `Pseudomonas sp. ON4a`, rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, `Pseudomonas`, and `unclassified Pseudomonas`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:100476`, label `Pseudomonas sp. ON4a`, rank `SPECIES`, parent `NCBITaxon:196821`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | `curation/seed_scope.tsv` lists `NCBITaxon:100476` as in scope by an `attested rule` with 1 source including NCBI. |

## Completeness

The omitted `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. A boundary-guarded, gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found only the NCBI taxonomy row plus the scope and path entries for this exact NCBI ID and label.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:100476`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_on4a.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
