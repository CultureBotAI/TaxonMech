# YAML Record Review: Domibacillus enclensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/domibacillus_enclensis.yaml
- Started UTC: 2026-10-02T10:30:25Z
- Finished UTC: 2026-10-02T10:30:25Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017273` |
| Label | `Domibacillus enclensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1433999` |
| Parent label | `Domibacillus` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/domibacillus_enclensis.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/fictibacillus_enclensis.yaml data/taxa/bacteria/bacillus_sp_nioc10.yaml data/taxa/bacteria/bacillus_sp_nioc11.yaml data/taxa/bacteria/domibacillus_enclensis.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 637 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB taxonomy mapping, 2 synonyms, 2 xrefs, 1 BacDive strain, and 6 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, AllTheBacteria, seed, and exact strain-linked rows; confirmed all 9 lineage rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*-domibacillus_enclensis.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017273)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `legacy_page_paths.tsv`, `seed_scope.tsv`, raw-source TSVs, ATB link TSVs, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10308 maps `NCBITaxon:1017273` to `domibacillus_enclensis`.
- `curation/legacy_page_paths.tsv` row 603 preserves the historical page path.
- `curation/seed_scope.tsv` row 10779 keeps this species in scope with an attested NCBI+LPSN+GTDB+BacDive+GOLD+MADIN rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218642 names `NCBITaxon:1017273` as `Domibacillus enclensis`, places it under `NCBITaxon:1433999`, and advertises NCBI, GTDB, BacDive, LPSN, GOLD, and MADIN source coverage.
- `data/raw/lpsn_names.tsv` row 28904 supplies the legitimate, validly published, correct LPSN name, its DSM 25145 type-strain designation, three publication accessions, `INSDC:JF893466`, and the linked GTDB species.
- `data/raw/gtdb_mappings.tsv` row 1181 maps the taxon to `GTDB:s__Domibacillus_enclensis` with `skos:closeMatch` and 3 genomes.
- `data/raw/gtdb_species.tsv` row 56320 preserves that GTDB species under `GTDB:g__Domibacillus`.
- `data/raw/madin_taxa.tsv` row 477 contributes the 4 MADIN trait assertions preserved in `source_attestations`.

## Evidence

- The YAML identifier, species rank, parent genus, and genetic code agree with the exact NCBI Taxonomy row.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:1433999` / `Domibacillus`.
- The LPSN nomenclature block preserves `lpsn:792122`, its authority, ICNP status flags, type strain, publications, sequence accession, and LPSN xref.
- The GTDB mapping preserves the raw close-match predicate and 3-genome count, including the note that LPSN links this GTDB species to the taxon's name.
- NCBI's authority-bearing `Domibacillus enclensis Sonalkar et al. 2014` and strain-like `Domibacillus sp. NIO-1016` names are retained as related synonyms.
- The single BacDive strain `kgmicrobe.strain:bacdive_130211` corresponds to `NIO-1016` and carries the canonical CCTCC AB 2011121, DSM 25145, and NCIM 5462 culture-collection identifiers.
- The nested strain evidence includes 13 assembly rows, 13 genome rows, and 23 related records from BacDive, BV-BRC, GTDB, NCBI Assembly, GOLD, and ATB cross-links.

## Completeness

- The record is complete for the exact NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, and ATB rows currently present for this taxon.
- `data/raw/ncbi_type_material.tsv` rows 1162-1170 are aliases of the same CCTCC AB 2011121 / DSM 25145 / NCIM 5462 / NIO-1016 type material captured through BacDive and LPSN rather than missing standalone strains.
- `data/raw/strain_assemblies.tsv` rows 13861-13873 match the 13 generated `genome_assemblies` entries.
- `data/raw/strain_genome_records.tsv` rows 10773-10784 plus `data/atb/genome_links.tsv` rows 1764-1765 match the 13 generated `genome_records` entries.
- `data/raw/strain_related_records.tsv` rows 41466-41488 plus `data/atb/strain_links.tsv` row 419 match the 23 generated `related_records` entries and the ATB sample link.
- `data/raw/gold_organisms.tsv` row 299 supports the GOLD source attestation count of 2 organisms.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/domibacillus_enclensis.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/domibacillus_enclensis.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- The bounded report helper reported an NCBI source mismatch for this multi-source generated species, so this review relied on `taxonmech_yaml_summary.py` plus direct exact-ID raw-source scans instead.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10308 |
| `curation/legacy_page_paths.tsv` | 603 |
| `curation/seed_scope.tsv` | 10779 |
| `data/raw/ncbitaxon_taxa.tsv` | 218642 |
| `data/raw/lpsn_names.tsv` | 28904 |
| `data/raw/gtdb_mappings.tsv` | 1181 |
| `data/raw/gtdb_species.tsv` | 56320 |
| `data/raw/madin_taxa.tsv` | 477 |
| `data/raw/bacdive_strains.tsv` | 52527 |
| `data/raw/strain_assemblies.tsv` | 13861-13873 |
| `data/raw/strain_genome_records.tsv` | 10773-10784 |
| `data/raw/strain_related_records.tsv` | 41466-41488 |
| `data/atb/genome_links.tsv` | 1764-1765 |
| `data/atb/strain_links.tsv` | 419 |
| `data/raw/gold_organisms.tsv` | 299 |
| `data/taxa/bacteria/domibacillus_enclensis.yaml` | 1, 36, 56, 63, 70, 75, and 597 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/domibacillus_enclensis.yaml`.
- The generated record has no top-level `genomes`, `strains`, or `causal_graphs` blocks beyond its canonical nested BacDive strain.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/domibacillus_enclensis.yaml` directly.
