# YAML Record Review: Acetobacter tropicalis NRIC 0312

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_tropicalis_nric_0312.yaml
- Reviewed UTC: 2026-09-26T12:09:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1307920 |
| Label | Acetobacter tropicalis NRIC 0312 |
| Rank / domain | STRAIN / BACTERIA |
| Parent | NCBITaxon:104102, Acetobacter tropicalis |
| PATHS row | data/taxa/PATHS.tsv:107665 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:22487 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_tropicalis_nric_0312.md` report |
| `just validate data/taxa/bacteria/acetobacter_tropicalis_nric_0312.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_tropicalis_nbrc_101654.yaml data/taxa/bacteria/acetobacter_tropicalis_nric_0312.yaml data/taxa/bacteria/acetobacter_vaccinii.yaml data/taxa/bacteria/acetobacter_zythi.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 1524 lines, 10 lineage entries, 1 GTDB mapping, 1 GTDB exact synonym, 1 xref, 1 BacDive strain, 29 genome assemblies, 18 genome records, 72 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, GTDB, BacDive, MediaDive, native GOLD, culture-collection, raw strain, and StrainInfo rows checked with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact same-taxon rows |

## Identity and Grounding

- `NCBITaxon:1307920`, label `Acetobacter tropicalis NRIC 0312`, rank `STRAIN`, parent `NCBITaxon:104102`, genetic code `11`, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:309522`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:22487`.
- The bounded NCBI scan resolved all 10 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/bacdive_strains.tsv:18` supports the one local strain `kgmicrobe.strain:bacdive_17` / `bacdive:17` and all 7 represented culture-collection IDs.
- `data/raw/gtdb_mappings.tsv:17798` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_tropicalis`; `genome_count: 11` matches the GTDB source attestation and the GTDB exact synonym.
- `data/raw/mediadive_taxa.tsv:2895` supports the 2 MediaDive media counted by the `MEDIADIVE` source attestation.
- The nested genome block for BacDive 17 is complete: `data/raw/strain_assemblies.tsv` has 26 rows, `data/straininfo/assemblies.tsv` has 3 rows, `data/raw/strain_genome_records.tsv` has 18 rows, `data/raw/strain_related_records.tsv` has 54 rows, and `data/straininfo/related_records.tsv.gz` has 18 rows for `kgmicrobe.strain:bacdive_17`.

## Completeness

- The generated NCBI identity, GTDB close match, GTDB synonym, xref, one BacDive strain, MediaDive attestation, genome links, and StrainInfo related records are complete for the pinned local source rows.
- `strain_count: 1` is complete: the only exact BacDive row is present, its 7 culture IDs are represented, and all rows matched through `kgmicrobe.strain:bacdive_17` are nested under that strain.
- Native GOLD has one exact organism, project, and analysis for this strain, but no compact `data/raw/gold_organisms.tsv` aggregate row was generated for this target and no YAML GOLD claim depends on that native side evidence.
- No LPSN nomenclature, NCBI synonym, BactoTraits row, Madin et al. row, NCBI merged-ID row, NCBI type-material row, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any NCBI, GTDB, BacDive, MediaDive, GOLD, or StrainInfo refresh.

## Additional Notes

- BacDive 17 is also gathered by the parent `Acetobacter tropicalis` species record; the generated rows are duplicated intentionally so the exact NCBI strain and the species both expose the same curated strain payload.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
