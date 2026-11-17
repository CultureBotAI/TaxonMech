# YAML Record Review: Achromobacter denitrificans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_denitrificans.yaml
- Started UTC: 2026-09-26T20:56:38Z
- Finished UTC: 2026-09-26T20:56:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_denitrificans.yaml` |
| Identifier | `NCBITaxon:32002` |
| Label | `Achromobacter denitrificans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its
path is pinned by `data/taxa/PATHS.tsv:435979`, and all reviewed fields are
owned by the seeder, `curation/seed_scope.tsv`, or upstream kg-microbe inputs
rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_denitrificans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_colocynthi.yaml data/taxa/bacteria/achromobacter_cycloclastes.yaml data/taxa/bacteria/achromobacter_deleyi.yaml data/taxa/bacteria/achromobacter_denitrificans.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 6,796 YAML lines, 9 lineage entries, 7 source attestations, 2 LPSN nomenclature entries, 3 GTDB `skos:broadMatch` mappings, 6 exact and 11 related synonyms, 2 xrefs, 34 BacDive strains, 47 genome assemblies, 37 genome records, 353 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, MADIN, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, the generated descendant strain YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:3396`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 2 LPSN rows, 3 GTDB broadMatch rows, 1 GOLD aggregate row, 142 native GOLD organisms, 12 native GOLD projects, 10 native GOLD analyses, 34 BacDive exact hits, 49 culture-collection rows, 21 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, 29 raw strain-assembly rows, 25 raw strain-genome rows, 148 raw strain-related rows, 3 StrainInfo assembly rows, 118 StrainInfo related rows, 41 direct StrainInfo hits, 101 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:32002` resolves in the committed NCBI inventory to label
`Achromobacter denitrificans`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`,
and taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1806484` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and its 13 direct
synonyms. The 2 LPSN rows support the correct species name, the orphaned
subspecies `Alcaligenes denitrificans denitrificans`, 4 LPSN-sourced related
synonyms, the 8 type-strain aliases on both LPSN entries, and sequence
accession `INSDC:AJ278451`.

The GTDB evidence consists of 3 broadMatch rows for
`GTDB:s__Achromobacter_denitrificans`, `GTDB:s__Achromobacter_ruhlandii`, and
`GTDB:s__Achromobacter_spanius`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs support 34 BacDive strain blocks,
including one type strain, 47 genome assemblies, 37 genome records, and 353
related records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 143 organisms, MediaDive asserts 2 media, and MADIN asserts 5 traits
for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:4646`, which records
`NCBITaxon:32002` as added on `2026-09-12` with reason `attested rule:
Achromobacter denitrificans, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, StrainInfo, ATB, culture-collection, type-material,
normalized assembly, normalized genome, normalized related-record, descendant
strain, and generated YAML inputs, and found no BactoTraits or StrainInfo
exclusion row for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other records are explained by shared
strain and related-record links or by the direct descendant strain
`achromobacter_denitrificans_nbrc_15125`, not by duplicate `NCBITaxon:32002`
species target records.

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
