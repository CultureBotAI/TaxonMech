# YAML Record Review: Acetobacterium woodii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_woodii.yaml
- Started UTC: 2026-09-26T17:34:59Z
- Finished UTC: 2026-09-26T17:34:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_woodii.yaml` |
| Identifier | `NCBITaxon:33952` |
| Label | `Acetobacterium woodii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33951` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:453456`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_woodii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_woodii.yaml data/taxa/bacteria/acetobacterium_woodii_dsm_1030.yaml data/taxa/bacteria/acetobacteroides_hydrogenigenes.yaml data/taxa/bacteria/acetobacteroides_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated record: 780 YAML lines, 9 lineage entries, 1 LPSN name, 1 GTDB `skos:closeMatch`, 1 BacDive strain filed under descendant `NCBITaxon:931626`, 9 genome assemblies, 6 genome records, 33 related records, 3 xrefs, and 6 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, GOLD, GTDB, LPSN, Madin, BacDive descendant, StrainInfo, and related-record rows; found `lpsn:772534`, `GTDB:s__Acetobacterium_woodii`, and `GTDB:s__Acetobacterium_woodii_A` in the expected raw LPSN and GTDB rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:3682`, the LPSN row at `data/raw/lpsn_names.tsv:14830`, the GTDB mapping at `data/raw/gtdb_mappings.tsv:276838`, one native BacDive row filed to this species plus strain `NCBITaxon:931626`, one GOLD aggregate row covering two native GOLD organisms, one Madin row with 4 assertions, 13 StrainInfo related rows, 9 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:33952` resolves in the committed NCBI inventory to label
`Acetobacterium woodii`, rank `SPECIES`, parent `NCBITaxon:33951`, related
synonym `Acetobacterium woodii Balch et al. 1977`, genetic code `11`, and
taxonomy snapshot `2026-09-13`. The record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:33951` Acetobacterium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:14830`, including
`lpsn:772534`, the `Acetobacterium woodii` name, valid publication flags, the
`Balch et al. 1977 (Approved Lists 1980)` authority, two DOI publications,
`INSDC:X96954`, and three type-strain designations.

The direct GTDB mapping is supported by `data/raw/gtdb_mappings.tsv:276838`,
which maps `GTDB:s__Acetobacterium_woodii_A` to `NCBITaxon:33952` with
predicate `skos:closeMatch` and `genome_count: 1`. The related BacDive,
BV-BRC, GOLD, GTDB genome, NCBI Assembly, and StrainInfo rows for DSM 1030 are
properly filed through the descendant `NCBITaxon:931626` strain record.

The seed event is supported by `curation/seed_scope.tsv:20837`, which records
`NCBITaxon:33952` as added on `2026-09-12` with reason `attested rule:
Acetobacterium woodii, 5 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
record. The generated record covers the LPSN name, direct GTDB species mapping,
direct GOLD and Madin attestations, the descendant BacDive type strain, and
the strain-linked genome and related-record evidence; the bounded scan found no
direct BacDive strain row, type-material conflict, MediaDive row, BactoTraits
row, or NCBI merge row for the species target itself.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

The exact source scan also found `curation/legacy_page_paths.tsv:46905`; that
is legacy route metadata and does not require a TaxonRecord field.
