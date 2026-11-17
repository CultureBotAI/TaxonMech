# YAML Record Review: Acetofilamentum rigidum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetofilamentum_rigidum.yaml
- Started UTC: 2026-09-26T17:38:52Z
- Finished UTC: 2026-09-26T17:38:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetofilamentum_rigidum.yaml` |
| Identifier | `NCBITaxon:1653170` |
| Label | `Acetofilamentum rigidum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:558418` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:237733`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetofilamentum_rigidum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteroides_sp_miz14.yaml data/taxa/bacteria/acetofilamentum_rigidum.yaml data/taxa/bacteria/acetofilamentum_sp.yaml data/taxa/bacteria/acetohalobium_arabaticum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected LPSN/BacDive-backed shape: 111 YAML lines, 11 lineage entries, 1 LPSN name, 1 BacDive type strain, 1 related GOLD organism record, 1 NCBITaxon related synonym, 1 LPSN xref, 0 taxonomy mappings, 0 genome assemblies, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, BacDive, LPSN, culture-collection, and NCBI type-material rows; found `lpsn:772536` in the expected raw LPSN row. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:432180`, the LPSN row at `data/raw/lpsn_names.tsv:14831`, 1 BacDive row, 1 normalized culture-collection row, 4 NCBI type-material rows, 11 checked lineage entries with no missing rows or mismatches, and no GTDB, StrainInfo, assembly, GOLD aggregate, MediaDive, Madin, BactoTraits, or NCBI merge rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1653170` resolves in the committed NCBI inventory to label
`Acetofilamentum rigidum`, rank `SPECIES`, parent `NCBITaxon:558418`, related
synonym `Acetofilamentum rigidum Dietrich et al. 1989`, genetic code `11`, and
taxonomy snapshot `2026-09-13`. The record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 11
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:558418`
Acetofilamentum. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:14831`, including
`lpsn:772536`, the `Acetofilamentum rigidum` name, valid publication flags, the
`Dietrich et al. 1989` authority, two DOI publications, and the DSM 20769
type-strain designation.

The BacDive type strain is supported by `data/raw/bacdive_strains.tsv:90524`
for BacDive 168291, designation `MN`, and culture collection `DSM-20769`.
The NCBI type-material rows list `DSM 20769`, `DSM:20769`, `personal::MN`, and
`strain MN` as equivalent type designations.

The seed event is supported by `curation/seed_scope.tsv:30737`, which records
`NCBITaxon:1653170` as added on `2026-09-12` with reason `attested rule:
Acetofilamentum rigidum, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated LPSN/BacDive
record. The bounded scan found the expected name and strain sources and found
no GTDB, StrainInfo, normalized assembly/genome, GOLD aggregate, MediaDive,
Madin, BactoTraits, or NCBI merge row for this target.

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

The exact source scan also found `curation/legacy_page_paths.tsv:26197`; that
is legacy route metadata and does not require a TaxonRecord field.
