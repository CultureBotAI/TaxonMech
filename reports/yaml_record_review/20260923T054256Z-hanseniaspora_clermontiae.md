# YAML Record Review: Hanseniaspora clermontiae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_clermontiae.yaml
- Started UTC: 2026-09-23T05:42:56Z
- Finished UTC: 2026-09-23T05:42:56Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:211099` |
| Label | `Hanseniaspora clermontiae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:29832` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_clermontiae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hamiltosporidium_tvaerminnensis.yaml data/taxa/eukaryota/hanseniaspora_clermontiae.yaml data/taxa/eukaryota/hanseniaspora_gamundiae.yaml data/taxa/eukaryota/hanseniaspora_guilliermondii.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, five exact current native GOLD organisms with six linked native GOLD projects and two linked native analyses, nine exact NCBI type-material rows, one side NCBI merged-ID row with no retained old ID, two direct exact StrainInfo rows with seven deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:211099`, `label: Hanseniaspora clermontiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:29832`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:41621`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hanseniaspora`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:20173`, which records five retained direct organisms for `NCBITaxon:211099`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs also contain exact organisms for `yHDO704`, `yHDO705`, `yHDO706`, `yHMicronic5000034693`, and `NRRL Y-27515`, with six linked projects and two native analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:211099`. `data/raw/ncbitaxon_taxa.tsv:41621` has no exact or broad synonyms for this species, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have five exact organism rows for `Hanseniaspora clermontiae`, four resequencing projects for the `yHDO` / `yHMicronic` organisms, two linked projects for `NRRL Y-27515`, and two native analyses linked to those `NRRL Y-27515` projects.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:84676` through `data/raw/ncbi_type_material.tsv:84684` as nine spellings for `CBS 8821`, `NBRC 100528`, `NRRL Y-27515`, and `UWO-PS 87-2370.1`. The NCBI merged side inventory maps `NCBITaxon:504903` into `NCBITaxon:211099`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected in the generated YAML.

StrainInfo also has two direct exact rows with seven deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record. No exact BacDive row or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, both NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_clermontiae.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_clermontiae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_clermontiae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
