# YAML Record Review: Achromobacter anxifer

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_anxifer.yaml
- Started UTC: 2026-09-26T20:45:10Z
- Finished UTC: 2026-09-26T20:45:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_anxifer.yaml` |
| Identifier | `NCBITaxon:1287737` |
| Label | `Achromobacter anxifer` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive, GOLD,
StrainInfo, ATB, BV-BRC, and NCBI assembly inputs. Its path is pinned by
`data/taxa/PATHS.tsv:99527`, and all reviewed fields are owned by the seeder,
`curation/seed_scope.tsv`, or upstream kg-microbe inputs rather than this YAML
file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_anxifer.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_agilis.yaml data/taxa/bacteria/achromobacter_aloeverae.yaml data/taxa/bacteria/achromobacter_animicus.yaml data/taxa/bacteria/achromobacter_anxifer.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,224 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 1 exact and 3 related NCBI synonyms, 2 xrefs, 3 BacDive strains, 18 genome assemblies, 14 genome records, 47 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, and generated YAML rows; found three cross-record related-row references in `achromobacter_insolitus.yaml`; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:301760`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 2 native GOLD organisms, 2 native GOLD projects, 2 native GOLD analyses, 3 BacDive rows, 6 culture-collection rows, 5 NCBI type-material rows, 16 raw strain-assembly rows, 12 raw strain-genome rows, 36 raw strain-related rows, 2 StrainInfo assembly rows, 14 StrainInfo related rows, 4 direct StrainInfo hits, 6 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1287737` resolves in the committed NCBI inventory to label
`Achromobacter anxifer`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same identity fields and
correctly lands in the `bacteria` path bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1389640` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, the exact synonym
`Achromobacter genogroup 7`, and the three related synonyms. LPSN row
`lpsn:791415` supports the legitimate, validly published, correct species name,
authority `Vandamme et al. 2014`, type-strain aliases `CCUG-62444` and
`LMG-26857`, and sequence accession `INSDC:HF586508`.

The GTDB evidence is the single `GTDB:s__Achromobacter_anxifer` closeMatch row
with `genome_count: 4`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs support three BacDive strain blocks,
including one type strain, 6 culture-collection aliases, 18 genome assemblies,
14 genome records, and 47 related records. Two ATB genome records are backed by
`atb.assembly:202505.SAMEA6647246` and
`atb.assembly:202505.SAMEA6797399`.

The seed event is supported by `curation/seed_scope.tsv:13811`, which records
`NCBITaxon:1287737` as added on `2026-09-12` with reason `attested rule:
Achromobacter anxifer, 5 sources incl. NCBI`.

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

`data/taxa/bacteria/achromobacter_insolitus.yaml` contains three related
StrainInfo records whose normalized `taxon_id` fields point at
`NCBITaxon:1287737`; those are cross-evidence rows inside another generated
record, not a second generated record for `Achromobacter anxifer`.

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
