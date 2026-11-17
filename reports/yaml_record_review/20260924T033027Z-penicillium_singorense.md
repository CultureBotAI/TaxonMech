# Review: Penicillium singorense

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_singorense.yaml`
- Target: `NCBITaxon:1566357`

## Target

The record grounds `Penicillium singorense` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 403239.

## Validation

- `just validate data/taxa/eukaryota/penicillium_singorense.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sinaicum.yaml data/taxa/eukaryota/penicillium_singorense.yaml data/taxa/eukaryota/penicillium_sizovae.yaml data/taxa/eukaryota/penicillium_skrjabinii.yaml`: scanned 4 files with 0 files with errors and 0 total error rows
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60477 with the expected reason: `attested rule: Penicillium singorense, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium singorense C.M. Visagie, K.A. Seifert & R.A. Samson, 2014`; the YAML mirrors those values.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:1566357`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 403239.
- GOLD aggregate: line 12584 records `organism_count=1` for `NCBITaxon:1566357`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: four exact rows at lines 42914-42917, covering culture-from-holotype spellings `CBS 138214` / `CBS:138214` and culture-from-type-material spellings `DTO 133C6` / `DTO:133C6`.
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

The type-material evidence uses paired space and colon variants of the same CBS and DTO culture identifiers; the generated YAML does not store those source-only rows directly.
