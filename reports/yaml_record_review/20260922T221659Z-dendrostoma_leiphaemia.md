# YAML Record Review: Dendrostoma leiphaemia

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dendrostoma_leiphaemia.yaml
- Started UTC: 2026-09-22T22:16:59Z
- Finished UTC: 2026-09-22T22:16:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2608779` |
| Label | `Dendrostoma leiphaemia` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2170436` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dendrostoma_leiphaemia.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/delitschia_confertaspora.yaml data/taxa/eukaryota/delphinella_strobiligena.yaml data/taxa/eukaryota/dendrostoma_leiphaemia.yaml data/taxa/eukaryota/dendrothele_bispora.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to one project and one analysis, no exact NCBI type-material rows, four exact StrainInfo direct records carrying eight matching deposit designations, four joined StrainInfo overlay rows that were not retained into the final raw strain tables, no exact BacDive rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2608779`, `label: Dendrostoma leiphaemia`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2170436`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:536686`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dendrostoma` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:24067`, which records one retained direct organism for `NCBITaxon:2608779`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2608779`. The YAML carries all three exact synonyms and all three related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0676798` for `Dendrostoma leiphaemia CFCC 54038`; one project, `Gp0778603`, under that organism; and one analysis named `Dendrostoma leiphaemia CFCC 54038` that links back through `AP PROJECT GOLD IDS`.

The exact StrainInfo side inventory has four direct records and eight matching deposit designations for `NCBITaxon:2608779`. Four joined intermediate overlay rows in `data/straininfo/related_records.tsv.gz` map `IMET 9017` and `CBS 881.70` deposit and strain records to `kgmicrobe.strain:bacdive_16588`, but no exact rows are present in the maintained final strain tables and no `STRAININFO` source attestation is generated for this taxon. No exact NCBI type-material or BacDive rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dendrostoma_leiphaemia.yaml` plus `just validate-strict data/taxa/eukaryota/dendrostoma_leiphaemia.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:136413` and `NCBITaxon:2082087` into `NCBITaxon:2608779`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
