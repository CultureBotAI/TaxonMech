# Review: Penicillium vulpinum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_vulpinum.yaml`
- Target: `NCBITaxon:29845`

## Target

The record grounds `Penicillium vulpinum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 3278.

## Validation

- `just validate data/taxa/eukaryota/penicillium_vulpinum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_vulpinum.yaml data/taxa/eukaryota/penicillium_westlingii.yaml data/taxa/eukaryota/penicillium_wotroi.yaml data/taxa/eukaryota/penicillium_xanthomelinii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52212 with the expected reason: `attested rule: Penicillium vulpinum, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, `Coremium vulpinum` and `Penicillium claviforme`, no broad synonyms, and three related synonyms, `Coremium vulpinum Cooke & Massee, 1888`, `Penicillium claviforme Bainier, 1905`, and `Penicillium vulpinum (Cooke & Massee) Seifert & Samson, 1986`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 3278.
- GOLD aggregate: line 29873 records `organism_count=1` for `NCBITaxon:29845`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: 20 exact rows at lines 152395-152414, covering culture-from-epitype spellings for `ATCC 10426`, `CBS 126.23`, `IMI 040237`, `NRRL 2031`, and `VKMF 257`.
- StrainInfo: 121 exact deposit rows and 71 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

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
