# YAML Record Review: Acetobacter tropicalis NBRC 101654

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_tropicalis_nbrc_101654.yaml
- Reviewed UTC: 2026-09-26T12:09:33Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:749388 |
| Label | Acetobacter tropicalis NBRC 101654 |
| Rank / domain | STRAIN / BACTERIA |
| Parent | NCBITaxon:104102, Acetobacter tropicalis |
| PATHS row | data/taxa/PATHS.tsv:584717 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:34202 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacter_tropicalis_nbrc_101654.md` report |
| `just validate data/taxa/bacteria/acetobacter_tropicalis_nbrc_101654.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacter_tropicalis_nbrc_101654.yaml data/taxa/bacteria/acetobacter_tropicalis_nric_0312.yaml data/taxa/bacteria/acetobacter_vaccinii.yaml data/taxa/bacteria/acetobacter_zythi.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 87 lines, 10 lineage entries, 1 GTDB mapping, 4 exact synonyms, 1 xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, GTDB, Madin et al., and native GOLD rows checked with no lineage mismatches and no BacDive, StrainInfo, LPSN, BactoTraits, MediaDive, NCBI merged-ID, or NCBI type-material rows for this strain |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, ATB, StrainInfo, and history paths and found the expected exact rows for this target |

## Identity and Grounding

- `NCBITaxon:749388`, label `Acetobacter tropicalis NBRC 101654`, rank `STRAIN`, parent `NCBITaxon:104102`, genetic code `11`, three NCBI exact synonyms, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:173208`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:34202`.
- The bounded NCBI scan resolved all 10 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/gtdb_mappings.tsv:305888` supports the `skos:closeMatch` to `GTDB:s__Acetobacter_senegalensis`; `genome_count: 17` matches the GTDB source attestation.
- `data/raw/madin_taxa.tsv:30156` supports the 6 Madin et al. trait assertions recorded by the `MADIN` source attestation.
- `data/raw/ncbitaxon_taxa.tsv:173208` supports the NCBI exact synonyms `Acetobacter tropicalis SKU1100`, `Acetobacter tropicalis str. NBRC 101654`, and `Acetobacter tropicalis strain NBRC 101654`; the GTDB synonym `Acetobacter senegalensis` is scoped to the GTDB close match.
- Bounded raw scans found no exact BacDive, compact culture-collection, final strain-assembly, final strain-genome, final related-record, StrainInfo, LPSN, BactoTraits, MediaDive, NCBI merged-ID, or NCBI type-material row for `NCBITaxon:749388`, matching the empty optional blocks in the YAML.

## Completeness

- The generated NCBI identity, GTDB close match, four exact synonyms, single xref, and NCBI, GTDB, and Madin et al. source attestations are complete for the pinned local source rows.
- `strain_count: 0` is complete for the generated corpus because there is no exact `data/raw/bacdive_strains.tsv` row, no compact culture-collection strain row, no final StrainInfo overlay, and no final strain genome row for this taxon.
- Native GOLD has one exact organism, project, and analysis for this strain, but no compact `data/raw/gold_organisms.tsv` aggregate row was generated for this target and no YAML GOLD claim depends on that native side evidence.
- No LPSN nomenclature, BacDive strain block, MediaDive medium, BactoTraits row, NCBI merged-ID row, NCBI type-material row, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any NCBI, GTDB, Madin et al., BacDive, StrainInfo, GOLD, or MediaDive refresh.

## Additional Notes

- `GTDB:s__Acetobacter_senegalensis` is also a broad match for the parent Acetobacter species, but the local GTDB mapping has an exact close-match row for the NBRC 101654 NCBI strain itself.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
