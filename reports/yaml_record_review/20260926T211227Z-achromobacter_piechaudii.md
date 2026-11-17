# YAML Record Review: Achromobacter piechaudii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_piechaudii.yaml
- Started UTC: 2026-09-26T21:12:27Z
- Finished UTC: 2026-09-26T21:12:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_piechaudii.yaml` |
| Identifier | `NCBITaxon:72556` |
| Label | `Achromobacter piechaudii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive, GOLD,
MADIN, StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its path is pinned by
`data/taxa/PATHS.tsv:581478`, and all reviewed fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than this YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_piechaudii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_mucicolens.yaml data/taxa/bacteria/achromobacter_obae.yaml data/taxa/bacteria/achromobacter_pestifer.yaml data/taxa/bacteria/achromobacter_piechaudii.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 3,730 YAML lines, 9 lineage entries, 6 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 1 exact and 4 related synonyms, 2 xrefs, 15 BacDive strains, 37 genome assemblies, 22 genome records, 189 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MADIN, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:10142`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 59 native GOLD organisms, 5 native GOLD projects, 5 native GOLD analyses, 15 BacDive rows, 20 culture-collection rows, 21 NCBI type-material rows, 1 MADIN row, 26 raw strain-assembly rows, 14 raw strain-genome rows, 116 raw strain-related rows, 4 StrainInfo assembly rows, 63 StrainInfo related rows, 20 direct StrainInfo hits, 41 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:72556` resolves in the committed NCBI inventory to label
`Achromobacter piechaudii`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1273564` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, the exact synonym
`Alcaligenes piechaudii`, and 3 related synonyms. LPSN row `lpsn:772562`
supports the legitimate, validly published, correct species name, one LPSN
synonym for `Alcaligenes piechaudii`, type-strain aliases from `ATCC-43552`
through `NCTC-11970`, and sequence accession `INSDC:AB681803`.

The GTDB evidence is the single `GTDB:s__Achromobacter_piechaudii` closeMatch
row with `genome_count: 9`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs support 15 BacDive strain blocks,
including the BacDive 320 type strain filed under descendant
`NCBITaxon:1216977`, 37 genome assemblies, 22 genome records, and 189 related
records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 59 organisms and MADIN asserts 5 traits for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:8500`, which records
`NCBITaxon:72556` as added on `2026-09-12` with reason `attested rule:
Achromobacter piechaudii, 6 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive, GOLD,
MADIN, StrainInfo, ATB, culture-collection, type-material, normalized
assembly, normalized genome, normalized related-record, and generated YAML
inputs, and found no MediaDive, BactoTraits, or StrainInfo exclusion row for
this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other records are explained by shared
strain and related-record links, not by duplicate `NCBITaxon:72556` target
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
