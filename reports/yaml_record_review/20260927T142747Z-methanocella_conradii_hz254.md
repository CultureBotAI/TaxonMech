# YAML Record Review: Methanocella conradii HZ254

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/methanocella_conradii_hz254.yaml
- Started UTC: 2026-09-27T14:27:47Z
- Finished UTC: 2026-09-27T14:27:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/methanocella_conradii_hz254.yaml` |
| Identifier | `NCBITaxon:1041930` |
| Label | `Methanocella conradii HZ254` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:1175444` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB, MADIN, and NCBI-backed Methanocella strain
record, with path pinned by `data/taxa/PATHS.tsv:16479`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/methanocella_conradii_hz254.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/methanosarcina_spelaei.yaml data/taxa/archaea/thermococcus_sp_9on_7.yaml data/taxa/archaea/methanocella_conradii_hz254.yaml data/taxa/archaea/thermococcus_sp_4557.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 90 YAML lines, 11 lineage entries, 1 GTDB mapping, 4 exact synonyms, 1 xref, 3 source attestations, 0 strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1041930` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:223883`, 11 checked lineage entries with no missing rows or mismatches, 1 GTDB row at line 1613, 1 MADIN row, 1 native GOLD organism, 1 native GOLD project, 1 native GOLD analysis, 2 normalized assembly rows, 3 genome rows, 5 exact-target related rows, 0 NCBI merge rows, 0 NCBI type-material rows, no exact BacDive strain row, and no LPSN, MediaDive, or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1041930` resolves to `Methanocella conradii HZ254`, rank `STRAIN`,
parent `NCBITaxon:1175444`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
species `NCBITaxon:1175444` Methanocella conradii. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the strain identity, direct species parent, genetic code,
three exact NCBI synonyms, source set, and snapshot date. The GTDB row supports
the `GTDB:s__Methanocella_conradii` closeMatch with 3 genomes.

The MADIN row supports the eight-assertion MADIN attestation. Native GOLD has
exact organism, project, and analysis rows for HZ254, but no retained GOLD
aggregate or exact BacDive strain row files this taxon as a local strain.

BacDive row 17669 is filed under parent species `NCBITaxon:1175444`; the
normalized HZ254 BacDive/GOLD assembly and related rows remain source-table
side evidence and are not materialized in this exact strain record.

## Completeness

No required generated claim is absent for this record under the current
exact-BacDive gating. Exact and bounded scans accounted for expected NCBI,
GTDB, MADIN, seed, path, native GOLD, and normalized side rows.

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
`strain_count: 0` is expected without an exact BacDive row.
The GTDB closeMatch has 3 genomes.
The MADIN row has 8 trait assertions.
Two normalized assembly rows remained side evidence.
Three normalized genome rows remained side evidence.
Five normalized related rows remained side evidence.
No `nomenclature` section is expected.
Native GOLD rows were side evidence only.
No NCBI type-material row exists on this strain.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 90-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
