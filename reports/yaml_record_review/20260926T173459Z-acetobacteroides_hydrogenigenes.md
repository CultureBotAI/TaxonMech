# YAML Record Review: Acetobacteroides hydrogenigenes

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteroides_hydrogenigenes.yaml
- Started UTC: 2026-09-26T17:34:59Z
- Finished UTC: 2026-09-26T17:34:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetobacteroides_hydrogenigenes.yaml` |
| Identifier | `NCBITaxon:979970` |
| Label | `Acetobacteroides hydrogenigenes` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1647173` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:621068`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacteroides_hydrogenigenes.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetobacterium_woodii.yaml data/taxa/bacteria/acetobacterium_woodii_dsm_1030.yaml data/taxa/bacteria/acetobacteroides_hydrogenigenes.yaml data/taxa/bacteria/acetobacteroides_sp.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a source-rich generated record: 404 YAML lines, 11 lineage entries, 1 LPSN name, 1 GTDB `skos:closeMatch`, 1 BacDive type strain, 3 genome assemblies, 5 genome records, 13 related records, 2 NCBITaxon related synonyms, 2 xrefs, and 7 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, BacDive, StrainInfo, GOLD, GTDB, MediaDive, BactoTraits, BV-BRC, ATB, and related-record rows; found `lpsn:792130` and `GTDB:s__Acetobacteroides_hydrogenigenes` in the expected LPSN and GTDB raw rows. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:204284`, the LPSN row at `data/raw/lpsn_names.tsv:28912`, the GTDB mapping at `data/raw/gtdb_mappings.tsv:321477`, one BacDive row, one GOLD aggregate row covering three native GOLD organisms and one native GOLD project/analysis chain, one MediaDive row with three media, one BactoTraits row, 11 checked lineage entries with no missing rows or mismatches, and no retained old NCBI IDs. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:979970` resolves in the committed NCBI inventory to label
`Acetobacteroides hydrogenigenes`, rank `SPECIES`, parent
`NCBITaxon:1647173`, related synonyms `Acetobacteroides hydrogenigenes Su et
al. 2014` and `Bacteroidetes bacterium RL-C`, genetic code `11`, and taxonomy
snapshot `2026-09-13`. The record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 11
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:1647173`
Acetobacteroides. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The LPSN name block is supported by `data/raw/lpsn_names.tsv:28912`, including
`lpsn:792130`, the `Acetobacteroides hydrogenigenes` name, valid publication
flags, the `Su et al. 2014 emend. Garcia-Lopez et al. 2019` authority, three
publication IDs, `INSDC:AB611036`, and two type-strain designations.

The GTDB close-match is supported by `data/raw/gtdb_mappings.tsv:321477`,
which maps `GTDB:s__Acetobacteroides_hydrogenigenes` to `NCBITaxon:979970`
with predicate `skos:closeMatch` and `genome_count: 1`. BacDive, BV-BRC, GOLD,
AllTheBacteria, MediaDive, and BactoTraits evidence rows all resolve to the
RL-C / DSM 24657 / JCM 17603 type-strain identity.

The seed event is supported by `curation/seed_scope.tsv:7161`, which records
`NCBITaxon:979970` as added on `2026-09-12` with reason `attested rule:
Acetobacteroides hydrogenigenes, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated source-rich
record. The bounded scan found the expected LPSN, GTDB, BacDive, MediaDive,
GOLD, BactoTraits, normalized strain, genome, and related-record rows, and no
Madin row, NCBI merge row, StrainInfo assembly row, or raw StrainInfo
exclusion row for the target.

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

The exact source scan also found `curation/legacy_page_paths.tsv:62869`; that
is legacy route metadata and does not require a TaxonRecord field.
