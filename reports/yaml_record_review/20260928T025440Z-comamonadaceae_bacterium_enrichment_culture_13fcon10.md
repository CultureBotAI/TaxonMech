# YAML Record Review: Comamonadaceae bacterium enrichment culture 13Fcon10

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/comamonadaceae_bacterium_enrichment_culture_13fcon10.yaml
- Started UTC: 2026-09-28T02:54:40Z
- Finished UTC: 2026-09-28T02:54:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/comamonadaceae_bacterium_enrichment_culture_13fcon10.yaml` |
| Identifier | `NCBITaxon:1010717` |
| Label | `Comamonadaceae bacterium enrichment culture 13Fcon10` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:128082` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only environmental Comamonadaceae record,
with path pinned by `data/taxa/PATHS.tsv:3825`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/comamonadaceae_bacterium_enrichment_culture_13fcon10.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_nrs_1692.yaml data/taxa/bacteria/chloroflexi_bacterium_enrichment_culture_13scon79.yaml data/taxa/bacteria/comamonadaceae_bacterium_enrichment_culture_13fcon10.yaml data/taxa/bacteria/comamonadaceae_bacterium_enrichment_culture_13fcon25.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 51 YAML lines, 9 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010717` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212387`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010717` resolves to `Comamonadaceae bacterium enrichment culture
13Fcon10`, rank `SPECIES`, parent `NCBITaxon:128082`, genetic code `11`,
source set `ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:128082` Comamonadaceae environmental samples. The bounded scan
found no NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the enrichment-culture Comamonadaceae identity,
environmental-samples parent, genetic code, single NCBITAXON source
attestation, and 2026-09-13 snapshot date.

No LPSN, GTDB, GOLD aggregate, native GOLD organism/project/analysis, BacDive,
MediaDive, MADIN, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or normalized
related-record row is filed.

## Completeness

No native GOLD organism, project, or analysis rows were found for this exact
NCBI taxon, and no GOLD aggregate or normalized genome/strain row was retained.
No BacDive, LPSN, MediaDive, MADIN, BactoTraits, type-material, or StrainInfo
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
No native GOLD organism, project, or analysis row was filed.
No retained GOLD aggregate row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Nine NCBI lineage rows are expected.
The lineage reaches the Comamonadaceae environmental-samples parent.
The 51-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
