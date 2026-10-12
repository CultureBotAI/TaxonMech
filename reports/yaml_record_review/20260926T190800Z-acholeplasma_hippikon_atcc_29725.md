# YAML Record Review: Acholeplasma hippikon ATCC 29725

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml
- Started UTC: 2026-09-26T19:08:00Z
- Finished UTC: 2026-09-26T19:08:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml` |
| Identifier | `NCBITaxon:1408416` |
| Label | `Acholeplasma hippikon ATCC 29725` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:264636` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:148762`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml data/taxa/bacteria/acholeplasma_laidlawii.yaml data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml data/taxa/bacteria/acholeplasma_oculi.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 814 YAML lines, 10 lineage entries, 4 source attestations, 1 GTDB `skos:closeMatch` mapping, 1 GTDB exact synonym, 1 xref, 1 BacDive strain, 2 culture collection IDs, 14 genome assemblies, 11 genome records, 36 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, GTDB, Madin, BacDive, GOLD, NCBI Assembly, BV-BRC, strain-normalization, and generated YAML rows, and found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:347501`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB mapping row, 1 Madin row, 1 BacDive row, 2 culture-collection rows, 8 raw assembly rows, 6 raw genome rows, 18 raw related rows, 1 native GOLD organism/project/analysis set, 0 NCBI merge rows, and 0 direct LPSN, StrainInfo, BactoTraits, or MediaDive target rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1408416` resolves in the committed NCBI inventory to label
`Acholeplasma hippikon ATCC 29725`, rank `STRAIN`, parent
`NCBITaxon:264636`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:264636` Acholeplasma
hippikon. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1408416`, source label `Acholeplasma hippikon ATCC 29725`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB mapping to `GTDB:s__Acholeplasma_hippikon`, BacDive `167814`, 2
normalized culture collection rows, GOLD organism `Go0018831`, GOLD project
`Gp0018831`, GOLD analysis `Ga0005300`, and the Madin row all support the
ATCC 29725 strain payload.

The record's BacDive block is rooted in the exact `NCBITaxon:1408416` ATCC
29725 rows and also folds in species-scoped NCTC 10172 and StrainInfo evidence
through the same BacDive `167814` culture-identifier set. The 14 assemblies,
11 genome records, and 36 related records are backed by the raw BacDive, GOLD,
GTDB, NCBI Assembly, BV-BRC, and species-scoped StrainInfo rows checked above.

The seed event is supported by `curation/seed_scope.tsv:22560`, which records
`NCBITaxon:1408416` as added on `2026-09-12` with reason `attested rule:
Acholeplasma hippikon ATCC 29725, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, GTDB, BacDive,
GOLD, NCBI Assembly, BV-BRC, Madin, StrainInfo, and strain-normalization
inputs, and found no NCBI merge, direct LPSN, direct StrainInfo, BactoTraits,
MediaDive, or AllTheBacteria row that would require another YAML section.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

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

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
