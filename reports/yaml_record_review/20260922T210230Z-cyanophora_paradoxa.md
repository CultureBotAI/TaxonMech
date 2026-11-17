# YAML Record Review: Cyanophora paradoxa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cyanophora_paradoxa.yaml
- Started UTC: 2026-09-22T21:02:30Z
- Finished UTC: 2026-09-22T21:02:30Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2762` |
| Label | `Cyanophora paradoxa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2761` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cyanophora_paradoxa.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cyanodermella_asteris.yaml data/taxa/eukaryota/cyanophora_paradoxa.yaml data/taxa/eukaryota/cyanoptyche_gloeocystis.yaml data/taxa/eukaryota/cyathus_pallidus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with twenty-two retained organisms, twenty-three exact native GOLD organism rows, twenty-nine exact native GOLD project rows, eight exact NCBI type-material rows, twelve exact StrainInfo records not retained in the final StrainInfo overlay, no exact native GOLD analysis rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2762`, `label: Cyanophora paradoxa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2761`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:1937`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cyanophora` genus; the bounded scan checked all 7 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:26054`, which records twenty-two retained organisms for `NCBITaxon:2762`; this agrees with `source_attestations[1].assertion_count: 22`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2762`. The YAML carries NCBI's single related synonym, `Cyanophora paradoxa Korshikov, 1924`, and NCBI supplies no exact or broad synonyms for this row.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has twenty-three exact organism rows: two early rows for unstrained `Cyanophora paradoxa` and `CCMP359`, plus twenty-one `CCMP359 Cp_*` or `CCMP359 Cp_ML` isolate rows. Exact native project rows include two early projects for `Go0002370`, twenty-one `CCMP359` resequencing projects, and six `CCMP359` expression-profiling projects; no exact native analysis rows are linked.

The NCBI type-material inventory contributes eight exact rows: four `culture from epitype` spelling variants for `CCAP 981/1` and four `epitype` spelling variants for `TNS AL-57397`. Exact StrainInfo records are keyed to this NCBI taxon, but none are retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cyanophora_paradoxa.yaml` plus `just validate-strict data/taxa/eukaryota/cyanophora_paradoxa.yaml`.

## Additional Notes

The retained aggregate GOLD source in `data/raw/gold_organisms.tsv` currently counts twenty-two organisms, while an exact native pass over `data/gold/organisms.jsonl.gz` finds twenty-three native organism rows keyed to `NCBITaxon:2762`. This record is faithful to the retained aggregate that owns generation, so the native-only extra row was treated as follow-up context rather than a generated-record defect.

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:2762`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
