# YAML Record Review: Mesorhizobium sp. CCBAU 831015

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mesorhizobium_sp_ccbau_831015.yaml`
- Started UTC: 2026-09-22T18:16:34Z
- Finished UTC: 2026-09-22T18:17:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004269` |
| Label | `Mesorhizobium sp. CCBAU 831015` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:325217` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species-level record under the `unclassified Mesorhizobium` no-rank parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mesorhizobium_sp_ccbau_831015.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/oceanobacillus_indicireducens.yaml data/taxa/bacteria/bacillus_sp_mra1.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_monolepta_hieroglyphica.yaml data/taxa/bacteria/mesorhizobium_sp_ccbau_831015.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004269` is the pinned NCBI row for `Mesorhizobium sp. CCBAU 831015`, rank `SPECIES`, parent `NCBITaxon:325217`, and genetic code `11`. The lineage follows NCBI from `Bacteria` through `Pseudomonadota`, `Alphaproteobacteria`, `Hyphomicrobiales`, `Phyllobacteriaceae`, `Mesorhizobium`, and `unclassified Mesorhizobium`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and lineage | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004269`, label `Mesorhizobium sp. CCBAU 831015`, rank `SPECIES`, parent `NCBITaxon:325217`, genetic code `11`, and `ncbitaxon` as its only source. |
| Seed provenance | The seed history lists the expected single source: `NCBITAXON`. |

## Completeness

The empty `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows. A gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1004269` and the slug found only the NCBI taxonomy row plus the `PATHS.tsv` entry for this target.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004269`.

## Additional Notes

The live NCBI lookup was unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot.
