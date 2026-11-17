# YAML Record Review: Acholeplasma granularum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_granularum.yaml
- Started UTC: 2026-09-26T19:02:58Z
- Finished UTC: 2026-09-26T19:02:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_granularum.yaml` |
| Identifier | `NCBITaxon:264635` |
| Label | `Acholeplasma granularum` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:358965`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_granularum.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_equirhinis.yaml data/taxa/bacteria/acholeplasma_granularum.yaml data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml data/taxa/bacteria/acholeplasma_hippikon.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 662 YAML lines, 9 lineage entries, 4 source attestations, 1 nomenclature entry, 0 taxonomy mappings, 4 synonyms, 2 xrefs, 1 BacDive type strain, 8 genome assemblies, 6 genome records, 23 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or its `NCBITaxon:1278304` strain child in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, BacDive, GOLD, GTDB, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, strain-normalization, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:54105`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:21368`, 2 native GOLD organisms for the species taxon, 1 exact BacDive hit for the ATCC 19168 child, 2 direct StrainInfo strains with 5 deposits, 8 NCBI type-material designations, 1 StrainInfo assembly row, 10 StrainInfo related rows, 0 NCBI merge rows, and 0 BactoTraits or MediaDive rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:264635` resolves in the committed NCBI inventory to label
`Acholeplasma granularum`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:264635`, source label `Acholeplasma granularum`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The nomenclature block is backed by `lpsn:783252`, a legitimate, validly
published LPSN species row whose type strains are `ATCC-19168`, `IFO-14847`,
`NBRC-14847`, and `NCTC-10128`. The 4 synonyms come from the committed NCBI
row, including the exact `Mycoplasma granularum` and `Sapromyces granularum`
synonyms.

The BacDive `168827` strain block is classified as `NCBITaxon:1278304` and is
supported by the child rows for 7 raw assemblies, 5 raw genome records, 13 raw
related records, and a GOLD organism/project/analysis set. The eighth assembly
and 10 related records come from species-scoped StrainInfo rows, and the sixth
genome record is the AllTheBacteria `atb.assembly:202505.SAMN02584924` row
linked through `kgmicrobe.strain:bacdive_168827`.

The seed event is supported by `curation/seed_scope.tsv:32121`, which records
`NCBITaxon:264635` as added on `2026-09-12` with reason `attested rule:
Acholeplasma granularum, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, BacDive,
GOLD, GTDB, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo,
strain-normalization, and type-material inputs, and found no NCBI merge,
species-level GTDB mapping, Madin, BactoTraits, or MediaDive row that would
require another YAML section.

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
