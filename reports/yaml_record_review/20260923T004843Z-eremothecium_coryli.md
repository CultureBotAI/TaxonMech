# YAML Record Review: Eremothecium coryli

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/eremothecium_coryli.yaml
- Started UTC: 2026-09-23T00:48:43Z
- Finished UTC: 2026-09-23T00:48:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:33173` |
| Label | `Eremothecium coryli` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:33170` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/eremothecium_coryli.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epicoccum_nigrum.yaml data/taxa/eukaryota/epicoccum_sorghinum.yaml data/taxa/eukaryota/epithele_typhae.yaml data/taxa/eukaryota/eremothecium_coryli.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine organism assertions, nine exact native GOLD organism rows, no exact native GOLD project/analysis rows, 21 NCBI type-material rows, 22 exact StrainInfo rows with 47 deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:33173`, `label: Eremothecium coryli`, `rank: SPECIES`, `parent_taxon: NCBITaxon:33170`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3548`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Eremothecium` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32331`, which records nine retained direct organisms for `NCBITaxon:33173`; this agrees with `source_attestations[1].assertion_count: 9` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:33173`. The YAML preserves NCBI's exact synonym `Nematospora coryli` plus the related synonyms `Eremothecium coryli (Peglion) Kurtzman, 1995` and `Nematospora coryli Peglion, 1901`; NCBI supplies no broad synonyms and no old-ID side rows.

The native GOLD catalogs contain nine exact organism rows for `Nematospora coryli`, matching the nine retained aggregate assertions and spanning `VKM Y-271`, `NRRL Y-12970`, `NCYC 504`, `NBRC 1220`, `IFO 1220`, `DSM 6981`, `CCRC 21343`, `CBS 2608`, and `ATCC 24237`; no current exact native GOLD projects or analyses are linked.

NCBI type-material evidence contributes 21 aliases for `Nematospora coryli`, including ATCC, BCRC, CBS, CCRC, DBVPG, IFO, NCYC, NRRL, UCD, and VKM variants. StrainInfo contains 22 exact target rows with 47 deposit designations for `Eremothecium coryli`; those side rows do not produce BacDive-derived local strain children for this taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/eremothecium_coryli.yaml` plus `just validate-strict data/taxa/eukaryota/eremothecium_coryli.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the nine current native GOLD organism rows. The NCBI type-material table contributes evidence but does not create child strain records by itself.
