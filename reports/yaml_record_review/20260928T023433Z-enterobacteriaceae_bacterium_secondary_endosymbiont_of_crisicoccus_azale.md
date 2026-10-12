# YAML Record Review: Enterobacteriaceae bacterium secondary endosymbiont of Crisicoccus azaleae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/enterobacteriaceae_bacterium_secondary_endosymbiont_of_crisicoccus_azale.yaml
- Started UTC: 2026-09-28T02:34:33Z
- Finished UTC: 2026-09-28T02:34:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/enterobacteriaceae_bacterium_secondary_endosymbiont_of_crisicoccus_azale.yaml` |
| Identifier | `NCBITaxon:1010661` |
| Label | `Enterobacteriaceae bacterium secondary endosymbiont of Crisicoccus azaleae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:36866` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only unclassified Enterobacteriaceae record,
with path pinned by `data/taxa/PATHS.tsv:3808`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/enterobacteriaceae_bacterium_secondary_endosymbiont_of_crisicoccus_azale.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_nrs_1186.yaml data/taxa/bacteria/enterobacteriaceae_bacterium_secondary_endosymbiont_of_crisicoccus_azale.yaml data/taxa/bacteria/enterobacteriaceae_bacterium_nsa.yaml data/taxa/bacteria/bacillus_sp_nrs_1198.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 52 YAML lines, 9 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010661` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212374`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010661` resolves to
`Enterobacteriaceae bacterium secondary endosymbiont of Crisicoccus azaleae`,
rank `SPECIES`, parent `NCBITaxon:36866`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:36866` unclassified Enterobacteriaceae. No NCBI merge row was retained.

## Evidence

The NCBI row supports the Enterobacteriaceae bacterium secondary endosymbiont
of Crisicoccus azaleae species identity, unclassified Enterobacteriaceae parent,
genetic code, single NCBITAXON source attestation, and the 2026-09-13 snapshot date.

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
The nine-line lineage reaches the unclassified Enterobacteriaceae parent.
The 52-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
