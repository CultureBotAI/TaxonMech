# YAML Record Review: Achromobacter aegrifaciens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_aegrifaciens.yaml
- Started UTC: 2026-09-26T20:39:47Z
- Finished UTC: 2026-09-26T20:39:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_aegrifaciens.yaml` |
| Identifier | `NCBITaxon:1287736` |
| Label | `Achromobacter aegrifaciens` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, BV-BRC, and NCBI
assembly inputs. Its path is pinned by `data/taxa/PATHS.tsv:99526`, and all
reviewed fields are owned by the seeder, `curation/seed_scope.tsv`, or
upstream kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_aegrifaciens.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromatium_sp_wms2.yaml data/taxa/bacteria/achromatium_sp_wms3.yaml data/taxa/bacteria/achromobacter_aegrifaciens.yaml data/taxa/bacteria/achromobacter_agile.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1,693 YAML lines, 9 lineage entries, 8 source attestations, 1 LPSN nomenclature entry, 2 GTDB `skos:broadMatch` mappings, 7 NCBI synonyms, 2 xrefs, 8 BacDive strains, 18 genome assemblies, 14 genome records, 68 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/legacy_page_paths.tsv`, `curation/seed_scope.tsv`, NCBI, LPSN, GTDB, GOLD, BacDive, MediaDive, MADIN, BactoTraits, type-material, culture-collection, normalized strain, ATB, `data/taxa/PATHS.tsv`, and generated YAML rows; found seven cross-record related-row references in `achromobacter_denitrificans.yaml`; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:301759`, 9 checked lineage entries with no missing rows or mismatches, 4 NCBI merge rows, 1 LPSN row, 2 GTDB broadMatch rows, 1 GOLD aggregate row, 5 native GOLD organisms, 5 native GOLD projects, 5 native GOLD analyses, 8 BacDive JSONL records, 8 normalized BacDive rows, 16 culture-collection rows, 5 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 16 raw strain-assembly rows, 12 raw strain-genome rows, 36 raw strain-related rows, 2 StrainInfo assembly rows, 39 StrainInfo related rows, 14 direct StrainInfo hits, 23 StrainInfo deposit hits, and 0 StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1287736` resolves in the committed NCBI inventory to label
`Achromobacter aegrifaciens`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and
taxonomy snapshot `2026-09-13`. The generated record carries those same
identity fields and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. Four NCBI
merge rows retire `NCBITaxon:1389623`, `NCBITaxon:1389636`,
`NCBITaxon:1806481`, and `NCBITaxon:2479855` into this identifier, and the
bounded scan found no retained raw `ncbitaxon_taxa.tsv` rows for those old IDs.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:1287736`, source label `Achromobacter aegrifaciens`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match. The seven YAML synonyms preserve the one exact synonym and six
related synonyms from that NCBI row.

The LPSN evidence is supported by `lpsn:791414`, which records the same species
name, the authority `Vandamme et al. 2014`, legitimate and validly-published
correct-name flags, URL `/species/achromobacter-aegrifaciens`, type-strain
aliases `CCUG-62438` and `LMG-26852`, three publication identifiers, and
`INSDC:HF586507`.

The GTDB evidence is supported by two committed `skos:broadMatch` rows:
`GTDB:s__Achromobacter_aegrifaciens` with 16 genomes and
`GTDB:s__Achromobacter_bronchisepticus_A` with 10 genomes. The YAML preserves
both mappings and uses the former as the representative GTDB source
attestation with `assertion_count: 16` and a note pointing back to
`taxonomy_mappings`.

The BacDive, culture-collection, StrainInfo, GOLD, BV-BRC, ATB, and assembly
inputs support 8 generated BacDive strain blocks. They include one type strain
block for BacDive 156528 / LMG 26852 / CCUG 62438, 16 culture-collection
aliases, 18 normalized genome assemblies, 14 genome records, and 68 related
records. Two AllTheBacteria genome records are backed by
`atb.assembly:202505.SAMEA6647245` for LMG 26852 and
`atb.assembly:202505.SAMEA6797398` for LMG 26854.

The remaining source attestations line up with the compact provider rows: GOLD
asserts 5 organisms, MediaDive asserts 2 media, MADIN asserts 1 trait, and
BactoTraits asserts 1 trait for the same NCBI taxon.

The seed event is supported by `curation/seed_scope.tsv:424`, which records
`NCBITaxon:1287736` as added on `2026-09-12` with reason `attested rule:
Achromobacter aegrifaciens, 8 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this rich generated record. The
exact and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive,
MediaDive, GOLD, MADIN, BactoTraits, StrainInfo, ATB, culture-collection,
type-material, normalized assembly, normalized genome, normalized
related-record, and generated YAML inputs for this taxon.

The exact scan also found an old `curation/legacy_page_paths.tsv` entry for the
same taxon. That row only records the historical HTML path and does not imply
an omitted `TaxonRecord` field.

`data/taxa/bacteria/achromobacter_denitrificans.yaml` contains seven related
StrainInfo records whose normalized `taxon_id` fields point at
`NCBITaxon:1287736`; those are cross-evidence rows inside another generated
record, not a second generated record for `Achromobacter aegrifaciens`.

The NCBI merge rows are represented by the current target identifier rather
than as YAML xrefs, and the bounded scan found no retained raw NCBI rows for
the four old identifiers.

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
