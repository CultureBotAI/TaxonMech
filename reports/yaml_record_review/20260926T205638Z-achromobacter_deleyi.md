# YAML Record Review: Achromobacter deleyi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_deleyi.yaml
- Started UTC: 2026-09-26T20:56:38Z
- Finished UTC: 2026-09-26T20:56:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_deleyi.yaml` |
| Identifier | `NCBITaxon:1353891` |
| Label | `Achromobacter deleyi` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its path
is pinned by `data/taxa/PATHS.tsv:126937`, and all reviewed fields are owned by
the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs rather
than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_deleyi.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_colocynthi.yaml data/taxa/bacteria/achromobacter_cycloclastes.yaml data/taxa/bacteria/achromobacter_deleyi.yaml data/taxa/bacteria/achromobacter_denitrificans.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,023 YAML lines, 9 lineage entries, 6 source attestations, 1 LPSN nomenclature entry, 5 GTDB `skos:broadMatch` mappings, 3 NCBI related synonyms, 2 xrefs, 2 BacDive strains, 12 genome assemblies, 10 genome records, 40 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:327057`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 5 GTDB broadMatch rows, 1 GOLD aggregate row, 8 native GOLD organisms, 8 native GOLD projects, 8 native GOLD analyses, 2 BacDive rows, 4 culture-collection rows, 5 NCBI type-material rows, 1 MediaDive row, 19 raw strain-assembly rows, 11 raw strain-genome rows, 43 raw strain-related rows, 1 StrainInfo assembly row, 29 StrainInfo related rows, 8 direct StrainInfo hits, 14 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1353891` resolves in the committed NCBI inventory to label
`Achromobacter deleyi`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold`, and taxonomy
snapshot `2026-09-13`. The generated record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1173153` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and all 3 related
synonyms. LPSN row `lpsn:794613` supports the legitimate, validly published,
correct species name, authority `Vandamme et al. 2016`, type-strain aliases
`CCUG-62433` and `LMG-3458`, and sequence accession `INSDC:HG324053`.

The GTDB evidence consists of 5 broadMatch rows for
`GTDB:s__Achromobacter_deleyi`, `GTDB:s__Achromobacter_deleyi_A`,
`GTDB:s__Achromobacter_deleyi_B`, `GTDB:s__Achromobacter_insuavis_A`, and
`GTDB:s__Achromobacter_sp002975275`. The BacDive, culture-collection, GOLD,
BV-BRC, NCBI-assembly, StrainInfo, and ATB inputs support 2 BacDive strain
blocks, including one type strain, 12 genome assemblies, 10 genome records, and
40 related records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 9 organisms and MediaDive asserts 2 media for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:9043`, which records
`NCBITaxon:1353891` as added on `2026-09-12` with reason `attested rule:
Achromobacter deleyi, 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, StrainInfo, ATB, culture-collection, type-material,
normalized assembly, normalized genome, normalized related-record, and
generated YAML inputs, and found no MADIN, BactoTraits, or StrainInfo
exclusion row for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other Achromobacter pages are
explained by shared strain and related-record links, not by duplicate
`NCBITaxon:1353891` target records.

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
