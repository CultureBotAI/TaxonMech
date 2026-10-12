# Review: Perkinsus olseni

- Verdict: pass
- Record: `data/taxa/eukaryota/perkinsus_olseni.yaml`
- Target: `NCBITaxon:32597`

## Target

The record grounds `Perkinsus olseni` as an exact seeded NCBI species under `NCBITaxon:28000` (`Perkinsus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 3457.

## Validation

- `just validate data/taxa/eukaryota/perkinsus_olseni.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/perkinsus_chesapeaki.yaml data/taxa/eukaryota/perkinsus_marinus.yaml data/taxa/eukaryota/perkinsus_marinus_atcc_50983.yaml data/taxa/eukaryota/perkinsus_olseni.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52244 with the expected reason: `attested rule: Perkinsus olseni, 2 sources incl. NCBI`.
- The NCBI raw row has the exact synonym `Perkinsus atlanticus`, no broad synonyms, and one related synonym, `Perkinsus olseni Lester & Davis, 1981`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 2264 maps old ID `NCBITaxon:106964` into `NCBITaxon:32597`, and line 67129 maps old ID `NCBITaxon:32596` into `NCBITaxon:32597`; exact retained-row greps of `data/raw/ncbitaxon_taxa.tsv` found no remaining rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 3457.
- GOLD aggregate: line 32151 records `organism_count=5` for `NCBITaxon:32597`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have five exact rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: one exact deposit row and one direct exact strain were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:106964` and `NCBITaxon:32596` IDs are consumed only through the merge map, not as retained source rows.
