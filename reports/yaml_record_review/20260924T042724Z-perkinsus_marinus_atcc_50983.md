# Review: Perkinsus marinus ATCC 50983

- Verdict: pass
- Record: `data/taxa/eukaryota/perkinsus_marinus_atcc_50983.yaml`
- Target: `NCBITaxon:423536`

## Target

The record grounds `Perkinsus marinus ATCC 50983` as an exact seeded NCBI strain under `NCBITaxon:31276` (`Perkinsus marinus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 93022.

## Validation

- `just validate data/taxa/eukaryota/perkinsus_marinus_atcc_50983.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/perkinsus_chesapeaki.yaml data/taxa/eukaryota/perkinsus_marinus.yaml data/taxa/eukaryota/perkinsus_marinus_atcc_50983.yaml data/taxa/eukaryota/perkinsus_olseni.yaml`: exited successfully
- Lineage audit: checked 11 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55611 with the expected reason: `attested rule: Perkinsus marinus ATCC 50983, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 93022.
- GOLD aggregate: line 35125 records `organism_count=1` for `NCBITaxon:423536`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
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

None.
