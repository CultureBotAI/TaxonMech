# Review: Phenoliferia glacialis

- Verdict: pass
- Record: `data/taxa/eukaryota/phenoliferia_glacialis.yaml`
- Target: `NCBITaxon:418497`

## Target

The record grounds `Phenoliferia glacialis` as an exact seeded NCBI species under `NCBITaxon:1799530` (`Phenoliferia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 91617.

## Validation

- `just validate data/taxa/eukaryota/phenoliferia_glacialis.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phellinus_viticola.yaml data/taxa/eukaryota/phellopilus_nigrolimitatus.yaml data/taxa/eukaryota/phenoliferia_glacialis.yaml data/taxa/eukaryota/phenoliferia_psychrophenolica.yaml`: zero errors across 4 files
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55585 with the expected reason: `attested rule: Phenoliferia glacialis, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Rhodotorula glacialis`, six related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 60222, 79977-79980, 79985-79987, and 95214 map nine retired IDs to this identifier; exact retained-row greps found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 91617.
- GOLD aggregate: line 34972 records `organism_count=3` for `NCBITaxon:418497`, matching the YAML GOLD attestation count; native GOLD has three exact organism rows, one exact project row, and one exact analysis row for this target.
- NCBI type material: lines 207247-207252 record six exact `Rhodotorula glacialis` type-material rows.
- StrainInfo: 2 direct exact strains and 3 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
