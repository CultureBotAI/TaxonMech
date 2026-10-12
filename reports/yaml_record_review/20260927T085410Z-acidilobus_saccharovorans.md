# YAML Record Review: Acidilobus saccharovorans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobus_saccharovorans.yaml
- Started UTC: 2026-09-27T08:54:10Z
- Finished UTC: 2026-09-27T08:54:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobus_saccharovorans.yaml` |
| Identifier | `NCBITaxon:242703` |
| Label | `Acidilobus saccharovorans` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:105850` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated type-strain species record with LPSN, BacDive,
MediaDive, GOLD, MADIN, GTDB xref, and StrainInfo support.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobus_saccharovorans.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidilobales_archaeon.yaml data/taxa/archaea/acidilobus_aceticus.yaml data/taxa/archaea/acidilobus_saccharovorans.yaml data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 308 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 NCBI related synonym, 2 xrefs, 1 BacDive strain, 3 culture-collection IDs, 2 genome assemblies, 3 genome records, 11 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:242703` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no direct exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:47559`, 9 checked lineage entries, 1 LPSN row, 1 BacDive exact row, 1 MediaDive row with 2 media, 1 GOLD aggregate row with 2 organisms, 1 MADIN row, 2 native GOLD organisms, 7 NCBI type-material rows, 1 direct StrainInfo hit with 1 deposit, 3 culture-collection rows, 4 raw strain-related rows, 2 StrainInfo related rows, and no lineage mismatches. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:242703` resolves to label `Acidilobus saccharovorans`, rank
`SPECIES`, parent `NCBITaxon:105850`, genetic code `11`, source set
`ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:105850` Acidilobus. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

LPSN `lpsn:772592` supports legitimate, validly published, correct-name
nomenclature; the Prokofeva et al. 2009 authority; DSM 16705 type-strain
designation; DOI and PMID publication identifiers; and `INSDC:AY350586`.

BacDive `17800` contributes type strain 345-15 and DSM 16705, JCM 18335, and
VKM B-2471 collection IDs. GOLD supplies the 345-15 assembly and IMG genome
rows plus direct species related rows for VKM B-2471 and JCM 18335. StrainInfo
emits two DSM 16705 related records. The LPSN xref retains the GTDB species ID.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, MediaDive, GOLD,
MADIN, native GOLD, StrainInfo, type-material, seed, path, and YAML inputs, and
found no omitted NCBI merge, direct GTDB mapping, BactoTraits, normalized
species-level assembly, or StrainInfo exclusion row.

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
`strain_count: 1` matches the single BacDive-derived strain.
The direct GTDB `closeMatch` is filed to strain taxon `NCBITaxon:666510`.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
The LPSN xref carries the GTDB species as a side xref.
The type strain row is filed directly under the species taxon.
The native GOLD species rows are represented as related records.
No NCBI merge row complicates identity.
No StrainInfo exclusion row applies.
The ignored report probe included gitignored files.
