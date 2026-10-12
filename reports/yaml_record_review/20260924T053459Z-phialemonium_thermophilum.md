# Review: Phialemonium thermophilum

- Verdict: pass
- Record: `data/taxa/eukaryota/phialemonium_thermophilum.yaml`
- Target: `NCBITaxon:223376`

## Target

The record grounds `Phialemonium thermophilum` as an exact seeded NCBI species under `NCBITaxon:83822` (`Phialemonium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 43889.

## Validation

- `just validate data/taxa/eukaryota/phialemonium_thermophilum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phenoliferia_psychrophila.yaml data/taxa/eukaryota/phialemonium_atrogriseum.yaml data/taxa/eukaryota/phialemonium_globosum.yaml data/taxa/eukaryota/phialemonium_thermophilum.yaml`: zero errors across 4 files
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54609 with the expected reason: `attested rule: Phialemonium thermophilum, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Acremonium thermophilum`, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 60266 maps retired `NCBITaxon:3003059` to this identifier; an exact retained-row grep found no `NCBITaxon:3003059` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 43889.
- GOLD aggregate: line 21128 records `organism_count=1` for `NCBITaxon:223376`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 89099-89102 record four exact `Acremonium thermophilum` type-material rows.
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
