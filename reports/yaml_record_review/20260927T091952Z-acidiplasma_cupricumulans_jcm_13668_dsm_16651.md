# YAML Record Review: Acidiplasma cupricumulans JCM 13668 = DSM 16651

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml
- Started UTC: 2026-09-27T09:19:52Z
- Finished UTC: 2026-09-27T09:19:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml` |
| Identifier | `NCBITaxon:1295373` |
| Label | `Acidiplasma cupricumulans JCM 13668 = DSM 16651` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:312540` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBI strain record with GTDB, BacDive, MediaDive, GOLD,
and genome-overlay evidence, with path pinned by `data/taxa/PATHS.tsv:102771`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidiplasma_aeolicum.yaml data/taxa/archaea/acidiplasma_cupricumulans.yaml data/taxa/archaea/acidiplasma_cupricumulans_jcm_13668_dsm_16651.yaml data/taxa/archaea/acidiplasma_sp.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 642 YAML lines, 10 lineage entries, 0 LPSN nomenclature entries, 1 GTDB mapping, 5 exact synonyms, 1 xref, 1 BacDive strain, 12 genome assemblies, 8 genome records, 26 related records, 5 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1295373` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, GTDB, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:304905`, 10 checked lineage rows with no mismatches, 1 GTDB mapping, 1 exact BacDive row, 1 MediaDive row with 2 media, 1 GOLD aggregate row with 1 organism, 1 native GOLD organism/project/analysis chain, 9 strain assemblies, 7 genome records, 20 related records, and no LPSN, MADIN, BactoTraits, exact StrainInfo, NCBI type-material, or NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1295373` resolves to label `Acidiplasma cupricumulans JCM 13668 =
DSM 16651`, rank `STRAIN`, parent `NCBITaxon:312540`, genetic code `11`, source
set `ncbitaxon|gtdb|bacdive|mediadive|gold`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through species `NCBITaxon:312540` Acidiplasma
cupricumulans. The bounded scan found no NCBI merge row and no retained old-id
row.

## Evidence

NCBI supplies exact synonyms for BH2, DSM 16651, JCM 13668, and the old
Ferroplasma combination. No LPSN nomenclature row maps directly to the NCBI
strain taxon, so no type-strain designations or LPSN xref are expected here.

BacDive exact row `bacdive:5460` supplies BH2 with deposits DSM 16651 and JCM
13668. The strain block carries BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and
StrainInfo overlay links that produce 12 assembly, 8 genome, and 26 related
rows in the generated record.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, GTDB, BacDive, MediaDive, GOLD,
native GOLD, seed, path, and YAML inputs, and found no omitted NCBI merge, LPSN,
MADIN, BactoTraits, exact StrainInfo, or type-material row.

The exact GOLD organism `Go0093115`, project `Gp0093115`, and analysis
`Ga0128368` support the generated GOLD strain-genome and related-record links.
StrainInfo rows are inherited through the BacDive strain overlay, not through an
exact StrainInfo taxon row keyed to `NCBITaxon:1295373`.

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
`strain_count: 1` matches the single exact BacDive BH2 strain.
The generated xref is the retained GTDB species.
The `MEDIADIVE` row contributes 2 media to this strain taxon.
NCBI Assembly contributes both GenBank and RefSeq accessions for JCM 13668.
The StrainInfo overlay contributes DSM 16651 and JCM 13668 deposit links.
No direct LPSN xref is expected on this strain-level NCBI record.
No upstream side row needs staging in kg-microbe or the seeder.
The ignored report probe included gitignored files.
