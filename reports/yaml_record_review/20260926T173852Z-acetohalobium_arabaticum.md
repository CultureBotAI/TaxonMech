# YAML Record Review: Acetohalobium arabaticum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetohalobium_arabaticum.yaml
- Started UTC: 2026-09-26T17:38:52Z
- Finished UTC: 2026-09-26T17:38:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetohalobium_arabaticum.yaml` |
| Identifier | `NCBITaxon:28187` |
| Label | `Acetohalobium arabaticum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:28186` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:379978`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetohalobium_arabaticum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacteroides_sp_miz14.yaml data/taxa/bacteria/acetofilamentum_rigidum.yaml data/taxa/bacteria/acetofilamentum_sp.yaml data/taxa/bacteria/acetohalobium_arabaticum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated record: 713 YAML lines, 9 lineage entries, 1 LPSN name, 1 BacDive type strain classified as descendant `NCBITaxon:574087`, 10 genome assemblies, 8 genome records, 27 related records, 2 xrefs, and 5 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, LPSN, GOLD, Madin, BacDive descendant, StrainInfo, BV-BRC, ATB, and related-record rows; found `lpsn:772538` and `GTDB:s__Acetohalobium_arabaticum` in the expected LPSN and GTDB raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:2895`, the LPSN row at `data/raw/lpsn_names.tsv:14833`, one native BacDive row filed to this species plus strain `NCBITaxon:574087`, one GOLD aggregate row covering two native GOLD organisms, one Madin row with 2 assertions, 5 StrainInfo related rows, 9 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:28187` resolves in the committed NCBI inventory to label
`Acetohalobium arabaticum`, rank `SPECIES`, parent `NCBITaxon:28186`, related
synonym `Acetohalobium arabaticum Zhilina and Zavarzin 1990`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:28186` Acetohalobium. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:14833`, including
`lpsn:772538`, the `Acetohalobium arabaticum` name, valid publication flags,
the `Zhilina and Zavarzin 1990` authority, DOI publication, `INSDC:X89077`,
and the ATCC 49924 / DSM 5501 type-strain designations.

The GTDB xref to `GTDB:s__Acetohalobium_arabaticum` is consistent with the
raw GTDB row at `data/raw/gtdb_mappings.tsv:297193`, which maps that GTDB
species to descendant strain `NCBITaxon:574087` with predicate
`skos:closeMatch`. The BacDive, GOLD, BV-BRC, GTDB genome, NCBI Assembly, and
StrainInfo genome rows are correspondingly filed through the DSM 5501 strain.

The seed event is supported by `curation/seed_scope.tsv:23349`, which records
`NCBITaxon:28187` as added on `2026-09-12` with reason `attested rule:
Acetohalobium arabaticum, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
record. The bounded scan found the expected LPSN, native GOLD, Madin,
descendant BacDive/StrainInfo/genome, and type-material rows, and no direct
GTDB mapping, MediaDive, BactoTraits, or NCBI merge row for the species target
itself.

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

The exact source scan also found `curation/legacy_page_paths.tsv:40673`; that
is legacy route metadata and does not require a TaxonRecord field.
