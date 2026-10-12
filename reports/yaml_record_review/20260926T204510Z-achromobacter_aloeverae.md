# YAML Record Review: Achromobacter aloeverae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/achromobacter_aloeverae.yaml
- Started UTC: 2026-09-26T20:45:10Z
- Finished UTC: 2026-09-26T20:45:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/achromobacter_aloeverae.yaml` |
| Identifier | `NCBITaxon:1750518` |
| Label | `Achromobacter aloeverae` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:222` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from NCBI, GTDB, LPSN, BacDive, GOLD,
and StrainInfo inputs. Its path is pinned by `data/taxa/PATHS.tsv:263513`, and
all reviewed fields are owned by the seeder, `curation/seed_scope.tsv`, or
upstream kg-microbe inputs rather than this YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/achromobacter_aloeverae.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/achromobacter_agilis.yaml data/taxa/bacteria/achromobacter_aloeverae.yaml data/taxa/bacteria/achromobacter_animicus.yaml data/taxa/bacteria/achromobacter_anxifer.yaml` | Passed the four-file strict batch with 4 files scanned, 0 files in error, and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 203 YAML lines, 9 lineage entries, 5 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch` mapping, 3 NCBI related synonyms, 1 GTDB exact synonym, 2 xrefs, 1 BacDive strain, 2 genome assemblies, 2 genome records, 2 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected seed, legacy path, NCBI, LPSN, GTDB, GOLD, BacDive, type-material, culture-collection, normalized strain, `data/taxa/PATHS.tsv`, and generated YAML rows; found no ATB row and no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:456947`, 9 checked lineage entries with no missing rows or mismatches, 1 NCBI merge row, 1 LPSN row, 1 GTDB closeMatch row, 1 GOLD aggregate row, 1 native GOLD organism/project/analysis, 1 BacDive row, 4 culture-collection rows, 12 NCBI type-material rows, 2 raw strain-assembly rows, 2 raw strain-genome rows, 2 StrainInfo related rows, 1 direct StrainInfo hit, 1 StrainInfo deposit hit, and 0 raw strain-related, StrainInfo assembly, or StrainInfo exclusion rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1750518` resolves in the committed NCBI inventory to label
`Achromobacter aloeverae`, rank `SPECIES`, parent `NCBITaxon:222`, genetic
code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and taxonomy
snapshot `2026-09-13`. The generated record carries those same identity fields
and correctly lands in the `bacteria` path bucket through
`taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:222` Achromobacter. One NCBI
merge row retires `NCBITaxon:1836984` into this identifier, and the bounded
scan found no retained raw `ncbitaxon_taxa.tsv` row for that old ID.

## Evidence

The NCBI row supports the `NCBITAXON` source attestation and the three NCBI
related synonyms. LPSN row `lpsn:795050` supports the legitimate, validly
published, correct species name, authority `Kuncharoen et al. 2017`,
type-strain aliases `LMG-29108` and `NBRC-111463`, and sequence accession
`INSDC:MT758162`.

The GTDB evidence is the single `GTDB:s__Bordetella_C_aloeverae` closeMatch
row with `genome_count: 2`; the YAML preserves that mapping, the same xref, and
the GTDB exact synonym `Bordetella C aloeverae`. The BacDive and
culture-collection rows support one generated type-strain block for BacDive
133323 / AVA-1 with four collection aliases, two BacDive genome assemblies,
and two BacDive genome records.

The seed event is supported by `curation/seed_scope.tsv:16271`, which records
`NCBITaxon:1750518` as added on `2026-09-12` with reason `attested rule:
Achromobacter aloeverae, 5 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. The exact
and bounded scans account for the expected NCBI, GTDB, LPSN, BacDive, GOLD,
StrainInfo, culture-collection, type-material, normalized assembly, normalized
genome, normalized related-record, and generated YAML inputs, and found no ATB,
Madin, MediaDive, BactoTraits, raw strain-related, StrainInfo assembly, or
StrainInfo exclusion row for this taxon.

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
