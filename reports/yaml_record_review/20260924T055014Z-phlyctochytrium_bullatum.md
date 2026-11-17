# Review: Phlyctochytrium bullatum

- Verdict: pass
- Record: `data/taxa/eukaryota/phlyctochytrium_bullatum.yaml`
- Target: `NCBITaxon:1352834`

## Target

The record grounds `Phlyctochytrium bullatum` as an exact seeded NCBI species under `NCBITaxon:4819` (`Phlyctochytrium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 326766.

## Validation

- `just validate data/taxa/eukaryota/phlyctochytrium_bullatum.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phlyctochytrium_bullatum.yaml data/taxa/eukaryota/phlyctochytrium_planicorne.yaml data/taxa/eukaryota/pholiota_brunnescens.yaml data/taxa/eukaryota/pholiota_conissans.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59622 with the expected reason: `attested rule: Phlyctochytrium bullatum, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 326766.
- GOLD aggregate: line 8546 records `organism_count=1` for `NCBITaxon:1352834`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
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
