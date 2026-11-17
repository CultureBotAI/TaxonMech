# YAML Record Review: Acholeplasma brassicae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_brassicae.yaml
- Started UTC: 2026-09-26T18:59:00Z
- Finished UTC: 2026-09-26T18:59:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_brassicae.yaml` |
| Identifier | `NCBITaxon:61635` |
| Label | `Acholeplasma brassicae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:552051`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_brassicae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_brassicae.yaml data/taxa/bacteria/acholeplasma_brassicae_0502.yaml data/taxa/bacteria/acholeplasma_equifetale.yaml data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 324 YAML lines, 9 lineage entries, 5 source attestations, 1 nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 4 synonyms, 2 xrefs, 1 BacDive strain, 1 GOLD genome assembly, 1 GOLD genome record, 10 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or its `NCBITaxon:1318465` strain child in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, GTDB, Madin, BacDive, GOLD, StrainInfo, strain-normalization, and generated YAML rows; found no unexpected duplicate generated record. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:7806`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:21363`, 1 GTDB mapping row, 1 Madin row, 1 exact BacDive hit for the `0502` type strain, 1 direct StrainInfo strain with 1 deposit, 5 NCBI type-material designations, 6 StrainInfo related rows, 0 NCBI merge rows, and 0 BactoTraits or MediaDive rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:61635` resolves in the committed NCBI inventory to label
`Acholeplasma brassicae`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:61635`, source label `Acholeplasma brassicae`, `assertion_count: 1`,
`assertion_unit: NAME`, and the 2026-09-13 snapshot note all match.

The nomenclature block is backed by `lpsn:783247`, a legitimate, validly
published LPSN species row whose type strain is `kgmicrobe.strain:ATCC-49388`.
The GTDB mapping to `GTDB:s__Paracholeplasma_brassicae` is the committed
`skos:closeMatch` row with `genome_count: 5`, and the `Paracholeplasma
brassicae` exact synonym comes from that GTDB label.

The single strain block represents BacDive `167887`, designation `0502`,
culture collection `kgmicrobe.strain:ATCC-49388`, and `classified_as:
NCBITaxon:1318465`. Its GOLD assembly, GOLD genome record, 4 GOLD related
records, and 6 StrainInfo related records are supported by the exact source
rows for the strain child. NCBI type-material and StrainInfo both identify
`ATCC 49388` as type material for `Acholeplasma brassicae`.

The seed event is supported by `curation/seed_scope.tsv:23490`, which records
`NCBITaxon:61635` as added on `2026-09-12` with reason `attested rule:
Acholeplasma brassicae, 4 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, GTDB, BacDive,
GOLD, StrainInfo, Madin, strain-normalization, and type-material inputs, and
found no NCBI merge, direct native GOLD target, BactoTraits, MediaDive, or
extra direct strain rows for the species taxon that would require another
YAML section.

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
