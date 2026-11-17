# YAML Record Review: Cystobasidiopsis nirenbergiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cystobasidiopsis_nirenbergiae.yaml
- Started UTC: 2026-09-22T21:22:24Z
- Finished UTC: 2026-09-22T21:22:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:643910` |
| Label | `Cystobasidiopsis nirenbergiae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:643909` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cystobasidiopsis_nirenbergiae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cystinarius_sp.yaml data/taxa/eukaryota/cystobasidiopsis_lactophilus.yaml data/taxa/eukaryota/cystobasidiopsis_nirenbergiae.yaml data/taxa/eukaryota/cystobasidium_fimetarium.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, three exact native GOLD organism rows with no exact project or analysis rows, four exact NCBI type-material rows, one exact StrainInfo record not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:643910`, `label: Cystobasidiopsis nirenbergiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:643909`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:148587`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cystobasidiopsis` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40262`, which records three retained organisms for `NCBITaxon:643910`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:643910`. The YAML carries both related synonyms filed for this row, `Cystobasidiopsis nirenbergiae R. Bauer, B. Metzler, Begerow & Oberw., 2009` and `Cystobasidiopsis sp. RB-2009a`; NCBI supplies no exact or broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. Exact native GOLD organism rows are keyed to the strains `TU F-580`, `DSM 22580`, and `BBA 65452`; none currently join to exact native GOLD project or analysis rows.

The NCBI type-material inventory contributes four exact rows for the designation variants `BBA 65452`, `BBA:65452`, `TUB 019163`, and `TUB:019163`. The single direct StrainInfo record is keyed to `NCBITaxon:643910` for `DSM 22580`, but it has not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cystobasidiopsis_nirenbergiae.yaml` plus `just validate-strict data/taxa/eukaryota/cystobasidiopsis_nirenbergiae.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:643910`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
