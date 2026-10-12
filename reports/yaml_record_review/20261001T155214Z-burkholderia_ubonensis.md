# YAML Record Review: Burkholderia ubonensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/burkholderia_ubonensis.yaml
- Started UTC: 2026-10-01T15:52:14Z
- Finished UTC: 2026-10-01T15:52:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/burkholderia_ubonensis.yaml` |
| Identifier | `NCBITaxon:101571` |
| Label | `Burkholderia ubonensis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:87882` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a multi-source seeded Burkholderia species record, with path pinned
by `data/taxa/PATHS.tsv:8998`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/burkholderia_ubonensis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 1,385 YAML lines, 10 lineage entries, 1 LPSN nomenclature entry, 3 taxonomy mappings, 6 synonyms, 2 xrefs, 1 BacDive strain, and 8 source attestations. |
| Exact local scans | Found `NCBITaxon:101571` in expected seed, NCBI, LPSN, GTDB, BacDive, GOLD, MediaDive, MADIN, BactoTraits, StrainInfo, ATB, `PATHS.tsv`, YAML, and descendant-taxonomy contexts; the ignored-file-inclusive report probe found no prior report for this stem. |
| Structured strain scan | Confirmed the single BacDive type-strain block contains 5 culture-collection identifiers, 16 nested genome assemblies, 13 nested genome records, and 62 nested related records. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101571` resolves to `Burkholderia ubonensis`, rank `SPECIES`,
parent `NCBITaxon:87882`, genetic code `11`, and source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`.

The ten-line lineage is root-first and reaches `NCBITaxon:87882`, NCBI's
Burkholderia cepacia complex species group.

LPSN names `lpsn:774309` as the validly published correct name and links it to
four type-strain culture IDs plus the INSDC accession `MT672505`.

Three GTDB broad mappings are retained: `s__Burkholderia_ubonensis`,
`s__Burkholderia_vietnamiensis`, and `s__Burkholderia_ubonensis_B`.

## Evidence

NCBI contributes the primary row, five synonym strings, 14 type-material rows,
two merge rows into this taxon, and expected descendant rows.
LPSN contributes the nomenclature row; BacDive contributes one type-strain row.
GOLD, MediaDive, MADIN, BactoTraits, GTDB, NCBI Assembly, BV-BRC, ATB, and
StrainInfo rows are all represented under the single normalized strain block.

## Strain and Genomes

The sole declared strain is `kgmicrobe.strain:bacdive_1964`, BacDive `1964`,
designation `EY 3383`, marked as the type strain.
The YAML keeps five culture-collection identifiers: CCUG 48852, CIP 107078,
DSM 17311, LMG 20358, and NCTC 13147.
The strain embeds 16 genome assemblies, 13 genome records, and 62 related records;
no top-level genome or related-record block is present outside the strain.

## Completeness

The 1,385-line YAML contains one LPSN nomenclature entry, three GTDB mappings,
six synonyms, two xrefs, one strain, and eight source attestations.
It has no causal graphs and no unnormalized standalone strain block.
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

Descendant references to Burkholderia ubonensis strain/subspecies YAMLs are expected.
The merged old IDs `NCBITaxon:410874` and `NCBITaxon:410876` target this taxon.
The GTDB rows are broad matches, so exact synonym minting from GTDB is not implied.
The ignored report probe included gitignored files.
