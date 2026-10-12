# YAML Record Review: Heterosigma akashiwo

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/heterosigma_akashiwo.yaml
- Started UTC: 2026-09-23T06:53:00Z
- Finished UTC: 2026-09-23T06:53:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2829` |
| Label | `Heterosigma akashiwo` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2828` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/heterosigma_akashiwo.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/heterocapsa_rotundata.yaml data/taxa/eukaryota/heterodoassansia_hygrophilae.yaml data/taxa/eukaryota/heterogastridium_pycnidioideum_atcc_mya_4631.yaml data/taxa/eukaryota/heterosigma_akashiwo.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with four organism assertions, four exact current native GOLD organisms with no linked native GOLD projects or analyses, no exact NCBI type-material rows, one side NCBI merged-ID row, 25 direct exact StrainInfo rows with 25 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2829`, `label: Heterosigma akashiwo`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2828`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:1954`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Heterosigma`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:27360`, which records four retained direct organisms for `NCBITaxon:2829`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit. The current native GOLD catalogs also contain four exact organisms.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2829`. `Entomosigma akashiwo`, `Heterosigma carterae`, and `Heterosigma inlandica` are present in `data/raw/ncbitaxon_taxa.tsv:1954` as exact synonyms, and `Entomosigma akashiwo Y.Hada, 1967`, `Heterosigma akashiwo (Hada) Hada ex Y.Hara & Chihara, 1987`, and `Heterosigma carterae strain=CCMP 452` are present in the source row as related synonyms.

The retained GOLD aggregate supplies four organism assertions. The current native GOLD catalogs have exact organisms `Go0368702` for `CCMP 2393`, `Go0368703` for `CCMP 3107`, `Go0368704` for `CCMP 452`, and `Go0368705` for `NB`, with no linked native GOLD project or analysis rows.

NCBI merged-ID side data maps retired `NCBITaxon:28465` into `NCBITaxon:2829`, but no retained retired source row exists for that old ID in `data/raw/ncbitaxon_taxa.tsv`, so the absence of a generated `replaces` value is consistent with the generator inputs.

StrainInfo has 25 direct exact rows with 25 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/heterosigma_akashiwo.yaml` plus `just validate-strict data/taxa/eukaryota/heterosigma_akashiwo.yaml`.

## Additional Notes

No prior exact ignored review report existed for `heterosigma_akashiwo` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism rows are exact by NCBI taxon ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
