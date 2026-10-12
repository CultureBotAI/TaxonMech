# YAML Record Review: Cryptococcus floricola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_floricola.yaml
- Started UTC: 2026-09-22T16:42:43Z
- Finished UTC: 2026-09-22T16:42:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2591691` |
| Label | `Cryptococcus floricola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5206` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_floricola.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml data/taxa/eukaryota/cryptococcus_deuterogattii_ram5.yaml data/taxa/eukaryota/cryptococcus_floricola.yaml data/taxa/eukaryota/cryptococcus_gattii.yaml` | Passed; the strict batch reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, one exact native GOLD project row, one exact native GOLD analysis row, six NCBI type-material rows, one exact StrainInfo row, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2591691`, `label: Cryptococcus floricola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5206`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:534801`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptococcus` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:23751`, which records one retained organism for `NCBITaxon:2591691`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2591691`. NCBI supplies related synonyms `Cryptococcus floricola Yurkov, A.R. Passer, M.A. Coelho, R.B. Billmyre, M. Nowrousian, M. Mittelbach, C.A. Cuomo, A.F. Averette, S. Sun and J. Heitman, 2019` and `Cryptococcus sp. DSM 27421`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0632147`, exact project `Gp0645968`, and one native analysis row for `Cryptococcus floricola DSM 27421` tied to that project.

NCBI type-material rows record CBS 15421, YCC 8315, and DSM 27421 as holotype-associated labels, and the exact StrainInfo match for `siID` 406903 carries DOI `10.60712/SI-ID406903.3`; however, no BacDive-derived local strain row exists for this taxon, so no StrainInfo overlay is expected in the final strain tables and `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_floricola.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_floricola.yaml`.

## Additional Notes

The bounded scan found one side-inventory row in `data/raw/ncbi_merged_ids.tsv:42383` that maps old ID `NCBITaxon:2479495` into active ID `NCBITaxon:2591691`; it found no retained retired rows that would generate `replaces` entries.
