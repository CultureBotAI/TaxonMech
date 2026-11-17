# YAML Record Review: Gymnopus androsaceus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gymnopus_androsaceus.yaml
- Started UTC: 2026-09-23T05:30:44Z
- Finished UTC: 2026-09-23T05:30:44Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1447940` |
| Label | `Gymnopus androsaceus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:93827` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gymnopus_androsaceus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gymnopilus_junonius.yaml data/taxa/eukaryota/gymnopus_androsaceus.yaml data/taxa/eukaryota/gymnopus_dryophilus_jgi_sc001dcmidf.yaml data/taxa/eukaryota/gymnopus_earleae.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and one linked native analysis, no exact NCBI type-material rows, two side NCBI merged-ID rows with no retained old IDs, 20 direct exact StrainInfo rows with 20 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1447940`, `label: Gymnopus androsaceus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:93827`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:364879`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gymnopus`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:10884`, which records one retained direct organism for `NCBITaxon:1447940`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0046757` for strain `JB14`, linked projects `Gp0046757` and `Gp0046758`, and one native analysis linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1447940`. `Agaricus androsaceus`, `Agaricus pineti`, `Androsaceus androsaceus`, `Chamaeceras androsaceus`, `Marasmius androsaceus`, `Merulius androsaceus`, and `Setulipes androsaceus` are present in `data/raw/ncbitaxon_taxa.tsv:364879` as exact synonyms, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Gymnopus androsaceus JB14`, two linked projects, and one native analysis linked to project `Gp0046757`.

The NCBI merged side inventory maps `NCBITaxon:181677` and `NCBITaxon:330520` into `NCBITaxon:1447940`, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected in the generated YAML. StrainInfo also has 20 direct exact rows with 20 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gymnopus_androsaceus.yaml` plus `just validate-strict data/taxa/eukaryota/gymnopus_androsaceus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gymnopus_androsaceus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
