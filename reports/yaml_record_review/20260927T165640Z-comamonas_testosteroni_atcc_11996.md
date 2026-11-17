# YAML Record Review: Comamonas testosteroni ATCC 11996

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/comamonas_testosteroni_atcc_11996.yaml
- Started UTC: 2026-09-27T16:56:40Z
- Finished UTC: 2026-09-27T16:56:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/comamonas_testosteroni_atcc_11996.yaml` |
| Identifier | `NCBITaxon:1009852` |
| Label | `Comamonas testosteroni ATCC 11996` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:285` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated ATCC 11996 strain record with BacDive, BactoTraits,
GTDB, MADIN, MediaDive, and NCBI support, pinned by `data/taxa/PATHS.tsv:3208`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/comamonas_testosteroni_atcc_11996.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/vibrio_vulnificus_vv.yaml data/taxa/bacteria/burkholderia_cepacia_gg4.yaml data/taxa/bacteria/comamonas_testosteroni_atcc_11996.yaml data/taxa/bacteria/xanthomonas_oryzae_x11_5a.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 2767 YAML lines, 10 lineage entries, 6 source attestations, 6 synonyms, 0 nomenclature entries, 1 taxonomy mapping, 1 xref, 1 strain, 28 genome assemblies, 22 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009852` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and 1 GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211811`, 1 GTDB row, 1 BacDive row, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 10 matching lineage rows, 28 culture-collection rows, 11 exact normalized assemblies, 10 exact genome rows, 26 exact related-record rows, 0 NCBI merge rows, no LPSN row, and no exact StrainInfo target rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009852` resolves to `Comamonas testosteroni ATCC 11996`,
rank `STRAIN`, parent `NCBITaxon:285`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|madin_etal|bactotraits`, and snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:285` Comamonas testosteroni. The bounded scan found no NCBI merge row
and no retained old-id row.

## Evidence

BacDive `2923` is retained as one strain with 28 culture collection IDs and
matches ATCC 11996, NBRC 14951, NCTC 10698, and B337 genome evidence from
BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo.

The exact raw rows support the GTDB closeMatch at line 1133, MediaDive at line
60, MADIN at line 407, BactoTraits at line 43, BacDive at line 2822, and the
6-source seed event at `curation/seed_scope.tsv:10778`.

## Completeness

The retained BacDive strain, GTDB closeMatch, six exact synonyms, 28 assembly
rows, 22 genome rows, and 133 related records are expected for this target.
Native GOLD has organism `Go0011899` with two projects and two analyses; exact
GOLD aggregate rows are absent, but normalized GOLD rows are retained via strain evidence.

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
`strain_count: 1` matches the single BacDive strain row.
The GTDB closeMatch and xref are expected.
Six exact synonyms are expected.
Twenty-eight culture collection IDs are expected.
Twenty-eight genome assembly entries are expected.
No LPSN nomenclature section is expected.
No retained GOLD aggregate row is filed on this target.
Species-level StrainInfo rows are represented in normalized related records.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 2767-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
