# YAML Record Review: Acetobacteraceae bacterium 3279O2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium_3279o2.yaml
- Reviewed UTC: 2026-09-26T12:14:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1459166 |
| Label | Acetobacteraceae bacterium 3279O2 |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:41293, unclassified Acetobacteraceae |
| PATHS row | data/taxa/PATHS.tsv:172892 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:441921 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacteraceae_bacterium_3279o2.md` report |
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium_3279o2.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium.yaml data/taxa/bacteria/acetobacteraceae_bacterium_184_22.yaml data/taxa/bacteria/acetobacteraceae_bacterium_3279o2.yaml data/taxa/bacteria/acetobacteraceae_bacterium_3292o2.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 51 lines, 9 lineage entries, 0 GTDB mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records |
| Bounded source scan | Pass; exact NCBI and seed-scope rows checked with no lineage mismatches and no BacDive, GOLD, StrainInfo, GTDB, LPSN, Madin et al., BactoTraits, MediaDive, NCBI merged-ID, or NCBI type-material rows |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, BacDive, StrainInfo, AllTheBacteria, and history paths and found only the expected exact NCBI and scope rows for this target |

## Identity and Grounding

- `NCBITaxon:1459166`, label `Acetobacteraceae bacterium 3279O2`, rank `SPECIES`, parent `NCBITaxon:41293`, genetic code `11`, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:370756`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:441921`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:370756` supports the generated label, species rank, parent, bacterial genetic code, lack of synonyms, `NCBITAXON`-only attestation, and `2026-09-13` taxonomy snapshot.
- `curation/seed_scope.tsv:441921` supports keeping this otherwise sparse NCBI-only species in the record corpus.
- The bounded and exact ignored-aware source scans found no exact LPSN, GTDB, BacDive, GOLD, Madin et al., BactoTraits, MediaDive, StrainInfo, AllTheBacteria, compact culture-collection, strain-assembly, strain-genome, or related-record rows for `NCBITaxon:1459166`.

## Completeness

- The generated NCBI identity and single `NCBITAXON` source attestation are complete for the pinned local source rows.
- `strain_count: 0` is complete because there is no exact compact BacDive strain row, no compact culture-collection strain row, no final strain genome row, and no final StrainInfo overlay for this taxon.
- No nomenclature, taxonomy mapping, xref, generated definition, or curator-added causal graph is present or implied by the inspected source inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any NCBI, BacDive, StrainInfo, GTDB, LPSN, or GOLD refresh.

## Additional Notes

- This is a deliberately sparse NCBI-only placeholder species record under `unclassified Acetobacteraceae`.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
