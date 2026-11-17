# YAML Record Review: Cyanidioschyzon merolae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyanidioschyzon_merolae.yaml
- Started UTC: 2026-09-22T20:59:06Z
- Finished UTC: 2026-09-22T20:59:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45157` |
| Label | `Cyanidioschyzon merolae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:45156` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyanidioschyzon_merolae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cutaneotrichosporon_sp_pl3408a.yaml data/taxa/eukaryota/cyanidiococcus_yangmingshanensis.yaml data/taxa/eukaryota/cyanidioschyzon_merolae.yaml data/taxa/eukaryota/cyanidioschyzon_merolae_strain_10d.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five retained organisms, six exact native GOLD organism rows, nine exact native GOLD project rows, three exact native GOLD analysis rows, four exact StrainInfo records not retained in the final StrainInfo overlay, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45157`, `label: Cyanidioschyzon merolae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:45156`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5500`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cyanidioschyzon` genus; the bounded scan checked all 8 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35874`, which records five retained organisms for `NCBITaxon:45157`; this agrees with `source_attestations[1].assertion_count: 5` and with the note that records filed directly under this taxon are gathered while descendant taxa are not.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45157`. The YAML carries NCBI's single related synonym, `Cyanidioschyzon merolae P.De Luca, R.Taddei & L.Varano, 1978`, and NCBI supplies no exact or broad synonyms for this row.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has six exact organism IDs for this NCBI taxon, with nine direct projects: the unstrained `Cyanidioschyzon merolae` row, strains `5508`, `10D-T`, `GT`, `Soos_CM`, and the `NEIS 3377` organism whose four projects are expression-profiling rows. Three exact native analysis rows are linked to the `10D-T`, `GT`, and `Soos_CM` projects.

The four exact StrainInfo records are keyed directly to `NCBITaxon:45157` and contain non-type deposits `NIES-1804`, `NIES-1805`, `NIES-1806`, and `NIES-1332`; they have not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyanidioschyzon_merolae.yaml` plus `just validate-strict data/taxa/eukaryota/cyanidioschyzon_merolae.yaml`.

## Additional Notes

The retained aggregate GOLD source in `data/raw/gold_organisms.tsv` currently counts five organisms, while an exact native pass over `data/gold/organisms.jsonl.gz` finds six native organism rows keyed to `NCBITaxon:45157`. This record is faithful to the retained aggregate that owns generation, so the native-only extra row was treated as follow-up context rather than a generated-record defect.

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:45157`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
