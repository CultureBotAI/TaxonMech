# YAML Record Review: Hypomyces rosellus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypomyces_rosellus.yaml
- Started UTC: 2026-09-23T08:07:35Z
- Finished UTC: 2026-09-23T08:07:35Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5132` |
| Label | `Hypomyces rosellus` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:5130` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypomyces_rosellus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/hypomyces_pseudocorticiicola.yaml data/taxa/eukaryota/hypomyces_rosellus.yaml data/taxa/eukaryota/hypomyces_semicircularis.yaml data/taxa/eukaryota/hypomyces_semitranslucens.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypomyces_rosellus.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5132`, `label: Hypomyces rosellus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5130`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2252`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hypomyces`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37560`, which records two retained direct organisms for `NCBITaxon:5132`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs have no exact organism, project, or analysis rows for this taxon.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5132`. `Cladobotryum dendroides`, `Dactylium dendroides`, and `Sphaeria rosella` are present in `data/raw/ncbitaxon_taxa.tsv:2252` as exact synonyms, and both authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies two organism assertions, although the current native GOLD catalogs do not have exact `ORGANISM NCBI TAX ID: 5132` rows or linked projects/analyses in the local snapshot.

The raw StrainInfo JSONL contains 49 exact direct source records and 61 exact deposit matches for `NCBITaxon:5132`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:5561` to current `NCBITaxon:5132`, but no retained retired NCBI row has `retired_into: NCBITaxon:5132`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypomyces_rosellus.yaml` plus `just validate-strict data/taxa/eukaryota/hypomyces_rosellus.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypomyces_rosellus` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`, which can differ from the current native GOLD organism, project, and analysis rows. Native GOLD evidence creates generated child strains only after joining to BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
