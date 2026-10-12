# YAML Record Review: Cystofilobasidium infirmominiatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cystofilobasidium_infirmominiatum.yaml
- Started UTC: 2026-09-22T21:34:59Z
- Finished UTC: 2026-09-22T21:34:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:89913` |
| Label | `Cystofilobasidium infirmominiatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5410` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cystofilobasidium_infirmominiatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cystofilobasidium_infirmominiatum.yaml data/taxa/eukaryota/cystofilobasidium_intermedium.yaml data/taxa/eukaryota/cystofilobasidium_macerans.yaml data/taxa/eukaryota/cystoisospora_suis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, 27 exact NCBI type-material rows, 27 exact StrainInfo records with 75 deposit designations not retained in the final StrainInfo overlay, no exact native GOLD rows keyed to `NCBITaxon:89913`, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:89913`, `label: Cystofilobasidium infirmominiatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5410`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:14427`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cystofilobasidium` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44072`, which records one retained organism for `NCBITaxon:89913`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:89913`. The YAML carries all four exact synonyms and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. An exact native GOLD scan found no organism, project, or analysis rows currently keyed to `NCBITaxon:89913`.

The NCBI type-material inventory contributes 27 exact rows under the synonym taxon name `Rhodosporidium infirmominiatum`, with `CBS 323` variants as `culture from type material` plus designation variants of `ATCC 16182`, `BCRC 22467`, `CCRC 22467`, `DBVPG 6006`, `DBVPG 6672`, `IFO 1057`, `IGC 3955`, `JCM 3788`, `MUCL 30407`, `NCYC 2667`, `NRRL Y-1586`, and `VKM Y-1265` as `type material`.

Twenty-seven exact StrainInfo records are keyed directly to `NCBITaxon:89913`, covering 75 deposit designations, but they have not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cystofilobasidium_infirmominiatum.yaml` plus `just validate-strict data/taxa/eukaryota/cystofilobasidium_infirmominiatum.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:89913`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
