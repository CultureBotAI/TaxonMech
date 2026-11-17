# Review: Penicillium tricolor

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_tricolor.yaml`
- Target: `NCBITaxon:60170`

## Target

The record grounds `Penicillium tricolor` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7582.

## Validation

- `just validate data/taxa/eukaryota/penicillium_tricolor.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_thiersii.yaml data/taxa/eukaryota/penicillium_tricolor.yaml data/taxa/eukaryota/penicillium_tropicoides.yaml data/taxa/eukaryota/penicillium_tropicum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53014 with the expected reason: `attested rule: Penicillium tricolor, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CMV-2018k` and `Penicillium tricolor Frisvad, Seifert, Samson & John T. Mills, 1994`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 38751 maps old ID `NCBITaxon:2184416` into `NCBITaxon:60170`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7582.
- GOLD aggregate: line 39772 records `organism_count=1` for `NCBITaxon:60170`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 241020-241025, covering culture-from-holotype spellings for `CBS 635.93` plus type-material spellings for `DAOM 216240` and `IBT 12493`.
- StrainInfo: 13 exact deposit rows and five direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:2184416` ID is consumed only through the merge map, not as a retained source row.
