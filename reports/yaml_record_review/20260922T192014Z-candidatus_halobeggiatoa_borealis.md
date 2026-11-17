# YAML Record Review: Candidatus Halobeggiatoa borealis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_halobeggiatoa_borealis.yaml`
- Started UTC: 2026-09-22T19:18:43Z
- Finished UTC: 2026-09-22T19:20:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004492` |
| Label | `Candidatus Halobeggiatoa borealis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1003179` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |
| Synonyms | 8 NCBI related synonyms |

This is a generated NCBI species-level record under the `Candidatus Halobeggiatoa` clade.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_halobeggiatoa_borealis.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/candidatus_halobeggiatoa_borealis.yaml data/taxa/bacteria/candidatus_halobeggiatoa_sp_hmw_s2528.yaml data/taxa/bacteria/candidatus_halobeggiatoa_sp_hmw_w562.yaml data/taxa/bacteria/candidatus_halobeggiatoa_sp_hmw_w572.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004492` is the pinned NCBI row for `Candidatus Halobeggiatoa borealis`, rank `SPECIES`, parent `NCBITaxon:1003179`, and genetic code `11`. The lineage follows NCBI through `Pseudomonadota`, `Gammaproteobacteria`, `Thiotrichales`, `Thiotrichaceae`, and `Candidatus Halobeggiatoa`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004492`, label `Candidatus Halobeggiatoa borealis`, rank `SPECIES`, parent `NCBITaxon:1003179`, genetic code `11`, and `ncbitaxon` as its only source. |
| NCBI related synonyms | The same `data/raw/ncbitaxon_taxa.tsv` row has the eight related synonyms projected in this YAML record. |
| Seed provenance | `curation/seed_scope.tsv` lists `NCBITaxon:1004492` as in scope by an `attested rule` with 1 source including NCBI. |

## Completeness

The omitted `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. Gitignore-independent `rg --no-ignore --hidden` scans over `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found the NCBI taxonomy, scope, path, and NCBI merged-ID rows for this exact NCBI ID and label, with no ATB or StrainInfo rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004492`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-candidatus_halobeggiatoa_borealis.md'` check, which includes ignored report files, found no prior local report before this one was written. `data/raw/ncbi_merged_ids.tsv` maps old IDs `NCBITaxon:1004487`, `NCBITaxon:1004488`, `NCBITaxon:1004489`, `NCBITaxon:1004490`, `NCBITaxon:1004491`, and `NCBITaxon:1004493` into this current ID, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at it with `retired_into`, so the generated record correctly omits `replaces`. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
