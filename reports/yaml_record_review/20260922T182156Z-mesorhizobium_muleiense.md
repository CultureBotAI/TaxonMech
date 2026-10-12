# YAML Record Review: Mesorhizobium muleiense

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mesorhizobium_muleiense.yaml`
- Started UTC: 2026-09-22T18:20:55Z
- Finished UTC: 2026-09-22T18:21:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004279` |
| Label | `Mesorhizobium muleiense` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:68287` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated bacterial species record with one listed BacDive strain, `bacdive:130530`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mesorhizobium_muleiense.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/mesorhizobium_sp_ccbau_83943.yaml data/taxa/bacteria/mesorhizobium_sp_ccbau_83948.yaml data/taxa/bacteria/mesorhizobium_sp_ccbau_83953.yaml data/taxa/bacteria/mesorhizobium_muleiense.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004279` is the pinned NCBI species row for `Mesorhizobium muleiense`, parented directly by genus `NCBITaxon:68287` with genetic code `11`. LPSN row `lpsn:790290` is the correct species name and lists `DSM-100038`; that designation matches one BacDive deposit on `bacdive:130530` and supports `is_type_strain: true`.

`GTDB:s__Mesorhizobium_muleiense` maps to this species with `skos:closeMatch` and genome count `62`; LPSN links that GTDB species to the same name.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and related synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004279`, label `Mesorhizobium muleiense`, rank `SPECIES`, parent `NCBITaxon:68287`, genetic code `11`, and the five NCBI related synonyms in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:790290` carries the `Mesorhizobium muleiense` species name, correct-name status, DOI/PMID and INSDC support, and the DSM type-strain designation. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Mesorhizobium_muleiense` to `NCBITaxon:1004279` as `skos:closeMatch` with count `62`. |
| Direct source counts | Exact rows support `MEDIADIVE` count `1`, `GOLD` count `4`, `MADIN` count `16`, and `BACTOTRAITS` count `14`. |
| BacDive strain and linked genomes | `data/raw/bacdive_strains.tsv` has `bacdive:130530` with exact taxon `NCBITaxon:1004279`, LPSN id `lpsn:790290`, and the CCBAU/CGMCC/DSM/HAMBI deposits; `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` support the NCBI, GTDB, GOLD, IMG, BV-BRC/PATRIC, BioProject, BioSample, and GOLD related records. |
| AllTheBacteria and StrainInfo overlays | `data/atb/strain_links.tsv`, `data/atb/genome_links.tsv`, `data/straininfo/strain_links.tsv`, and compressed `data/straininfo/related_records.tsv.gz` support the `atb.assembly:202505.SAMN05428953` genome, the shared BioSample chains, and the DSM 100038 SI-DP/SI-ID related records. |

## Completeness

The record has the exact NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, BactoTraits, AllTheBacteria, and StrainInfo rows found by gitignore-independent searches for `NCBITaxon:1004279`, `bacdive:130530`, `lpsn:790290`, `GTDB:s__Mesorhizobium_muleiense`, `biosample:SAMN05428953`, and `straininfo.strain:401978`.

`strain_count: 1` matches the one BacDive row filed under this species. The NCBI merged IDs `NCBITaxon:1004270`, `NCBITaxon:1004275`, and `NCBITaxon:1472393` correctly collapse into the current `NCBITaxon:1004279` record and do not require separate YAML records.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused validators and an exact `rg --no-ignore --hidden` scan for `NCBITaxon:1004279`, `bacdive:130530`, `atb.assembly:202505.SAMN05428953`, `straininfo.strain:401978`, `lpsn:790290`, and `GTDB:s__Mesorhizobium_muleiense` after any source refresh that changes this species or the CGMCC 1.11022 / DSM 100038 strain links.

## Additional Notes

The BacDive source row has no free-text `designation`, so the YAML correctly represents the strain through its culture-collection identifiers and related genome evidence rather than inventing a bare designation.
