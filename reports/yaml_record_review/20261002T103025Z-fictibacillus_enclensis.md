# YAML Record Review: Fictibacillus enclensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/fictibacillus_enclensis.yaml
- Started UTC: 2026-10-02T10:30:25Z
- Finished UTC: 2026-10-02T10:30:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017270` |
| Label | `Fictibacillus enclensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1329200` |
| Parent label | `Fictibacillus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/fictibacillus_enclensis.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/fictibacillus_enclensis.yaml data/taxa/bacteria/bacillus_sp_nioc10.yaml data/taxa/bacteria/bacillus_sp_nioc11.yaml data/taxa/bacteria/domibacillus_enclensis.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 396 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB taxonomy mapping, 3 synonyms, 2 xrefs, 1 BacDive strain, and 5 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected NCBI, LPSN, GTDB, BacDive, GOLD, AllTheBacteria, seed, and exact strain-linked rows; confirmed all 9 lineage rows; and found no MADIN row for `NCBITaxon:1017270`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*-fictibacillus_enclensis.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017270)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `legacy_page_paths.tsv`, `seed_scope.tsv`, raw-source TSVs, ATB link TSVs, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10305 maps `NCBITaxon:1017270` to `fictibacillus_enclensis`.
- `curation/legacy_page_paths.tsv` row 602 preserves the historical page path.
- `curation/seed_scope.tsv` row 14822 keeps this species in scope with an attested NCBI+LPSN+GTDB+BacDive+GOLD rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218639 names `NCBITaxon:1017270` as `Fictibacillus enclensis`, places it under `NCBITaxon:1329200`, and advertises NCBI, GTDB, BacDive, LPSN, and GOLD source coverage.
- `data/raw/lpsn_names.tsv` row 28581 supplies the legitimate, validly published, correct LPSN name, its DSM 25142 type-strain designation, three publication accessions, and `INSDC:JF893461`.
- `data/raw/gtdb_mappings.tsv` row 1180 maps the taxon to `GTDB:s__Fictibacillus_C_enclensis` with `skos:closeMatch` and 6 genomes.
- `data/raw/gtdb_species.tsv` row 62644 preserves that GTDB species under `GTDB:g__Fictibacillus_C`.

## Evidence

- The YAML identifier, species rank, parent genus, and genetic code agree with the exact NCBI Taxonomy row.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:1329200` / `Fictibacillus`.
- The LPSN nomenclature block preserves `lpsn:791783`, its authority, ICNP status flags, type strain, publications, sequence accession, and LPSN xref.
- The GTDB mapping preserves the raw close-match predicate and 6-genome count, and it adds `Fictibacillus C enclensis` as an exact synonym.
- NCBI's authority-bearing `Fictibacillus enclensis Dastager et al. 2014` and strain-like `Fictibacillus sp. NIO-1003` names are retained as related synonyms.
- The single BacDive strain `kgmicrobe.strain:bacdive_23767` corresponds to `NIO-1003` and carries the canonical DSM 25142 and NCIM 5458 culture-collection identifiers.
- The nested strain evidence includes 5 assembly rows, 8 genome rows, and 11 related records from BacDive, BV-BRC, GOLD, and ATB cross-links.

## Completeness

- The record is complete for the exact NCBI, LPSN, GTDB, BacDive, GOLD, and ATB rows currently present for this taxon.
- `data/raw/ncbi_type_material.tsv` rows 1156-1161 are aliases of the same DSM 25142 / NCIM 5458 / NIO-1003 type material captured through BacDive and LPSN rather than missing standalone strains.
- `data/raw/strain_assemblies.tsv` rows 110923-110927 match the 5 generated `genome_assemblies` entries.
- `data/raw/strain_genome_records.tsv` rows 89159-89165 plus `data/atb/genome_links.tsv` rows 15739-15740 match the 8 generated `genome_records` entries.
- `data/raw/strain_related_records.tsv` rows 320816-320826 plus `data/atb/strain_links.tsv` row 3618 match the 11 generated `related_records` entries and the ATB sample link.
- `data/raw/gold_organisms.tsv` row 298 supports the GOLD source attestation count of 1 organism.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/fictibacillus_enclensis.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/fictibacillus_enclensis.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- The bounded report helper reported an NCBI source mismatch for this multi-source generated species, so this review relied on `taxonmech_yaml_summary.py` plus direct exact-ID raw-source scans instead.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10305 |
| `curation/legacy_page_paths.tsv` | 602 |
| `curation/seed_scope.tsv` | 14822 |
| `data/raw/ncbitaxon_taxa.tsv` | 218639 |
| `data/raw/lpsn_names.tsv` | 28581 |
| `data/raw/gtdb_mappings.tsv` | 1180 |
| `data/raw/gtdb_species.tsv` | 62644 |
| `data/raw/bacdive_strains.tsv` | 23465 |
| `data/raw/strain_assemblies.tsv` | 110923-110927 |
| `data/raw/strain_genome_records.tsv` | 89159-89165 |
| `data/raw/strain_related_records.tsv` | 320816-320826 |
| `data/atb/genome_links.tsv` | 15739-15740 |
| `data/atb/strain_links.tsv` | 3618 |
| `data/raw/gold_organisms.tsv` | 298 |
| `data/taxa/bacteria/fictibacillus_enclensis.yaml` | 1, 36, 56, 62, 73, 78, and 361 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/fictibacillus_enclensis.yaml`.
- The generated record has no top-level `genomes`, `strains`, or `causal_graphs` blocks beyond its canonical nested BacDive strain.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/fictibacillus_enclensis.yaml` directly.
