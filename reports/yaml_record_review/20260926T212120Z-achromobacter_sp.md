# YAML Record Review: Achromobacter sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_sp.yaml
- Started UTC: 2026-09-26T21:21:20Z
- Finished UTC: 2026-09-26T21:21:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_sp.yaml` |
| Identifier | `NCBITaxon:134375` |
| Label | `Achromobacter sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2626865` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, BacDive, MediaDive,
GOLD, MADIN, BactoTraits, StrainInfo, and ATB inputs. Its path is pinned by
`data/taxa/PATHS.tsv:122380`, and all reviewed fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than this YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_ruhlandii.yaml data/taxa/bacteria/achromobacter_seleniivolatilans.yaml data/taxa/bacteria/achromobacter_semiaridum.yaml data/taxa/bacteria/achromobacter_sp.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,571 YAML lines, 10 lineage entries, 7 source attestations, 20 GTDB `skos:broadMatch` mappings, 0 synonyms, 0 xrefs, 24 BacDive strains, 1 genome assembly, 2 genome records, 66 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, GTDB, GOLD, BacDive, MediaDive, MADIN, BactoTraits, culture-collection, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:26536`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 20 GTDB broadMatch rows, 1 GOLD aggregate row, 2 native GOLD organisms, 2 native GOLD projects, 2 native GOLD analyses, 24 BacDive rows, 34 culture-collection rows, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 0 NCBI type-material rows, 0 direct raw strain-assembly rows, 0 direct raw strain-genome rows, 0 direct raw strain-related rows, and no target-id StrainInfo assembly, StrainInfo related, direct StrainInfo, StrainInfo deposit, or StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:134375` resolves in the committed NCBI inventory to label
`Achromobacter sp.`, rank `SPECIES`, parent `NCBITaxon:2626865`, genetic code
`11`, source set `ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`,
and taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2626865` unclassified
Achromobacter. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation. The GTDB evidence
consists of 20 broadMatch rows headed by `GTDB:s__Achromobacter_insuavis`,
`GTDB:s__Achromobacter_denitrificans`, `GTDB:s__Achromobacter_dolens`, and
`GTDB:s__Achromobacter_animicus`.

The BacDive and culture-collection inputs support 24 BacDive strain blocks.
Those strains do not have target-id raw assembly/genome/related rows, but the
generated YAML still includes one BacDive assembly, 2 BacDive genome records,
and 66 related records linked through the BacDive strain rows and shared
StrainInfo deposits.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 6 organisms, MediaDive asserts 7 media, MADIN asserts 1 trait, and
BactoTraits asserts 5 traits for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:8451`, which records
`NCBITaxon:134375` as added on `2026-09-12` with reason `attested rule:
Achromobacter sp., 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, BacDive, GOLD,
MediaDive, MADIN, BactoTraits, StrainInfo, ATB, culture-collection, seed, path,
and generated YAML inputs, and found no LPSN, NCBI type-material, NCBI merge,
normalized target-id assembly/genome/related-record, or StrainInfo exclusion
row for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under several `Pseudomonas syringae pv.
actinidiae` records are explained by shared strain and related-record links,
not by duplicate `NCBITaxon:134375` target records.

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
