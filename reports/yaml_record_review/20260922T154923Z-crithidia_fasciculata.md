# YAML Record Review: Crithidia fasciculata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/crithidia_fasciculata.yaml
- Started UTC: 2026-09-22T15:49:23Z
- Finished UTC: 2026-09-22T15:49:23Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5656` |
| Label | `Crithidia fasciculata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5655` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/crithidia_fasciculata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/crithidia_bombi.yaml data/taxa/eukaryota/crithidia_expoeki.yaml data/taxa/eukaryota/crithidia_fasciculata.yaml data/taxa/eukaryota/crithidia_mellificae.yaml` | Passed; the strict validator exited successfully for the four-file batch, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, two exact native GOLD project rows, one exact native GOLD analysis row, no NCBI type-material rows, four exact StrainInfo records covering four deposits, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5656`, `label: Crithidia fasciculata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5655`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2517`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Crithidia` genus; the bounded scan checked all 11 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38984`, which records one retained organism for `NCBITaxon:5656`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5656`. NCBI supplies the related synonym `Crithidia fasciculata Leger, 1902`, matching the YAML synonym.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0008981`, exact projects `Gp0008981` and `Gp0038357`, and one native analysis row tied to `Gp0038357`.

StrainInfo has exact direct records for the taxon, but no BacDive-backed strain row joins them into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; `strain_count: 0` is therefore consistent with the maintained generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/crithidia_fasciculata.yaml` plus `just validate-strict data/taxa/eukaryota/crithidia_fasciculata.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:5656`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
