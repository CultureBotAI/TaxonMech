# YAML Record Review: Candidatus Thiopilula aggregata

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_thiopilula_aggregata.yaml`
- Started UTC: 2026-09-22T19:21:20Z
- Finished UTC: 2026-09-22T19:23:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004498` |
| Label | `Candidatus Thiopilula aggregata` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1004497` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Synonyms | 1 NCBI exact synonym and 14 NCBI related synonyms |

This is a generated NCBI species-level record under the `Candidatus Thiopilula` genus.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_thiopilula_aggregata.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/candidatus_thiopilula_aggregata.yaml data/taxa/bacteria/bacillus_sp_0310ard8h_11.yaml data/taxa/bacteria/streptomyces_sp_0310ard15n_6.yaml data/taxa/bacteria/shigella_sp_0310ard15n_4.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004498` is the pinned NCBI row for `Candidatus Thiopilula aggregata`, rank `SPECIES`, parent `NCBITaxon:1004497`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadota`, `Gammaproteobacteria`, `Thiotrichales`, `Thiotrichaceae`, and `Candidatus Thiopilula`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004498`, label `Candidatus Thiopilula aggregata`, rank `SPECIES`, parent `NCBITaxon:1004497`, genetic code `11`, and `ncbitaxon` as its only source. |
| NCBI synonyms | The same `data/raw/ncbitaxon_taxa.tsv` row has exact synonym `Thiopilula aggregata` plus the fourteen related synonyms projected in this YAML record. |
| Seed provenance | `curation/seed_scope.tsv` lists `NCBITaxon:1004498` as in scope by an `attested rule` with 1 source including NCBI. |

## Completeness

The omitted `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. Gitignore-independent `rg --no-ignore --hidden` scans over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found the NCBI taxonomy, scope, path, and NCBI merged-ID rows for this exact NCBI ID and label, with no ATB or StrainInfo rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004498`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-candidatus_thiopilula_aggregata.md'` check, which includes ignored report files, found no prior local report before this one was written. `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:886765` through `NCBITaxon:886777` into this current ID, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at it with `retired_into`, so the generated record correctly omits `replaces`. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
