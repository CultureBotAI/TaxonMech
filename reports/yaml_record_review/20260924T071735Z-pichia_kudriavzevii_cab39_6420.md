# Review: Pichia kudriavzevii CAB39-6420

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_kudriavzevii_cab39_6420.yaml`
- Target: `NCBITaxon:1231518`

## Target

The record grounds `Pichia kudriavzevii CAB39-6420` as an exact seeded NCBI strain under `NCBITaxon:4909` (`Pichia kudriavzevii`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonym, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 281263.

## Validation

- `just validate data/taxa/eukaryota/pichia_kudriavzevii_cab39_6420.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_kudriavzevii.yaml data/taxa/eukaryota/pichia_kudriavzevii_cab39_6420.yaml data/taxa/eukaryota/pichia_manshurica.yaml data/taxa/eukaryota/pichia_membranifaciens.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 58589 with the expected reason: `attested rule: Pichia kudriavzevii CAB39-6420, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym and no related or broad synonyms; the YAML mirrors that synonym assertion.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 281263.
- GOLD aggregate: line 5539 records `organism_count=1` for `NCBITaxon:1231518`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this strain target.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the NCBI synonym, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia kudriavzevii CAB39-6420` is a strain-rank NCBI taxon under the `Pichia kudriavzevii` species lineage entry.
