# YAML Record Review: Achromobacter ruhlandii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_ruhlandii.yaml
- Started UTC: 2026-09-26T21:21:20Z
- Finished UTC: 2026-09-26T21:21:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_ruhlandii.yaml` |
| Identifier | `NCBITaxon:72557` |
| Label | `Achromobacter ruhlandii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, BV-BRC, and NCBI
assembly inputs. Its path is pinned by `data/taxa/PATHS.tsv:581479`, and all
reviewed fields are owned by the seeder, `curation/seed_scope.tsv`, or
upstream kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_ruhlandii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_ruhlandii.yaml data/taxa/bacteria/achromobacter_seleniivolatilans.yaml data/taxa/bacteria/achromobacter_semiaridum.yaml data/taxa/bacteria/achromobacter_sp.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 2,692 YAML lines, 9 lineage entries, 8 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 2 exact and 3 related synonyms, 2 xrefs, 7 BacDive strains, 25 genome assemblies, 15 genome records, 129 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, MADIN, BactoTraits, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:10143`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 10 native GOLD organisms, 9 native GOLD projects, 9 native GOLD analyses, 7 BacDive rows, 28 culture-collection rows, 14 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 22 raw strain-assembly rows, 12 raw strain-genome rows, 45 raw strain-related rows, 3 StrainInfo assembly rows, 37 StrainInfo related rows, 5 direct StrainInfo hits, 19 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:72557` resolves in the committed NCBI inventory to label
`Achromobacter ruhlandii`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. The
bounded scan found no NCBI merge row and no retained old-id row that would
change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, 2 exact synonyms, and
2 related synonyms. LPSN row `lpsn:772563` supports the legitimate, validly
published, correct species name, one LPSN synonym for `Alcaligenes ruhlandii`,
type-strain aliases from `ATCC-15749` through `LMG-1866`, and sequence
accession `INSDC:AB010840`.

The GTDB evidence is the single `GTDB:s__Achromobacter_ruhlandii` closeMatch
row with `genome_count: 64`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs support 7 BacDive strain blocks,
including one type strain, 25 genome assemblies, 15 genome records, and 129
related records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 10 organisms, MediaDive asserts 3 media, MADIN asserts 4 traits, and
BactoTraits asserts 1 trait for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:457`, which records
`NCBITaxon:72557` as added on `2026-09-12` with reason `attested rule:
Achromobacter ruhlandii, 8 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
type-material, normalized assembly, normalized genome, normalized
related-record, and generated YAML inputs, and found no StrainInfo exclusion
row for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other records are explained by shared
strain and related-record links, not by duplicate `NCBITaxon:72557` target
records.

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
