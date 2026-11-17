# YAML Record Review: Acetobacter thailandicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_thailandicus.yaml
- Reviewed UTC: 2026-09-26T12:03:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1502842 |
| Label | Acetobacter thailandicus |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:434, Acetobacter |
| PATHS row | data/taxa/PATHS.tsv:189340 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:15817 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_thailandicus.md` report |
| `just validate data/taxa/bacteria/acetobacter_thailandicus.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_syzygii.yaml data/taxa/bacteria/acetobacter_syzygii_nric_0483.yaml data/taxa/bacteria/acetobacter_thailandicus.yaml data/taxa/bacteria/acetobacter_tropicalis.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 121 lines, 9 lineage entries, 1 LPSN nomenclature row, 1 GTDB mapping, 3 NCBI synonyms, 2 xrefs, 1 BacDive strain, 0 genome assemblies, 0 genome records, 0 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, LPSN, GTDB, BacDive, GOLD, culture-collection, native GOLD, NCBI merged-ID, native StrainInfo side, and NCBI type-material rows found with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact same-taxon rows |

## Identity and Grounding

- `NCBITaxon:1502842`, label `Acetobacter thailandicus`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, three NCBI related synonyms, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:385929`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:15817`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/lpsn_names.tsv:30668` supports the single non-deprecated, legitimate, validly published, correct LPSN species name `lpsn:794091`, type-strain identifier `kgmicrobe.strain:NBRC-103583`, two publications, LPSN URL, and 16S accession `INSDC:AB937775`.
- `data/raw/gtdb_mappings.tsv:32670` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_thailandicus`; `genome_count: 8` matches the GTDB source attestation.
- `data/raw/bacdive_strains.tsv:91209` supports the one local strain `kgmicrobe.strain:bacdive_168976` / `bacdive:168976`, designation `AD25`, and culture IDs `kgmicrobe.strain:BCC-15839` and `kgmicrobe.strain:NBRC-103583`.
- `data/raw/gold_organisms.tsv:11779` records 6 direct GOLD organisms, matching the `GOLD` / `ORGANISM` source attestation.
- `data/raw/ncbi_merged_ids.tsv:18024` maps old ID `NCBITaxon:1502837` into this taxon; no retained retired old-ID row was present, so the record correctly has no generated `replaces` entry.

## Completeness

- The generated NCBI identity, LPSN nomenclature, GTDB close match, three NCBI synonyms, xrefs, BacDive type strain, GOLD attestation, and seed history are complete for the pinned local source rows.
- `strain_count: 1` is complete: the only exact BacDive row is present, its two culture IDs are represented, and no exact `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv` rows exist for `kgmicrobe.strain:bacdive_168976`.
- Native StrainInfo has one direct row and one exact deposit for `NCBITaxon:1502842`, but no generated StrainInfo assembly, exclusion, or related-record rows exist for this target, so no nested StrainInfo rows are missing.
- NCBI has 11 exact type-material rows for this species; they agree with represented aliases and do not imply additional local strains beyond BacDive 168976.
- No BactoTraits, Madin et al., MediaDive, generated definition, generated genome link, generated related-record, or curator-added causal graph is present for this species identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any LPSN, GTDB, BacDive, GOLD, or StrainInfo refresh.

## Additional Notes

- Native GOLD and native StrainInfo rows are exact side evidence; without BacDive-derived genome rows or final StrainInfo overlay rows, they do not imply additional generated child links.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
