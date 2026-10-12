# YAML Record Review: Weeksella virosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/weeksella_virosa.yaml
- Started UTC: 2026-09-30T11:53:10Z
- Finished UTC: 2026-09-30T11:53:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/weeksella_virosa.yaml` |
| Identifier | `NCBITaxon:1014` |
| Label | `Weeksella virosa` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1013` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated species record with NCBI, GTDB, BacDive, LPSN, GOLD,
MADIN, genome, and StrainInfo-backed side evidence, with its path pinned by
`data/taxa/PATHS.tsv:7189`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/weeksella_virosa.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 2394 YAML lines, 11 lineage entries, 6 source attestations, 4 NCBI related synonyms, 1 LPSN nomenclature entry, 1 GTDB taxonomy mapping, 2 xrefs, 16 BacDive strains, 29 culture-collection IDs, 15 genome assemblies, 12 genome records, 125 related records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:1014` with a numeric boundary in the expected seed, NCBI, MADIN, LPSN, GOLD, GTDB, StrainInfo, NCBI type-material, related-record, child-YAML, and `data/taxa/PATHS.tsv` rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:787`, 11 checked lineage entries with no missing rows or mismatches, 16 BacDive matches, LPSN `lpsn:783088`, GTDB `GTDB:s__Weeksella_virosa`, 1 MADIN row, 1 GOLD aggregate row, 40 native GOLD organism rows, 2 native GOLD project rows, 2 native GOLD analysis rows, 43 StrainInfo deposits, 2 StrainInfo assembly rows, 59 StrainInfo related rows, 21 NCBI type-material rows, and 0 NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1014` resolves to `Weeksella virosa`, rank `SPECIES`, parent
`NCBITaxon:1013`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:1013` Weeksella. The bounded scan found no NCBI merge row and no
retained old-id row.

NCBI retains four related synonyms for this species; the generated record
retains all four as `RELATED_SYNONYM` entries sourced to NCBITaxon.

## Evidence

The LPSN row at `data/raw/lpsn_names.tsv:21266` grounds the legitimate,
validly published, correct species name and the GTDB closeMatch to
`GTDB:s__Weeksella_virosa`.

BacDive, NCBI type-material, and StrainInfo support 16 exact strains,
including the type-strain row. StrainInfo contributes 43 available deposits,
2 assembly rows, and 59 related records for this target.

GOLD contributes 40 native organism rows, 2 project rows, 2 analysis rows, and
one aggregate row for `NCBITaxon:1014`. MADIN contributes 4 trait assertions.

## Completeness

No exact BactoTraits row, exact MediaDive row, NCBI merge row, retained old-id
row, or causal graph is filed for this exact species.

The exact NCBITaxon probe used a numeric boundary so the scan for
`NCBITaxon:1014` did not conflate this short identifier with longer neighboring
identifiers.

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
The 125 related records are all side evidence records retained by the generator.
The source attestations cover NCBITAXON, GTDB, BACDIVE, LPSN, GOLD, and MADIN.
The GTDB `skos:closeMatch` maps through `GTDB:s__Weeksella_virosa`.
The type strain is retained from BacDive and NCBI type-material evidence.
The record keeps 4 NCBI related synonyms.
The exact species has 2 xrefs.
The bounded scan found no retained old-id evidence.
The short-ID boundary probe excluded longer neighboring identifiers.
The ignored report probe included gitignored files.
