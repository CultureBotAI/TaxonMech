# YAML Record Review: Acholeplasma oculi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_oculi.yaml
- Started UTC: 2026-09-26T19:08:00Z
- Finished UTC: 2026-09-26T19:08:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_oculi.yaml` |
| Identifier | `NCBITaxon:35623` |
| Label | `Acholeplasma oculi` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2147` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:469900`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_oculi.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml data/taxa/bacteria/acholeplasma_laidlawii.yaml data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml data/taxa/bacteria/acholeplasma_oculi.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected enriched generated shape: 1000 YAML lines, 9 lineage entries, 6 source attestations, 1 nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 4 synonyms, 2 xrefs, 3 BacDive strains, 4 culture collection IDs, 13 genome assemblies, 11 genome records, 38 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, LPSN, GTDB, Madin, BacDive, GOLD, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, strain-normalization, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:3913`, 9 checked lineage entries with no missing rows or mismatches, the LPSN row at `data/raw/lpsn_names.tsv:21373`, 1 GTDB mapping row, 1 Madin row, 3 exact BacDive hits, 2 native GOLD organisms, 3 native GOLD projects, 3 native GOLD analyses, 11 raw assembly rows, 10 raw genome rows, 26 raw related rows, 5 exact StrainInfo direct hits with 6 deposits, 2 StrainInfo assembly rows, 12 StrainInfo related rows, 4 NCBI type-material rows, 0 NCBI merge rows, and 0 BactoTraits or MediaDive rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:35623` resolves in the committed NCBI inventory to label
`Acholeplasma oculi`, rank `SPECIES`, parent `NCBITaxon:2147`, genetic code
`11`, and taxonomy snapshot `2026-09-13`. The record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2147` Acholeplasma. There
are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:35623`, source label `Acholeplasma oculi`, `assertion_count: 1`,
`assertion_unit: NAME`, and the 2026-09-13 snapshot note all match.

The nomenclature block is backed by `lpsn:783257`, a legitimate, validly
published LPSN species row whose type strains are `ATCC-27350` and
`NCTC-10150`. The GTDB mapping to `GTDB:s__Acholeplasma_oculi` is the
committed species-level `skos:closeMatch` row with `genome_count: 4`.

The three BacDive strain blocks, four normalized culture collection rows, 13
assemblies, 11 genome records, and 38 related records are backed by the raw
BacDive, GOLD, GTDB, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, and
strain-normalization rows checked above. The AllTheBacteria link is
`atb.assembly:202505.SAMN02745122`, and the NCBI type-material rows cover the
ATCC 27350 and NCTC 10150 designations.

The seed event is supported by `curation/seed_scope.tsv:8730`, which records
`NCBITaxon:35623` as added on `2026-09-12` with reason `attested rule:
Acholeplasma oculi, 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated enriched record.
The exact and bounded scans account for the expected NCBI, LPSN, GTDB,
BacDive, GOLD, NCBI Assembly, BV-BRC, AllTheBacteria, StrainInfo, Madin,
strain-normalization, and type-material inputs, and found no NCBI merge,
BactoTraits, or MediaDive row that would require another YAML section.

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
