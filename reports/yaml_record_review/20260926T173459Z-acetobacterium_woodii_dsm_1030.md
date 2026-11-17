# YAML Record Review: Acetobacterium woodii DSM 1030

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacterium_woodii_dsm_1030.yaml
- Started UTC: 2026-09-26T17:34:59Z
- Finished UTC: 2026-09-26T17:34:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacterium_woodii_dsm_1030.yaml` |
| Identifier | `NCBITaxon:931626` |
| Label | `Acetobacterium woodii DSM 1030` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33952` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:611830`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacterium_woodii_dsm_1030.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_woodii.yaml data/taxa/bacteria/acetobacterium_woodii_dsm_1030.yaml data/taxa/bacteria/acetobacteroides_hydrogenigenes.yaml data/taxa/bacteria/acetobacteroides_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated strain record: 768 YAML lines, 10 lineage entries, 1 GTDB `skos:closeMatch`, 5 exact synonyms, 1 BacDive strain, 9 genome assemblies, 6 genome records, 33 related records, 1 xref, and 7 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, BacDive, MediaDive, GOLD, GTDB, Madin, BactoTraits, StrainInfo-linked, and related-record rows; found `GTDB:s__Acetobacterium_woodii` in the expected GTDB raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:196325`, the GTDB mapping at `data/raw/gtdb_mappings.tsv:320764`, one BacDive row, one GOLD aggregate row covering two native GOLD organisms and one native GOLD project/analysis chain, one MediaDive row, one Madin row with 3 assertions, one BactoTraits row with 2 assertions, 10 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:931626` resolves in the committed NCBI inventory to label
`Acetobacterium woodii DSM 1030`, rank `STRAIN`, parent
`NCBITaxon:33952`, four exact NCBITaxon synonyms, genetic code `11`, and
taxonomy snapshot `2026-09-13`. The record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:33952`
Acetobacterium woodii. There are no retained old identifiers for this target in
the NCBI merge input.

## Evidence

The GTDB close-match is supported by `data/raw/gtdb_mappings.tsv:320764`,
which maps `GTDB:s__Acetobacterium_woodii` to `NCBITaxon:931626` with
predicate `skos:closeMatch` and `genome_count: 1`.

The BacDive, GOLD, BV-BRC, GTDB genome, NCBI Assembly, Madin, MediaDive, and
BactoTraits rows all resolve to the DSM 1030 strain identity or its
`WB1`/`ATCC 29683` synonyms. The generated record keeps the complete-genome
assembly and related BioProject/BioSample/GOLD rows under the single
`kgmicrobe.strain:bacdive_5402` strain.

The seed event is supported by `curation/seed_scope.tsv:7128`, which records
`NCBITaxon:931626` as added on `2026-09-12` with reason `attested rule:
Acetobacterium woodii DSM 1030, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
strain record. The bounded scan found the expected GTDB, BacDive, MediaDive,
GOLD, Madin, BactoTraits, normalized strain, genome, and related-record rows
for the target and no direct LPSN, NCBI type-material, NCBI merge, or native
StrainInfo taxon rows filed directly to `NCBITaxon:931626`.

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

The exact source scan also found `curation/legacy_page_paths.tsv:62208`; that
is legacy route metadata and does not require a TaxonRecord field.
