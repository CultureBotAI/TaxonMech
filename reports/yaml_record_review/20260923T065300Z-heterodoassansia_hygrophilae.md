# YAML Record Review: Heterodoassansia hygrophilae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/heterodoassansia_hygrophilae.yaml
- Started UTC: 2026-09-23T06:53:00Z
- Finished UTC: 2026-09-23T06:53:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2031139` |
| Label | `Heterodoassansia hygrophilae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2031137` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/heterodoassansia_hygrophilae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/heterocapsa_rotundata.yaml data/taxa/eukaryota/heterodoassansia_hygrophilae.yaml data/taxa/eukaryota/heterogastridium_pycnidioideum_atcc_mya_4631.yaml data/taxa/eukaryota/heterosigma_akashiwo.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and one linked native GOLD analysis, ten exact NCBI type-material rows, two side NCBI merged-ID rows, one direct exact StrainInfo row with four deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2031139`, `label: Heterodoassansia hygrophilae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2031137`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:512328`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Heterodoassansia`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:19164`, which records one retained direct organism for `NCBITaxon:2031139`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, two linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2031139`. `Doassansia hygrophilae Thirum., 1946` is present in `data/raw/ncbitaxon_taxa.tsv:512328` as an exact synonym, and `Heterodoassansia hygrophilae (Thirum.) Vanky, 2006` is present in the source row as a related synonym.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0411612` organism for `CBS 346.65`, linked projects `Gp0306062` and `Gp0306499`, and one native analysis linked by `Gp0306062`.

NCBI carries ten exact type-material aliases for `Doassansia hygrophilae` at `data/raw/ncbi_type_material.tsv:79611` through `data/raw/ncbi_type_material.tsv:79620`, spanning ATCC, CBS, HACC, and IMI spellings. These aliases are source evidence for the species name, but they do not create generated local strains because no exact BacDive, StrainInfo assembly, or maintained final strain rows are linked to `NCBITaxon:2031139`.

NCBI merged-ID side data maps retired `NCBITaxon:2082645` and `NCBITaxon:62639` into `NCBITaxon:2031139`, but no retained retired source rows exist for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so the absence of generated `replaces` values is consistent with the generator inputs.

StrainInfo has one direct exact row for this taxon, with `CBS 346.65`, `ATCC 16202`, `ATCC 16575`, and `IMI 113699` as deposits. That side-inventory row is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/heterodoassansia_hygrophilae.yaml` plus `just validate-strict data/taxa/eukaryota/heterodoassansia_hygrophilae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `heterodoassansia_hygrophilae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
