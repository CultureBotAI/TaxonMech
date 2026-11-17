# Review: Petasospora xishuangbannaensis

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_xishuangbannaensis.yaml`
- Target: `NCBITaxon:1943667`

## Target

The record grounds `Petasospora xishuangbannaensis` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 498082.

## Validation

- `just validate data/taxa/eukaryota/petasospora_xishuangbannaensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_veronae.yaml data/taxa/eukaryota/petasospora_xishuangbannaensis.yaml data/taxa/eukaryota/petasospora_xylosilytica.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 61697 with the expected reason: `attested rule: Petasospora xishuangbannaensis, 2 sources incl. NCBI`.
- The exact synonym and three related synonyms in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 498082.
- GOLD aggregate: line 17878 records `organism_count=1` for `NCBITaxon:1943667`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 73877-73882 record six exact rows for this target.
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
