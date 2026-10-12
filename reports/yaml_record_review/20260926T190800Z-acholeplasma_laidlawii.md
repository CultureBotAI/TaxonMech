# YAML Record Review: Acholeplasma laidlawii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_laidlawii.yaml
- Started UTC: 2026-09-26T19:08:00Z
- Finished UTC: 2026-09-26T19:08:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_laidlawii.yaml` |
| Identifier | `NCBITaxon:2148` |
| Label | `Acholeplasma laidlawii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:329986`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_laidlawii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml data/taxa/bacteria/acholeplasma_laidlawii.yaml data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml data/taxa/bacteria/acholeplasma_oculi.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 1550 YAML lines, 9 lineage entries, 7 source attestations, 1 nomenclature entry, 2 GTDB `skos:broadMatch` mappings, 9 NCBI synonyms, 2 xrefs, 6 BacDive strains, 12 culture collection IDs, 14 genome assemblies, 12 genome records, 66 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, GTDB, Madin, MediaDive, BacDive, GOLD, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, strain-normalization, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:1691`, 9 checked lineage entries with no missing rows or mismatches, 1 LPSN row, 2 GTDB `skos:broadMatch` rows, 1 Madin row, 1 MediaDive row, 6 exact BacDive hits, 26 native GOLD organisms, 4 native GOLD projects, 4 native GOLD analyses, 12 raw assembly rows, 11 raw genome rows, 37 raw related rows, 12 exact StrainInfo direct hits with 20 deposits, 2 StrainInfo assembly rows, 29 StrainInfo related rows, 20 NCBI type-material rows, 0 NCBI merge rows, and 0 BactoTraits rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:2148` resolves in the committed NCBI inventory to label
`Acholeplasma laidlawii`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic
code `11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:2148`, source label `Acholeplasma laidlawii`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The nomenclature block is backed by `lpsn:772547`, a legitimate, validly
published LPSN species row whose type strains are `ATCC-23206`, `CIP-75`,
`DSM-23060`, `IFO-14400`, `NBRC-14400`, and `NCTC-10116`. The two GTDB rows
are the committed `skos:broadMatch` mappings to `GTDB:s__Acholeplasma_laidlawii`
and `GTDB:s__Acholeplasma_laidlawii_A`.

The 6 BacDive strain blocks, 12 normalized culture collection rows, 14
assemblies, 12 genome records, and 66 related records are backed by the raw
BacDive, GOLD, GTDB, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, and
strain-normalization rows checked above. MediaDive contributes 1 direct medium
row and Madin contributes 3 direct trait assertions for this species.

The seed event is supported by `curation/seed_scope.tsv:4806`, which records
`NCBITaxon:2148` as added on `2026-09-12` with reason `attested rule:
Acholeplasma laidlawii, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, GTDB,
BacDive, GOLD, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, MediaDive,
Madin, strain-normalization, and type-material inputs, and found no NCBI merge
or BactoTraits row that would require another YAML section.

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
