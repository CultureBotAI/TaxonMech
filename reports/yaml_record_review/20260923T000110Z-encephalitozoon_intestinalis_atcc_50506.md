# YAML Record Review: Encephalitozoon intestinalis ATCC 50506

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/encephalitozoon_intestinalis_atcc_50506.yaml
- Started UTC: 2026-09-23T00:01:10Z
- Finished UTC: 2026-09-23T00:01:10Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:876142` |
| Label | `Encephalitozoon intestinalis ATCC 50506` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:58839` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/encephalitozoon_intestinalis_atcc_50506.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/encephalitozoon_cuniculi_gb_m1.yaml data/taxa/eukaryota/encephalitozoon_intestinalis_atcc_50506.yaml data/taxa/eukaryota/endocalyx_cinctus.yaml data/taxa/eukaryota/endocarpon_pallidulum.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis chain, no NCBI type-material or merged-ID rows, no exact StrainInfo or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:876142`, `label: Encephalitozoon intestinalis ATCC 50506`, `rank: STRAIN`, `parent_taxon: NCBITaxon:58839`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:185878`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the parent species, `Encephalitozoon intestinalis`; the bounded scan checked all 11 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:43693`, which records one retained direct organism for `NCBITaxon:876142`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:876142`. NCBI supplies no exact, broad, or related synonyms and no old-ID side rows for this target, matching the absent `synonyms` and `replaces` fields in the YAML.

The native GOLD catalogs contain one exact organism row, `Go0006942`, with one matching project, `Gp0006942`, and one matching analysis row linked through that project. The native GOLD name fields render the strain as `Encephalitozoon intestinalis ATCC 5050`, while the records remain keyed to exact NCBI Taxon ID `876142`.

No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/encephalitozoon_intestinalis_atcc_50506.yaml` plus `just validate-strict data/taxa/eukaryota/encephalitozoon_intestinalis_atcc_50506.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row.
