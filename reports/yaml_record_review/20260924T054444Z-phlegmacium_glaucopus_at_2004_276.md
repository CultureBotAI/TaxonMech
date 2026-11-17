# Review: Phlegmacium glaucopus AT 2004 276

- Verdict: pass
- Record: `data/taxa/eukaryota/phlegmacium_glaucopus_at_2004_276.yaml`
- Target: `NCBITaxon:1149754`

## Target

The record grounds `Phlegmacium glaucopus AT 2004 276` as an exact seeded NCBI strain under `NCBITaxon:171480` (`Phlegmacium glaucopus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 251457.

## Validation

- `just validate data/taxa/eukaryota/phlegmacium_glaucopus_at_2004_276.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlebopus_sp.yaml data/taxa/eukaryota/phlegmacium_cistoglaucopus.yaml data/taxa/eukaryota/phlegmacium_glaucopus.yaml data/taxa/eukaryota/phlegmacium_glaucopus_at_2004_276.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 57995 with the expected reason: `attested rule: Phlegmacium glaucopus AT 2004 276, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms, matching the absence of YAML synonyms.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 251457.
- GOLD aggregate: line 3029 records `organism_count=2` for `NCBITaxon:1149754`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

None.
