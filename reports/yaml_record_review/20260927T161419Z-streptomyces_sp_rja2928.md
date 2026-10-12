# YAML Record Review: Streptomyces sp. RJA2928

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptomyces_sp_rja2928.yaml
- Started UTC: 2026-09-27T16:14:19Z
- Finished UTC: 2026-09-27T16:14:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/streptomyces_sp_rja2928.yaml` |
| Identifier | `NCBITaxon:1009461` |
| Label | `Streptomyces sp. RJA2928` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2593676` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Streptomyces unclassified record, with
path pinned by `data/taxa/PATHS.tsv:3170`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/streptomyces_sp_rja2928.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/pseudonocardia_sp_ass1.yaml data/taxa/bacteria/leptolyngbya_sp_rs03.yaml data/taxa/bacteria/streptomyces_sp_rja2928.yaml data/taxa/bacteria/streptomyces_sp_rja2961.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 54 YAML lines, 10 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009461` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211774`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, 1 native GOLD organism and project row, no native GOLD analysis row, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009461` resolves to `Streptomyces sp. RJA2928`, rank `SPECIES`,
parent `NCBITaxon:2593676`, genetic code `11`, source set `ncbitaxon`, and
taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:2593676` unclassified Streptomyces. The bounded scan found no NCBI
merge row and no retained old-id row.

## Evidence

The NCBI row supports the species-rank RJA2928 identity, direct
unclassified-Streptomyces parent, genetic code, single NCBITAXON source
attestation, and 2026-09-13 snapshot date. The seed event is supported by
`curation/seed_scope.tsv:312393`.

No LPSN, GTDB, GOLD aggregate, BacDive, MediaDive, MADIN, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly, normalized
genome, or normalized related-record row is filed; native GOLD rows are side
evidence only.

## Completeness

Native GOLD rows for `Go0098940` / `Gp0098940` are side evidence only: no GOLD
aggregate or normalized genome/strain row was retained, and no BacDive, LPSN,
MediaDive, MADIN, BactoTraits, type-material, or StrainInfo row was filed under
this exact taxon.

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
Native GOLD rows were side evidence only.
No native GOLD analysis row is filed on this target.
No retained GOLD aggregate row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Ten NCBI lineage rows are expected.
The 54-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
