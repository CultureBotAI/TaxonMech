# YAML Record Review: Viridibacillus neidei

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/viridibacillus_neidei.yaml
- Started UTC: 2026-09-28T02:17:38Z
- Finished UTC: 2026-09-28T02:17:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/viridibacillus_neidei.yaml` |
| Identifier | `NCBITaxon:101059` |
| Label | `Viridibacillus neidei` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:496496` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multi-source Viridibacillus species record,
with path pinned by `data/taxa/PATHS.tsv:3794`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/viridibacillus_neidei.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_bd_121.yaml data/taxa/bacteria/bacillus_sp_bd_83.yaml data/taxa/bacteria/bacillus_sp_bd_85.yaml data/taxa/bacteria/viridibacillus_neidei.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 339 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 8 synonyms, 1 LPSN xref, 1 BacDive type strain, 4 culture IDs, 12 related rows, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:101059` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17383`, 9 checked lineage rows, 1 LPSN row, 1 BacDive row, 1 GOLD aggregate row, 2 native GOLD organisms, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 4 GOLD related rows, 8 StrainInfo related rows, 8 type-material rows, 2 NCBI merge rows, no GTDB row, and no native GOLD project or analysis rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101059` resolves to `Viridibacillus neidei`, rank `SPECIES`,
parent `NCBITaxon:496496`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:496496` genus `Viridibacillus`. The bounded scan found old IDs
`NCBITaxon:101047` and `NCBITaxon:101048` merged into this current taxon.

## Evidence

The NCBI row supports the current species name, parent, genetic code, two
exact synonyms, five related synonyms, seven upstream source flags, and the
2026-09-13 snapshot date.

LPSN `lpsn:786989` supplies the nomenclature row, type-strain designations,
three publications, one sequence accession, and the LPSN xref.

BacDive `bacdive:569` supplies one type strain with four culture IDs.
GOLD contributes `Go0626364` and `Go0626365` related organism rows, while
StrainInfo contributes 4 deposit and 4 strain related rows.

MediaDive, MADIN, and BactoTraits each contribute target-level rows.

## Completeness

No exact GTDB mapping, genome assembly, genome record, causal graph, native
GOLD project, or native GOLD analysis row was filed.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

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
`strain_count: 1` is expected from the exact BacDive row.
The LPSN synonym plus seven NCBI synonyms make eight synonym entries.
No `taxonomy_mappings` section is expected; LPSN is represented by nomenclature and xref.
Two native GOLD organism rows generate four related rows through strain and culture matches.
The GOLD source attestation preserves the aggregate organism count of 3.
The retained StrainInfo rows are tied to BacDive strain `bacdive:569`.
MediaDive contributes one medium; MADIN and BactoTraits contribute trait assertions.
The two NCBI merge rows were checked.
The 339-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
