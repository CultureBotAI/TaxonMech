# Review: Phaffia rhodozyma

- Verdict: pass
- Record: `data/taxa/eukaryota/phaffia_rhodozyma.yaml`
- Target: `NCBITaxon:264483`

## Target

The record grounds `Phaffia rhodozyma` as an exact seeded NCBI species under `NCBITaxon:107449` (`Phaffia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 54063.

## Validation

- `just validate data/taxa/eukaryota/phaffia_rhodozyma.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeotremella_skinneri.yaml data/taxa/eukaryota/phaffia_rhodozyma.yaml data/taxa/eukaryota/phaffomyces_antillensis.yaml data/taxa/eukaryota/phaffomyces_coquimbonensis.yaml`: exited successfully
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54869 with the expected reason: `attested rule: Phaffia rhodozyma, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, four related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 1029 and 85342 map retired `NCBITaxon:103478` and `NCBITaxon:5421` to this identifier; exact retained-row greps found neither old ID in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 54063.
- GOLD aggregate: line 24252 records `organism_count=15` for `NCBITaxon:264483`, matching the YAML GOLD attestation count; native GOLD has 14 exact organism rows, 43 exact project rows, and 3 exact analysis rows for this target.
- NCBI type material: lines 106814-106844 record 31 exact rows across `Phaffia rhodozyma` and `Xanthophyllomyces dendrorhous` type-material designations.
- StrainInfo: 33 direct exact strains and 82 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
