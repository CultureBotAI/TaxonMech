# YAML Record Review: Methylobacterium gnaphalii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/methylobacterium_gnaphalii.yaml
- Started UTC: 2026-09-28T02:23:11Z
- Finished UTC: 2026-09-28T02:23:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/methylobacterium_gnaphalii.yaml` |
| Identifier | `NCBITaxon:1010610` |
| Label | `Methylobacterium gnaphalii` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:407` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated multi-source Methylobacterium species record,
with path pinned by `data/taxa/PATHS.tsv:3797`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/methylobacterium_gnaphalii.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_bd_89.yaml data/taxa/bacteria/bacillus_sp_bd_93.yaml data/taxa/bacteria/methylobacterium_gnaphalii.yaml data/taxa/bacteria/thalassovita_litoralis.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 1214 YAML lines, 9 lineage entries, 1 LPSN nomenclature entry, 2 synonyms, 2 xrefs, 1 BacDive type strain, 2 culture IDs, 26 genome assemblies, 19 genome records, 56 related rows, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1010610` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:212368`, 9 checked lineage rows, 1 LPSN row, 1 BacDive row, 1 GOLD aggregate row, 3 native GOLD organisms, 3 GOLD projects, 3 GOLD analyses, 1 MediaDive row, 1 MADIN row, 1 BactoTraits row, 6 type-material rows, and no NCBI merge rows. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1010610` resolves to `Methylobacterium gnaphalii`, rank `SPECIES`,
parent `NCBITaxon:407`, genetic code `11`, source set with eight upstreams,
and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 9 committed NCBI rows, ending at
`NCBITaxon:407` genus `Methylobacterium`; no NCBI merge row was retained.

## Evidence

The NCBI row supports the current species name, parent, genetic code, two
related synonyms, eight upstream source flags, and the 2026-09-13 snapshot date.

LPSN `lpsn:790288` supplies the legitimate correct-name nomenclature row,
type-strain designations DSM 24027 and NBRC 107716, three publications,
sequence accession `INSDC:AB627071`, and the LPSN xref.

BacDive `bacdive:7200` supplies the 23e type strain with two culture IDs.
GOLD contributes 3 organism rows and assembly/genome/related rows for 3 projects.
GTDB contributes the `skos:closeMatch` and 3 matched genome records; MediaDive,
MADIN, BactoTraits, BV-BRC, NCBI Assembly, and StrainInfo add retained rows.

## Completeness

No native `data/raw/gtdb_species.tsv`, NCBI merge, retained old-id,
StrainInfo exclusion, definition, or causal-graph row was filed.
The normalized raw inventories account for the generated assembly, genome,
and related-record counts under this exact NCBI taxon.

An ignored-file-inclusive `rg --no-ignore --hidden` check returned no existing
Markdown report for this stem before this report was written.

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
`strain_count: 1` is expected from the exact BacDive row.
The GTDB mapping is `GTDB:s__Methylobacterium_gnaphalii` with 3 genomes.
The GOLD source attestation preserves the aggregate organism count of 3.
The related records include GOLD, BV-BRC, NCBI Assembly, and StrainInfo evidence.
StrainInfo contributes one DSM 24027 assembly and two DSM 24027 related rows.
The NCBI synonyms are related, not exact, synonyms.
MediaDive contributes one medium; MADIN and BactoTraits contribute trait assertions.
The 26 assembly entries and 19 genome records are expected after source cross-links.
The 1214-line YAML shape is expected for this target.
The ignored report probe included gitignored files.
