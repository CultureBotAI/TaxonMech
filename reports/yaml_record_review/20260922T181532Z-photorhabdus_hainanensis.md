# YAML Record Review: Photorhabdus hainanensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photorhabdus_hainanensis.yaml`
- Started UTC: 2026-09-22T18:13:52Z
- Finished UTC: 2026-09-22T18:15:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004166` |
| Label | `Photorhabdus hainanensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:29487` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated species record with one listed BacDive strain, `bacdive:5050` / C8404.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/photorhabdus_hainanensis.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/photorhabdus_hainanensis.yaml data/taxa/eukaryota/williopsis_mrakii.yaml data/taxa/eukaryota/williopsis_subsufficiens.yaml data/taxa/bacteria/capnocytophaga_catalasegens.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004166` is the pinned NCBI species row for `Photorhabdus hainanensis`, parented by `Photorhabdus` with genetic code `11`. LPSN row `lpsn:798514` is the correct species name and lists `CIP-109946` and `DSM-22397`; those type designations match two of the culture-collection deposits on the BacDive C8404 strain, so `is_type_strain: true` is supported.

GTDB places the NCBI species' DSM 22397 genome in `GTDB:s__Photorhabdus_akhurstii`; TaxonMech keeps that as a 1:1 `skos:closeMatch` taxonomy mapping while keeping LPSN's `Photorhabdus hainanensis` as the nomenclatural name. The mapping is a visible GTDB-vs-LPSN taxonomic disagreement, not a wrong NCBI grounding.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004166`, label `Photorhabdus hainanensis`, rank `SPECIES`, parent `NCBITaxon:29487`, genetic code `11`, and the NCBI synonym spellings in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:798514` carries the `Photorhabdus hainanensis` species name, correct-name status, DOI/PMID and INSDC support, and CIP/DSM type-strain designations. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Photorhabdus_akhurstii` to `NCBITaxon:1004166` as `skos:closeMatch` with count `27`. |
| Direct source counts | Exact rows support `MEDIADIVE` count `4` in `data/raw/mediadive_taxa.tsv` and `GOLD` count `1` in `data/raw/gold_organisms.tsv`. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:5050`, designation `C8404`, exact taxon `NCBITaxon:1004166`, LPSN id `lpsn:798514`, and the CIP/CN/DSM culture-collection deposits present in the YAML. |
| Genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/straininfo/assemblies.tsv`, `data/straininfo/strain_links.tsv`, and compressed `data/straininfo/related_records.tsv.gz` support the NCBI, GTDB, GOLD, IMG, BV-BRC/PATRIC, BioProject, BioSample, INSDC, StrainInfo deposit, and StrainInfo strain rows for `bacdive:5050`. |

## Completeness

The record has the exact NCBI, LPSN, GTDB, BacDive, MediaDive, and GOLD source coverage found by the ignored-file scans for this species and its C8404 strain. `strain_count: 1` matches the single `bacdive_5050` source row filed under `NCBITaxon:1004166`.

The older `Photorhabdus luminescens` GOLD organism for CIP 109946 is preserved only as a typed related record through an exact culture-deposit match. It does not alter the record's species identity.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused validators and an exact `rg --no-ignore --hidden` scan for `NCBITaxon:1004166`, `bacdive:5050`, `straininfo.strain:370406`, `lpsn:798514`, and `GTDB:s__Photorhabdus_akhurstii` after any source refresh that changes this species or the C8404 strain.

## Additional Notes

The `GTDB:s__Photorhabdus_akhurstii` exact synonym comes from the 1:1 GTDB `closeMatch` mapping; LPSN does not link that GTDB species to `lpsn:798514`, so the mismatch is worth preserving in future manual reviews.
