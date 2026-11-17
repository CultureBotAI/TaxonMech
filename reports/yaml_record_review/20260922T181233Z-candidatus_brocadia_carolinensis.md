# YAML Record Review: Candidatus Brocadia carolinensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_brocadia_carolinensis.yaml`
- Started UTC: 2026-09-22T18:10:48Z
- Finished UTC: 2026-09-22T18:12:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004156` |
| Label | `Candidatus Brocadia carolinensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:380240` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated species-level taxon record under `data/taxa/bacteria/`, owned by the pinned source inventories and the TaxonMech seeder.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_brocadia_carolinensis.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_aa86.yaml data/taxa/bacteria/candidatus_brocadia_carolinensis.yaml data/taxa/bacteria/photorhabdus_tasmaniensis.yaml data/taxa/bacteria/photorhabdus_caribbeanensis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004156` is the pinned NCBI species row for `Candidatus Brocadia carolinensis`, with parent genus `NCBITaxon:380240`. The root-first lineage in the YAML carries that NCBI placement through `Planctomycetota`, `Candidatus Brocadiia`, `Candidatus Brocadiales`, `Candidatus Brocadiaceae`, and `Candidatus Brocadia`.

The synonym set preserves the spelling correction visible in NCBI: `Candidatus Brocadia caroliniensis` is an exact synonym, and the corrected `Candidatus Brocadia carolinensis` authority string plus `Candidatus Brocadia sp. NRRL B-50286` are related synonyms. `GTDB:s__Brocadia_carolinensis` maps directly to this species with a single genome, and the GTDB-derived exact synonym `Brocadia carolinensis` agrees with the NCBI exact synonym.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI species identity and synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004156`, label `Candidatus Brocadia carolinensis`, rank `SPECIES`, parent `NCBITaxon:380240`, genetic code `11`, the exact synonyms, and the related synonyms that appear in the YAML. |
| GTDB species mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Brocadia_carolinensis` to `NCBITaxon:1004156` with `skos:closeMatch` and genome count `1`. |
| Madin attestation | `data/raw/madin_taxa.tsv` has `NCBITaxon:1004156` with count `2`, matching the `MADIN` `TRAIT_ASSERTION` attestation. |
| Seed provenance | The seed history lists exactly the sources found for this target: `GTDB`, `MADIN`, and `NCBITAXON`. |

## Completeness

The empty `nomenclature`, `strains`, record-level `evidence`, `causal_graphs`, and discussion sections are appropriate for the inspected source rows. A gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1004156` and the slug found only NCBI, GTDB, and Madin records for this exact taxon; no same-taxon BacDive, LPSN, MediaDive, GOLD, BactoTraits, StrainInfo, or AllTheBacteria rows were present.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004156` or `GTDB:s__Brocadia_carolinensis`.

## Additional Notes

The live NCBI lookup was unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot that seeds the record.
