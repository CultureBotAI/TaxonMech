# YAML Record Review: Fibulobasidium inconspicuum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fibulobasidium_inconspicuum.yaml
- Started UTC: 2026-09-23T01:37:45Z
- Finished UTC: 2026-09-23T01:37:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:57688` |
| Label | `Fibulobasidium inconspicuum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:57687` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fibulobasidium_inconspicuum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fermentozyma_sake.yaml data/taxa/eukaryota/fibrocapsa_japonica.yaml data/taxa/eukaryota/fibroporia_radiculosa.yaml data/taxa/eukaryota/fibulobasidium_inconspicuum.yaml` | Passed; strict validation exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects, 13 direct StrainInfo rows, two NCBI type-material rows, no current exact native GOLD analyses, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:57688`, `label: Fibulobasidium inconspicuum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:57687`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7326`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fibulobasidium` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39301`, which records two retained direct organisms for `NCBITaxon:57688`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:57688`. The YAML preserves NCBI's related synonym `Fibulobasidium inconspicuum Bandoni, 1979`.

No NCBI merged-ID rows target `NCBITaxon:57688`, and no retained old IDs in `data/raw/ncbitaxon_taxa.tsv` retire into it, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions, and the current native GOLD catalogs still contain two exact organism rows and two linked project rows for the target NCBI taxon.

NCBI type-material rows 237907-237908 list two type-material designations for `Fibulobasidium inconspicuum`, and StrainInfo contains exact side evidence for the target in both the direct SI-ID view and the deposit view. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fibulobasidium_inconspicuum.yaml` plus `just validate-strict data/taxa/eukaryota/fibulobasidium_inconspicuum.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
