# YAML Record Review: Acholeplasma equifetale ATCC 29724

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml
- Started UTC: 2026-09-26T18:59:00Z
- Finished UTC: 2026-09-26T18:59:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml` |
| Identifier | `NCBITaxon:1408415` |
| Label | `Acholeplasma equifetale ATCC 29724` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:264634` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:148761`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_brassicae.yaml data/taxa/bacteria/acholeplasma_brassicae_0502.yaml data/taxa/bacteria/acholeplasma_equifetale.yaml data/taxa/bacteria/acholeplasma_equifetale_atcc_29724.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 683 YAML lines, 10 lineage entries, 5 source attestations, 0 nomenclature entries, 1 GTDB `skos:closeMatch` mapping, 1 synonym, 1 xref, 1 BacDive strain, 9 genome assemblies, 6 genome records, 29 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, GTDB, Madin, BacDive, GOLD, NCBI Assembly, BV-BRC, strain-normalization, and generated YAML rows, and found the `NCBITaxon:264634` species-scoped StrainInfo rows that contextualize the strain; found no unexpected duplicate generated record. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:347500`, 10 checked lineage entries with no missing rows or mismatches, 1 BacDive strain row, 3 culture-collection rows, 8 strain assembly rows, 6 strain genome rows, 18 raw related rows, 1 GOLD organism/project/analysis set, 1 GTDB mapping row, 1 Madin row, 0 NCBI merge rows, and 0 LPSN, StrainInfo, BactoTraits, or MediaDive direct target rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1408415` resolves in the committed NCBI inventory to label
`Acholeplasma equifetale ATCC 29724`, rank `STRAIN`, parent
`NCBITaxon:264634`, genetic code `11`, and taxonomy snapshot `2026-09-13`.
The record carries those same identity fields and correctly lands in the
`bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:264634` Acholeplasma
equifetale. There are no retained old identifiers for this target in the NCBI
merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1408415`, source label `Acholeplasma equifetale ATCC 29724`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB source attestation and taxonomy mapping are supported by
`GTDB:s__Acholeplasma_equifetale`, which maps to `NCBITaxon:1408415` with
`skos:closeMatch` and `genome_count: 1`. The BacDive row for ID `167728`, GOLD
organism `Go0018775`, GOLD project `Gp0018775`, GOLD analysis `Ga0005301`,
and the normalized `ATCC-29724`, `DSM-116313`, and `NCTC-10171` culture
collection rows support the single `C112` strain block.

The child strain payload is supported by 8 raw assembly rows from BacDive,
BV-BRC, GOLD, GTDB, and NCBI Assembly; 6 raw genome rows from BacDive, BV-BRC,
GOLD, and GTDB; 18 raw related rows from BV-BRC, GOLD, GTDB, and NCBI
Assembly; and 11 species-scoped StrainInfo related records for ATCC 29724.

The seed event is supported by `curation/seed_scope.tsv:15620`, which records
`NCBITaxon:1408415` as added on `2026-09-12` with reason `attested rule:
Acholeplasma equifetale ATCC 29724, 5 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, GTDB, BacDive, GOLD,
NCBI Assembly, BV-BRC, Madin, StrainInfo, and strain-normalization inputs, and
found no NCBI merge, direct LPSN, direct type-material, BactoTraits, or
MediaDive row for the strain taxon that would require another YAML section.

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
