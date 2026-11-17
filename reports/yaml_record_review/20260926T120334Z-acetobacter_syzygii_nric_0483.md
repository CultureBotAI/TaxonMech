# YAML Record Review: Acetobacter syzygii NRIC 0483

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_syzygii_nric_0483.yaml
- Reviewed UTC: 2026-09-26T12:03:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1307919 |
| Label | Acetobacter syzygii NRIC 0483 |
| Rank / domain | STRAIN / BACTERIA |
| Parent | NCBITaxon:146476, Acetobacter syzygii |
| PATHS row | data/taxa/PATHS.tsv:107663 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:22486 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_syzygii_nric_0483.md` report |
| `just validate data/taxa/bacteria/acetobacter_syzygii_nric_0483.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_syzygii.yaml data/taxa/bacteria/acetobacter_syzygii_nric_0483.yaml data/taxa/bacteria/acetobacter_thailandicus.yaml data/taxa/bacteria/acetobacter_tropicalis.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 833 lines, 10 lineage entries, 1 GTDB mapping, 2 exact synonyms, 1 xref, 1 BacDive strain, 12 genome assemblies, 8 genome records, 39 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, GTDB, BacDive, MediaDive, native GOLD, raw strain, and NCBI merged-ID rows found with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact strain rows plus shared BacDive 14 rows |

## Identity and Grounding

- `NCBITaxon:1307919`, label `Acetobacter syzygii NRIC 0483`, rank `STRAIN`, parent `NCBITaxon:146476`, genetic code `11`, exact synonym `Acetobacter syzygii 9H-2`, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:309521`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:22486`.
- The bounded NCBI scan resolved all 10 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/gtdb_mappings.tsv:17797` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_syzygii`; `genome_count: 16` matches the GTDB source attestation and GTDB exact synonym.
- `data/raw/bacdive_strains.tsv:15` supports the one local strain `kgmicrobe.strain:bacdive_14` / `bacdive:14`, designation `9H-2`, six culture IDs, and source taxon `NCBITaxon:1307919`.
- `data/raw/mediadive_taxa.tsv:2894` supports the `MEDIADIVE` attestation of two media for this exact strain taxon.
- `data/raw/ncbi_merged_ids.tsv:8776` maps old ID `NCBITaxon:1231343` into this strain; no retained retired old-ID row was present, so the record correctly has no generated `replaces` entry.
- The nested genome block is complete for BacDive 14. The canonical strain has 11 raw assemblies, 8 raw genome records, 27 raw related records, 1 StrainInfo assembly row, and 12 StrainInfo related rows, including rows whose asserted `taxon_id` is the parent species.

## Completeness

- NCBI supplies the strain identity, exact synonym, merged old ID, exact 10-ancestor lineage, and the `Acetobacter syzygii` parent.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a 16-genome source attestation.
- BacDive supplies the single local strain and six normalized culture-collection identifiers.
- MediaDive supplies the only same-taxon aggregate source attestation beyond NCBI, GTDB, and BacDive.
- The native GOLD table has one exact `NRIC 0483` organism, project, and analysis, but no same-taxon processed `data/raw/gold_organisms.tsv` row; no aggregate GOLD source attestation is missing.
- No exact LPSN name, Madin et al., BactoTraits, NCBI type-material, StrainInfo native direct row, generated definition, or curator-added causal graph is present for the strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any GTDB, BacDive, MediaDive, GOLD, or StrainInfo refresh.

## Additional Notes

- This strain record and its parent species record share the same generated BacDive 14 strain block, including genome links keyed by the parent species when that is how a source asserted the genome.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
