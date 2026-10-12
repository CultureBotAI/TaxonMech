# YAML Record Review: Acetobacter syzygii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_syzygii.yaml
- Reviewed UTC: 2026-09-26T12:03:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:146476 |
| Label | Acetobacter syzygii |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:434, Acetobacter |
| PATHS row | data/taxa/PATHS.tsv:174746 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:21070 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_syzygii.md` report |
| `just validate data/taxa/bacteria/acetobacter_syzygii.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_syzygii.yaml data/taxa/bacteria/acetobacter_syzygii_nric_0483.yaml data/taxa/bacteria/acetobacter_thailandicus.yaml data/taxa/bacteria/acetobacter_tropicalis.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 868 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB mapping, 1 NCBI synonym, 2 xrefs, 1 BacDive strain, 12 genome assemblies, 8 genome records, 39 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, LPSN, GTDB, GOLD, Madin et al., native GOLD, BacDive, StrainInfo, final strain, and NCBI type-material rows found with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact rows for this species and its gathered `NCBITaxon:1307919` descendant strain |

## Identity and Grounding

- `NCBITaxon:146476`, label `Acetobacter syzygii`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:29733`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:21070`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/lpsn_names.tsv:14819` supports the single non-deprecated, legitimate, validly published, correct LPSN species name `lpsn:772520`, its five type-strain culture identifiers, three publications, LPSN URL, and 16S accession `INSDC:AB681084`.
- `data/raw/gtdb_mappings.tsv:31584` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_syzygii`; `genome_count: 16` matches the GTDB source attestation.
- `data/raw/bacdive_strains.tsv:15` supports the gathered `kgmicrobe.strain:bacdive_14` / `bacdive:14` strain filed under descendant `NCBITaxon:1307919`, with designation `9H-2`, six culture IDs, and source LPSN ID `lpsn:772520`.
- The nested genome block is complete for the canonical BacDive 14 strain: `data/raw/strain_assemblies.tsv` has 11 rows, `data/straininfo/assemblies.tsv` has 1 row, `data/raw/strain_genome_records.tsv` has 8 rows, `data/raw/strain_related_records.tsv` has 27 rows, and `data/straininfo/related_records.tsv.gz` has 12 rows for `kgmicrobe.strain:bacdive_14`.
- `data/raw/gold_organisms.tsv:11248` records 8 direct GOLD organisms and `data/raw/madin_taxa.tsv:16826` records 2 direct Madin et al. trait assertions, matching the aggregate source attestations.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB close match, NCBI synonym, xrefs, BacDive type strain, GOLD and Madin aggregate attestations, genome links, and StrainInfo related records are complete for the pinned local source rows.
- The `BACDIVE` source attestation correctly notes that its one strain is filed under descendant NCBI taxon `NCBITaxon:1307919`.
- Native StrainInfo has 4 direct rows and 9 deposit hits for `NCBITaxon:146476`, but only the records joined to BacDive 14's culture identifiers materialize in the final StrainInfo overlays.
- NCBI has 17 exact type-material rows for this species; they agree with the represented type-strain aliases and do not imply additional local strains beyond BacDive 14.
- No BactoTraits, MediaDive, NCBI merged-ID, generated definition, or curator-added causal graph row is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any LPSN, GTDB, BacDive, GOLD, StrainInfo, or Madin refresh.

## Additional Notes

- `Acetobacter syzygii` and `Acetobacter syzygii NRIC 0483` share the same generated BacDive 14 strain block; the species record marks it `classified_as: NCBITaxon:1307919`.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
