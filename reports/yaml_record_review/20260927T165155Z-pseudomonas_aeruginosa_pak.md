# YAML Record Review: Pseudomonas aeruginosa PAK

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_aeruginosa_pak.yaml
- Started UTC: 2026-09-27T16:51:55Z
- Finished UTC: 2026-09-27T16:51:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/pseudomonas_aeruginosa_pak.yaml` |
| Identifier | `NCBITaxon:1009714` |
| Label | `Pseudomonas aeruginosa PAK` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:287` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Pseudomonas aeruginosa strain record with NCBI, GOLD,
GTDB, and MADIN support, with path pinned by `data/taxa/PATHS.tsv:3204`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_aeruginosa_pak.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/flavobacterium_sp_scgc_aaa536_p05.yaml data/taxa/bacteria/flavobacterium_sp_scgc_aaa536_g18.yaml data/taxa/bacteria/pseudomonas_aeruginosa_pak.yaml data/taxa/bacteria/gracilibacillus_sp_hva_1.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 92 YAML lines, 11 lineage entries, 4 source attestations, 3 synonyms, 0 nomenclature entries, 1 taxonomy mapping, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009714` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, generated target YAML, and 1 GTDB mapping row; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211807`, 1 GTDB row, 1 GOLD aggregate row, 1 MADIN row, 2 native GOLD organism/project/analysis rows, 11 checked lineage entries with no mismatches, 0 NCBI merge rows, no BacDive, LPSN, MediaDive, or BactoTraits rows, and no normalized strain or StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009714` resolves to `Pseudomonas aeruginosa PAK`, rank `STRAIN`,
parent `NCBITaxon:287`, genetic code `11`, source set
`ncbitaxon|gtdb|gold|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 11 committed NCBI rows, ending at
`NCBITaxon:287` Pseudomonas aeruginosa. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the PAK strain identity, parent, genetic code, two
NCBI exact synonyms, and source set. `curation/seed_scope.tsv:26040` records the
4-source seed event for this target.

GTDB row `data/raw/gtdb_mappings.tsv:1131` supports the closeMatch, xref, and
GTDB exact synonym. GOLD aggregate line 210 and MADIN line 404 support the
GOLD and MADIN attestations. Native GOLD has two organism/project/analysis rows.

## Completeness

The retained GOLD aggregate, GTDB, MADIN, NCBI synonym, and native GOLD rows are
consistent with the generated YAML. No BacDive, LPSN, MediaDive, BactoTraits,
normalized assembly, normalized genome, normalized strain, or StrainInfo row
was filed under this exact taxon.

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
One GTDB closeMatch and xref are expected.
Three exact synonyms are expected.
The GOLD aggregate row is retained on this target.
The MADIN trait assertion row is retained on this target.
No native GOLD genome row materializes on the generated target.
No normalized assembly row is filed on this target.
No normalized genome row is filed on this target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Eleven NCBI lineage rows are expected.
The 92-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
