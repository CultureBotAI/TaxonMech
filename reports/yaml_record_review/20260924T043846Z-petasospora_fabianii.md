# Review: Petasospora fabianii

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_fabianii.yaml`
- Target: `NCBITaxon:36022`

## Target

The record grounds `Petasospora fabianii` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 4034.

## Validation

- `just validate data/taxa/eukaryota/petasospora_fabianii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_easanensis.yaml data/taxa/eukaryota/petasospora_euphorbiae.yaml data/taxa/eukaryota/petasospora_euphorbiiphila.yaml data/taxa/eukaryota/petasospora_fabianii.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52303 with the expected reason: `attested rule: Petasospora fabianii, 2 sources incl. NCBI`.
- The five exact synonyms and four related synonyms in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 4034.
- GOLD aggregate: line 33244 records `organism_count=4` for `NCBITaxon:36022`, matching the YAML GOLD attestation count; native GOLD has four exact organism rows, four exact project rows, and two exact analysis rows for this target.
- NCBI type material: lines 193575-193587 record 13 exact rows for this target.
- StrainInfo: 25 direct exact strains and 71 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
