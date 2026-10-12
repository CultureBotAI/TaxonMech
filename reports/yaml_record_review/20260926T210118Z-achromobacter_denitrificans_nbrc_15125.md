# YAML Record Review: Achromobacter denitrificans NBRC 15125

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_denitrificans_nbrc_15125.yaml
- Started UTC: 2026-09-26T21:01:18Z
- Finished UTC: 2026-09-26T21:01:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_denitrificans_nbrc_15125.yaml` |
| Identifier | `NCBITaxon:1255278` |
| Label | `Achromobacter denitrificans NBRC 15125` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:32002` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded strain record from NCBI, GTDB, BacDive,
MediaDive, MADIN, GOLD, StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its
path is pinned by `data/taxa/PATHS.tsv:86586`, and all reviewed fields are
owned by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs
rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_denitrificans_nbrc_15125.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_denitrificans_nbrc_15125.yaml data/taxa/bacteria/achromobacter_dolens.yaml data/taxa/bacteria/achromobacter_insolitus.yaml data/taxa/bacteria/achromobacter_insuavis.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 2,831 YAML lines, 10 lineage entries, 5 source attestations, 1 GTDB `skos:closeMatch` mapping, 1 exact GTDB synonym, 1 xref, 1 BacDive strain, 26 genome assemblies, 23 genome records, 143 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, GTDB, BacDive, MediaDive, MADIN, GOLD, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, parent species YAML, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:289482`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB closeMatch row, 1 BacDive row, 1 MediaDive row, 1 MADIN row, 1 native GOLD organism/project/analysis, 20 culture-collection rows, 9 direct raw strain-assembly rows, 7 direct raw strain-genome rows, 20 direct raw strain-related rows, 0 NCBI merge rows, 0 LPSN rows, 0 BactoTraits rows, 0 GOLD aggregate rows, 0 StrainInfo target rows, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1255278` resolves in the committed NCBI inventory to label
`Achromobacter denitrificans NBRC 15125`, rank `STRAIN`, parent
`NCBITaxon:32002`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:32002` Achromobacter
denitrificans. The bounded scan found no NCBI merge row and no retained old-id
row that would change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation. The GTDB evidence is
the single `GTDB:s__Achromobacter_denitrificans` closeMatch row with
`genome_count: 27`; that row also supports the GTDB exact synonym and xref.
BacDive row 318 supports the one generated strain block and its 20 culture
collection aliases.

The direct compact provider rows support 3 MediaDive media and 1 MADIN trait.
The native GOLD exact hit lacks a `data/raw/gold_organisms.tsv` aggregate row,
so it does not produce a top-level GOLD source attestation, but GOLD still
contributes matched assembly, genome, and related-record rows under the shared
BacDive 318 strain block.

The seed event is supported by `curation/seed_scope.tsv:15298`, which records
`NCBITaxon:1255278` as added on `2026-09-12` with reason `attested rule:
Achromobacter denitrificans NBRC 15125, 5 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, BacDive, MediaDive,
MADIN, seed, path, direct GOLD, culture-collection, normalized assembly,
normalized genome, normalized related-record, ATB, and generated YAML inputs,
and found no LPSN, BactoTraits, NCBI merge, or StrainInfo exclusion row for
this taxon.

Several generated assemblies, genome records, and related records in the
BacDive 318 block are taxonomized to the parent species `NCBITaxon:32002`
rather than to the strain. They are still part of this generated strain page
because they resolve through the same BacDive strain and NBRC/DSM/LMG culture
aliases, not through a competing target record.

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
