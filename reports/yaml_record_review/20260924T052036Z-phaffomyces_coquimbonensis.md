# Review: Phaffomyces coquimbonensis

- Verdict: pass
- Record: `data/taxa/eukaryota/phaffomyces_coquimbonensis.yaml`
- Target: `NCBITaxon:1460421`

## Target

The record grounds `Phaffomyces coquimbonensis` as an exact seeded NCBI species under `NCBITaxon:83172` (`Phaffomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 371377.

## Validation

- `just validate data/taxa/eukaryota/phaffomyces_coquimbonensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeotremella_skinneri.yaml data/taxa/eukaryota/phaffia_rhodozyma.yaml data/taxa/eukaryota/phaffomyces_antillensis.yaml data/taxa/eukaryota/phaffomyces_coquimbonensis.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60225 with the expected reason: `attested rule: Phaffomyces coquimbonensis, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Candida coquimbonensis`, eight related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 1830-1835 map six retired IDs from `NCBITaxon:1053442` through `NCBITaxon:1053447` to this identifier; exact retained-row greps found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 371377.
- GOLD aggregate: line 11166 records `organism_count=1` for `NCBITaxon:1460421`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 32833-32838 record `USCFST 12-103`/`USCFST:12-103` cultures from holotype and four `CBS 12348` holotype variants.
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
