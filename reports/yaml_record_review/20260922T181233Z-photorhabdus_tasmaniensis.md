# YAML Record Review: Photorhabdus tasmaniensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photorhabdus_tasmaniensis.yaml`
- Started UTC: 2026-09-22T18:10:48Z
- Finished UTC: 2026-09-22T18:12:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004159` |
| Label | `Photorhabdus tasmaniensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:29487` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated species record. The one listed BacDive strain, `bacdive:5052`, is the T327 type strain with CIP and DSM culture-collection deposits.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/photorhabdus_tasmaniensis.yaml` | Pass; `linkml-validate` exited 0. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_aa86.yaml data/taxa/bacteria/candidatus_brocadia_carolinensis.yaml data/taxa/bacteria/photorhabdus_tasmaniensis.yaml data/taxa/bacteria/photorhabdus_caribbeanensis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004159` is the pinned NCBI species row for `Photorhabdus tasmaniensis`, parented by the `Photorhabdus` genus with genetic code `11`. The record's LPSN entry `lpsn:798523` is the correct species name, and its type designations `CIP-109948` and `DSM-22387` match deposits on the single BacDive strain.

`GTDB:s__Photorhabdus_tasmaniensis` maps to the same species with `skos:closeMatch` and genome count `3`, so the GTDB mapping, xref, and source attestation are at species scope rather than strain scope.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity and synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004159`, label `Photorhabdus tasmaniensis`, rank `SPECIES`, parent `NCBITaxon:29487`, genetic code `11`, and the synonym spellings in the YAML. |
| LPSN correct-name nomenclature | `data/raw/lpsn_names.tsv` row `lpsn:798523` carries the `Photorhabdus tasmaniensis` species name, correct-name status, DOI/PMID and INSDC support, and CIP/DSM type-strain designations. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Photorhabdus_tasmaniensis` to `NCBITaxon:1004159` as `skos:closeMatch` with count `3`. |
| Direct source counts | Exact rows support `MEDIADIVE` count `4` in `data/raw/mediadive_taxa.tsv` and `GOLD` count `1` in `data/raw/gold_organisms.tsv`. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `bacdive:5052`, designation `T327`, exact taxon `NCBITaxon:1004159`, LPSN id `lpsn:798523`, and the ATU/CIP/DSM culture-collection deposits present in the YAML. |
| Genome and related records | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/straininfo/strain_links.tsv`, and compressed `data/straininfo/related_records.tsv.gz` support the NCBI, BV-BRC/PATRIC, IMG, GOLD, BioProject, BioSample, StrainInfo, and INSDC related records for `bacdive:5052`. |

## Completeness

The record has the one BacDive strain filed under `NCBITaxon:1004159`, the one LPSN correct-name entry linked to that species, and every direct NCBI, GTDB, BacDive, LPSN, MediaDive, and GOLD source attestation found by the exact gitignore-independent searches.

Some genome and related records retain older `NCBITaxon:574560` / `Photorhabdus temperata` source taxonomy. Those rows are still complete in this record because they are tied to `kgmicrobe.strain:bacdive_5052` through the exact BacDive source or an explicit DSM 22387 culture-deposit match.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused validators and an exact `rg --no-ignore --hidden` scan for `NCBITaxon:1004159`, `bacdive:5052`, `straininfo.strain:370407`, `lpsn:798523`, and `GTDB:s__Photorhabdus_tasmaniensis` after any source refresh that changes this species or the T327 strain.

## Additional Notes

The record has no curator-authored `causal_graphs` and no record-level `evidence`; seeded source provenance through `source_attestations` and strain-level related-record provenance is sufficient here.
