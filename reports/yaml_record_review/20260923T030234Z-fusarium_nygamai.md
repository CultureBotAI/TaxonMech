# YAML Record Review: Fusarium nygamai

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_nygamai.yaml
- Started UTC: 2026-09-23T03:02:34Z
- Finished UTC: 2026-09-23T03:02:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:42673` |
| Label | `Fusarium nygamai` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_nygamai.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_nurragi.yaml data/taxa/eukaryota/fusarium_nygamai.yaml data/taxa/eukaryota/fusarium_odoratissimum.yaml data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four organism assertions, four current native GOLD organism rows with five linked projects and two native analysis rows, no NCBI merged-ID side rows, 23 exact direct StrainInfo entries, 32 exact StrainInfo deposit references, 14 NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:42673`, `label: Fusarium nygamai`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5022`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35207`, which records four retained direct organisms for `NCBITaxon:42673`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit. The current native GOLD catalogs still contain four exact organisms, five linked projects, and two project-linked analyses for `Fusarium nygamai`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:42673`. The YAML preserves the exact synonym `Gibberella nygamai` and two related author-qualified NCBI synonyms: `Fusarium nygamai L.W. Burgess & Trimboli, 1986` and `Gibberella nygamai Klaasen & P.E. Nelson, 1997`.

The retained GOLD aggregate supplies four organism assertions. The current native GOLD catalogs still contain exact organism rows for `FRC M-7492`, `MRC8546`, `NRRL 66327`, and `CS10214`; they also contain five linked project rows and two analysis rows linked to those projects.

No side-inventory NCBI old IDs merge into `NCBITaxon:42673`, so the YAML correctly has no generated `replaces` entry. StrainInfo contains 23 exact direct rows and 32 exact deposit references for the target. NCBI has 14 culture-from-holotype aliases for the target in `typematerial.dmp`: `ATCC 58555`, `ATCC:58555`, `BBA 69862`, `BBA:69862`, `CBS 749.97`, `CBS:749.97`, `DAOM 225148`, `DAOM:225148`, `FRC M-1375`, `FRC:M:1375`, `IMI 375354`, `IMI:375354`, `NRRL 13448`, and `NRRL:13448`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_nygamai.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_nygamai.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_nygamai` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
