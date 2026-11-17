# Review: Penicillium subrubescens

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_subrubescens.yaml`
- Target: `NCBITaxon:1316194`

## Target

The record grounds `Penicillium subrubescens` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 313267.

## Validation

- `just validate data/taxa/eukaryota/penicillium_subrubescens.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sterculiniicola.yaml data/taxa/eukaryota/penicillium_submersum.yaml data/taxa/eukaryota/penicillium_subrubescens.yaml data/taxa/eukaryota/penicillium_subspinulosum.yaml`: scanned 4 files with 0 files with errors and 0 total error rows
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59410 with the expected reason: `attested rule: Penicillium subrubescens, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium subrubescens Houbraken, Mansouri, Samson & Frisvad, 2012`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:1316194`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 313267.
- GOLD aggregate: line 7739 records `organism_count=7` for `NCBITaxon:1316194`, matching the YAML GOLD attestation count. Native GOLD exact rows include 7 unique organisms, 161 projects, and 1 analysis for this target.
- NCBI type material: 10 exact rows at lines 22074-22083, covering culture-from-holotype spellings for `CBS 132785`, `DTO 188-D6`, `FBCC 1632`, and `IBT 31985` plus holotype spellings for `CBS H-21029`.
- StrainInfo: exact StrainInfo has 2 direct strains and 2 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:1316194`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The 161 native GOLD projects all roll up to the seven aggregate organisms counted in the generated GOLD attestation.
