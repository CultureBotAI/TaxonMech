# YAML Record Review: Acidianus sulfidivorans JP7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml
- Started UTC: 2026-09-27T08:46:57Z
- Finished UTC: 2026-09-27T08:46:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml` |
| Identifier | `NCBITaxon:619593` |
| Label | `Acidianus sulfidivorans JP7` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:312539` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated strain record with GTDB, BacDive, MediaDive, and MADIN
support, with path pinned by `data/taxa/PATHS.tsv:552262`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidianus_sp_syk_eso_2.yaml data/taxa/archaea/acidianus_sulfidivorans.yaml data/taxa/archaea/acidianus_sulfidivorans_jp7.yaml data/taxa/archaea/acidianus_tengchongensis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 314 YAML lines, 10 lineage entries, 1 GTDB `closeMatch`, 3 exact synonyms, 1 xref, 1 BacDive strain, 3 genome assemblies, 4 genome records, 11 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:619593` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:142922`, the GTDB row at `data/raw/gtdb_mappings.tsv:299830`, 10 checked lineage entries with no missing rows or mismatches, 1 BacDive exact row, 1 MediaDive row with 2 media, 1 MADIN row with 4 assertions, 1 native GOLD organism, 1 BacDive strain row, 2 culture-collection rows, 3 raw strain-assembly rows, 4 raw strain-genome rows, 5 raw strain-related rows, 0 NCBI merge rows, and no StrainInfo rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:619593` resolves to label `Acidianus sulfidivorans JP7`, rank
`STRAIN`, parent `NCBITaxon:312539`, genetic code `11`, source set
`ncbitaxon|gtdb|bacdive|mediadive|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through species `NCBITaxon:312539` Acidianus
sulfidivorans. The bounded scan found no NCBI merge row.

## Evidence

GTDB species `GTDB:s__Acidianus_sulfidivorans` maps to this strain with
`skos:closeMatch` and `genome_count: 1`; the generated mapping, xref, GTDB
attestation, and `Acidianus sulfidivorans` exact synonym mirror that row.

BacDive `16644` contributes the JP7 base strain, DSM 18786 and JCM 13667
culture-collection IDs, 3 assembly rows, and 4 genome rows. The related-record
section mirrors 5 direct JP7 rows plus GOLD and StrainInfo rows from the species.

MediaDive contributes 2 media and MADIN contributes 4 trait assertions for the
strain. Native GOLD has organism `Go0002318`, but no retained GOLD aggregate
row emits a GOLD source attestation on the strain YAML.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, MediaDive, MADIN,
native GOLD, normalized strain, culture-collection, genome, related-record,
seed, path, and YAML inputs, and found no omitted LPSN, BactoTraits,
type-material, NCBI merge, GOLD aggregate, or StrainInfo row.

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
`Acidianus sp. JP7` and `Acidianus sulfidivorans DSM 18786` come from NCBI.
The GTDB exact synonym comes from the seeded GTDB mapping.
`strain_count: 1` matches the single BacDive-derived JP7 strain.
The JP7 record intentionally repeats species-filed GOLD and StrainInfo related
rows that match DSM 18786 or JCM 13667.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
