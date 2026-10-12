# Review: Penicillium simplicissimum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_simplicissimum.yaml`
- Target: `NCBITaxon:69488`

## Target

The record grounds `Penicillium simplicissimum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 9621.

## Validation

- `just validate data/taxa/eukaryota/penicillium_simplicissimum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_shearii.yaml data/taxa/eukaryota/penicillium_sicoris.yaml data/taxa/eukaryota/penicillium_simile.yaml data/taxa/eukaryota/penicillium_simplicissimum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53176 with the expected reason: `attested rule: Penicillium simplicissimum, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, `Spicaria simplicissima`, no broad synonyms, and two related synonyms, `Penicillium simplicissimum (Oudem.) Thom, 1930` and `Spicaria simplicissima Oudem., 1903`; the YAML mirrors those values.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:69488`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 9621.
- GOLD aggregate: line 41489 records `organism_count=2` for `NCBITaxon:69488`, matching the YAML GOLD attestation count. Native GOLD exact rows include one organism row, `Go0666268` at line 491755, and one project row, `Gp0734714` at line 551004; no native analysis rows were found.
- NCBI type material: 12 exact rows at lines 257877-257888 for the synonym name `Spicaria simplicissima`, covering `ATCC 10495`, `CBS 372.48`, `FRR 902`, `IFO 5762`, `IMI 039816`, and `QM 1939` delimiter variants.
- StrainInfo: exact StrainInfo has 156 direct strains and 241 deposit rows for this target. The BacDive-derived StrainInfo overlay emitted two generated `related_records.tsv.gz` rows, lines 16737 and 16739, for `NRRL 1521` / `straininfo.strain:48219`; no generated StrainInfo assembly or exclusion rows were found.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The type-material rows are keyed to the exact synonym `Spicaria simplicissima`; this agrees with NCBI's synonym inventory for the accepted `Penicillium simplicissimum` target.
