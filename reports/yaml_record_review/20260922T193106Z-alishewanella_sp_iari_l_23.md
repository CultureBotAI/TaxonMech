# YAML Record Review: Alishewanella sp. IARI-L-23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alishewanella_sp_iari_l_23.yaml`
- Started UTC: 2026-09-22T19:29:37Z
- Finished UTC: 2026-09-22T19:31:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004541` |
| Label | `Alishewanella sp. IARI-L-23` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2628974` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level record under the `unclassified Alishewanella` no-rank parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/alishewanella_sp_iari_l_23.yaml` | Pass; `linkml-validate` exited 0 with no diagnostics. |
| `just validate-strict data/taxa/bacteria/alishewanella_sp_iari_l_23.yaml data/taxa/bacteria/arthrobacter_sp_iari_l_120.yaml data/taxa/bacteria/arthrobacter_sp_iari_l_29.yaml data/taxa/bacteria/arthrobacter_sp_iari_l_72.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004541` is the pinned NCBI row for `Alishewanella sp. IARI-L-23`, rank `SPECIES`, parent `NCBITaxon:2628974`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadota`, `Gammaproteobacteria`, `Alteromonadales`, `Alteromonadaceae`, `Alishewanella`, and `unclassified Alishewanella`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004541`, label `Alishewanella sp. IARI-L-23`, rank `SPECIES`, parent `NCBITaxon:2628974`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | `curation/seed_scope.tsv` lists `NCBITaxon:1004541` as in scope by an `attested rule` with 1 source including NCBI. |

## Completeness

The omitted `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. Gitignore-independent `rg --no-ignore --hidden` scans over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found only the NCBI taxonomy row plus the scope and path entries for this exact NCBI ID and label.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004541`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-alishewanella_sp_iari_l_23.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
