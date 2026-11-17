# YAML Record Review: Acidianus brierleyi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_brierleyi.yaml
- Started UTC: 2026-09-27T08:25:14Z
- Finished UTC: 2026-09-27T08:25:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_brierleyi.yaml` |
| Identifier | `NCBITaxon:41673` |
| Label | `Acidianus brierleyi` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is generated from NCBI, LPSN, GTDB, BacDive, GOLD, MediaDive, MADIN,
BV-BRC, NCBI Assembly, and StrainInfo; path `data/taxa/PATHS.tsv:498669`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_brierleyi.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidarchaeum_fankouense_seqcode.yaml data/taxa/archaea/acidianus_ambivalens.yaml data/taxa/archaea/acidianus_brierleyi.yaml data/taxa/archaea/acidianus_convivator.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 921 YAML lines, 9 lineage entries, 7 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch`, 5 synonyms, 2 xrefs, 2 BacDive strains, 12 genome assemblies, 9 genome records, 41 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:41673` in the expected seed, NCBI, GTDB mapping, path, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:4858`, LPSN row `lpsn:772573`, GTDB `s__Aramenus_brierleyi`, 2 BacDive strains, 1 GOLD aggregate row, 4 native GOLD organisms, 2 native GOLD projects, 1 native GOLD analysis, 4 culture-collection rows, 11 raw strain-assembly rows, 9 raw strain-genome rows, 28 raw strain-related rows, 1 StrainInfo assembly row, 13 StrainInfo related rows, 2 StrainInfo direct rows with 5 deposits, 8 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, and no NCBI merge, BactoTraits, or StrainInfo exclusion row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:41673` resolves to label `Acidianus brierleyi`, rank `SPECIES`,
parent `NCBITaxon:12914`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:12914` Acidianus. The bounded
scan found no NCBI merge row and no retained old-id row that would change the
active identifier.

## Evidence

The LPSN row `lpsn:772573` supports the legitimate, validly published, correct
name, four type-strain designations, accession `INSDC:D26489`, the same NCBI
ID, and synonym `Sulfolobus brierleyi`. The GTDB mapping retains
`GTDB:s__Aramenus_brierleyi` as a `skos:closeMatch`.

The two BacDive rows account for both emitted local strains: type-strain
`bacdive:16640` with `DSM 1651`, `IFO 15269`, and `NBRC 15269`, and non-type
`bacdive:16641` with designation `Sp3a/1` and `DSM 6334`. Their blocks fold in
BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo normalized evidence.

Retained side evidence matches the attestations: MediaDive contributes 4 media,
MADIN contributes 10 trait assertions, GOLD contributes 5 organism assertions
with projects `Gp0002296` and `Gp0376662`, and StrainInfo carries exact SI-IDs
for the type-strain and `DSM 6334` rows.

The seed event is supported by `curation/seed_scope.tsv:5224`, which records
`NCBITaxon:41673` as added on `2026-09-12` with reason `attested rule:
Acidianus brierleyi, 7 sources incl. NCBI`.

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
