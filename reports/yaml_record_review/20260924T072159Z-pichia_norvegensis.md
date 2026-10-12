# Review: Pichia norvegensis

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_norvegensis.yaml`
- Target: `NCBITaxon:4921`

## Target

The record grounds `Pichia norvegensis` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2142.

## Validation

- `just validate data/taxa/eukaryota/pichia_norvegensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_nakasei.yaml data/taxa/eukaryota/pichia_nanzhaoensis.yaml data/taxa/eukaryota/pichia_norvegensis.yaml data/taxa/eukaryota/pichia_occidentalis.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 51877 with the expected reason: `attested rule: Pichia norvegensis, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, three related synonyms, and no broad synonyms; the YAML mirrors those five synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 2142.
- GOLD aggregate: line 37136 records `organism_count=1` for `NCBITaxon:4921`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and two exact analysis rows for this target.
- NCBI type material: 12 exact rows were found at lines 223096-223107.
- StrainInfo: 38 direct exact strains and 69 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia norvegensis` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
