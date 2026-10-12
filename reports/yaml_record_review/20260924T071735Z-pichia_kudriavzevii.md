# Review: Pichia kudriavzevii

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_kudriavzevii.yaml`
- Target: `NCBITaxon:4909`

## Target

The record grounds `Pichia kudriavzevii` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2134.

## Validation

- `just validate data/taxa/eukaryota/pichia_kudriavzevii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_kudriavzevii.yaml data/taxa/eukaryota/pichia_kudriavzevii_cab39_6420.yaml data/taxa/eukaryota/pichia_manshurica.yaml data/taxa/eukaryota/pichia_membranifaciens.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 51872 with the expected reason: `attested rule: Pichia kudriavzevii, 2 sources incl. NCBI`.
- The NCBI raw row has five exact synonyms, six related synonyms, and no broad synonyms; the YAML mirrors those 11 synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:272698` and `NCBITaxon:742423` into this identifier at lines 49586 and 94053; exact retained-row checks found no rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 2134.
- GOLD aggregate: line 37094 records `organism_count=396` for `NCBITaxon:4909`, matching the YAML direct-target GOLD attestation count; native GOLD has 387 exact organism rows, 736 exact project rows, and 29 exact analysis rows for this target.
- NCBI type material: 31 exact rows were found at lines 222828-222858.
- StrainInfo: 396 direct exact strains and 536 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the direct-target GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia kudriavzevii` is a species-rank NCBI taxon under the `Pichia` genus lineage entry; its GOLD attestation intentionally counts only records filed directly under this taxon.
