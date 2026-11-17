# YAML Record Review: Echinodontium tinctorium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/echinodontium_tinctorium.yaml
- Started UTC: 2026-09-22T23:40:50Z
- Finished UTC: 2026-09-22T23:40:50Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:40440` |
| Label | `Echinodontium tinctorium` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:40439` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/echinodontium_tinctorium.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/durotheca_rogersii.yaml data/taxa/eukaryota/earliella_scabrosa.yaml data/taxa/eukaryota/ebollia_carnea.yaml data/taxa/eukaryota/echinodontium_tinctorium.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, one exact native GOLD organism, three native GOLD projects, one native GOLD analysis, nine exact StrainInfo direct records carrying ten matching deposit designations, no NCBI type-material, NCBI merged-ID, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:40440`, `label: Echinodontium tinctorium`, `rank: SPECIES`, `parent_taxon: NCBITaxon:40439`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4610`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Echinodontium` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34548`, which records two retained direct organisms for `NCBITaxon:40440`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:40440`. The YAML carries the one exact synonym and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms or old-ID side rows.

The native GOLD catalogs contain one current exact organism row, `Go0033208` for `Echinodontium tinctorium Aho-80`, three linked projects, and one analysis for the base `Gp0033141` project. The two additional project rows are transcriptomes for the same native organism.

The exact StrainInfo side inventory has nine direct records and ten matching deposit designations for `NCBITaxon:40440`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/echinodontium_tinctorium.yaml` plus `just validate-strict data/taxa/eukaryota/echinodontium_tinctorium.yaml`.

## Additional Notes

The retained GOLD aggregate count of two is larger than the one current exact row in the local native GOLD organism catalog. The generated YAML follows the retained aggregate input that seeded the record.
