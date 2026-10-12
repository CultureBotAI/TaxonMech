# YAML Record Review: Archaeoglobus veneficus SNP6

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/archaeoglobus_veneficus_snp6.yaml
- Started UTC: 2026-09-27T11:15:48Z
- Finished UTC: 2026-09-27T11:15:48Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/archaeoglobus_veneficus_snp6.yaml` |
| Identifier | `NCBITaxon:693661` |
| Label | `Archaeoglobus veneficus SNP6` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:58290` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multisource strain record with BacDive, GOLD, GTDB,
MediaDive, and MADIN attestations, with path pinned by
`data/taxa/PATHS.tsv:573573`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/archaeoglobus_veneficus_snp6.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/archaeoglobus_veneficus.yaml data/taxa/archaea/archaeoglobus_veneficus_snp6.yaml data/taxa/archaea/archaeon.yaml data/taxa/archaea/archaeon_13_1_20cm_2_51_10.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed 447 YAML lines, 10 lineage entries, 6 source attestations across NCBITAXON, BACDIVE, GOLD, GTDB, MADIN, and MEDIADIVE, 1 GTDB taxonomy mapping, 4 exact synonyms, 1 xref, 1 BacDive strain, 3 genome assemblies, 4 genome records, 17 related records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:693661` in the expected seed, NCBI, GTDB, `data/taxa/PATHS.tsv`, generated target YAML, and parent-species related-record YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:162891`, 10 checked lineage entries with no missing rows or mismatches, 0 NCBI merge rows, 1 GTDB mapping row, 1 retained GOLD aggregate row, 1 native GOLD organism row, 1 native GOLD project row, 1 native GOLD analysis row, 1 MediaDive row, 1 MADIN row, 1 exact BacDive row, 1 raw BacDive row, 1 culture-collection row, 3 raw assembly rows, 4 raw genome rows, 10 raw related rows, and no exact LPSN, BactoTraits, StrainInfo, or NCBI type-material rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:693661` resolves to label `Archaeoglobus veneficus SNP6`, rank
`STRAIN`, parent `NCBITaxon:58290`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:58290` Archaeoglobus veneficus. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the strain identity, parent species, three NCBI exact
synonyms, the six-source attestation set, genetic code, and 2026-09-13 snapshot
date; the seed event is supported by `curation/seed_scope.tsv:10439`.

The GTDB row at `data/raw/gtdb_mappings.tsv:302667` supports the closeMatch
mapping to `GTDB:s__Archaeoglobus_C_veneficus`, the generated GTDB exact
synonym, the GTDB xref, and its one-genome assertion count.

BacDive exact row `data/raw/bacdive_strains.tsv:17906` and raw row 17907
support the generated bacdive:18098 strain, SNP6 designation, DSM-11195 culture
ID, and the LPSN back-reference. MediaDive row 12771 and MADIN row 29359
support one medium and five trait assertions.

The retained GOLD aggregate at `data/raw/gold_organism_counts.tsv:41456`
supports the GOLD attestation. Native GOLD rows tie Go0003485, Gp0003485, and
one analysis row to this strain; normalized tables retain 3 assembly rows, 4
genome rows, and 10 GOLD related records under the same exact taxon.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, seed, path, GTDB, BacDive, GOLD,
MediaDive, MADIN, and normalized GOLD inputs, and found no omitted exact LPSN,
BactoTraits, StrainInfo, or NCBI type-material row.

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
The ignored report probe included gitignored files.
