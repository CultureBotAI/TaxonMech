# YAML Record Review: Achromobacter insuavis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_insuavis.yaml
- Started UTC: 2026-09-26T21:01:18Z
- Finished UTC: 2026-09-26T21:01:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_insuavis.yaml` |
| Identifier | `NCBITaxon:1287735` |
| Label | `Achromobacter insuavis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, BV-BRC, and NCBI
assembly inputs. Its path is pinned by `data/taxa/PATHS.tsv:99525`, and all
reviewed fields are owned by the seeder, `curation/seed_scope.tsv`, or
upstream kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_insuavis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_denitrificans_nbrc_15125.yaml data/taxa/bacteria/achromobacter_dolens.yaml data/taxa/bacteria/achromobacter_insolitus.yaml data/taxa/bacteria/achromobacter_insuavis.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,729 YAML lines, 9 lineage entries, 8 source attestations, 1 LPSN nomenclature entry, 2 GTDB `skos:broadMatch` mappings, 1 exact and 2 related NCBI synonyms, 2 xrefs, 8 BacDive strains, 18 genome assemblies, 14 genome records, 72 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, MADIN, BactoTraits, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, generated descendant YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:301758`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 LPSN row, 2 GTDB broadMatch rows, 1 GOLD aggregate row, 4 native GOLD organisms, 2 native GOLD projects, 2 native GOLD analyses, 8 BacDive rows, 16 culture-collection rows, 5 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 16 raw strain-assembly rows, 12 raw strain-genome rows, 38 raw strain-related rows, 2 StrainInfo assembly rows, 36 StrainInfo related rows, 12 direct StrainInfo hits, 19 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1287735` resolves in the committed NCBI inventory to label
`Achromobacter insuavis`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. The
bounded scan found no NCBI merge row and no retained old-id row that would
change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, the exact synonym
`Achromobacter genogroup 2`, and 2 related synonyms. LPSN row `lpsn:791417`
supports the legitimate, validly published, correct species name, authority
`Vandamme et al. 2014`, type-strain aliases `CCUG-62426` and `LMG-26845`, and
sequence accession `INSDC:HF586506`.

The GTDB evidence consists of 2 broadMatch rows for
`GTDB:s__Achromobacter_insuavis` and `GTDB:s__Achromobacter_insuavis_A`. The
BacDive, culture-collection, GOLD, BV-BRC, NCBI-assembly, StrainInfo, and ATB
inputs support 8 BacDive strain blocks, including one type strain, 18 genome
assemblies, 14 genome records, and 72 related records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 4 organisms, MediaDive asserts 2 media, MADIN asserts 4 traits, and
BactoTraits asserts 1 trait for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:423`, which records
`NCBITaxon:1287735` as added on `2026-09-12` with reason `attested rule:
Achromobacter insuavis, 8 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
type-material, normalized assembly, normalized genome, normalized
related-record, descendant, and generated YAML inputs, and found no NCBI merge
or StrainInfo exclusion row for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other records are explained by shared
strain and related-record links, and the generated descendant hit is a child of
this species rather than a duplicate `NCBITaxon:1287735` target record.

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
