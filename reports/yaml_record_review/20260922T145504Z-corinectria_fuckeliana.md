# YAML Record Review: Corinectria fuckeliana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/corinectria_fuckeliana.yaml
- Started UTC: 2026-09-22T14:55:18Z
- Finished UTC: 2026-09-22T14:55:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:930093` |
| Label | `Corinectria fuckeliana` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2060652` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/corinectria_fuckeliana.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/corinectria_fuckeliana.yaml` | Passed; the strict validator exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organism/project/analysis chains, no NCBI type-material rows, one NCBI merged-ID side row, 27 exact StrainInfo side deposits, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:930093`, `label: Corinectria fuckeliana`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2060652`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:195925`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Corinectria` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44633`, which records two retained organisms for `NCBITaxon:930093`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:930093`. NCBI supplies all three exact synonyms and all three related synonyms present in the YAML.

The native GOLD snapshot has two exact organism rows for this NCBI taxon, `Go0517403` / `Corinectria fuckeliana IMI 342667` and `Go0678570` / `Corinectria fuckeliana CBS 125109`. Those organisms link to projects `Gp0441456` and `Gp0780530`, and each project has one analysis row; this supports the retained aggregate organism count.

The exact StrainInfo side inventory has 27 deposits and 25 direct DOI records for the same NCBI taxon. They do not currently join into the maintained final strain tables, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated NCBI synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:930093`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/corinectria_fuckeliana.yaml` plus `just validate-strict data/taxa/eukaryota/corinectria_fuckeliana.yaml`.

## Additional Notes

The bounded scan found one side row in `data/raw/ncbi_merged_ids.tsv` mapping old ID `NCBITaxon:78401` into `NCBITaxon:930093`, but there are no side-inventory old IDs and no retained retired rows that would generate a `replaces` entry.
