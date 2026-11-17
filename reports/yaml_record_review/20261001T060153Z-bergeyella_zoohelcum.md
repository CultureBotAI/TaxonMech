# YAML Record Review: Bergeyella zoohelcum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bergeyella_zoohelcum.yaml
- Started UTC: 2026-10-01T06:01:53Z
- Finished UTC: 2026-10-01T06:01:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/bergeyella_zoohelcum.yaml` |
| Identifier | `NCBITaxon:1015` |
| Label | `Bergeyella zoohelcum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:59735` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded bacterial species record with path pinned by
`data/taxa/PATHS.tsv:8234`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bergeyella_zoohelcum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected rich species shape: 3762 YAML lines, 11 lineage entries, 5 synonyms, 1 LPSN nomenclature entry, 2 GTDB taxonomy mappings, 2 xrefs, 29 BacDive strains, 1 type strain, 45 culture collection IDs, 25 genome assemblies, 19 genome records, 202 related records, 6 source attestations, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:1015` in the expected NCBI, BacDive, LPSN, GTDB, MADIN, GOLD, culture-collection, type-material, StrainInfo, related-record, legacy path, seed, YAML, and `data/taxa/PATHS.tsv` rows; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:788`, 11 checked lineage entries with no missing rows or mismatches, 29 exact BacDive rows, 29 culture-collection rows, 32 NCBI type-material rows, 1 LPSN row, 2 GTDB mapping rows, 1 MADIN row, 1 GOLD aggregate row, 74 native GOLD organism rows, 5 native GOLD project rows, 3 native GOLD analysis rows, 4 StrainInfo assembly rows, 91 StrainInfo related rows, 34 direct StrainInfo rows with 61 deposits, 0 NCBI merge rows, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1015` resolves to `Bergeyella zoohelcum`, rank `SPECIES`,
parent `NCBITaxon:59735`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:59735` Bergeyella. The bounded scan found no NCBI merge row and no
retained old-id row for this target.

## Evidence

The raw NCBI row supports the accepted label, parent, rank, two exact synonyms,
two related synonyms, source set, and 2026-09-13 snapshot date.

The LPSN row at `data/raw/lpsn_names.tsv:15767` supplies the correct-name
nomenclature assertion, two publications, one sequence accession, and type
strain links to 11 collection IDs. The NCBI type-material table supplies 32
designation variants under the Weeksella zoohelcum basionym.

GTDB supplies two broad-match mappings with 8 and 1 genomes respectively.
MADIN line 451 supports 5 trait assertions. The GOLD aggregate line plus native
GOLD inventory supports 74 organisms, 5 projects, and 3 analyses.

BacDive and the raw culture-collection table support 29 exact BacDive strains
and 29 exact collection rows; the generated YAML expands those into 45 culture
collection identifiers. StrainInfo contributes 4 assembly rows, 91 related
records, and 34 direct strain rows with 61 deposits.

## Completeness

The 3762-line YAML carries all exact local BacDive, culture collection, GOLD,
GTDB, LPSN, MADIN, NCBITaxon, and StrainInfo evidence summarized by the
bounded scan for `NCBITaxon:1015`.

No BactoTraits, MediaDive, GTDB species, NCBI merge, retained retired NCBI row,
StrainInfo exclusion row, or causal graph is filed for this exact target, so
those empty sections are consistent with the inspected source inventories.

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
Two GTDB broad matches are expected for this species.
The LPSN correct-name row is retained as one nomenclature entry.
The LPSN row also contributes the `GTDB:s__Bergeyella_zoohelcum` xref.
The second xref is `lpsn:774016`.
The BacDive source attestation covers 29 strains.
The GOLD source attestation covers the 74-organism aggregate row.
The GTDB source attestation covers eight genomes and points to the extra broad match.
The MADIN source attestation covers five trait assertions.
The NCBITaxon source attestation covers the accepted name and NCBI synonyms.
The LPSN source attestation covers the correct-name nomenclature row.
The counted exact `NCBITaxon:` probe also saw child YAML references that point back to this species.
The ignored report probe included gitignored files.
