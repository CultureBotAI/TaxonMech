# YAML Record Review: Acidiplasma sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidiplasma_sp.yaml
- Started UTC: 2026-09-27T09:19:52Z
- Finished UTC: 2026-09-27T09:19:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidiplasma_sp.yaml` |
| Identifier | `NCBITaxon:1872114` |
| Label | `Acidiplasma sp.` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:2641301` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI species-level record under unclassified
Acidiplasma with three pooled GTDB broad mappings and path pinned by
`data/taxa/PATHS.tsv:296633`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidiplasma_sp.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_aeolicum.yaml data/taxa/archaea/acidiplasma_cupricumulans.yaml data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml data/taxa/archaea/acidiplasma_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 83 YAML lines, 10 lineage entries, 0 LPSN nomenclature entries, 3 GTDB taxonomy mappings, 0 synonyms, 0 xrefs, 0 strains, 0 genome assemblies, 0 genome records, 2 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1872114` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:489195`, 10 checked lineage rows with no mismatches, 3 broad GTDB mapping rows, 0 NCBI merge rows, and no LPSN, BacDive, MediaDive, GOLD, MADIN, BactoTraits, native GOLD, StrainInfo, type-material, strain-assembly, genome-record, or related-record rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1872114` resolves to label `Acidiplasma sp.`, rank `SPECIES`, parent
`NCBITaxon:2641301`, genetic code `11`, source set `ncbitaxon|gtdb`, and
taxonomy snapshot `2026-09-13`. The generated record carries those fields and
lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2641301` unclassified
Acidiplasma. The bounded scan found no NCBI merge row and no retained old-id
row.

## Evidence

NCBI supplies no exact, broad, or related synonyms for this placeholder species.
The generated record therefore correctly has no `synonyms`, `nomenclature`, or
`xrefs` section.

GTDB supplies 3 `skos:broadMatch` rows for
`GTDB:s__Acidiplasma_aeolicum`, `GTDB:s__Acidiplasma_sp021846395`, and
`GTDB:s__Acidiplasma_sp021835025`, with 17, 8, and 6 genomes respectively. The
record keeps them as pooled broad mappings and exposes only the primary 17
genomes in the GTDB source attestation.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, seed, path, and YAML inputs,
and found no omitted NCBI merge, LPSN, BacDive, MediaDive, GOLD, MADIN,
BactoTraits, native GOLD, StrainInfo, type-material, or final strain rows.

The absence of strains and genome records is expected: no BacDive-derived row
or final strain overlay row is keyed to `NCBITaxon:1872114`.

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
`strain_count: 0` is expected without a retained BacDive or normalized strain row.
The three generated GTDB entries are broad mappings, not identity xrefs.
No generated xref section is expected.
No LPSN row maps directly to this placeholder species.
No GOLD or MADIN attestation is expected.
The GTDB source attestation correctly names only the first pooled mapping.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
