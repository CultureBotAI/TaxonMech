# YAML Record Review: alpha proteobacterium SCGC AAA536-B06

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/alpha_proteobacterium_scgc_aaa536_b06.yaml
- Started UTC: 2026-09-27T16:40:50Z
- Finished UTC: 2026-09-27T16:40:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/alpha_proteobacterium_scgc_aaa536_b06.yaml` |
| Identifier | `NCBITaxon:1009707` |
| Label | `alpha proteobacterium SCGC AAA536-B06` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:33807` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Alphaproteobacteria unclassified record,
with path pinned by `data/taxa/PATHS.tsv:3197`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/alpha_proteobacterium_scgc_aaa536_b06.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_trissolcus_grandis.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_trissolcus_simoni.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_trissolcus_rufiventris.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa536_b06.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 45 YAML lines, 7 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009707` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211800`, 7 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009707` resolves to `alpha proteobacterium SCGC AAA536-B06`,
rank `SPECIES`, parent `NCBITaxon:33807`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 7 committed NCBI rows, ending at
`NCBITaxon:33807` unclassified Alphaproteobacteria. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank SCGC AAA536-B06 identity, direct
unclassified-Alphaproteobacteria parent, genetic code, single NCBITAXON source
attestation, and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:312417`.

Native GOLD has side evidence for `Go0012897`: organism line 11365, project
`Gp0012897` at project line 11227, and analysis line 16633. No GOLD aggregate,
assembly, genome, or strain row was retained for the generated YAML.

## Completeness

Native GOLD side rows exist for this exact NCBI taxon, but no GOLD aggregate or
normalized genome/strain row was retained.
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
No NCBI synonym was present to materialize.
No `taxonomy_mappings` section is expected.
No xref section is expected.
Native GOLD side rows do not currently materialize on the generated target.
No retained GOLD aggregate row is filed on this target.
No normalized assembly row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Seven NCBI lineage rows are expected.
The 45-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
