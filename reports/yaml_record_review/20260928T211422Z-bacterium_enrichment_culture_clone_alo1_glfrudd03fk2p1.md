# YAML Record Review: bacterium enrichment culture clone ALO1_GLFRUDD03FK2P1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bacterium_enrichment_culture_clone_alo1_glfrudd03fk2p1.yaml
- Started UTC: 2026-09-28T21:14:22Z
- Finished UTC: 2026-09-28T21:14:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/bacterium_enrichment_culture_clone_alo1_glfrudd03fk2p1.yaml` |
| Identifier | `NCBITaxon:1011748` |
| Label | `bacterium enrichment culture clone ALO1_GLFRUDD03FK2P1` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:48479` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only enrichment-culture clone record,
with path pinned by `data/taxa/PATHS.tsv:4868`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bacterium_enrichment_culture_clone_alo1_glfrudd03fk2p1.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 36 YAML lines, 4 lineage entries, 1 NCBITAXON source attestation, 0 synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1011748` in the expected seed, NCBI, and `data/taxa/PATHS.tsv` rows; found no exact GTDB mapping or prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:213386`, 4 checked lineage entries with no missing rows or mismatches, no native GOLD organism, project, or analysis rows, 0 GOLD aggregate rows, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no auxiliary rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1011748` resolves to `bacterium enrichment culture clone ALO1_GLFRUDD03FK2P1`, rank `SPECIES`,
parent `NCBITaxon:48479`, genetic code `11`, source set `ncbitaxon`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 4 committed NCBI rows, ending at
`NCBITaxon:48479` environmental samples. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the enrichment-culture clone identity, environmental
samples parent, genetic code, NCBITAXON source attestation, and 2026-09-13
snapshot date.

No native GOLD organism, project, or analysis rows and no retained GOLD
aggregate row are filed for this exact NCBI taxon.

## Completeness

No MADIN, BacDive, LPSN, GTDB, GOLD, MediaDive, BactoTraits, NCBI
type-material, StrainInfo, culture-collection, normalized assembly,
normalized genome, or exact-target related-record row is filed.

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
`strain_count: 0` is expected without an exact BacDive or normalized strain row.
The rank is the NCBI retained rank for this uncultured clone.
The parent is NCBI's environmental samples grouping.
No NCBI synonym was present; no `taxonomy_mappings` section is expected.
No GTDB row is expected for this placeholder target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Four NCBI lineage rows are expected.
The four-line lineage reaches environmental samples.
The 36-line YAML shape omits all non-NCBI sections.
The bounded scan found no native GOLD evidence.
The record has no MADIN row.
The source set is just `ncbitaxon`.
The exact `NCBITaxon:` probe found no GTDB mapping.
The ignored report probe included gitignored files.
