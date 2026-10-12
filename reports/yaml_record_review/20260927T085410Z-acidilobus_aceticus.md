# YAML Record Review: Acidilobus aceticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/acidilobus_aceticus.yaml
- Started UTC: 2026-09-27T08:54:10Z
- Finished UTC: 2026-09-27T08:54:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/archaea/acidilobus_aceticus.yaml` |
| Identifier | `NCBITaxon:105851` |
| Label | `Acidilobus aceticus` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `ARCHAEA` |
| Parent | `NCBITaxon:105850` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated type-strain species record with LPSN, BacDive,
MediaDive, GOLD, MADIN, NCBI Assembly, BV-BRC, and StrainInfo support.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/archaea/acidilobus_aceticus.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/archaea/acidilobales_archaeon.yaml data/taxa/archaea/acidilobus_aceticus.yaml data/taxa/archaea/acidilobus_saccharovorans.yaml data/taxa/archaea/acidilobus_saccharovorans_345_15.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 429 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 2 NCBI synonyms, 1 BacDive strain, 3 culture-collection IDs, 2 NCBI Assembly assemblies, 2 BV-BRC genome records, 20 related records, 6 source attestations, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:105851` in the expected seed, NCBI, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no exact GTDB mapping; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:18996`, 9 checked lineage entries, 1 LPSN row, 1 BacDive exact row, 1 MediaDive row with 2 media, 1 GOLD aggregate row with 4 organisms, 1 MADIN row with 5 assertions, 3 native GOLD organisms, 9 NCBI type-material rows, 3 exact StrainInfo deposits, 2 raw strain-assembly rows, 2 raw strain-genome rows, 13 raw strain-related rows, 7 StrainInfo related rows, 0 NCBI merge rows, and 0 StrainInfo exclusion rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:105851` resolves to label `Acidilobus aceticus`, rank `SPECIES`,
parent `NCBITaxon:105850`, genetic code `11`, source set
`ncbitaxon|bacdive|lpsn|mediadive|gold|madin_etal`, and taxonomy snapshot
`2026-09-13`. The generated record carries those fields and lands in `ARCHAEA`.

The lineage is root-first and matches the committed NCBI rows for all 9 stored
taxa, from `NCBITaxon:1` root through genus `NCBITaxon:105850` Acidilobus. The
bounded scan found no NCBI merge row and no retained old-id row.

## Evidence

LPSN `lpsn:772577` supports legitimate, validly published, correct-name
nomenclature; the Prokofeva et al. 2000 authority; ATCC BAA-268, DSM 11585,
and JCM 11320 type strain designations; DOI and PMID publication identifiers;
and `INSDC:AF191225`.

BacDive `17799` contributes strain 1904, the 3 collection IDs, and the single
base strain. NCBI Assembly emits `GCA_055392325.1` and `GCF_055392325.1`; BV-BRC
emits 2 PATRIC rows for JCM 11320; StrainInfo emits 3 deposits, 3 strain rows,
and the `INSDC:AB245528` sequence row. GOLD and MediaDive attest direct rows.

## Completeness

No consequential required generated claim is absent for this record. Exact and
bounded scans accounted for expected NCBI, LPSN, BacDive, MediaDive, GOLD,
MADIN, native GOLD, NCBI Assembly, BV-BRC, StrainInfo, type-material, seed,
path, and YAML inputs, and found no omitted NCBI merge, GTDB, BactoTraits,
StrainInfo assembly, or StrainInfo exclusion row.

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
The NCBI exact synonym `Acidolobus aceticus` is retained as exact.
No seeder, scope, or kg-microbe edit is indicated by this read-only review.
The report therefore has no follow-up curation item.
The LPSN xref is the only generated xref.
No GTDB species maps to this taxon in `data/raw/gtdb_mappings.tsv`.
The type strain row is filed directly under the species taxon.
The native GOLD rows are represented through related-record evidence.
The ignored report probe included gitignored files.
