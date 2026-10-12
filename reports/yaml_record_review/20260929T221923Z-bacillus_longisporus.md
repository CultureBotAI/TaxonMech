# YAML Record Review: Bacillus longisporus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bacillus_longisporus.yaml
- Started UTC: 2026-09-29T22:19:23Z
- Finished UTC: 2026-09-29T22:19:23Z
- Verdict: pass-with-findings

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/bacillus_longisporus.yaml` |
| Identifier | `NCBITaxon:101332` |
| Label | `Bacillus longisporus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1386` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon Bacillus species record with an NCBI exact synonym,
with path pinned by `data/taxa/PATHS.tsv:6486`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bacillus_longisporus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 54 YAML lines, 9 lineage entries, 1 NCBITAXON source attestation, 1 exact NCBI synonym, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101332` in the expected seed, NCBI, YAML, and `data/taxa/PATHS.tsv` rows, plus 3 exact StrainInfo links and references from `uncultured_bacillus_sp`; the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17507`, 9 checked lineage entries with no missing rows or mismatches, 8 direct StrainInfo rows, 18 StrainInfo deposits, 6 normalized related-record rows, no native GOLD organism, project, or analysis rows, 0 GOLD aggregate rows, 0 NCBI merge rows, 0 NCBI type-material rows, and no BacDive rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101332` resolves to `Bacillus longisporus`, rank `SPECIES`,
parent `NCBITaxon:1386`, genetic code `11`, source set `ncbitaxon`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:1386` Bacillus. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the Bacillus longisporus identity, genus parent,
exact synonym, genetic code, NCBITAXON source attestation, and
2026-09-13 snapshot date.

Exact StrainInfo rows exist for this taxon even though no exact BacDive,
culture-collection, strain-assembly, or strain-genome row is filed.

## Completeness

No MADIN, BacDive, LPSN, GTDB, GOLD, MediaDive, BactoTraits, NCBI
type-material, culture-collection, normalized assembly, or normalized
genome row is filed directly for the exact target.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

## Findings

- Major: Exact StrainInfo evidence is not represented in the YAML.

The bounded scan found 8 direct StrainInfo strains, 18 deposits, and 6
normalized related-record rows for `NCBITaxon:101332`, while the YAML has
`strain_count: 0`, no `strains`, and no `related_records`.

## Recommended Edits

Regenerate or extend this record so exact StrainInfo strains/deposits are
represented instead of leaving the record as NCBITaxon-only.

## Follow-up Checks

After regeneration, rerun `just validate`, `just validate-strict`, and exact
StrainInfo target scans for `NCBITaxon:101332`.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
The rank is the NCBI retained rank for this Bacillus species record.
The parent is the Bacillus genus `NCBITaxon:1386`.
One NCBI exact synonym is present and mirrors NCBI's quoted spelling.
No taxonomy mapping section is expected from the local rows.
No GTDB row is expected for this exact target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The nine-line lineage reaches Bacillus.
The 54-line YAML shape omits StrainInfo-derived sections.
Six normalized StrainInfo related rows were available.
The source set is just `ncbitaxon`.
The ignored report probe included gitignored files.
