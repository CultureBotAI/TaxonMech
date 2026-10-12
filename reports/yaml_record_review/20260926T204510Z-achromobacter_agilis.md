# YAML Record Review: Achromobacter agilis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_agilis.yaml
- Started UTC: 2026-09-26T20:45:10Z
- Finished UTC: 2026-09-26T20:45:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_agilis.yaml` |
| Identifier | `NCBITaxon:1353888` |
| Label | `Achromobacter agilis` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive, GOLD,
StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its path is pinned by
`data/taxa/PATHS.tsv:126934`, and all reviewed fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than this YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_agilis.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_agilis.yaml data/taxa/bacteria/achromobacter_aloeverae.yaml data/taxa/bacteria/achromobacter_animicus.yaml data/taxa/bacteria/achromobacter_anxifer.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 678 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 3 NCBI related synonyms, 2 xrefs, 1 BacDive strain, 9 genome assemblies, 7 genome records, 25 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:327054`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 1 native GOLD organism/project/analysis, 1 BacDive row, 2 culture-collection rows, 8 NCBI type-material rows, 8 raw strain-assembly rows, 6 raw strain-genome rows, 18 raw strain-related rows, 1 StrainInfo assembly row, 5 StrainInfo related rows, 1 direct StrainInfo hit, 3 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1353888` resolves in the committed NCBI inventory to label
`Achromobacter agilis`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1389625` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and all three related
synonyms. LPSN row `lpsn:794605` supports the legitimate, validly published,
correct species name, authority `(ex Bergey et al. 1925) Vandamme et al.
2016`, type-strain aliases `CCUG-62454` and `LMG-3411`, and sequence accession
`INSDC:HG324050`.

The GTDB evidence is the single `GTDB:s__Achromobacter_agilis` closeMatch row
with `genome_count: 1`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs all converge on the one generated
type-strain block for BacDive 140509 / LMG 3411 / CCUG 62454, with one ATB
genome record backed by `atb.assembly:202505.SAMEA4780388`.

The seed event is supported by `curation/seed_scope.tsv:15548`, which records
`NCBITaxon:1353888` as added on `2026-09-12` with reason `attested rule:
Achromobacter agilis, 5 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive, GOLD,
StrainInfo, ATB, culture-collection, type-material, normalized assembly,
normalized genome, normalized related-record, and generated YAML inputs, and
found no Madin, MediaDive, BactoTraits, or StrainInfo exclusion row for this
taxon.

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
