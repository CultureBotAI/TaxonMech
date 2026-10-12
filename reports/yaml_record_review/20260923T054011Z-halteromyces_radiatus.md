# YAML Record Review: Halteromyces radiatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/halteromyces_radiatus.yaml
- Started UTC: 2026-09-23T05:40:11Z
- Finished UTC: 2026-09-23T05:40:11Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101107` |
| Label | `Halteromyces radiatus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101106` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/halteromyces_radiatus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/halteria_grandinella.yaml data/taxa/eukaryota/halteromyces_radiatus.yaml data/taxa/eukaryota/hamamotoa_singularis.yaml data/taxa/eukaryota/hamiltosporidium_magnivora.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and one linked native analysis, six exact NCBI type-material rows, no side NCBI merged-ID rows, one direct exact StrainInfo row with five deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:101107`, `label: Halteromyces radiatus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101106`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17426`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Halteromyces`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:248`, which records one retained direct organism for `NCBITaxon:101107`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0302459` for strain `CBS 162.75`, linked projects `Gp0156930` and `Gp0251490`, and one native analysis linked by `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:101107`. `data/raw/ncbitaxon_taxa.tsv:17426` has no exact or broad synonyms for this species, and the generated related synonym `Halteromyces radiatus Shipton & Schipper, 1975` is present in the source row as a related synonym.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Halteromyces radiatus CBS 162.75`, two linked projects, and one native analysis linked to project `Gp0156930`.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:869` through `data/raw/ncbi_type_material.tsv:874` as `ATCC 36777`, `ATCC:36777`, `CBS 162.75`, `CBS:162.75`, `IMI 169827`, and `IMI:169827`, all marked type material for `Halteromyces radiatus`. StrainInfo also has one direct exact row, `siID 155306`, with five deposits for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the one NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/halteromyces_radiatus.yaml` plus `just validate-strict data/taxa/eukaryota/halteromyces_radiatus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `halteromyces_radiatus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
