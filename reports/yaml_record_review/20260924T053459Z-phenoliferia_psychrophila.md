# Review: Phenoliferia psychrophila

- Verdict: pass
- Record: `data/taxa/eukaryota/phenoliferia_psychrophila.yaml`
- Target: `NCBITaxon:418499`

## Target

The record grounds `Phenoliferia psychrophila` as an exact seeded NCBI species under `NCBITaxon:1799530` (`Phenoliferia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 91619.

## Validation

- `just validate data/taxa/eukaryota/phenoliferia_psychrophila.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phenoliferia_psychrophila.yaml data/taxa/eukaryota/phialemonium_atrogriseum.yaml data/taxa/eukaryota/phialemonium_globosum.yaml data/taxa/eukaryota/phialemonium_thermophilum.yaml`: zero errors across 4 files
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55587 with the expected reason: `attested rule: Phenoliferia psychrophila, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Rhodotorula psychrophila`, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 91619.
- GOLD aggregate: line 34974 records `organism_count=3` for `NCBITaxon:418499`, matching the YAML GOLD attestation count; native GOLD has three exact organism rows and no exact project or analysis rows for this target.
- NCBI type material: lines 207261-207268 record eight exact `Rhodotorula psychrophila` type-material rows.
- StrainInfo: one direct exact strain and one exact deposit row were found for this target; no generated StrainInfo overlay rows were found.

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
