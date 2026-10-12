# YAML Record Review: Acidianus sp. SYK-ESO-2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_sp_syk_eso_2.yaml
- Started UTC: 2026-09-27T08:46:57Z
- Finished UTC: 2026-09-27T08:46:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_sp_syk_eso_2.yaml` |
| Identifier | `NCBITaxon:1071530` |
| Label | `Acidianus sp. SYK-ESO-2` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2629519` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input only, with path
pinned by `data/taxa/PATHS.tsv:22676` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_sp_syk_eso_2.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_sp_syk_eso_2.yaml data/taxa/archaea/acidianus_sulfidivorans.yaml data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml data/taxa/archaea/acidianus_tengchongensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 NCBI source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1071530` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:229450`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1071530` resolves to label `Acidianus sp. SYK-ESO-2`, rank
`SPECIES`, parent `NCBITaxon:2629519`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`. The generated record carries
those same fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2629519` unclassified
Acidianus. The bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row has no synonym to project. The generated record correctly contains
no LPSN nomenclature, GTDB mapping, provider xref, strain, genome assembly,
genome record, or related-record sections.

The seed event is supported by `curation/seed_scope.tsv:328677`, which records
`NCBITaxon:1071530` as added on `2026-09-13` with reason `attested rule:
Acidianus sp. SYK-ESO-2, 1 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. Exact and
bounded scans accounted for the expected NCBI, seed, path, and YAML inputs, and
found no omitted NCBI merge, NCBI type-material, LPSN, GTDB, GOLD, BacDive,
MediaDive, MADIN, BactoTraits, StrainInfo, normalized strain, or StrainInfo
exclusion row for this taxon.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
All exact side-surface scans were empty.
This record's parent is `NCBITaxon:2629519`, the unclassified
`Acidianus` branch, so the ten-entry lineage is expected.
No GTDB species pools onto `NCBITaxon:1071530` in `data/raw/gtdb_mappings.tsv`.
No MediaDive row is present either, leaving NCBI as the only source
attestation.
The lack of synonyms in `data/raw/ncbitaxon_taxa.tsv` is mirrored by the
absent generated `synonyms` section.
No upstream side row needs staging in kg-microbe or the seeder.
The report therefore has no follow-up curation item.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
