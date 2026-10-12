# Review: Penicillium tardochrysogenum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_tardochrysogenum.yaml`
- Target: `NCBITaxon:1304713`

## Target

The record grounds `Penicillium tardochrysogenum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 308412.

## Validation

- `just validate data/taxa/eukaryota/penicillium_tardochrysogenum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_swiecickii.yaml data/taxa/eukaryota/penicillium_synnematicola.yaml data/taxa/eukaryota/penicillium_tannophilum.yaml data/taxa/eukaryota/penicillium_tardochrysogenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59313 with the expected reason: `attested rule: Penicillium tardochrysogenum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. JH-2013e` and `Penicillium tardochrysogenum Frisvad, Houbraken & Samson, 2013`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 11543 maps old ID `NCBITaxon:1303723` into `NCBITaxon:1304713`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 308412.
- GOLD aggregate: line 7450 records `organism_count=1` for `NCBITaxon:1304713`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: eight exact rows at lines 21188-21195, covering culture-from-type-material spellings for `CBS 132200` plus type-material spellings for `DTO 149-B9`, `DTO 149B9`, and `IBT 30075`.
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

The retired `NCBITaxon:1303723` ID is consumed only through the merge map, not as a retained source row.
