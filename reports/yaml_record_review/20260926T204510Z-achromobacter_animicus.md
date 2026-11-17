# YAML Record Review: Achromobacter animicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_animicus.yaml
- Started UTC: 2026-09-26T20:45:10Z
- Finished UTC: 2026-09-26T20:45:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_animicus.yaml` |
| Identifier | `NCBITaxon:1389935` |
| Label | `Achromobacter animicus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, BV-BRC, and NCBI
assembly inputs. Its path is pinned by `data/taxa/PATHS.tsv:141628`, and all
reviewed fields are owned by the seeder, `curation/seed_scope.tsv`, or
upstream kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_animicus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_agilis.yaml data/taxa/bacteria/achromobacter_aloeverae.yaml data/taxa/bacteria/achromobacter_animicus.yaml data/taxa/bacteria/achromobacter_anxifer.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,823 YAML lines, 9 lineage entries, 8 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 1 exact and 2 related NCBI synonyms, 2 xrefs, 4 BacDive strains, 27 genome assemblies, 21 genome records, 74 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, MADIN, BactoTraits, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:340744`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 6 native GOLD organisms, 3 native GOLD projects, 3 native GOLD analyses, 4 BacDive rows, 9 culture-collection rows, 9 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 24 raw strain-assembly rows, 18 raw strain-genome rows, 58 raw strain-related rows, 3 StrainInfo assembly rows, 13 StrainInfo related rows, 3 direct StrainInfo hits, 6 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1389935` resolves in the committed NCBI inventory to label
`Achromobacter animicus`, rank `SPECIES`, parent `NCBITaxon:222`, genetic code
`11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1117180` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation, the exact synonym
`Achromobacter genogroup 6`, and the two related synonyms. LPSN row
`lpsn:790791` supports the legitimate, validly published, correct species name,
authority `Vandamme et al. 2013`, type-strain aliases `CCUG-61966`,
`DSM-29601`, and `LMG-26690`, and sequence accession `INSDC:HE613448`.

The GTDB evidence is the single `GTDB:s__Achromobacter_animicus` closeMatch row
with `genome_count: 18`. The BacDive, culture-collection, GOLD, BV-BRC,
NCBI-assembly, StrainInfo, and ATB inputs support four BacDive strain blocks,
including one type strain, 9 culture-collection aliases, 27 genome assemblies,
21 genome records, and 74 related records. Three ATB genome records are backed
by `atb.assembly:202505.SAMEA6647241`,
`atb.assembly:202505.SAMEA6797392`, and
`atb.assembly:202505.SAMEA6797393`.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 6 organisms, MediaDive asserts 1 medium, MADIN asserts 1 trait, and
BactoTraits asserts 1 trait for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:1019`, which records
`NCBITaxon:1389935` as added on `2026-09-12` with reason `attested rule:
Achromobacter animicus, 8 sources incl. NCBI`.

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
