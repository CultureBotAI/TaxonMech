# YAML Record Review: Hanseniaspora pseudoguilliermondii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_pseudoguilliermondii.yaml
- Started UTC: 2026-09-23T05:54:59Z
- Finished UTC: 2026-09-23T05:54:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:332229` |
| Label | `Hanseniaspora pseudoguilliermondii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_pseudoguilliermondii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_pseudoguilliermondii.yaml data/taxa/eukaryota/hanseniaspora_singularis_nom_inval.yaml data/taxa/eukaryota/hanseniaspora_taiwanica_nom_inval.yaml data/taxa/eukaryota/hanseniaspora_thailandica_nom_inval.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with six organism assertions, six exact current native GOLD organisms with six linked native GOLD projects and one linked native analysis, four exact NCBI type-material rows, no side NCBI merged-ID rows, two direct exact StrainInfo rows with three deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:332229`, `label: Hanseniaspora pseudoguilliermondii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:68042`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32348`, which records six retained direct organisms for `NCBITaxon:332229`; this agrees with `source_attestations[1].assertion_count: 6` and its organism assertion unit. The current native GOLD catalogs also contain six exact organisms, six linked projects, and one native analysis linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:332229`. The generated related synonym `Hanseniaspora pseudoguilliermondii Cadez, Raspor & M.T. Sm., 2006` is present in `data/raw/ncbitaxon_taxa.tsv:68042`.

The retained GOLD aggregate supplies six organism assertions. The current native GOLD catalogs have exact organisms for `yHDO725`, `yHDO726`, `yHDO727`, `yHMicronic5000035695`, `ZIM213 Neza Cadez`, and `CBS 8772`; all six organisms have linked projects, and the `Gp0441073` project has a native analysis row.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:179131` through `data/raw/ncbi_type_material.tsv:179134` as four spellings for `CBS 8772` and `NRRL Y-63756`. StrainInfo also has two direct exact rows with three deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_pseudoguilliermondii.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_pseudoguilliermondii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_pseudoguilliermondii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
