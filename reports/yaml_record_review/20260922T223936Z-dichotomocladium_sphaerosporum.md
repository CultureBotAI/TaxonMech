# YAML Record Review: Dichotomocladium sphaerosporum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dichotomocladium_sphaerosporum.yaml
- Started UTC: 2026-09-22T22:39:36Z
- Finished UTC: 2026-09-22T22:39:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1265307` |
| Label | `Dichotomocladium sphaerosporum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:64643` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dichotomocladium_sphaerosporum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dichotomocladium_sphaerosporum.yaml data/taxa/eukaryota/dichotomopilus_funicola.yaml data/taxa/eukaryota/dicranophora_fulva.yaml data/taxa/eukaryota/dicrateria_rotunda.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to one project and no analyses, no exact NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1265307`, `label: Dichotomocladium sphaerosporum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:64643`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:293272`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dichotomocladium` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:6227`, which records one retained direct organism for `NCBITaxon:1265307`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1265307`. The YAML carries the single related synonym filed for this row; NCBI supplies no exact or broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0470762` for `Dichotomocladium sphaerosporum NRRL 22118`; one project, `Gp0345250`, under that organism; and no exact analysis rows linked through that project ID.

No NCBI type-material, StrainInfo, BacDive, or maintained final strain-table rows are present for the exact target, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dichotomocladium_sphaerosporum.yaml` plus `just validate-strict data/taxa/eukaryota/dichotomocladium_sphaerosporum.yaml`.

## Additional Notes

The bounded scan found no side-inventory `data/raw/ncbi_merged_ids.tsv` mappings into `NCBITaxon:1265307`.
