# YAML Record Review: Fibrocapsa japonica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fibrocapsa_japonica.yaml
- Started UTC: 2026-09-23T01:37:45Z
- Finished UTC: 2026-09-23T01:37:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:94617` |
| Label | `Fibrocapsa japonica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:94616` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fibrocapsa_japonica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fermentozyma_sake.yaml data/taxa/eukaryota/fibrocapsa_japonica.yaml data/taxa/eukaryota/fibroporia_radiculosa.yaml data/taxa/eukaryota/fibulobasidium_inconspicuum.yaml` | Passed; strict validation exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row, nine direct StrainInfo rows, one NCBI merged-ID side row, no current exact native GOLD project/analysis rows, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:94617`, `label: Fibrocapsa japonica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:94616`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:15664`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fibrocapsa` genus; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45018`, which records one retained direct organism for `NCBITaxon:94617`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:94617`. The YAML preserves NCBI's exact synonym `Chattonella japonica` plus one related synonym.

`data/raw/ncbi_merged_ids.tsv:96289` maps the old side-inventory ID `NCBITaxon:82998` to `NCBITaxon:94617`; it is not retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion, and the current native GOLD catalogs still contain one exact organism row for the target NCBI taxon.

StrainInfo contains exact side evidence for the target in both the direct SI-ID view and the deposit view, but those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fibrocapsa_japonica.yaml` plus `just validate-strict data/taxa/eukaryota/fibrocapsa_japonica.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact row is side evidence only and does not create generated child strains without a BacDive-derived local strain inventory entry. The NCBI merged-ID side row is side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
