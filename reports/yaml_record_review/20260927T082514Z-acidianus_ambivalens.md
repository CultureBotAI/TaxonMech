# YAML Record Review: Acidianus ambivalens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_ambivalens.yaml
- Started UTC: 2026-09-27T08:25:14Z
- Finished UTC: 2026-09-27T08:25:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_ambivalens.yaml` |
| Identifier | `NCBITaxon:2283` |
| Label | `Acidianus ambivalens` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is generated from NCBI, LPSN, GTDB, BacDive, GOLD, MediaDive, MADIN,
BV-BRC, NCBI Assembly, and StrainInfo; path `data/taxa/PATHS.tsv:336041`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_ambivalens.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidarchaeum_fankouense_seqcode.yaml data/taxa/archaea/acidianus_ambivalens.yaml data/taxa/archaea/acidianus_brierleyi.yaml data/taxa/archaea/acidianus_convivator.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 1125 YAML lines, 9 lineage entries, 7 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch`, 5 synonyms, 2 xrefs, 1 BacDive type strain, 12 genome assemblies, 10 genome records, 49 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:2283` in the expected seed, NCBI, GTDB mapping, path, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:1799`, LPSN row `lpsn:772572`, GTDB `s__Acidianus_ambivalens`, 1 BacDive strain, 1 GOLD aggregate row, 4 native GOLD organisms, 2 native GOLD projects, 2 native GOLD analyses, 3 culture-collection rows, 11 raw strain-assembly rows, 10 raw strain-genome rows, 27 raw strain-related rows, 1 StrainInfo assembly row, 22 StrainInfo related rows, 1 StrainInfo direct row with 3 deposits, 8 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, and no NCBI merge, BactoTraits, or StrainInfo exclusion row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:2283` resolves to label `Acidianus ambivalens`, rank `SPECIES`,
parent `NCBITaxon:12914`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:12914` Acidianus. The bounded
scan found no NCBI merge row and no retained old-id row that would change the
active identifier.

## Evidence

The LPSN row `lpsn:772572` supports the legitimate, validly published, correct
name, type-strain designations `CIP 104912`, `DSM 3772`, and `JCM 9191`,
accession `INSDC:D85506`, the same NCBI ID, and the GTDB species
`GTDB:s__Acidianus_ambivalens`, retained as `skos:closeMatch`.

The single BacDive seed row `bacdive:16643` accounts for the local strain
`kgmicrobe.strain:bacdive_16643` and its three culture-collection identifiers,
then folds in BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo assembly,
genome, and related-record evidence from normalized strain tables.

Retained side evidence matches the attestations: MediaDive contributes 3 media,
MADIN contributes 5 trait assertions, GOLD contributes 4 organism assertions
with projects `Gp0548891` and `Gp0551223`, and StrainInfo carries one SI-ID
with `DSM 3772`, `JCM 9191`, and `CIP 104912` deposits.

The seed event is supported by `curation/seed_scope.tsv:5586`, which records
`NCBITaxon:2283` as added on `2026-09-12` with reason `attested rule:
Acidianus ambivalens, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. Exact and
bounded scans accounted for NCBI, LPSN, GTDB, BacDive, GOLD, MediaDive, MADIN,
culture-collection, normalized strain, StrainInfo, path, seed, and YAML inputs,
and found no omitted NCBI merge, BactoTraits, StrainInfo exclusion, or graph row.

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

This was a read-only generated-record review; it did not append history, promote `mapping_status`, or touch YAML.
