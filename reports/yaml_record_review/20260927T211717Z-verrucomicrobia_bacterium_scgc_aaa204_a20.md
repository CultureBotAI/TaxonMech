# YAML Record Review: Verrucomicrobia bacterium SCGC AAA204-A20

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_a20.yaml
- Started UTC: 2026-09-27T21:17:17Z
- Finished UTC: 2026-09-27T21:17:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_a20.yaml` |
| Identifier | `NCBITaxon:1010147` |
| Label | `Verrucomicrobia bacterium SCGC AAA204-A20` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:417295` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified Verrucomicrobiota record,
with path pinned by `data/taxa/PATHS.tsv:3489`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_a20.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_a20.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_a21.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_b02.yaml data/taxa/bacteria/verrucomicrobia_bacterium_scgc_aaa204_b08.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 45 YAML lines, 7 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010147` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212091`, 7 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010147` resolves to `Verrucomicrobia bacterium SCGC AAA204-A20`, rank `SPECIES`,
parent `NCBITaxon:417295`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 7 committed NCBI rows, ending at
`NCBITaxon:417295` unclassified Verrucomicrobiota. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the SCGC AAA204-A20 species identity, unclassified
Verrucomicrobiota parent, genetic code, single NCBITAXON source attestation, and
2026-09-13 snapshot date. The seed event is supported by `curation/seed_scope.tsv:312692`.

Native GOLD side tables carry organism `Go0044569`, project `Gp0044569`, and
one analysis linked to that project; there is still no retained GOLD aggregate,
BacDive, LPSN, GTDB, MediaDive, MADIN, BactoTraits, NCBI type-material,
StrainInfo, culture-collection, normalized strain, or normalized genome row.

## Completeness

No GOLD aggregate or normalized genome/strain row was retained for this exact
NCBI taxon, even though native GOLD side tables have one organism/project/analysis
chain. No BacDive, LPSN, MediaDive, MADIN, BactoTraits, type-material, or StrainInfo
row was filed under this exact taxon.

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
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
No NCBI synonym was present; no `taxonomy_mappings` section is expected.
No xref section is expected.
A native GOLD organism, project, and analysis row were side evidence only.
No retained GOLD aggregate row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Seven NCBI lineage rows are expected.
The seven-line lineage reaches only the unclassified Verrucomicrobiota parent.
The 45-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
