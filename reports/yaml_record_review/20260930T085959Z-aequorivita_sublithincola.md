# YAML Record Review: Aequorivita sublithincola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/aequorivita_sublithincola.yaml
- Started UTC: 2026-09-30T08:59:59Z
- Finished UTC: 2026-09-30T08:59:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/aequorivita_sublithincola.yaml` |
| Identifier | `NCBITaxon:101385` |
| Label | `Aequorivita sublithincola` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:153265` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated species record with NCBI, LPSN, GOLD, MADIN, BacDive,
genome, and StrainInfo-backed side evidence, with its path pinned by
`data/taxa/PATHS.tsv:7027`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/aequorivita_sublithincola.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 654 YAML lines, 11 lineage entries, 5 source attestations, 2 NCBI related synonyms, 1 LPSN nomenclature entry, 2 xrefs, 1 BacDive strain, 1 declared strain, 1 type strain, 4 culture-collection IDs, 10 genome assemblies, 7 genome records, 28 related records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101385` with a numeric boundary in the expected seed, NCBI, MADIN, LPSN, GOLD, StrainInfo, NCBI type-material, related-record, and YAML rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17518`, 11 checked lineage entries with no missing rows or mismatches, BacDive `5477`, LPSN `lpsn:772873`, 1 MADIN row, 1 GOLD aggregate row, 2 native GOLD organism rows, 2 raw GOLD related rows, 3 StrainInfo deposits, 1 StrainInfo assembly row, 6 StrainInfo related rows, 4 NCBI type-material rows, and 0 NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101385` resolves to `Aequorivita sublithincola`, rank `SPECIES`,
parent `NCBITaxon:153265`, genetic code `11`, source set
`ncbitaxon|lpsn|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows. The bounded
scan found no NCBI merge row and no retained old-id row.

NCBI retains two related synonyms for this exact species: `Aequorivita
sublithincola Bowman and Nichols 2002` and `Cytophaga-like bacterium QSSC9-3`.

## Evidence

The LPSN row at `data/raw/lpsn_names.tsv:15054` grounds the legitimate,
validly published, correct species name and points at type strain
`kgmicrobe.strain:DSM-14238`.

BacDive `5477`, the NCBI type-material rows, and the exact StrainInfo rows
support the type-strain side evidence. StrainInfo contributes available
deposits for LMG 21432, DSM 14238, and CIP 107454, plus one DSM 14238 assembly
row.

GOLD contributes two native organism rows for `NCBITaxon:101385`, one GOLD
aggregate row, and two raw GOLD related-record rows for `Go0625823`. MADIN
contributes four trait assertions through `data/raw/madin_taxa.tsv:448`.

## Completeness

No GTDB taxonomy mapping, BactoTraits target row, MediaDive target row, native
GOLD project row, native GOLD analysis row, NCBI merge row, or causal graph is
filed for this exact species.

The exact NCBITaxon probe used a numeric boundary so the scan for
`NCBITaxon:101385` did not conflate this species with the neighboring
`NCBITaxon:1013850` through `NCBITaxon:1013852` ALO1 clone records.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

No findings.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

No follow-up needed.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
The 28 related records are all side evidence records retained by the generator.
The 10 genome assemblies draw from BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo.
The 7 genome records draw from BacDive, BV-BRC, GOLD, and GTDB.
No `taxonomy_mappings` section is expected for this exact species record.
No exact BactoTraits or MediaDive source row is filed.
No native GOLD project or analysis row is filed.
The source attestations cover NCBITAXON, LPSN, GOLD, MADIN, and BACDIVE.
The exact species has 2 xrefs.
The bounded scan found no retained old-id evidence.
The ignored report probe included gitignored files.
