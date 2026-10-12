# YAML Record Review: Cystofilobasidium macerans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cystofilobasidium_macerans.yaml
- Started UTC: 2026-09-22T21:34:59Z
- Finished UTC: 2026-09-22T21:34:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:89926` |
| Label | `Cystofilobasidium macerans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5410` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cystofilobasidium_macerans.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cystofilobasidium_infirmominiatum.yaml data/taxa/eukaryota/cystofilobasidium_intermedium.yaml data/taxa/eukaryota/cystofilobasidium_macerans.yaml data/taxa/eukaryota/cystoisospora_suis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine retained organisms, nine exact native GOLD organism rows with no exact project or analysis rows, two exact NCBI type-material rows, 34 exact StrainInfo records with 65 deposit designations not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:89926`, `label: Cystofilobasidium macerans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5410`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:14429`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cystofilobasidium` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44074`, which records nine retained organisms for `NCBITaxon:89926`; this agrees with `source_attestations[1].assertion_count: 9`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:89926`. The YAML carries NCBI's exact synonym `Cryptococcus macerans` and the three related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. A full exact native GOLD organism scan found nine rows keyed to `NCBITaxon:89926`, under strains `ATCC 24194`, `CBS 2206`, `DSM 70822`, `IFO 1870`, `JCM 9048`, `MUCL 30616`, `NBRC 1870`, `No. 164`, and `NRRL Y-17373`, with no linked native GOLD project rows.

The NCBI type-material inventory contributes two exact `type material` rows for designation variants of `CBS 10757`.

Thirty-four exact StrainInfo records are keyed directly to `NCBITaxon:89926`, covering 65 deposit designations, but they have not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cystofilobasidium_macerans.yaml` plus `just validate-strict data/taxa/eukaryota/cystofilobasidium_macerans.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:138410` and `NCBITaxon:192669` into `NCBITaxon:89926`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
