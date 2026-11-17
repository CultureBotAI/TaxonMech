# Review: Penicillium sp. str. #12

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sp_str_12.yaml`
- Target: `NCBITaxon:2720512`

## Target

The record grounds `Penicillium sp. str. #12` as an exact seeded NCBI species under `NCBITaxon:2593313` (`unclassified Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 547183.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sp_str_12.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/penicillium_sp_str_12.yaml data/taxa/eukaryota/penicillium_spathulatum.yaml data/taxa/eukaryota/penicillium_spinulosum.yaml data/taxa/eukaryota/penicillium_steckii.yaml`: exited successfully
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 62989 with the expected reason: `attested rule: Penicillium sp. str. #12, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML correctly omits a `synonyms` block.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:2720512`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 547183.
- GOLD aggregate: line 25251 records `organism_count=1` for `NCBITaxon:2720512`, matching the YAML GOLD attestation count. Native GOLD exact rows include one organism, `Go0631251` at line 461737, one project, `Gp0644560` at line 481793, and one analysis at line 362437.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The YAML label preserves the NCBI punctuation with `#12`; that value matches the source taxonomy row and the seed-scope reason.
