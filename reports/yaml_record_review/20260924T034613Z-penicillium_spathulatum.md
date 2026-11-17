# Review: Penicillium spathulatum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_spathulatum.yaml`
- Target: `NCBITaxon:1263194`

## Target

The record grounds `Penicillium spathulatum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 292389.

## Validation

- `just validate data/taxa/eukaryota/penicillium_spathulatum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sp_str_12.yaml data/taxa/eukaryota/penicillium_spathulatum.yaml data/taxa/eukaryota/penicillium_spinulosum.yaml data/taxa/eukaryota/penicillium_steckii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58797 with the expected reason: `attested rule: Penicillium spathulatum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CBS 117192` and `Penicillium spathulatum Frisvad & Samson, 2012`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 6032 maps old ID `NCBITaxon:1167579` into `NCBITaxon:1263194`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 292389.
- GOLD aggregate: line 6203 records `organism_count=1` for `NCBITaxon:1263194`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 17726-17731, covering culture-from-holotype spellings for `IBT 22220` plus holotype spellings for `CBS 117192`.
- StrainInfo: exact StrainInfo has one direct strain and one deposit row for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:1263194`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:1167579` ID is consumed only by the merge map, so no generated `replaces` block is expected.
