# YAML Record Review: Acholeplasma equifetale

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_equifetale.yaml
- Started UTC: 2026-09-26T18:59:00Z
- Finished UTC: 2026-09-26T18:59:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_equifetale.yaml` |
| Identifier | `NCBITaxon:264634` |
| Label | `Acholeplasma equifetale` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:358964`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_equifetale.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_brassicae.yaml data/taxa/bacteria/acholeplasma_brassicae_0502.yaml data/taxa/bacteria/acholeplasma_equifetale.yaml data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 686 YAML lines, 9 lineage entries, 3 source attestations, 1 nomenclature entry, 0 taxonomy mappings, 1 synonym, 2 xrefs, 1 BacDive type strain, 9 genome assemblies, 6 genome records, 29 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier or its `NCBITaxon:1408415` strain child in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, BacDive, GOLD, GTDB, Madin, StrainInfo, strain-normalization, and generated YAML rows; found no unexpected duplicate generated record. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:54104`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:21366`, 1 exact BacDive hit for ATCC 29724/NCTC 10171/DSM 116313, 1 direct StrainInfo strain with 3 deposits, 6 NCBI type-material designations, 1 StrainInfo assembly row, 11 StrainInfo related rows, 0 NCBI merge rows, and 0 BactoTraits or MediaDive rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:264634` resolves in the committed NCBI inventory to label
`Acholeplasma equifetale`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:264634`, source label `Acholeplasma equifetale`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The nomenclature block is backed by `lpsn:783250`, a legitimate, validly
published LPSN species row whose type strains are `kgmicrobe.strain:ATCC-29724`
and `kgmicrobe.strain:NCTC-10171`. BacDive `167728`, designation `C112`, and
normalized culture collection identifiers `ATCC-29724`, `DSM-116313`, and
`NCTC-10171` support the single type-strain block.

The species record also carries the ATCC 29724 child payload: 9 genome
assemblies from BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo; 6
genome records from BacDive, BV-BRC, GOLD, and GTDB; and 29 related records
from BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo. Those records are
supported by exact source rows for `NCBITaxon:1408415` plus the species-scoped
StrainInfo rows for `NCBITaxon:264634`.

The seed event is supported by `curation/seed_scope.tsv:54870`, which records
`NCBITaxon:264634` as added on `2026-09-12` with reason `attested rule:
Acholeplasma equifetale, 2 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, BacDive, GOLD,
GTDB, NCBI Assembly, BV-BRC, StrainInfo, strain-normalization, and
type-material inputs, and found no NCBI merge, direct native GOLD target,
Madin, BactoTraits, MediaDive, or GTDB mapping row for the species taxon that
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
