# Review: Penicillium sicoris

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sicoris.yaml`
- Target: `NCBITaxon:3081130`

## Target

The record grounds `Penicillium sicoris` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 595761.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sicoris.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_shearii.yaml data/taxa/eukaryota/penicillium_sicoris.yaml data/taxa/eukaryota/penicillium_simile.yaml data/taxa/eukaryota/penicillium_simplicissimum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63548 with the expected reason: `attested rule: Penicillium sicoris, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sicoris Torres-Garcia, Gene & Dania Garcia, 2022` and `Penicillium sp. 9 DT-2020`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 51402 maps old ID `NCBITaxon:2772431` into `NCBITaxon:3081130`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 595761.
- GOLD aggregate: line 31218 records `organism_count=1` for `NCBITaxon:3081130`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: 12 exact rows at lines 165282-165293, covering culture-from-holotype spellings for `CBS 148241` and `FMR 18076` plus holotype spellings for `CBS H-24784`.
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

The type-material rows include delimiter variants of the same CBS/FMR culture-from-holotype identifiers and CBS holotype identifier; the YAML does not store type-material rows directly.
