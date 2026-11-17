# YAML Record Review: Acholeplasma hippikon

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_hippikon.yaml
- Started UTC: 2026-09-26T19:02:58Z
- Finished UTC: 2026-09-26T19:02:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_hippikon.yaml` |
| Identifier | `NCBITaxon:264636` |
| Label | `Acholeplasma hippikon` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:358966`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_hippikon.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_equirhinis.yaml data/taxa/bacteria/acholeplasma_granularum.yaml data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml data/taxa/bacteria/acholeplasma_hippikon.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 841 YAML lines, 9 lineage entries, 5 source attestations, 1 nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 1 synonym, 2 xrefs, 1 BacDive type strain, 14 genome assemblies, 11 genome records, 36 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or its `NCBITaxon:1408416` strain child in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, GTDB, Madin, BacDive, GOLD, NCBI Assembly, BV-BRC, StrainInfo, strain-normalization, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:54106`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:21369`, 1 species-level GTDB mapping row, 1 exact BacDive hit for the ATCC 29725/NCTC 10172 type-strain payload, 1 GOLD organism/project/analysis set, 1 direct StrainInfo strain with 2 deposits, 6 NCBI type-material designations, 2 StrainInfo assembly rows, 6 StrainInfo related rows, 0 NCBI merge rows, and 0 BactoTraits or MediaDive rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:264636` resolves in the committed NCBI inventory to label
`Acholeplasma hippikon`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:264636`, source label `Acholeplasma hippikon`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The nomenclature block is backed by `lpsn:783253`, a legitimate, validly
published LPSN species row whose type strains are `ATCC-29725` and
`NCTC-10172`. The GTDB mapping to `GTDB:s__Acholeplasma_hippikon` is the
committed species-level `skos:closeMatch` row with `genome_count: 2`.

The BacDive `167814` strain block is classified as `NCBITaxon:1408416` and
combines the ATCC 29725 child rows with the NCTC 10172 species-scoped rows.
The 14 assemblies are backed by 8 child assembly rows, 4 species-level raw
assembly rows, and 2 StrainInfo assembly rows; the 11 genome records by 6 child
rows and 5 species-level rows; and the 36 related records by 18 child rows, 12
species-level rows, and 6 StrainInfo rows.

The seed event is supported by `curation/seed_scope.tsv:23970`, which records
`NCBITaxon:264636` as added on `2026-09-12` with reason `attested rule:
Acholeplasma hippikon, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, GTDB,
BacDive, GOLD, NCBI Assembly, BV-BRC, StrainInfo, Madin, strain-normalization,
and type-material inputs, and found no NCBI merge, BactoTraits, MediaDive, or
AllTheBacteria row that would require another YAML section.

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
