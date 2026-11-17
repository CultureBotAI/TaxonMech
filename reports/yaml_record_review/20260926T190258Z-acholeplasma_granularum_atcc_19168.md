# YAML Record Review: Acholeplasma granularum ATCC 19168

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml
- Started UTC: 2026-09-26T19:02:58Z
- Finished UTC: 2026-09-26T19:02:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml` |
| Identifier | `NCBITaxon:1278304` |
| Label | `Acholeplasma granularum ATCC 19168` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:264635` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:95839`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_equirhinis.yaml data/taxa/bacteria/acholeplasma_granularum.yaml data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml data/taxa/bacteria/acholeplasma_hippikon.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 638 YAML lines, 10 lineage entries, 4 source attestations, 0 nomenclature entries, 1 GTDB `skos:closeMatch` mapping, 2 synonyms, 1 xref, 1 BacDive strain, 8 genome assemblies, 6 genome records, 23 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, GTDB, Madin, BacDive, GOLD, NCBI Assembly, BV-BRC, AllTheBacteria, strain-normalization, and generated YAML rows, and found the `NCBITaxon:264635` species-scoped StrainInfo rows that contextualize the strain; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:298249`, 10 checked lineage entries with no missing rows or mismatches, 1 BacDive strain row, 4 culture-collection rows, 7 raw assembly rows, 5 raw genome rows, 13 raw related rows, 1 GOLD organism/project/analysis set, 1 GTDB mapping row, 1 Madin row, 0 NCBI merge rows, and 0 direct LPSN, StrainInfo, BactoTraits, or MediaDive target rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1278304` resolves in the committed NCBI inventory to label
`Acholeplasma granularum ATCC 19168`, rank `STRAIN`, parent
`NCBITaxon:264635`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:264635` Acholeplasma
granularum. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1278304`, source label `Acholeplasma granularum ATCC 19168`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB mapping to `GTDB:s__Acholeplasma_granularum`, BacDive `168827`, 4
normalized culture collection rows, GOLD organism `Go0018661`, GOLD project
`Gp0018661`, GOLD analysis `Ga0001277`, and the Madin row all support the
single ATCC 19168 strain payload.

The record's 8 assemblies, 6 genome records, and 23 related records are
supported by the 7 raw assembly rows, 5 raw genome rows, 13 raw related rows,
the AllTheBacteria `atb.assembly:202505.SAMN02584924` link, and the 10
species-scoped StrainInfo related records for the ATCC 19168 type strain.

The seed event is supported by `curation/seed_scope.tsv:22413`, which records
`NCBITaxon:1278304` as added on `2026-09-12` with reason `attested rule:
Acholeplasma granularum ATCC 19168, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, GTDB, BacDive,
GOLD, NCBI Assembly, BV-BRC, AllTheBacteria, Madin, StrainInfo, and
strain-normalization inputs, and found no NCBI merge, direct LPSN,
type-material, BactoTraits, MediaDive, or direct StrainInfo target row that
would require another YAML section.

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
