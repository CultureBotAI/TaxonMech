# Review: Penicillium swiecickii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_swiecickii.yaml`
- Target: `NCBITaxon:1295096`

## Target

The record grounds `Penicillium swiecickii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 304771.

## Validation

- `just validate data/taxa/eukaryota/penicillium_swiecickii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_swiecickii.yaml data/taxa/eukaryota/penicillium_synnematicola.yaml data/taxa/eukaryota/penicillium_tannophilum.yaml data/taxa/eukaryota/penicillium_tardochrysogenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58967 with the expected reason: `attested rule: Penicillium swiecickii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium swiecickii K.W. Zaleski, 1927`; the YAML mirrors that value.
- `data/raw/ncbi_merged_ids.tsv` line 92955 maps old ID `NCBITaxon:70108` into `NCBITaxon:1295096`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 304771.
- GOLD aggregate: line 6940 records `organism_count=15` for `NCBITaxon:1295096`, matching the YAML GOLD attestation count. Native GOLD exact rows include 15 unique organisms and 15 projects, with no analyses for this target.
- NCBI type material: eight exact rows at lines 20194-20201, all culture from holotype, covering `CBS 119391` and `NRRL 918` delimiter variants.
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

The native GOLD organism count exactly matches the aggregate GOLD count used in the generated source attestation.
