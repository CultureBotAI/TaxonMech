# Review: Penicillium simile

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_simile.yaml`
- Target: `NCBITaxon:889210`

## Target

The record grounds `Penicillium simile` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 189483.

## Validation

- `just validate data/taxa/eukaryota/penicillium_simile.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_shearii.yaml data/taxa/eukaryota/penicillium_sicoris.yaml data/taxa/eukaryota/penicillium_simile.yaml data/taxa/eukaryota/penicillium_simplicissimum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56848 with the expected reason: `attested rule: Penicillium simile, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has three related synonyms, `Penicillium simile Davolos, Pietrangeli, Persiani and Maggi, 2011`, `Penicillium sp. 5(200)-3`, and `Penicillium sp. DD-2010`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 89926 maps old ID `NCBITaxon:641391` into `NCBITaxon:889210`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 189483.
- GOLD aggregate: line 43944 records `organism_count=1` for `NCBITaxon:889210`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 271128-271133, covering culture-from-holotype spellings for `ATCC MYA-4591` plus culture-from-type-material identifiers `414`, `CBS 129191`, and `CBS:129191`.
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

The retired `NCBITaxon:641391` ID is consumed only through `data/raw/ncbi_merged_ids.tsv`; the generated record therefore correctly omits `replaces`.
