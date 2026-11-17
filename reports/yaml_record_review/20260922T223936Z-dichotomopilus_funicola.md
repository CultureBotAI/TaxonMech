# YAML Record Review: Dichotomopilus funicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dichotomopilus_funicola.yaml
- Started UTC: 2026-09-22T22:39:36Z
- Finished UTC: 2026-09-22T22:39:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1934379` |
| Label | `Dichotomopilus funicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1934375` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dichotomopilus_funicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dichotomocladium_sphaerosporum.yaml data/taxa/eukaryota/dichotomopilus_funicola.yaml data/taxa/eukaryota/dicranophora_fulva.yaml data/taxa/eukaryota/dicrateria_rotunda.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to one project and no analyses, two exact NCBI type-material rows, 60 exact StrainInfo direct records carrying 77 matching deposit designations, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1934379`, `label: Dichotomopilus funicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1934375`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:496610`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dichotomopilus` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17757`, which records one retained direct organism for `NCBITaxon:1934379`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1934379`. The YAML carries the single exact synonym and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0382594` for `Chaetomium funicola CBS 141.50`; one project, `Gp0223624`, under that organism; and no exact analysis rows linked through that project ID.

The NCBI type-material inventory contributes two exact rows, covering both spelling variants of the `CBS 159.52` culture from epitype under the `Chaetomium funicola` synonym.

The exact StrainInfo side inventory has 60 direct records and 77 matching deposit designations for `NCBITaxon:1934379`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dichotomopilus_funicola.yaml` plus `just validate-strict data/taxa/eukaryota/dichotomopilus_funicola.yaml`.

## Additional Notes

The bounded scan found a side-inventory `data/raw/ncbi_merged_ids.tsv` mapping from `NCBITaxon:79816` into `NCBITaxon:1934379`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
