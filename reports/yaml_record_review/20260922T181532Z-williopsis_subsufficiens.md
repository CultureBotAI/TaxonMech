# YAML Record Review: Williopsis subsufficiens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/eukaryota/williopsis_subsufficiens.yaml`
- Started UTC: 2026-09-22T18:13:52Z
- Finished UTC: 2026-09-22T18:15:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004254` |
| Label | `Williopsis subsufficiens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4962` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated eukaryotic yeast species record under `data/taxa/eukaryota/`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/eukaryota/williopsis_subsufficiens.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/photorhabdus_hainanensis.yaml data/taxa/eukaryota/williopsis_mrakii.yaml data/taxa/eukaryota/williopsis_subsufficiens.yaml data/taxa/bacteria/capnocytophaga_catalasegens.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004254` is the pinned NCBI species row for `Williopsis subsufficiens`, with eukaryotic genetic code `1` and genus parent `NCBITaxon:4962`. The YAML lineage follows the same `Eukaryota` to `Williopsis` parent chain as its neighboring Williopsis record.

The NCBI exact synonyms cover `Cyberlindnera subsufficiens`, `Hansenula saturnus var. subsufficiens`, `Lindnera subsufficiens`, and `Williopsis saturnus var. subsufficiens`; the author-qualified names are related synonyms as projected from the pinned NCBI row.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004254`, label `Williopsis subsufficiens`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, and all exact and related NCBI synonyms projected into the YAML. |
| GOLD attestation | `data/raw/gold_organisms.tsv` has `NCBITaxon:1004254` with count `1`, matching the `GOLD` `ORGANISM` attestation. |
| Seed provenance | The seed history lists exactly the sources found for this target: `GOLD` and `NCBITAXON`. |

## Completeness

No LPSN, GTDB, BacDive, MediaDive, BactoTraits, StrainInfo, AllTheBacteria, record-level `evidence`, or `causal_graphs` entries are expected for the inspected source rows. A gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1004254` and the slug found NCBI, NCBI type-material, and GOLD rows, but no same-taxon rows from those other sources.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004254` or its GOLD organism count.

## Additional Notes

NCBI has type-material rows for the older `Hansenula saturnus var. subsufficiens` name, but TaxonMech does not synthesize BacDive-style strain entries from NCBI fungal type material alone.
