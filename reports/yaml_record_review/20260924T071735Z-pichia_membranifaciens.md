# Review: Pichia membranifaciens

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_membranifaciens.yaml`
- Target: `NCBITaxon:4926`

## Target

The record grounds `Pichia membranifaciens` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2147.

## Validation

- `just validate data/taxa/eukaryota/pichia_membranifaciens.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_kudriavzevii.yaml data/taxa/eukaryota/pichia_kudriavzevii_cab39_6420.yaml data/taxa/eukaryota/pichia_manshurica.yaml data/taxa/eukaryota/pichia_membranifaciens.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 51882 with the expected reason: `attested rule: Pichia membranifaciens, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, two related synonyms, and no broad synonyms; the YAML mirrors those five synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:208487` into this identifier at line 37334; an exact retained-row check found no `NCBITaxon:208487` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 2147.
- GOLD aggregate: line 37147 records `organism_count=1` for `NCBITaxon:4926`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, one exact project row, and one exact analysis row for this target.
- NCBI type material: 25 exact rows were found at lines 223156-223180.
- StrainInfo: 332 direct exact strains and 506 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia membranifaciens` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
