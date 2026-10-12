# Review: Penicillium sinaicum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sinaicum.yaml`
- Target: `NCBITaxon:1303722`

## Target

The record grounds `Penicillium sinaicum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 308124.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sinaicum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sinaicum.yaml data/taxa/eukaryota/penicillium_singorense.yaml data/taxa/eukaryota/penicillium_sizovae.yaml data/taxa/eukaryota/penicillium_skrjabinii.yaml`: scanned 4 files with 0 files with errors and 0 total error rows
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59305 with the expected reason: `attested rule: Penicillium sinaicum, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, `Eupenicillium sinaicum`, no broad synonyms, and two related synonyms, `Eupenicillium sinaicum Udagawa & S. Ueda, 1982` and `Penicillium sinaicum Udagawa & S. Ueda, 1982`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 60966 maps old ID `NCBITaxon:303253` into `NCBITaxon:1303722`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 308124.
- GOLD aggregate: line 7434 records `organism_count=1` for `NCBITaxon:1303722`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: four exact rows at lines 21074-21077, covering culture-from-holotype spellings `CBS 279.82` / `CBS:279.82` and type-material spellings `NHL 2894` / `NHL:2894`.
- StrainInfo: exact StrainInfo has 4 direct strains and 5 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:1303722`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The old `NCBITaxon:303253` ID is present only in the merge map, so the generated record correctly has no `replaces` block.
