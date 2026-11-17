# Review: Penicillium skrjabinii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_skrjabinii.yaml`
- Target: `NCBITaxon:104262`

## Target

The record grounds `Penicillium skrjabinii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 18632.

## Validation

- `just validate data/taxa/eukaryota/penicillium_skrjabinii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sinaicum.yaml data/taxa/eukaryota/penicillium_singorense.yaml data/taxa/eukaryota/penicillium_sizovae.yaml data/taxa/eukaryota/penicillium_skrjabinii.yaml`: scanned 4 files with 0 files with errors and 0 total error rows
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53677 with the expected reason: `attested rule: Penicillium skrjabinii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium skrjabinii Schmotina & Golovleva, 1974`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:104262`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 18632.
- GOLD aggregate: line 618 records `organism_count=1` for `NCBITaxon:104262`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: eight exact rows at lines 2661-2668, covering culture-from-neotype spellings `CBS 439.75` / `CBS:439.75` and type-material spellings for `FRR 1945`, `IMI 196528`, and `NRRL 13055`.
- StrainInfo: exact StrainInfo has one deposit row for this target and no direct exact strain rows; the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:104262`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The only exact StrainInfo hit was deposit-only, so no generated StrainInfo overlay is expected.
