# YAML Record Review: Endocarpon pusillum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/endocarpon_pusillum.yaml
- Started UTC: 2026-09-23T00:03:18Z
- Finished UTC: 2026-09-23T00:03:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:364733` |
| Label | `Endocarpon pusillum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:364710` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/endocarpon_pusillum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/endocarpon_pusillum.yaml data/taxa/eukaryota/endochytriaceae_sp_jel_072.yaml data/taxa/eukaryota/endoconidiophora_laricicola.yaml data/taxa/eukaryota/endoconidiophora_polonica.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two exact native GOLD organism/project/analysis chains, no NCBI type-material or merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:364733`, `label: Endocarpon pusillum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:364710`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:76224`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Endocarpon` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33393`, which records two retained direct organisms for `NCBITaxon:364733`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:364733`. The YAML carries the only related synonym filed for this NCBI row, `Endocarpon pusillum Hedwig, 1789`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The native GOLD catalogs contain two exact organism rows, `Go0090027` for `Endocarpon pusillum KoLRI No. LF000583` and `Go0631645` for `Endocarpon pusillum EPUS1.4`, each with a matching project and project-linked analysis row.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/endocarpon_pusillum.yaml` plus `just validate-strict data/taxa/eukaryota/endocarpon_pusillum.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the two current native GOLD organism rows.
