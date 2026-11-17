# YAML Record Review: Acholeplasma equirhinis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_equirhinis.yaml
- Started UTC: 2026-09-26T19:02:58Z
- Finished UTC: 2026-09-26T19:02:58Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_equirhinis.yaml` |
| Identifier | `NCBITaxon:555393` |
| Label | `Acholeplasma equirhinis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:538988`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_equirhinis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_equirhinis.yaml data/taxa/bacteria/acholeplasma_granularum.yaml data/taxa/bacteria/acholeplasma_granularum_atcc_19168.yaml data/taxa/bacteria/acholeplasma_hippikon.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 260 YAML lines, 9 lineage entries, 6 source attestations, 1 nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 2 synonyms, 2 xrefs, 1 BacDive type strain, 1 BacDive genome assembly, 2 BacDive genome records, 8 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, GTDB, MediaDive, BacDive, GOLD, StrainInfo, strain-normalization, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:130272`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:199`, 1 GTDB mapping row, 1 MediaDive row, 1 BacDive strain row, 3 culture-collection rows, 1 assembly row, 2 genome rows, 6 GOLD related rows, 2 StrainInfo related rows, 8 NCBI type-material designations, 0 NCBI merge rows, and 0 BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:555393` resolves in the committed NCBI inventory to label
`Acholeplasma equirhinis`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:555393`, source label `Acholeplasma equirhinis`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The nomenclature block is backed by `lpsn:3395`, a legitimate, validly
published LPSN species row whose type strains are `ATCC-TSD-139`,
`DSM-106692`, and `NCTC-14351`. The GTDB mapping to
`GTDB:s__Acholeplasma_equirhinis` is the committed `skos:closeMatch` row with
`genome_count: 1`, and `data/raw/mediadive_taxa.tsv:11470` supplies the
MediaDive medium assertion.

BacDive `159212`, designation `N93`, the 3 normalized culture collection rows,
the single BacDive assembly, and the 2 BacDive genome records all target
`NCBITaxon:555393` directly. The 8 related records are the expected 6 GOLD
organism links plus 2 StrainInfo links for `DSM 106692`.

The seed event is supported by `curation/seed_scope.tsv:10201`, which records
`NCBITaxon:555393` as added on `2026-09-12` with reason `attested rule:
Acholeplasma equirhinis, 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, GTDB,
MediaDive, BacDive, GOLD, StrainInfo, strain-normalization, and type-material
inputs, and found no NCBI merge, Madin, BactoTraits, extra assembly, or extra
direct StrainInfo assembly row that would require another YAML section.

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
