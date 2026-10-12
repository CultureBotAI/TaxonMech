# Review: Phialemonium atrogriseum

- Verdict: pass
- Record: `data/taxa/eukaryota/phialemonium_atrogriseum.yaml`
- Target: `NCBITaxon:1093897`

## Target

The record grounds `Phialemonium atrogriseum` as an exact seeded NCBI species under `NCBITaxon:83822` (`Phialemonium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 235272.

## Validation

- `just validate data/taxa/eukaryota/phialemonium_atrogriseum.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phenoliferia_psychrophila.yaml data/taxa/eukaryota/phialemonium_atrogriseum.yaml data/taxa/eukaryota/phialemonium_globosum.yaml data/taxa/eukaryota/phialemonium_thermophilum.yaml`: zero errors across 4 files
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 57588 with the expected reason: `attested rule: Phialemonium atrogriseum, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 86411 maps retired `NCBITaxon:561994` to this identifier; an exact retained-row grep found no `NCBITaxon:561994` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 235272.
- GOLD aggregate: line 1708 records `organism_count=1` for `NCBITaxon:1093897`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: lines 6060-6070 record 11 exact `Phaeoscopulariopsis atrogrisea` type-material rows.
- StrainInfo: 15 direct exact strains and 30 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
