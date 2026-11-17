# YAML Record Review: Achromobacter pulmonis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_pulmonis.yaml
- Started UTC: 2026-09-26T21:17:01Z
- Finished UTC: 2026-09-26T21:17:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_pulmonis.yaml` |
| Identifier | `NCBITaxon:1389932` |
| Label | `Achromobacter pulmonis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, BV-BRC, and NCBI
assembly inputs. Its path is pinned by `data/taxa/PATHS.tsv:141627`, and all
reviewed fields are owned by the seeder, `curation/seed_scope.tsv`, or
upstream kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_pulmonis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_piechaudii_atcc_43553.yaml data/taxa/bacteria/achromobacter_piechaudii_hle.yaml data/taxa/bacteria/achromobacter_piechaudii_nbrc_102461.yaml data/taxa/bacteria/achromobacter_pulmonis.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,707 YAML lines, 9 lineage entries, 8 source attestations, 1 LPSN nomenclature entry, 2 GTDB `skos:broadMatch` mappings, 1 exact and 3 related synonyms, 2 xrefs, 4 BacDive strains, 18 genome assemblies, 11 genome records, 74 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, MADIN, BactoTraits, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:340743`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 2 GTDB broadMatch rows, 1 GOLD aggregate row, 7 native GOLD organisms, 4 native GOLD projects, 4 native GOLD analyses, 4 BacDive rows, 9 culture-collection rows, 9 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 16 raw strain-assembly rows, 9 raw strain-genome rows, 42 raw strain-related rows, 2 StrainInfo assembly rows, 30 StrainInfo related rows, 4 direct StrainInfo hits, 8 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1389932` resolves in the committed NCBI inventory to label
`Achromobacter pulmonis`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1173154` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, the exact synonym
`Achromobacter genogroup 11`, and 3 related synonyms. LPSN row `lpsn:790793`
supports the legitimate, validly published, correct species name, authority
`Vandamme et al. 2013`, type-strain aliases `CCUG-61972`, `DSM-100240`,
`DSM-29617`, and `LMG-26696`, and sequence accession `INSDC:MH806389`.

The GTDB evidence consists of 2 broadMatch rows for
`GTDB:s__Achromobacter_pulmonis` and `GTDB:s__Achromobacter_pulmonis_A`. The
BacDive, culture-collection, GOLD, BV-BRC, NCBI-assembly, StrainInfo, and ATB
inputs support 4 BacDive strain blocks, including one type strain, 18 genome
assemblies, 11 genome records, and 74 related records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 7 organisms, MediaDive asserts 1 medium, MADIN asserts 1 trait, and
BactoTraits asserts 1 trait for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:775`, which records
`NCBITaxon:1389932` as added on `2026-09-12` with reason `attested rule:
Achromobacter pulmonis, 8 sources incl. NCBI`.

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
strain and related-record links, not by duplicate `NCBITaxon:1389932` target
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
