# YAML Record Review: Acidilobales archaeon

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobales_archaeon.yaml
- Started UTC: 2026-09-27T08:54:10Z
- Finished UTC: 2026-09-27T08:54:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobales_archaeon.yaml` |
| Identifier | `NCBITaxon:2268176` |
| Label | `Acidilobales archaeon` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2268146` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI input only, with path
pinned by `data/taxa/PATHS.tsv:335313` and fields owned by generated inputs.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobales_archaeon.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidilobales_archaeon.yaml data/taxa/archaea/acidilobus_aceticus.yaml data/taxa/archaea/acidilobus_saccharovorans.yaml data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 48 YAML lines, 8 lineage entries, 1 NCBI source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2268176` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:522440`, 8 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, no normalized strain rows, no StrainInfo assembly or related rows, no direct StrainInfo or StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2268176` resolves to label `Acidilobales archaeon`, rank `SPECIES`,
parent `NCBITaxon:2268146`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same fields
and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2268146` unclassified
Acidilobales. The bounded scan found no NCBI merge row and no retained old-id
row.

## Evidence

The NCBI row has no synonym to project. The generated record correctly contains
no LPSN nomenclature, GTDB mapping, provider xref, strain, genome assembly,
genome record, or related-record sections.

The seed event is supported by `curation/seed_scope.tsv:560624`, which records
`NCBITaxon:2268176` as added on `2026-09-13` with reason `attested rule:
Acidilobales archaeon, 1 sources incl. NCBI`.

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
The unclassified order-level parent means an 8-entry lineage is expected.
No upstream side row needs staging in kg-microbe or the seeder.
The report therefore has no follow-up curation item.
No generated xref section is expected.
No generated synonym section is expected.
No GTDB species pools onto this unresolved NCBI species.
No MediaDive row is present either.
The seed scope row names NCBI as the only source.
The ignored report probe included gitignored files.
