# YAML Record Review: Histoplasma capsulatum var. duboisii H88

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/histoplasma_capsulatum_var_duboisii_h88.yaml
- Started UTC: 2026-09-23T07:00:51Z
- Finished UTC: 2026-09-23T07:00:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:544711` |
| Label | `Histoplasma capsulatum var. duboisii H88` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:149546` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/histoplasma_capsulatum_var_duboisii_h88.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/histoplasma_capsulatum_var_duboisii_h88.yaml data/taxa/eukaryota/histoplasma_mississippiense.yaml data/taxa/eukaryota/histoplasma_ohiense.yaml data/taxa/eukaryota/hohenbuehelia_mastrucata.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with one linked native GOLD project and one linked native GOLD analysis, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:544711`, `label: Histoplasma capsulatum var. duboisii H88`, `rank: STRAIN`, `parent_taxon: NCBITaxon:149546`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:126505`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Histoplasma capsulatum var. duboisii`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38388`, which records two retained direct organisms for `NCBITaxon:544711`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, one linked project, and one linked analysis as side evidence.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:544711`. `Ajellomyces capsulatus H88` is present in `data/raw/ncbitaxon_taxa.tsv:126505` as an exact synonym, and the source row has no related synonyms to omit.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have an exact `Go0002629` organism for `H88`, a linked `Gp0002629` project in `data/gold/projects.jsonl.gz:2393`, and one native analysis linked by the exact project ID.

No NCBI type-material row, side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local child strain entries under this strain-rank NCBI target.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/histoplasma_capsulatum_var_duboisii_h88.yaml` plus `just validate-strict data/taxa/eukaryota/histoplasma_capsulatum_var_duboisii_h88.yaml`.

## Additional Notes

No prior exact ignored review report existed for `histoplasma_capsulatum_var_duboisii_h88` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
