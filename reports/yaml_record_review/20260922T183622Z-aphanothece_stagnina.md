# YAML Record Review: Aphanothece stagnina

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aphanothece_stagnina.yaml`
- Started UTC: 2026-09-22T18:35:04Z
- Finished UTC: 2026-09-22T18:36:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004305` |
| Label | `Aphanothece stagnina` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1121` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level Cyanobacteriota record enriched by one BacDive strain and one MediaDive medium count.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/aphanothece_stagnina.yaml` | Pass; `linkml-validate` exited 0. |
| `just validate-strict data/taxa/bacteria/hydrotalea_sandarakina.yaml data/taxa/bacteria/aphanothece_stagnina.yaml data/taxa/bacteria/aphanothece_stagnina_h5.yaml data/taxa/bacteria/nostoc_sp_r5.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004305` is the pinned NCBI row for `Aphanothece stagnina`, rank `SPECIES`, parent `NCBITaxon:1121`, and genetic code `11`. The lineage follows NCBI through `Cyanobacteriota`, `Cyanophyceae`, `Oscillatoriophycideae`, `Chroococcales`, `Aphanothecaceae`, and `Aphanothece`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, lineage, and synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004305`, label `Aphanothece stagnina`, rank `SPECIES`, parent `NCBITaxon:1121`, genetic code `11`, exact synonym `Coccochloris stagnina`, and the two related synonyms shown in the record. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:140170` classified under `NCBITaxon:1004305` with deposits `CCY 0618` and `DSM 101312`, matching the single projected strain. |
| StrainInfo deposit links | `data/straininfo/strain_links.tsv` links `kgmicrobe.strain:bacdive_140170` to `straininfo.strain:400253` and `straininfo.deposit:907106` through DSM 101312, matching the projected related records. |
| Source attestation counts | `data/raw/ncbitaxon_taxa.tsv`, `data/raw/bacdive_strains.tsv`, and `data/raw/mediadive_taxa.tsv` provide the NCBI name, one BacDive strain, and one MediaDive medium attested in the record. |

## Completeness

The three NCBI synonyms, one BacDive strain, StrainInfo related records, and NCBI/BacDive/MediaDive source attestations are populated from the inspected rows. The empty `nomenclature`, `taxonomy_mappings`, `xrefs`, record-level `evidence`, `causal_graphs`, and discussion sections are appropriate for the local source rows.

An exact, gitignore-independent `find` found no prior local review for this stem. The `rg --no-ignore --hidden` scans covered `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv`; same-label Aphanothece strain records exist elsewhere in `PATHS.tsv`, but only `NCBITaxon:1004305` owns the species-level rows reviewed here.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004305`, `bacdive:140170`, or `straininfo.strain:400253`.

## Additional Notes

Live source lookups were unavailable during this run, so identity and evidence were checked against the pinned committed source snapshots under `data/raw/` and `data/straininfo/`.
