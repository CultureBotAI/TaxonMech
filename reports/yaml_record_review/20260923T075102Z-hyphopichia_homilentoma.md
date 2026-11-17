# YAML Record Review: Hyphopichia homilentoma

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyphopichia_homilentoma.yaml
- Started UTC: 2026-09-23T07:51:02Z
- Finished UTC: 2026-09-23T07:51:02Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45558` |
| Label | `Hyphopichia homilentoma` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:507510` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Genetic Code | `12` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hyphopichia_homilentoma.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/hyphopichia_burtonii.yaml data/taxa/eukaryota/hyphopichia_buzzinii.yaml data/taxa/eukaryota/hyphopichia_fennica.yaml data/taxa/eukaryota/hyphopichia_homilentoma.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hyphopichia_homilentoma.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45558`, `label: Hyphopichia homilentoma`, `rank: SPECIES`, `parent_taxon: NCBITaxon:507510`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5610`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyphopichia`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36065`, which records two retained direct organisms for `NCBITaxon:45558`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, two linked projects, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45558`. `Candida homilentoma` is present in `data/raw/ncbitaxon_taxa.tsv:5610` as an exact synonym, and both authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact `Go0138997` and `Go0705202` organisms for `JCM 1507` and `NRRL Y-10941`, linked `Gp0144054` and `Gp0831226` projects, and one native analysis linked by project ID `Gp0144054`.

NCBI carries 16 exact type-material rows for `Candida homilentoma` and `Hyphopichia homilentoma` at `data/raw/ncbi_type_material.tsv:215283` through `data/raw/ncbi_type_material.tsv:215298`, spanning ATCC 56462, BCRC/CCRC 22395, CBS 6312, IFO 10413, JCM 1507, NRRL Y-10941, and MUCL 29911 spelling variants.

The raw StrainInfo JSONL contains five exact direct source records and 17 exact deposit matches for `NCBITaxon:45558`, but the maintained StrainInfo overlay tables have no exact rows for this taxon. No exact side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `12`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyphopichia_homilentoma.yaml` plus `just validate-strict data/taxa/eukaryota/hyphopichia_homilentoma.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyphopichia_homilentoma` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
