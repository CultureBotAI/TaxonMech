# Review: Phaeosphaeriaceae sp. SRC1lsM3a

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeosphaeriaceae_sp_src1lsm3a.yaml`
- Target: `NCBITaxon:765868`

## Target

The record grounds `Phaeosphaeriaceae sp. SRC1lsM3a` as an exact seeded NCBI species under `NCBITaxon:119085` (`unclassified Phaeosphaeriaceae`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 177820.

## Validation

- `just validate data/taxa/eukaryota/phaeosphaeriaceae_sp_src1lsm3a.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeosphaeria_sp.yaml data/taxa/eukaryota/phaeosphaeriaceae_sp_src1lsm3a.yaml data/taxa/eukaryota/phaeosphaeriaceae_sp_um_1110.yaml data/taxa/eukaryota/phaeotremella_fagi.yaml`: exited successfully
- Lineage audit: checked 17 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56687 with the expected reason: `attested rule: Phaeosphaeriaceae sp. SRC1lsM3a, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 177820.
- GOLD aggregate: line 42543 records `organism_count=2` for `NCBITaxon:765868`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and two exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
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
