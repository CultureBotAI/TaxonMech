# YAML Record Review: Photorhabdus caribbeanensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photorhabdus_caribbeanensis.yaml`
- Started UTC: 2026-09-22T18:10:48Z
- Finished UTC: 2026-09-22T18:12:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004165` |
| Label | `Photorhabdus caribbeanensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:29487` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated species record for `Photorhabdus caribbeanensis`; the single listed BacDive strain is `bacdive:5049` / HG29.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/photorhabdus_caribbeanensis.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_aa86.yaml data/taxa/bacteria/candidatus_brocadia_carolinensis.yaml data/taxa/bacteria/photorhabdus_tasmaniensis.yaml data/taxa/bacteria/photorhabdus_caribbeanensis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004165` is the pinned NCBI species row for `Photorhabdus caribbeanensis`, parented by `NCBITaxon:29487` with genetic code `11`. LPSN row `lpsn:798513` is the correct species name and lists the CIP 109949 and DSM 22391 designations that match the HG29 BacDive strain.

`GTDB:s__Photorhabdus_caribbeanensis` maps to this species with `skos:closeMatch` and genome count `2`, and the LPSN row links that GTDB species to the same name, so the GTDB mapping, xref, and attestation are scoped correctly.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004165`, label `Photorhabdus caribbeanensis`, rank `SPECIES`, parent `NCBITaxon:29487`, genetic code `11`, and the NCBI synonym spellings in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:798513` carries the `Photorhabdus caribbeanensis` species name, correct-name status, DOI/PMID and INSDC support, and CIP/DSM type-strain designations. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Photorhabdus_caribbeanensis` to `NCBITaxon:1004165` as `skos:closeMatch` with count `2`. |
| Direct source counts | Exact rows support `MEDIADIVE` count `2` in `data/raw/mediadive_taxa.tsv` and `GOLD` count `1` in `data/raw/gold_organisms.tsv`. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:5049`, designation `HG29`, exact taxon `NCBITaxon:1004165`, LPSN id `lpsn:798513`, and the CIP/DSM culture-collection deposits present in the YAML. |
| Genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/straininfo/strain_links.tsv`, and compressed `data/straininfo/related_records.tsv.gz` support the NCBI, GOLD, IMG, PATRIC, BioProject, BioSample, StrainInfo deposit, and StrainInfo strain rows for `bacdive:5049`. |

## Completeness

The record has the exact NCBI, LPSN, GTDB, BacDive, MediaDive, and GOLD source coverage found by gitignore-independent searches for `NCBITaxon:1004165`, `bacdive:5049`, `lpsn:798513`, `GTDB:s__Photorhabdus_caribbeanensis`, `straininfo.strain:370405`, and the linked GOLD identifiers.

The older `Photorhabdus luminescens` GOLD organism for CIP 109949 is preserved only as a typed related record with an exact culture-deposit match. It does not alter the taxon identity or over-count the one direct GOLD organism filed under `NCBITaxon:1004165`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused validators and the exact source-ID search after any refresh touching HG29, CIP 109949, DSM 22391, `lpsn:798513`, or `GTDB:s__Photorhabdus_caribbeanensis`.

## Additional Notes

The record has no curator-authored `causal_graphs` and no record-level `evidence`; the seeded source attestations and per-strain related-record provenance are adequate for the claims reviewed.
