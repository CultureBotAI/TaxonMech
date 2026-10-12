# Review: Phlyctochytrium aureliae

- Verdict: pass
- Record: `data/taxa/eukaryota/phlyctochytrium_aureliae.yaml`
- Target: `NCBITaxon:744527`

## Target

The record grounds `Phlyctochytrium aureliae` as an exact seeded NCBI species under `NCBITaxon:4819` (`Phlyctochytrium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 171663.

## Validation

- `just validate data/taxa/eukaryota/phlyctochytrium_aureliae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlegmacium_sp.yaml data/taxa/eukaryota/phleogena_faginea.yaml data/taxa/eukaryota/phlyctochytrium_arcticum.yaml data/taxa/eukaryota/phlyctochytrium_aureliae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56592 with the expected reason: `attested rule: Phlyctochytrium aureliae, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and two related synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 171663.
- GOLD aggregate: line 42177 records `organism_count=1` for `NCBITaxon:744527`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 261498-261500 record `KP 061`, `KP061`, and `KP:061` type-material designations.
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
