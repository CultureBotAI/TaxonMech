# YAML Record Review: Acholeplasmatales bacterium DTU056

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasmatales_bacterium_dtu056.yaml
- Started UTC: 2026-09-26T20:15:01Z
- Finished UTC: 2026-09-26T20:15:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasmatales_bacterium_dtu056.yaml` |
| Identifier | `NCBITaxon:1671633` |
| Label | `Acholeplasmatales bacterium DTU056` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1151603` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, and MADIN inputs. Its
path is pinned by `data/taxa/PATHS.tsv:241229`, and all reviewed fields are
owned by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs
rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasmatales_bacterium_dtu056.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasmatales_bacterium_canine_oral_taxon_316.yaml data/taxa/bacteria/acholeplasmatales_bacterium_canine_oral_taxon_375.yaml data/taxa/bacteria/acholeplasmatales_bacterium_dtu056.yaml data/taxa/bacteria/acholeplasmatales_bacterium_dtu067.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 72 YAML lines, 8 lineage entries, 3 source attestations, 0 nomenclature entries, 1 GTDB `skos:closeMatch` mapping, 1 GTDB exact synonym, 1 xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `curation/legacy_page_paths.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:435513`, 8 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row at `data/raw/gtdb_mappings.tsv:47618`, 1 MADIN row at `data/raw/madin_taxa.tsv:17850`, 0 NCBI merge rows, and 0 GOLD, LPSN, BacDive, StrainInfo, MediaDive, BactoTraits, type-material, normalized assembly, genome, or related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1671633` resolves in the committed NCBI inventory to label
`Acholeplasmatales bacterium DTU056`, rank `SPECIES`, parent
`NCBITaxon:1151603`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`. The generated
record carries those same identity fields and correctly lands in the `bacteria`
path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 8 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:1151603` unclassified
Acholeplasmatales. There are no retained old identifiers for this target in the
NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1671633`, source label `Acholeplasmatales bacterium DTU056`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB evidence is supported by one committed `skos:closeMatch` row:
`GTDB:s__DTU056_sp001512985`, label `s__DTU056_sp001512985`, parent
`GTDB:g__DTU056`, and `genome_count: 6`. The YAML preserves this mapping,
copies the 6-genome count into the representative GTDB attestation, adds the
expected exact synonym `DTU056 sp001512985`, and records the same GTDB ID as an
xref.

The MADIN evidence is supported by `data/raw/madin_taxa.tsv:17850`, whose 2
trait assertions are preserved as the `MADIN` source attestation with source
ID `NCBITaxon:1671633`, source label `Acholeplasmatales bacterium DTU056`, and
`assertion_unit: TRAIT_ASSERTION`.

The seed event is supported by `curation/seed_scope.tsv:47495`, which records
`NCBITaxon:1671633` as added on `2026-09-12` with reason `attested rule:
Acholeplasmatales bacterium DTU056, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated NCBI, GTDB, and
MADIN record. The exact and bounded scans account for the expected NCBI, GTDB,
MADIN, and generated YAML inputs, and found no NCBI merge, LPSN, GOLD,
BacDive, StrainInfo, MediaDive, BactoTraits, type-material, normalized
assembly, normalized genome, or normalized related-record row that would
require an enriched YAML section.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

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
