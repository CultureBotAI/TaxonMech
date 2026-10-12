# Review: Penicillium umkhoba

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_umkhoba.yaml`
- Target: `NCBITaxon:3078881`

## Target

The record grounds `Penicillium umkhoba` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 595234.

## Validation

- `just validate data/taxa/eukaryota/penicillium_umkhoba.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_umkhoba.yaml data/taxa/eukaryota/penicillium_vagum.yaml data/taxa/eukaryota/penicillium_vanluykii.yaml data/taxa/eukaryota/penicillium_velutinum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63541 with the expected reason: `attested rule: Penicillium umkhoba, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CMV-2020p` and `Penicillium umkhoba Visagie & Yilmaz, 2022`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 52276 maps old ID `NCBITaxon:2796925` into `NCBITaxon:3078881`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 595234.
- GOLD aggregate: line 31191 records `organism_count=1` for `NCBITaxon:3078881`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: 13 exact rows at lines 164761-164773, covering culture-from-holotype spellings for `CBS 147457`, `CMW 56200`, and `CN014D5` plus holotype spellings for `PREM 63222`.
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

The retired `NCBITaxon:2796925` ID is consumed only through the merge map, not as a retained source row.
