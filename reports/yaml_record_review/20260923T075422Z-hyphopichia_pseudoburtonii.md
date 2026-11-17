# YAML Record Review: Hyphopichia pseudoburtonii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml
- Started UTC: 2026-09-23T07:54:22Z
- Finished UTC: 2026-09-23T07:54:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:717741` |
| Label | `Hyphopichia pseudoburtonii` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:507510` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Genetic Code | `12` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/hyphopichia_khmerensis.yaml data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml data/taxa/eukaryota/hyphopichia_wangnamkhiaoensis.yaml data/taxa/eukaryota/hypocreales_sp.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:717741`, `label: Hyphopichia pseudoburtonii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:507510`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:169168`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyphopichia`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41927`, which records two retained direct organisms for `NCBITaxon:717741`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, two linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:717741`. Both authorship-bearing `Hyphopichia pseudoburtonii` names in the YAML are present in `data/raw/ncbitaxon_taxa.tsv:169168` as related synonyms, and NCBI has no exact synonyms for this taxon.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0519694` and `Go0705140` organisms for strains `makgeolli` and `CBS 2455`, linked `Gp0443845` and `Gp0831163` projects, and one native analysis linked by project ID `Gp0443845`.

NCBI carries four exact type-material rows for `Hyphopichia pseudoburtonii` at `data/raw/ncbi_type_material.tsv:260221` through `data/raw/ncbi_type_material.tsv:260224`, spanning `CBS 2455` and `JCM 16346` spelling variants.

The raw StrainInfo JSONL contains one exact direct source record and one exact deposit match for `NCBITaxon:717741`, `siID: 22267` / `IHEM 28402`, but the maintained StrainInfo overlay tables have no exact rows for this taxon. No exact side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml` plus `just validate-strict data/taxa/eukaryota/hyphopichia_pseudoburtonii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyphopichia_pseudoburtonii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
