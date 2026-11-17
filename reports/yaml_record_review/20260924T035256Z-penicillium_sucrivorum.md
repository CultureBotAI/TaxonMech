# Review: Penicillium sucrivorum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sucrivorum.yaml`
- Target: `NCBITaxon:1537407`

## Target

The record grounds `Penicillium sucrivorum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 396152.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sucrivorum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_subturcoseum.yaml data/taxa/eukaryota/penicillium_sucrivorum.yaml data/taxa/eukaryota/penicillium_sumatraense.yaml data/taxa/eukaryota/penicillium_svalbardense.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60415 with the expected reason: `attested rule: Penicillium sucrivorum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium sucrivorum C. M. Visagie & K. Jacobs, 2014`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:1537407`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 396152.
- GOLD aggregate: line 12206 records `organism_count=1` for `NCBITaxon:1537407`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: eight exact rows at lines 40420-40427, covering culture-from-holotype spellings for `CV 1840`, `DAOM 241042`, and `DTO 183E5` plus holotype spellings for `CBS H-21331`.
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

The NCBI type-material rows are source evidence only; they are not represented directly in the generated YAML.
