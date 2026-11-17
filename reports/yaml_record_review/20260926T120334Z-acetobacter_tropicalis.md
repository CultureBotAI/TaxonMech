# YAML Record Review: Acetobacter tropicalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_tropicalis.yaml
- Reviewed UTC: 2026-09-26T12:03:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:104102 |
| Label | Acetobacter tropicalis |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:434, Acetobacter |
| PATHS row | data/taxa/PATHS.tsv:16140 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:9424 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_tropicalis.md` report |
| `just validate data/taxa/bacteria/acetobacter_tropicalis.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_syzygii.yaml data/taxa/bacteria/acetobacter_syzygii_nric_0483.yaml data/taxa/bacteria/acetobacter_thailandicus.yaml data/taxa/bacteria/acetobacter_tropicalis.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 1577 lines, 9 lineage entries, 1 LPSN nomenclature row, 2 GTDB mappings, 1 NCBI synonym, 2 xrefs, 2 BacDive strains, 29 genome assemblies, 18 genome records, 72 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, LPSN, GTDB, BacDive, GOLD, Madin et al., native GOLD, StrainInfo, raw strain, and NCBI type-material rows found with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact rows for this species and its gathered `NCBITaxon:1307920` descendant strain |

## Identity and Grounding

- `NCBITaxon:104102`, label `Acetobacter tropicalis`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, related NCBI synonym, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:18605`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:9424`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/lpsn_names.tsv:14820` supports the single non-deprecated, legitimate, validly published, correct LPSN species name `lpsn:772521`, five type-strain culture identifiers, three publications, LPSN URL, and 16S accession `INSDC:AB032354`.
- `data/raw/gtdb_mappings.tsv:1571` supports the primary `skos:broadMatch` to `GTDB:s__Acetobacter_tropicalis`; `genome_count: 11` matches the GTDB source attestation. `data/raw/gtdb_mappings.tsv:1570` supports the pooled `GTDB:s__Acetobacter_senegalensis` broad match.
- The first BacDive strain is `kgmicrobe.strain:bacdive_17` / `bacdive:17`, filed under descendant `NCBITaxon:1307920`; the second is exact species-keyed `kgmicrobe.strain:bacdive_163303`, supported by `data/raw/bacdive_strains.tsv:85539`.
- The nested genome block for BacDive 17 is complete: `data/raw/strain_assemblies.tsv` has 26 rows, `data/straininfo/assemblies.tsv` has 3 rows, `data/raw/strain_genome_records.tsv` has 18 rows, `data/raw/strain_related_records.tsv` has 54 rows, and `data/straininfo/related_records.tsv.gz` has 18 rows for `kgmicrobe.strain:bacdive_17`.
- `data/raw/gold_organisms.tsv:576` records 35 direct GOLD organisms and `data/raw/madin_taxa.tsv:779` records 1 direct Madin et al. trait assertion, matching the aggregate source attestations.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB broad matches, NCBI synonym, xrefs, two BacDive strains, GOLD and Madin aggregate attestations, genome links, and StrainInfo related records are complete for the pinned local source rows.
- The `BACDIVE` source attestation correctly notes that one strain is filed under descendant NCBI taxon `NCBITaxon:1307920`.
- `bacdive_17` contributes the 29 genome assemblies, 18 genome records, and 72 related records after final StrainInfo overlay rows are included; `bacdive_163303` contributes two culture IDs and two MediaDive media but no genome rows.
- The GTDB xref is limited to `GTDB:s__Acetobacter_tropicalis`; the pooled `GTDB:s__Acetobacter_senegalensis` broad match is retained only in `taxonomy_mappings`, as intended.
- Native StrainInfo has 9 direct rows and 21 deposit hits for `NCBITaxon:104102`, but only the rows joined to BacDive 17's culture identifiers materialize in the final StrainInfo overlays.
- NCBI has 13 exact type-material rows for this species; they agree with the represented type-strain aliases and do not imply additional local strains beyond the generated BacDive rows.
- No BactoTraits, NCBI merged-ID, generated definition, or curator-added causal graph row is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any LPSN, GTDB, BacDive, GOLD, StrainInfo, or Madin refresh.

## Additional Notes

- `Acetobacter tropicalis` gathers BacDive 17 from the descendant `NCBITaxon:1307920` strain and BacDive 163303 from the species itself.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
