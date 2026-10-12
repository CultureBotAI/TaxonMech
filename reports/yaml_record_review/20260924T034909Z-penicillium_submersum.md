# Review: Penicillium submersum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_submersum.yaml`
- Target: `NCBITaxon:2745099`

## Target

The record grounds `Penicillium submersum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 549930.

## Validation

- `just validate data/taxa/eukaryota/penicillium_submersum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sterculiniicola.yaml data/taxa/eukaryota/penicillium_submersum.yaml data/taxa/eukaryota/penicillium_subrubescens.yaml data/taxa/eukaryota/penicillium_subspinulosum.yaml`: scanned 4 files with 0 files with errors and 0 total error rows
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63183 with the expected reason: `attested rule: Penicillium submersum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. 5 DT-2020` and `Penicillium submersum Torres-Garcia, Gene & Dania Garcia, 2022`; the YAML mirrors those values.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:2745099`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 549930.
- GOLD aggregate: line 25839 records `organism_count=1` for `NCBITaxon:2745099`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: 12 exact rows at lines 116659-116670, covering culture-from-holotype spellings for `CBS 148242` and `FMR 17140` plus holotype spellings for `CBS H-24785`.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The source evidence has no exact BacDive, StrainInfo, or native GOLD expansion beyond the GOLD aggregate support used for seeding.
