# Review: Petasospora maesae

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_maesae.yaml`
- Target: `NCBITaxon:1198496`

## Target

The record grounds `Petasospora maesae` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 269935.

## Validation

- `just validate data/taxa/eukaryota/petasospora_maesae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_hungchunana.yaml data/taxa/eukaryota/petasospora_japonica.yaml data/taxa/eukaryota/petasospora_maesae.yaml data/taxa/eukaryota/petasospora_maritima.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58309 with the expected reason: `attested rule: Petasospora maesae, 2 sources incl. NCBI`.
- The exact synonym and eight related synonyms in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps five old IDs to this target at lines 87848, 87851, 87852, 87853, and 87854; exact retained-row scans found no old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 269935.
- GOLD aggregate: line 4790 records `organism_count=1` for `NCBITaxon:1198496`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 13163-13167 record five exact rows for this target.
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
