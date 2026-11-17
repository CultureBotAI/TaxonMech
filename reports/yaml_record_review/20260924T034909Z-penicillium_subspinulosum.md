# Review: Penicillium subspinulosum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_subspinulosum.yaml`
- Target: `NCBITaxon:311491`

## Target

The record grounds `Penicillium subspinulosum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 63767.

## Validation

- `just validate data/taxa/eukaryota/penicillium_subspinulosum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sterculiniicola.yaml data/taxa/eukaryota/penicillium_submersum.yaml data/taxa/eukaryota/penicillium_subrubescens.yaml data/taxa/eukaryota/penicillium_subspinulosum.yaml`: scanned 4 files with 0 files with errors and 0 total error rows
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55136 with the expected reason: `attested rule: Penicillium subspinulosum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. NRRL 28144` and `Penicillium subspinulosum Houbraken, 2014`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 6152 maps old ID `NCBITaxon:116977` into `NCBITaxon:311491`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 63767.
- GOLD aggregate: line 31438 records `organism_count=1` for `NCBITaxon:311491`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: four exact rows at lines 168640-168643, all culture from holotype, covering `CBS 137946` / `CBS:137946` and `DTO041-F2` / `DTO:041-F2`.
- StrainInfo: exact StrainInfo has 2 direct strains and 2 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:311491`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:116977` ID is consumed only through the merge map, not as a retained source row.
