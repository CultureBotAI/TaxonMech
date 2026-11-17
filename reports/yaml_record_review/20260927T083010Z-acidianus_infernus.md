# YAML Record Review: Acidianus infernus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_infernus.yaml
- Started UTC: 2026-09-27T08:30:10Z
- Finished UTC: 2026-09-27T08:30:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_infernus.yaml` |
| Identifier | `NCBITaxon:12915` |
| Label | `Acidianus infernus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:12914` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is generated from NCBI, LPSN, GTDB, BacDive, GOLD, MediaDive, MADIN,
BV-BRC, NCBI Assembly, and StrainInfo; path `data/taxa/PATHS.tsv:100664`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_infernus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_hospitalis.yaml data/taxa/archaea/acidianus_hospitalis_w1.yaml data/taxa/archaea/acidianus_infernus.yaml data/taxa/archaea/acidianus_manzaensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 795 YAML lines, 9 lineage entries, 7 source attestations, 1 LPSN nomenclature entry, 1 GTDB `skos:closeMatch`, 1 synonym, 2 xrefs, 1 BacDive type strain, 10 genome assemblies, 7 genome records, 35 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:12915` in the expected seed, NCBI, GTDB mapping, path, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:2649`, LPSN row `lpsn:772574`, GTDB `s__Acidianus_infernus`, 1 BacDive strain, 1 GOLD aggregate row, 3 native GOLD organisms, 1 native GOLD project, 1 native GOLD analysis, 5 culture-collection rows, 9 raw strain-assembly rows, 7 raw strain-genome rows, 23 raw strain-related rows, 1 StrainInfo assembly row, 12 StrainInfo related rows, 1 StrainInfo direct row with 4 deposits, 10 NCBI type-material rows, 1 MediaDive row, 1 MADIN row, and no NCBI merge, BactoTraits, or StrainInfo exclusion row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:12915` resolves to label `Acidianus infernus`, rank `SPECIES`,
parent `NCBITaxon:12914`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those same fields.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:12914` Acidianus. The bounded
scan found no NCBI merge row and no retained old-id row.

## Evidence

The LPSN row `lpsn:772574` supports the legitimate, validly published, correct
name, four type-strain designations, accession `INSDC:D85505`, the same NCBI
ID, and GTDB species `GTDB:s__Acidianus_infernus`. The GTDB mapping is a
`skos:closeMatch` with genome count 3.

The BacDive row `bacdive:16642` accounts for emitted local type strain So4a and
its five culture-collection IDs: `DSM 3191`, `IFO 15270`, `JCM 8955`,
`NBRC 106462`, and `NBRC 15270`. Its strain block folds in BV-BRC, GOLD, GTDB,
NCBI Assembly, and StrainInfo assembly, genome, and related-record evidence.

Retained side evidence matches the attestations: MediaDive contributes 3 media,
MADIN contributes 3 trait assertions, GOLD contributes 3 organism assertions
and project `Gp0548892`, StrainInfo carries one exact SI-ID with 4 deposits,
and NCBI contributes 10 type-strain material aliases for Acidianus infernus.

The seed event is supported by `curation/seed_scope.tsv:5592`, which records
`NCBITaxon:12915` as added on `2026-09-12` with reason `attested rule:
Acidianus infernus, 7 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated record. Exact and
bounded scans accounted for the NCBI, LPSN, GTDB, BacDive, GOLD, MediaDive,
MADIN, culture-collection, normalized strain, StrainInfo, path, seed, and YAML
inputs, and found no omitted NCBI merge, BactoTraits, StrainInfo exclusion, or
causal-graph row for this taxon.

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
