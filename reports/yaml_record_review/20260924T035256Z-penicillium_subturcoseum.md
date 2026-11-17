# Review: Penicillium subturcoseum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_subturcoseum.yaml`
- Target: `NCBITaxon:639305`

## Target

The record grounds `Penicillium subturcoseum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 147335.

## Validation

- `just validate data/taxa/eukaryota/penicillium_subturcoseum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_subturcoseum.yaml data/taxa/eukaryota/penicillium_sucrivorum.yaml data/taxa/eukaryota/penicillium_sumatraense.yaml data/taxa/eukaryota/penicillium_svalbardense.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56198 with the expected reason: `attested rule: Penicillium subturcoseum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CMV-2009e` and `Penicillium subturcoseum Visagie & K. Jacobs, 2016`; the YAML mirrors those values.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:639305`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 147335.
- GOLD aggregate: line 40182 records `organism_count=1` for `NCBITaxon:639305`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 243706-243711, all culture from holotype, covering `CBS 139132`, `CV2835`, and `DTO 180-C9` delimiter variants.
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

The source footprint is limited to NCBI and the GOLD aggregate row; there is no native GOLD or StrainInfo expansion for this target.
