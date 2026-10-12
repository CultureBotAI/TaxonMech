# YAML Record Review: Acidianus uzoniensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_uzoniensis.yaml
- Started UTC: 2026-09-27T08:50:37Z
- Finished UTC: 2026-09-27T08:50:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_uzoniensis.yaml` |
| Identifier | `NCBITaxon:518068` |
| Label | `Acidianus uzoniensis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input only, with path
pinned by `data/taxa/PATHS.tsv:526097` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_uzoniensis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_uzoniensis.yaml data/taxa/archaea/acidilobaceae_archaeon.yaml data/taxa/archaea/acidilobaceae_archaeon_uba158.yaml data/taxa/archaea/acidilobaceae_archaeon_uba162.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 9 lineage entries, 1 NCBI related synonym, 1 NCBI source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:518068` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:117741`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:518068` resolves to label `Acidianus uzoniensis`, rank `SPECIES`,
parent `NCBITaxon:12914`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same fields
and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:12914` Acidianus. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

The generated NCBI related synonym, `"Acidianus uzoniensis" Bize et al. 2008`,
mirrors the only synonym in the source NCBI row.

The generated record correctly contains no LPSN nomenclature, GTDB mapping,
provider xref, strain, genome assembly, genome record, or related-record
sections.

The seed event is supported by `curation/seed_scope.tsv:228926`, which records
`NCBITaxon:518068` as added on `2026-09-13` with reason `attested rule:
Acidianus uzoniensis, 1 sources incl. NCBI`.

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
No exact side-source scan found an omitted retained provider row.
The genus-level parent means a 9-entry lineage is expected.
The NCBI synonym is a related authorship string, not an exact synonym.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
The record has no GTDB-backed synonym to reconcile.
No generated xref section is expected.
The ignored report probe included gitignored files.
