# YAML Record Review: Sphingobacterium mizutaii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/sphingobacterium_mizutaii.yaml
- Started UTC: 2026-09-27T19:03:29Z
- Finished UTC: 2026-09-27T19:03:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/sphingobacterium_mizutaii.yaml` |
| Identifier | `NCBITaxon:1010` |
| Label | `Sphingobacterium mizutaii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:28453` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a 2,139-line generated rich species record supported by NCBITaxon,
BacDive, GOLD, GTDB, LPSN, and MADIN, with path pinned by `data/taxa/PATHS.tsv:3340`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/sphingobacterium_mizutaii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/sphingobacterium_mizutaii.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_b16.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_c08.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa164_c09.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 11 lineage entries, 1 LPSN nomenclature entry, 3 GTDB broad mappings, 14 synonyms, 2 xrefs, 4 BacDive strains, 23 genome assemblies, 16 genome records, 95 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010` in the expected target YAML, seed, PATHS, NCBI, and GTDB mapping rows, including the expected child `NCBITaxon:1220576`; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, NCBI row 783, 11 checked lineage rows with no missing rows or mismatches, 1 NCBI merge row from `NCBITaxon:999469`, 24 NCBI type-material rows, 1 LPSN row, 3 GTDB rows, 4 exact BacDive rows, 1 GOLD aggregate row, native GOLD side rows, 1 MADIN row, and retained normalized strain, genome, and StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010` resolves to `Sphingobacterium mizutaii`, rank `SPECIES`,
parent `NCBITaxon:28453`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`,
and taxonomy snapshot `2026-09-13`.

The 11-entry lineage is root-first and matches committed NCBI rows down to
the `Sphingobacterium` genus. The bounded scan found one retained old NCBI ID:
`NCBITaxon:999469` now resolves to `NCBITaxon:1010`.

## Evidence

The LPSN row `lpsn:780977` supports the legitimate, validly published, correct
species name and supplies two related LPSN synonym names plus the type-strain
designations that are retained in `nomenclature`.

The three GTDB mapping rows at `data/raw/gtdb_mappings.tsv:1140`-`1142` support
the three `skos:broadMatch` mappings and the 15-genome GTDB source attestation.

GOLD and MADIN side rows are present for exact `NCBITaxon:1010`; normalized
GOLD rows are retained in genome and related records where they match strains.

BacDive supports four retained strains, including one type strain and one strain
classified as descendant `NCBITaxon:1220576`; normalized assemblies, genomes,
StrainInfo assemblies, and StrainInfo related records were retained.

## Completeness

The generated YAML retains 23 genome assemblies from BacDive, BV-BRC, GOLD,
GTDB, NCBI Assembly, and StrainInfo; it also retains 16 genome records from
AllTheBacteria, BacDive, BV-BRC, GOLD, and GTDB.

Exact raw rows include 3 normalized BacDive strain rows, 3 culture-collection rows,
11 strain assembly rows, 10 strain genome rows, 30 normalized strain related rows,
4 StrainInfo assemblies, and 41 StrainInfo sequence/deposit rows.

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
`strain_count: 4` is expected from the four exact BacDive rows retained under this species.
Three GTDB species are expected to pool onto this NCBI species by `skos:broadMatch`.
GOLD aggregate count 8 is represented through exact native side rows and normalized strain-matched rows.
StrainInfo evidence is retained only where it matches retained BacDive strain identifiers.
