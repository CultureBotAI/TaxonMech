# YAML Record Review: Hyaloperonospora arabidopsidis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyaloperonospora_arabidopsidis.yaml
- Started UTC: 2026-09-23T07:20:12Z
- Finished UTC: 2026-09-23T07:20:12Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:272952` |
| Label | `Hyaloperonospora arabidopsidis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:184462` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hyaloperonospora_arabidopsidis.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hyaloperonospora_arabidopsidis.yaml data/taxa/eukaryota/hyaloperonospora_arabidopsidis_emoy2.yaml data/taxa/eukaryota/hyaloperonospora_parasitica.yaml data/taxa/eukaryota/hyalopycnis_blepharistoma.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with three organism assertions, three exact current native GOLD organisms with three linked native GOLD projects and two linked native GOLD analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:272952`, `label: Hyaloperonospora arabidopsidis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:184462`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:56280`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyaloperonospora`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:25404`, which records three retained direct organisms for `NCBITaxon:272952`; this agrees with `source_attestations[1].assertion_count: 3`, its organism assertion unit, and its descendant-exclusion note. The current native GOLD catalogs also contain three exact organisms, three linked projects, and two linked analyses under this direct NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:272952`. `Hyaloperonospora arabidopsis` and `Peronospora arabidopsidis` are present in `data/raw/ncbitaxon_taxa.tsv:56280` as exact synonyms, and the two authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies three organism assertions. The current native GOLD catalogs have exact `Go0091982`, `Go0138506`, and `Go0139594` organisms for Waco9, Cala2, and Noks1, linked `Gp0091982`, `Gp0143552`, and `Gp0144676` projects, and two native analyses linked by the Cala2 and Noks1 project IDs.

The scan found no exact NCBI type-material rows, side NCBI merged-ID rows, exact StrainInfo rows, exact BacDive rows, or maintained final strain-table rows. `strain_count: 0` is therefore consistent with no generated local strain entries in the output even though NCBI also has child strain-rank taxa such as `Hyaloperonospora arabidopsidis Emoy2` represented separately.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, the direct-records-only GOLD note, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyaloperonospora_arabidopsidis.yaml` plus `just validate-strict data/taxa/eukaryota/hyaloperonospora_arabidopsidis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyaloperonospora_arabidopsidis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
