# YAML Record Review: Candidatus Spencerbrownia rhizoecinicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_spencerbrownia_rhizoecinicola.yaml
- Started UTC: 2026-09-28T02:43:38Z
- Finished UTC: 2026-09-28T02:43:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/candidatus_spencerbrownia_rhizoecinicola.yaml` |
| Identifier | `NCBITaxon:1010684` |
| Label | `Candidatus Spencerbrownia rhizoecinicola` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1010679` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Candidatus Spencerbrownia species record,
with path pinned by `data/taxa/PATHS.tsv:3816`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_spencerbrownia_rhizoecinicola.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/pediococcus_sp_siga1.yaml data/taxa/bacteria/candidatus_spencerbrownia_rhizoecinicola.yaml data/taxa/bacteria/microcystis_aeruginosa_lnsamb.yaml data/taxa/bacteria/burkholderia_sp_l5p11.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 68 YAML lines, 11 lineage entries, 3 NCBI synonyms, 1 NCBITAXON source attestation, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010684` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212381`, 11 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 0 NCBI type-material rows, 0 GOLD aggregate rows, no native GOLD organism, project, or analysis rows, no BacDive rows, no LPSN, GTDB, MediaDive, MADIN, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010684` resolves to `Candidatus Spencerbrownia rhizoecinicola`,
rank `SPECIES`, parent `NCBITaxon:1010679`, genetic code `11`, source set
`ncbitaxon`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:1010679` genus `Candidatus Spencerbrownia`; no NCBI merge row was retained.

## Evidence

The NCBI row supports the Candidatus Spencerbrownia rhizoecinicola species
identity, genus parent, genetic code, 2 exact synonyms, 1 related synonym,
single NCBITAXON source attestation, and the 2026-09-13 snapshot date.

No LPSN, GTDB, GOLD aggregate, native GOLD organism/project/analysis, BacDive,
MediaDive, MADIN, BactoTraits, NCBI type-material, StrainInfo,
culture-collection, normalized assembly, normalized genome, or normalized
related-record row is filed.

## Completeness

No `taxonomy_mappings`, xref, LPSN nomenclature, strain, genome assembly,
genome record, related-record, definition, or causal-graph row is expected
from the bounded source inventory.

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
The three synonyms all come from NCBITaxon.
No GTDB mapping is filed on this target.
No native GOLD organism, project, or analysis row was filed.
No retained GOLD aggregate row is filed on this target.
No BacDive row is filed under the exact NCBI species.
No StrainInfo row is filed under the exact NCBI species.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The eleven-line lineage reaches the Candidatus Spencerbrownia genus.
The 68-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
