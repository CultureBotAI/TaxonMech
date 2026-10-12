# YAML Record Review: Xylanimonas pachnodae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/xylanimonas_pachnodae.yaml
- Started UTC: 2026-10-01T04:24:26Z
- Finished UTC: 2026-10-01T04:24:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/xylanimonas_pachnodae.yaml` |
| Identifier | `NCBITaxon:101489` |
| Label | `Xylanimonas pachnodae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:186188` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded bacterial species record with path pinned by
`data/taxa/PATHS.tsv:8123`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/xylanimonas_pachnodae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected rich species shape: 1117 YAML lines, 9 lineage entries, 10 synonyms, 1 LPSN nomenclature entry, 2 xrefs, 1 BacDive strain, 1 type strain, 4 culture collection IDs, 18 genome assemblies, 15 genome records, 51 related records, 6 source attestations, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101489` in the expected NCBI, BacDive, LPSN, MediaDive, MADIN, GOLD, culture-collection, type-material, StrainInfo, related-record, legacy path, seed, YAML, and `data/taxa/PATHS.tsv` rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17576`, 9 checked lineage entries with no missing rows or mismatches, 1 exact BacDive row, 4 culture-collection rows, 10 NCBI type-material rows, 1 LPSN row, 1 MediaDive row, 1 MADIN row, 1 GOLD aggregate row, 3 native GOLD organism rows, 2 StrainInfo assembly rows, 6 StrainInfo related rows, 1 direct StrainInfo row with 3 deposits, 0 NCBI merge rows, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101489` resolves to `Xylanimonas pachnodae`, rank `SPECIES`,
parent `NCBITaxon:186188`, genetic code `11`, source set
`ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows. The bounded
scan found no NCBI merge row and no retained old-id row for this target.

## Evidence

The raw NCBI row supports the accepted label, parent, rank, four exact
synonyms, four related synonyms, source set, and 2026-09-13 snapshot date.
The LPSN row at `data/raw/lpsn_names.tsv:1100` supplies the correct-name
nomenclature assertion and type-strain links to DSM 12657 and JCM 13526.

`data/raw/bacdive_strains.tsv:12453` supports the BacDive 12610 strain VPCX2
and its DSM 12657, JCM 13526, NBRC 107786, and NCCB 100020 collection IDs.
The NCBI type-material table supplies ten designation variants across those
type-strain names and VPCX2.

MediaDive line 65 supports three media assertions, MADIN line 450 supports
two trait assertions, and GOLD aggregate line 279 plus three native GOLD
organism rows support the GOLD organism evidence for VPCX2, JCM 13526, and
DSM 12657.

StrainInfo contributes two assembly rows for JCM 13526, six related deposit
or strain rows, and one direct strain record with deposits for DSM 12657,
NCCB 100020, and JCM 13526.

## Completeness

The 1117-line YAML carries all exact local BacDive, culture collection, GOLD,
LPSN, MADIN, MediaDive, NCBITaxon, and StrainInfo evidence found by the
bounded scan for `NCBITaxon:101489`.

No BactoTraits, GTDB mapping, GTDB species, native GOLD project, native GOLD
analysis, NCBI merge, retained retired NCBI row, or StrainInfo exclusion row
is filed for this exact target, so the empty sections are consistent with the
inspected source inventories.

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
The record intentionally has no GTDB taxonomy mapping despite the LPSN GTDB ID.
`source_attestations` covers NAME, STRAIN, MEDIUM, TRAIT_ASSERTION, and ORGANISM units.
The BacDive source attestation covers the single local strain.
The GOLD source attestation covers the three-organism aggregate row.
The MediaDive source attestation covers three medium rows.
The MADIN source attestation covers two trait assertions.
The NCBITaxon source attestation covers the accepted name and synonyms.
The LPSN source attestation covers the correct-name nomenclature row.
The exact `NCBITaxon:` probe included YAML and source rows.
The ignored report probe included gitignored files.
