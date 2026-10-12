# Review: Phenoliferia psychrophenolica

- Verdict: pass
- Record: `data/taxa/eukaryota/phenoliferia_psychrophenolica.yaml`
- Target: `NCBITaxon:418498`

## Target

The record grounds `Phenoliferia psychrophenolica` as an exact seeded NCBI species under `NCBITaxon:1799530` (`Phenoliferia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 91618.

## Validation

- `just validate data/taxa/eukaryota/phenoliferia_psychrophenolica.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phellinus_viticola.yaml data/taxa/eukaryota/phellopilus_nigrolimitatus.yaml data/taxa/eukaryota/phenoliferia_glacialis.yaml data/taxa/eukaryota/phenoliferia_psychrophenolica.yaml`: zero errors across 4 files
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55586 with the expected reason: `attested rule: Phenoliferia psychrophenolica, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Rhodotorula psychrophenolica`, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 79981-79984 map four retired IDs to this identifier; exact retained-row greps found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 91618.
- GOLD aggregate: line 34973 records `organism_count=2` for `NCBITaxon:418498`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows and no exact project or analysis rows for this target.
- NCBI type material: lines 207253-207260 record eight exact `Rhodotorula psychrophenolica` type-material rows.
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
