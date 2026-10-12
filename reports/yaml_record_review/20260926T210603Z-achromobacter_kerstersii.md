# YAML Record Review: Achromobacter kerstersii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_kerstersii.yaml
- Started UTC: 2026-09-26T21:06:03Z
- Finished UTC: 2026-09-26T21:06:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_kerstersii.yaml` |
| Identifier | `NCBITaxon:1353890` |
| Label | `Achromobacter kerstersii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive, GOLD,
StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its path is pinned by
`data/taxa/PATHS.tsv:126936`, and all reviewed fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than this YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_kerstersii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_kerstersii.yaml data/taxa/bacteria/achromobacter_lyticus.yaml data/taxa/bacteria/achromobacter_maghribensis.yaml data/taxa/bacteria/achromobacter_marplatensis.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 623 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 2 GTDB `skos:broadMatch` mappings, 2 NCBI related synonyms, 2 xrefs, 1 BacDive strain, 9 genome assemblies, 7 genome records, 21 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, generated target YAML, and generated side-reference rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:327056`, 9 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 LPSN row, 2 GTDB broadMatch rows, 1 GOLD aggregate row, 1 native GOLD organism/project/analysis, 1 BacDive row, 2 culture-collection rows, 7 NCBI type-material rows, 8 raw strain-assembly rows, 6 raw strain-genome rows, 18 raw strain-related rows, 1 StrainInfo assembly row, 3 StrainInfo related rows, 3 direct StrainInfo hits, 4 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1353890` resolves in the committed NCBI inventory to label
`Achromobacter kerstersii`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and taxonomy
snapshot `2026-09-13`. The generated record carries those same identity fields
and correctly lands in the `bacteria` path bucket through `taxon_domain:
BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. The
bounded scan found no NCBI merge row and no retained old-id row that would
change the active identifier.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and 2 related
synonyms. LPSN row `lpsn:794611` supports the legitimate, validly published,
correct species name, authority `Vandamme et al. 2016`, type-strain aliases
`CCUG-62449` and `LMG-3441`, and sequence accession `INSDC:HG324052`.

The GTDB evidence consists of 2 broadMatch rows for
`GTDB:s__Achromobacter_kerstersii` and
`GTDB:s__Achromobacter_kerstersii_A`. The BacDive, culture-collection, GOLD,
BV-BRC, NCBI-assembly, StrainInfo, and ATB inputs support the one generated
type-strain block, 9 genome assemblies, 7 genome records, and 21 related
records.

The seed event is supported by `curation/seed_scope.tsv:15550`, which records
`NCBITaxon:1353890` as added on `2026-09-12` with reason `attested rule:
Achromobacter kerstersii, 5 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive, GOLD,
StrainInfo, ATB, culture-collection, type-material, normalized assembly,
normalized genome, normalized related-record, and generated YAML inputs, and
found no MediaDive, MADIN, BactoTraits, or StrainInfo exclusion row for this
taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

Generated YAML side-reference hits under other records are explained by shared
strain and related-record links, not by duplicate `NCBITaxon:1353890` target
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
