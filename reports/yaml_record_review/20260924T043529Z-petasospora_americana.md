# Review: Petasospora americana

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_americana.yaml`
- Target: `NCBITaxon:36016`

## Target

The record grounds `Petasospora americana` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 4030.

## Validation

- `just validate data/taxa/eukaryota/petasospora_americana.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_adriatica.yaml data/taxa/eukaryota/petasospora_americana.yaml data/taxa/eukaryota/petasospora_amylophila.yaml data/taxa/eukaryota/petasospora_bimundalis.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52299 with the expected reason: `attested rule: Petasospora americana, 2 sources incl. NCBI`.
- The five exact synonyms and three related synonyms in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 4030.
- GOLD aggregate: line 33237 records `organism_count=1` for `NCBITaxon:36016`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 193453-193488 record 36 exact rows for this target.
- StrainInfo: 5 direct exact strains and 27 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
