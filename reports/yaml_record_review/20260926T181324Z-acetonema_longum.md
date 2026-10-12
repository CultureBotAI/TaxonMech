# YAML Record Review: Acetonema longum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetonema_longum.yaml
- Started UTC: 2026-09-26T18:13:24Z
- Finished UTC: 2026-09-26T18:13:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetonema_longum.yaml` |
| Identifier | `NCBITaxon:2374` |
| Label | `Acetonema longum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2373` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:340159`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetonema_longum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_sp_uba5826.yaml data/taxa/bacteria/acetomicrobium_thermoterrenum.yaml data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml data/taxa/bacteria/acetonema_longum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a generated species record: 590 YAML lines, 9 lineage entries, 1 LPSN nomenclature row, 1 exact synonym, 1 BacDive type strain, 9 genome assemblies, 6 genome records, 25 related records, 2 xrefs, and 5 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, LPSN, GOLD, Madin, StrainInfo, NCBI type-material, and related-record rows; found its DSM 6540 strain support in BacDive, assembly, genome, BV-BRC, GTDB genome, GOLD, NCBI Assembly, and StrainInfo rows. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:1874`, 1 LPSN row, 1 BacDive species/strain match, 1 GOLD aggregate with 2 native GOLD organisms, 1 Madin row, 2 species-level related-record rows, StrainInfo ATCC 51454/DSM 6540 deposits, 6 NCBI type-material rows, and 9 checked lineage entries with no missing rows or mismatches. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2374` resolves in the committed NCBI inventory to label
`Acetonema longum`, rank `SPECIES`, parent `NCBITaxon:2373`, exact synonym
`Acetonema longum Kane and Breznak 1992`, genetic code `11`, and taxonomy
snapshot `2026-09-13`. The record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2373` Acetonema. There are
no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN row `lpsn:772544` supports the validly published correct-name
nomenclature, ATCC 51454 / DSM 6540 type-strain designations, publication and
sequence accessions, and the LPSN xref for this species.

BacDive 17111, StrainInfo strain 42994, and two native GOLD organism rows
support the APO-1 / ATCC 51454 / DSM 6540 type-strain surface. The strain
block also preserves DSM 6540 assembly, genome, and related-record evidence
through the child strain `NCBITaxon:1009370`.

The seed event is supported by `curation/seed_scope.tsv:23340`, which records
`NCBITaxon:2374` as added on `2026-09-12` with reason `attested rule:
Acetonema longum, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated species record.
The bounded scan found expected NCBI, LPSN, BacDive, StrainInfo, native GOLD,
Madin, NCBI type-material, and strain-linked genome rows and no direct target
rows in GTDB, MediaDive, BactoTraits, NCBI merge, or primary strain tables
that would require additional species-level sections.

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

The previously reviewed child strain
`data/taxa/bacteria/acetonema_longum_dsm_6540.yaml` carries its own
strain-level GTDB species-cluster projection issue. That finding does not
apply to this species-level `NCBITaxon:2374` record.
