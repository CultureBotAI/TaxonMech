# Review: Petasospora veronae

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_veronae.yaml`
- Target: `NCBITaxon:53496`

## Target

The record grounds `Petasospora veronae` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6769.

## Validation

- `just validate data/taxa/eukaryota/petasospora_veronae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_veronae.yaml data/taxa/eukaryota/petasospora_xishuangbannaensis.yaml data/taxa/eukaryota/petasospora_xylosilytica.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52876 with the expected reason: `attested rule: Petasospora veronae, 2 sources incl. NCBI`.
- The three exact synonyms and three related synonyms in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 6769.
- GOLD aggregate: line 38145 records `organism_count=1` for `NCBITaxon:53496`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 230277-230291 record 15 exact rows for this target.
- StrainInfo: 12 direct exact strains and 25 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
