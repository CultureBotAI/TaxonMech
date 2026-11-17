# Review: Petasospora rhodanensis

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_rhodanensis.yaml`
- Target: `NCBITaxon:53495`

## Target

The record grounds `Petasospora rhodanensis` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6768.

## Validation

- `just validate data/taxa/eukaryota/petasospora_rhodanensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_petersonii.yaml data/taxa/eukaryota/petasospora_rhodanensis.yaml data/taxa/eukaryota/petasospora_stauntonica.yaml data/taxa/eukaryota/petasospora_taoyuanica.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52875 with the expected reason: `attested rule: Petasospora rhodanensis, 2 sources incl. NCBI`.
- The six exact synonyms and three related synonyms in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 6768.
- GOLD aggregate: line 38144 records `organism_count=1` for `NCBITaxon:53495`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 230254-230276 record 23 exact rows for this target.
- StrainInfo: 20 direct exact strains and 44 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
