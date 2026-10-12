# YAML Record Review: Capnocytophaga catalasegens

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/capnocytophaga_catalasegens.yaml`
- Started UTC: 2026-09-22T18:13:52Z
- Finished UTC: 2026-09-22T18:15:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004260` |
| Label | `Capnocytophaga catalasegens` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1016` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated bacterial species record with one listed BacDive strain, `bacdive:170807` / KC07084.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/capnocytophaga_catalasegens.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/photorhabdus_hainanensis.yaml data/taxa/eukaryota/williopsis_mrakii.yaml data/taxa/eukaryota/williopsis_subsufficiens.yaml data/taxa/bacteria/capnocytophaga_catalasegens.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004260` is the pinned NCBI species row for `Capnocytophaga catalasegens`, parented by genus `NCBITaxon:1016` with genetic code `11`. The LPSN row `lpsn:37149` is the correct species name and lists `DSM-107252` and `JCM-32682`, which are the BacDive deposits for KC07084 and support `is_type_strain: true`.

`GTDB:s__Capnocytophaga_catalasegens` maps directly to this species with `skos:closeMatch` and genome count `3`; LPSN also links that GTDB species to `lpsn:37149`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and related synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004260`, label `Capnocytophaga catalasegens`, rank `SPECIES`, parent `NCBITaxon:1016`, genetic code `11`, and the four NCBI related synonyms in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:37149` carries the `Capnocytophaga catalasegens` species name, correct-name status, DOI/PMID and INSDC support, and DSM/JCM type-strain designations. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Capnocytophaga_catalasegens` to `NCBITaxon:1004260` as `skos:closeMatch` with count `3`. |
| Direct source counts | Exact rows support `MEDIADIVE` count `1` in `data/raw/mediadive_taxa.tsv` and `GOLD` count `2` in `data/raw/gold_organisms.tsv`. |
| BacDive strain and StrainInfo related records | `data/raw/bacdive_strains.tsv` has `bacdive:170807`, designation `KC07084`, exact taxon `NCBITaxon:1004260`, LPSN id `lpsn:37149`, and DSM/JCM deposits; `data/straininfo/strain_links.tsv` and compressed `data/straininfo/related_records.tsv.gz` support the DSM 107252 SI-DP and SI-ID related records. |

## Completeness

The record has the exact NCBI, LPSN, GTDB, BacDive, MediaDive, and GOLD source coverage found by gitignore-independent searches for `NCBITaxon:1004260`, `lpsn:37149`, `GTDB:s__Capnocytophaga_catalasegens`, and `bacdive:170807`. `strain_count: 1` matches the single BacDive row filed under this species.

The StrainInfo rows retain source taxon `NCBITaxon:1016`, the `Capnocytophaga` genus, but they are attached only as related records through BacDive strain `170807` and exact DSM 107252 culture-deposit evidence. No genome assembly or genome record rows were found for `bacdive:170807`, so the strain is complete without those sections.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused validators and an exact `rg --no-ignore --hidden` scan for `NCBITaxon:1004260`, `bacdive:170807`, `straininfo.strain:399755`, `lpsn:37149`, and `GTDB:s__Capnocytophaga_catalasegens` after any source refresh that changes this species or the KC07084 strain.

## Additional Notes

The NCBI merged-id rows from `NCBITaxon:2898427` and `NCBITaxon:2898428` to `NCBITaxon:1004260` do not require a YAML change; the current record correctly uses the merged target identifier.
