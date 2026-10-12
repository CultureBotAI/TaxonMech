# Review: Pholiota brunnescens

- Verdict: pass
- Record: `data/taxa/eukaryota/pholiota_brunnescens.yaml`
- Target: `NCBITaxon:1343360`

## Target

The record grounds `Pholiota brunnescens` as an exact seeded NCBI species under `NCBITaxon:13205` (`Pholiota`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 322832.

## Validation

- `just validate data/taxa/eukaryota/pholiota_brunnescens.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlyctochytrium_bullatum.yaml data/taxa/eukaryota/phlyctochytrium_planicorne.yaml data/taxa/eukaryota/pholiota_brunnescens.yaml data/taxa/eukaryota/pholiota_conissans.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59576 with the expected reason: `attested rule: Pholiota brunnescens, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 322832.
- GOLD aggregate: line 8361 records `organism_count=1` for `NCBITaxon:1343360`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, 15 exact project rows, and no exact analysis rows for this target.
- NCBI type material: lines 24313-24315 record `MICH 11657`, `MICH:11657`, and `MICH:11657 (holotype)` holotype designations.
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
