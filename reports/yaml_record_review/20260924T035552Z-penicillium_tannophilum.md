# Review: Penicillium tannophilum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_tannophilum.yaml`
- Target: `NCBITaxon:2972123`

## Target

The record grounds `Penicillium tannophilum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 580333.

## Validation

- `just validate data/taxa/eukaryota/penicillium_tannophilum.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/penicillium_swiecickii.yaml data/taxa/eukaryota/penicillium_synnematicola.yaml data/taxa/eukaryota/penicillium_tannophilum.yaml data/taxa/eukaryota/penicillium_tardochrysogenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63481 with the expected reason: `attested rule: Penicillium tannophilum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium tannophilum Stapp & Bortels, 1935`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:2972123`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 580333.
- GOLD aggregate: line 29667 records `organism_count=1` for `NCBITaxon:2972123`, matching the YAML GOLD attestation count. Native GOLD exact rows include one organism, `Go0679399` at line 504030, one project, `Gp0781387` at line 580424, and one analysis at line 411849.
- NCBI type material: no exact rows were found for this target.
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

The native GOLD organism, project, and analysis rows all link to `Penicillium tannophilum IBT 21756`.
