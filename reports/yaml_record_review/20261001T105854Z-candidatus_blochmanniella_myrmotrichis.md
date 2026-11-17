# YAML Record Review: Candidatus Blochmanniella myrmotrichis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_blochmanniella_myrmotrichis.yaml
- Started UTC: 2026-10-01T10:58:54Z
- Finished UTC: 2026-10-01T10:58:54Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/candidatus_blochmanniella_myrmotrichis.yaml` |
| Identifier | `NCBITaxon:101533` |
| Label | `Candidatus Blochmanniella myrmotrichis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:203804` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon-only Candidatus Blochmanniella record,
with path pinned by `data/taxa/PATHS.tsv:8582`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_blochmanniella_myrmotrichis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict <4 exact YAML paths>` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 76 YAML lines, 12 lineage entries, 1 NCBITAXON source attestation, 5 NCBITaxon synonyms, 0 nomenclature entries, 0 taxonomy mappings, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact local scans | Found `NCBITaxon:101533` in the expected seed, target NCBI, descendant NCBI/YAML, target YAML, and `data/taxa/PATHS.tsv` rows; found no exact GTDB mapping, and the ignored-file-inclusive report probe found no prior report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:17594`, 12 checked lineage entries with no missing rows or mismatches, no native GOLD organism, project, or analysis rows, 0 GOLD aggregate rows, 0 NCBI merge rows, 0 NCBI type-material rows, no BacDive rows, no auxiliary rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:101533` resolves to `Candidatus Blochmanniella myrmotrichis`, rank `SPECIES`,
parent `NCBITaxon:203804`, genetic code `11`, source set `ncbitaxon`,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 12 committed NCBI rows, ending at
`NCBITaxon:203804` Candidatus Blochmanniella. The bounded scan found no
NCBI merge row and no retained old-id row.

## Evidence

The NCBI row supports the Candidatus Blochmanniella myrmotrichis identity,
Candidatus Blochmanniella parent, five NCBI synonyms, genetic code,
NCBITAXON source attestation, and 2026-09-13 snapshot date.

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
The rank is the NCBI retained rank for this Candidatus Blochmanniella record.
The parent is NCBI's Candidatus Blochmanniella genus.
Five NCBI synonyms were present; no `taxonomy_mappings` section is expected.
No GTDB row is expected for this exact Candidatus target.
No NCBI type-material row is available to mint side-only strain evidence.
No NCBI merge row complicates identity.
Twelve NCBI lineage rows are expected.
The twelve-line lineage reaches Candidatus Blochmanniella.
The 76-line YAML shape omits all non-NCBI sections.
The bounded scan found no native GOLD evidence.
The record has no MADIN row.
The source set is just `ncbitaxon`.
The exact `NCBITaxon:` probe found no GTDB mapping.
The ignored report probe included gitignored files.
