# YAML Record Review: Acetobacter vaccinii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_vaccinii.yaml
- Reviewed UTC: 2026-09-26T12:09:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:2592655 |
| Label | Acetobacter vaccinii |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:434, Acetobacter |
| PATHS row | data/taxa/PATHS.tsv:355578 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:18175 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_vaccinii.md` report |
| `just validate data/taxa/bacteria/acetobacter_vaccinii.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_tropicalis_nbrc_101654.yaml data/taxa/bacteria/acetobacter_tropicalis_nric_0312.yaml data/taxa/bacteria/acetobacter_vaccinii.yaml data/taxa/bacteria/acetobacter_zythi.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 531 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB mapping, 2 NCBI related synonyms, 2 xrefs, 1 BacDive strain, 9 genome assemblies, 7 genome records, 22 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, LPSN, GTDB, BacDive, GOLD, culture-collection, raw strain, native StrainInfo, final StrainInfo, native GOLD, and NCBI type-material rows checked with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact same-taxon rows |

## Identity and Grounding

- `NCBITaxon:2592655`, label `Acetobacter vaccinii`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, two NCBI related synonyms, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:534878`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:18175`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/lpsn_names.tsv:5857` supports the single non-deprecated, legitimate, validly published, correct LPSN species name `lpsn:31769`, authority `Heo et al. 2022`, type-strain identifier `kgmicrobe.strain:LMG-31758`, three publications, LPSN URL, and 16S accession `INSDC:MN121517`.
- `data/raw/gtdb_mappings.tsv:201186` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_vaccinii`; `genome_count: 1` matches the GTDB source attestation.
- `data/raw/bacdive_strains.tsv:92918` supports the one local strain `kgmicrobe.strain:bacdive_170685` / `bacdive:170685`, designation `C17-3`, and culture IDs `kgmicrobe.strain:KACC-21233` and `kgmicrobe.strain:LMG-31758`.
- The nested genome block for BacDive 170685 is complete: `data/raw/strain_assemblies.tsv` has 9 rows, `data/raw/strain_genome_records.tsv` has 7 rows, `data/raw/strain_related_records.tsv` has 20 rows, and `data/straininfo/related_records.tsv.gz` has 2 rows for `kgmicrobe.strain:bacdive_170685`.
- Native StrainInfo row `data/straininfo/strain_links.tsv:72799` supports the matched `straininfo.strain:366576` and `straininfo.deposit:22670` related records with DOI `10.60712/SI-ID366576.1`.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB close match, two NCBI synonyms, xrefs, one BacDive type strain, GOLD attestation, genome links, and StrainInfo related records are complete for the pinned local source rows.
- `strain_count: 1` is complete: the only exact BacDive row is present, its 2 culture IDs are represented, and all rows matched through `kgmicrobe.strain:bacdive_170685` are nested under that strain.
- Native GOLD has exactly one organism, one project, and one analysis for `KACC 21233`; the compact `data/raw/gold_organisms.tsv:23768` aggregate records the same one organism.
- Native StrainInfo has one direct row and one deposit hit for `NCBITaxon:2592655`; the final overlay contributes exactly two related records and no strain assemblies, so no nested StrainInfo assembly row is missing.
- NCBI has 12 exact type-material rows for this species; they agree with the represented BacDive culture identifiers and do not imply additional local strains beyond BacDive 170685.
- No BactoTraits, Madin et al., MediaDive, NCBI merged-ID, generated definition, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any NCBI, LPSN, GTDB, BacDive, GOLD, or StrainInfo refresh.

## Additional Notes

- The StrainInfo deposit and strain records join through the LMG 31758 culture identifier, while the genome rows join through KACC 21233.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
