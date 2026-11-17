# Review: Petasospora adriatica

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_adriatica.yaml`
- Target: `NCBITaxon:1171601`

## Target

The record grounds `Petasospora adriatica` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 259256.

## Validation

- `just validate data/taxa/eukaryota/petasospora_adriatica.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_adriatica.yaml data/taxa/eukaryota/petasospora_americana.yaml data/taxa/eukaryota/petasospora_amylophila.yaml data/taxa/eukaryota/petasospora_bimundalis.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58173 with the expected reason: `attested rule: Petasospora adriatica, 2 sources incl. NCBI`.
- The exact synonym and seven related synonyms in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps four old IDs to this target at lines 2047, 2048, 3284, and 97922; exact retained-row scans found no old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 259256.
- GOLD aggregate: line 3692 records `organism_count=1` for `NCBITaxon:1171601`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 11143-11154 record 12 exact rows for this target.
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
