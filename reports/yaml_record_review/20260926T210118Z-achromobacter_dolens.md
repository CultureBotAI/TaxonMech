# YAML Record Review: Achromobacter dolens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_dolens.yaml
- Started UTC: 2026-09-26T21:01:18Z
- Finished UTC: 2026-09-26T21:01:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_dolens.yaml` |
| Identifier | `NCBITaxon:1287738` |
| Label | `Achromobacter dolens` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, BactoTraits, StrainInfo, ATB, BV-BRC, and NCBI assembly
inputs. Its path is pinned by `data/taxa/PATHS.tsv:99528`, and all reviewed
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_dolens.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_denitrificans_nbrc_15125.yaml data/taxa/bacteria/achromobacter_dolens.yaml data/taxa/bacteria/achromobacter_insolitus.yaml data/taxa/bacteria/achromobacter_insuavis.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,804 YAML lines, 9 lineage entries, 7 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 1 exact and 7 related NCBI synonyms, 2 xrefs, 4 BacDive strains, 27 genome assemblies, 21 genome records, 71 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, BactoTraits, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:301761`, 9 checked lineage entries with no missing rows or mismatches, 5 NCBI merge rows, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 5 native GOLD organisms, 5 native GOLD projects, 5 native GOLD analyses, 4 BacDive rows, 9 culture-collection rows, 5 NCBI type-material rows, 1 MediaDive row, 1 BactoTraits row, 24 raw strain-assembly rows, 18 raw strain-genome rows, 54 raw strain-related rows, 3 StrainInfo assembly rows, 34 StrainInfo related rows, 9 direct StrainInfo hits, 15 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1287738` resolves in the committed NCBI inventory to label
`Achromobacter dolens`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|bactotraits`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. Five NCBI
merge rows retire old Achromobacter IDs into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for those old IDs.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, the exact synonym
`Achromobacter genogroup 14`, and 7 related synonyms. LPSN row `lpsn:791416`
supports the legitimate, validly published, correct species name, authority
`Vandamme et al. 2014`, type-strain aliases `CCUG-62421` and `LMG-26840`, and
sequence accession `INSDC:HF586509`.

The GTDB evidence is the single `GTDB:s__Achromobacter_dolens` closeMatch row
with `genome_count: 24`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs support 4 BacDive strain blocks,
including one type strain, 27 genome assemblies, 21 genome records, and 71
related records.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 5 organisms, MediaDive asserts 2 media, and BactoTraits asserts 1 trait
for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:5023`, which records
`NCBITaxon:1287738` as added on `2026-09-12` with reason `attested rule:
Achromobacter dolens, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, BactoTraits, StrainInfo, ATB, culture-collection,
type-material, normalized assembly, normalized genome, normalized
related-record, and generated YAML inputs, and found no MADIN or StrainInfo
exclusion row for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other records are explained by shared
strain and related-record links, not by duplicate `NCBITaxon:1287738` target
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
