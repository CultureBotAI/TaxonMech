# YAML Record Review: Hypholoma australianum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hypholoma_australianum.yaml
- Started UTC: 2026-09-23T07:47:24Z
- Finished UTC: 2026-09-23T07:47:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2493788` |
| Label | `Hypholoma australianum` |
| Rank | `SPECIES` |
| Parent Taxon | `NCBITaxon:71944` |
| Taxon Domain | `EUKARYOTA` |
| Grounding Status | `EXACT` |
| Mapping Status | `SEEDED` |
| Strain Count | `0` |

## Validation

- `just validate data/taxa/eukaryota/hypholoma_australianum.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/hyphochytrium_catenoides.yaml data/taxa/eukaryota/hyphodiscus_hymeniophilus.yaml data/taxa/eukaryota/hypholoma_australianum.yaml data/taxa/eukaryota/hypholoma_sublateritium_fd_334_ss_4.yaml` scanned the four-record batch and reported zero ERROR rows.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/hypholoma_australianum.yaml` completed and emitted the bounded source scan used below.

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2493788`, `label: Hypholoma australianum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:71944`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:527135`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hypholoma`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22517`, which records one retained direct organism for `NCBITaxon:2493788`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs have no exact organism, project, or analysis rows for this taxon.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2493788`. `Hypholoma australe` is present in `data/raw/ncbitaxon_taxa.tsv:527135` as an exact synonym, and both authorship-bearing names in the YAML are present as related synonyms.

The retained GOLD aggregate supplies one organism assertion, although the current native GOLD catalogs do not have exact `ORGANISM NCBI TAX ID: 2493788` rows or linked projects/analyses in the local snapshot.

The raw StrainInfo JSONL contains one exact direct source record and one exact deposit match for `NCBITaxon:2493788`, `siID: 266936` / `ICMP 21474`, but the maintained StrainInfo overlay tables have no exact rows for this taxon.

The side merged-ID inventory maps old `NCBITaxon:1051812` to current `NCBITaxon:2493788`, but no retained retired NCBI row has `retired_into: NCBITaxon:2493788`, so no generated `replaces` entry is expected.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hypholoma_australianum.yaml` plus `just validate-strict data/taxa/eukaryota/hypholoma_australianum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hypholoma_australianum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`, which can differ from the current native GOLD organism, project, and analysis rows. Native GOLD evidence creates generated child strains only after joining to BacDive-derived local strain inventory entries.

StrainInfo only overlays BacDive-derived local strains in the generated final tables, so exact raw StrainInfo JSONL rows without exact final `data/straininfo` output rows are not generated as child strain records here.
