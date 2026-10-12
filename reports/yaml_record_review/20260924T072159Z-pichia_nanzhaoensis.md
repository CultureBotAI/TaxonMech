# Review: Pichia nanzhaoensis

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_nanzhaoensis.yaml`
- Target: `NCBITaxon:2860398`

## Target

The record grounds `Pichia nanzhaoensis` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 565511.

## Validation

- `just validate data/taxa/eukaryota/pichia_nanzhaoensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_nakasei.yaml data/taxa/eukaryota/pichia_nanzhaoensis.yaml data/taxa/eukaryota/pichia_norvegensis.yaml data/taxa/eukaryota/pichia_occidentalis.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 63323 with the expected reason: `attested rule: Pichia nanzhaoensis, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:2126708` into this identifier at line 37845; an exact retained-row check found no `NCBITaxon:2126708` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 565511.
- GOLD aggregate: line 27784 records `organism_count=1` for `NCBITaxon:2860398`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: six exact rows were found at lines 133238-133243.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia nanzhaoensis` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
