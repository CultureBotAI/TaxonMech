# Review: Penicillium westlingii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_westlingii.yaml`
- Target: `NCBITaxon:69792`

## Target

The record grounds `Penicillium westlingii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 9679.

## Validation

- `just validate data/taxa/eukaryota/penicillium_westlingii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_vulpinum.yaml data/taxa/eukaryota/penicillium_westlingii.yaml data/taxa/eukaryota/penicillium_wotroi.yaml data/taxa/eukaryota/penicillium_xanthomelinii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53192 with the expected reason: `attested rule: Penicillium westlingii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CBS 124313` and `Penicillium westlingii K.M. Zalessky, 1927`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 9679.
- GOLD aggregate: line 41551 records `organism_count=1` for `NCBITaxon:69792`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: two exact rows at lines 258227-258228, covering culture-from-neotype spellings for `CBS 231.28`.
- StrainInfo: 14 exact deposit rows and seven direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

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
