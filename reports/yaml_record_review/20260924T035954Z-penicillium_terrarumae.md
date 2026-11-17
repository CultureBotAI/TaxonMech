# Review: Penicillium terrarumae

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_terrarumae.yaml`
- Target: `NCBITaxon:2608786`

## Target

The record grounds `Penicillium terrarumae` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 536687.

## Validation

- `just validate data/taxa/eukaryota/penicillium_terrarumae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_taurinense.yaml data/taxa/eukaryota/penicillium_terrarumae.yaml data/taxa/eukaryota/penicillium_terrenum.yaml data/taxa/eukaryota/penicillium_terrigenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 62905 with the expected reason: `attested rule: Penicillium terrarumae, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has four related synonyms, `Penicillium sp. CBS 131811`, `Penicillium sp. HGUP2025`, `Penicillium sp. XCW-2019a`, and `Penicillium terrarumae Houbraken, Q.X. Zhou, K.D. Hyde, McKenzie & Yong Wang bis, 2016`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 11948 maps old ID `NCBITaxon:1316193` into `NCBITaxon:2608786`, and line 31124 maps old ID `NCBITaxon:1885293` into `NCBITaxon:2608786`; exact retained-row greps of `data/raw/ncbitaxon_taxa.tsv` found no remaining rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 536687.
- GOLD aggregate: line 24068 records `organism_count=1` for `NCBITaxon:2608786`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: seven exact rows at lines 105914-105920, covering culture-from-holotype spellings for `DTO 174-H2` and `HGUP2025` plus holotype spellings for `HGUP d2021`.
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

The retired `NCBITaxon:1316193` and `NCBITaxon:1885293` IDs are consumed only through the merge map, not as retained source rows.
