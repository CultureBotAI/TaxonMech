# YAML Record Review: Acetomicrobium flavidum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_flavidum.yaml
- Started UTC: 2026-09-26T17:43:31Z
- Finished UTC: 2026-09-26T17:43:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_flavidum.yaml` |
| Identifier | `NCBITaxon:49896` |
| Label | `Acetomicrobium flavidum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:49894` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:521319`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_flavidum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetohalobium_arabaticum_dsm_5501.yaml data/taxa/bacteria/acetohalobium_sp.yaml data/taxa/bacteria/acetomicrobium_flavidum.yaml data/taxa/bacteria/acetomicrobium_hydrogeniformans.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated record: 716 YAML lines, 9 lineage entries, 1 LPSN name, 1 `skos:closeMatch` GTDB taxonomy mapping, 1 BacDive type strain, 9 genome assemblies, 8 genome records, 27 related records, 2 xrefs, and 8 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, NCBI type-material, culture-collection, strain assembly, genome, related-record, StrainInfo, BV-BRC, and ATB rows; found `lpsn:772541` and `GTDB:s__Acetomicrobium_flavidum` in the expected raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:6297`, the LPSN row at `data/raw/lpsn_names.tsv:14835`, 1 GTDB mapping row, 1 BacDive row, 2 native GOLD organisms, 1 MediaDive row, 1 Madin row, 1 BactoTraits row, 5 StrainInfo related rows, 7 NCBI type-material rows, 9 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:49896` resolves in the committed NCBI inventory to label
`Acetomicrobium flavidum`, rank `SPECIES`, parent `NCBITaxon:49894`, related
synonym `Acetomicrobium flavidum Soutschek et al. 1985`, genetic code `11`,
and taxonomy snapshot `2026-09-13`. The record carries those same identity
fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:49894` Acetomicrobium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:14835`, including
`lpsn:772541`, the `Acetomicrobium flavidum` name, valid publication flags, the
`Soutschek et al. 1985` authority, two DOI publications, `INSDC:FR733692`, and
the ATCC 43122 / DSM 20664 / LMG 6941 type-strain designations.

The BacDive type strain is supported by `data/raw/bacdive_strains.tsv:1576`
for BacDive 1580, designation `P`, and the ATCC 43122 / DSM 20664 culture
collection identifiers. NCBI type-material and StrainInfo both mark the same
ATCC, DSM, and LMG deposits as type material.

The seed event is supported by `curation/seed_scope.tsv:1820`, which records
`NCBITaxon:49896` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium flavidum, 8 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
record. The bounded scan found the expected LPSN, GTDB, BacDive, StrainInfo,
native GOLD, MediaDive, Madin, BactoTraits, NCBI type-material, and genome rows
and found no NCBI merge row for this target.

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

The exact source scan also found `curation/legacy_page_paths.tsv:52289`; that
is legacy route metadata and does not require a TaxonRecord field.
