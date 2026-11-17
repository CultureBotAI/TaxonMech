# Review: Pichia manshurica

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_manshurica.yaml`
- Target: `NCBITaxon:121235`

## Target

The record grounds `Pichia manshurica` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 22754.

## Validation

- `just validate data/taxa/eukaryota/pichia_manshurica.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_kudriavzevii.yaml data/taxa/eukaryota/pichia_kudriavzevii_cab39_6420.yaml data/taxa/eukaryota/pichia_manshurica.yaml data/taxa/eukaryota/pichia_membranifaciens.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53870 with the expected reason: `attested rule: Pichia manshurica, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, four related synonyms, and no broad synonyms; the YAML mirrors those five synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:2898201`, `NCBITaxon:2898217`, `NCBITaxon:336311`, and `NCBITaxon:53662` into this identifier at lines 56667, 56677, 68605, and 85141; exact retained-row checks found no rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 22754.
- GOLD aggregate: line 5045 records `organism_count=5` for `NCBITaxon:121235`, matching the YAML GOLD attestation count; native GOLD has five exact organism rows, five exact project rows, and four exact analysis rows for this target.
- NCBI type material: 13 exact rows were found at lines 14097-14109.
- StrainInfo: 35 direct exact strains and 70 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia manshurica` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
