# Review: Penicillium xanthomelinii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_xanthomelinii.yaml`
- Target: `NCBITaxon:1297657`

## Target

The record grounds `Penicillium xanthomelinii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 305770.

## Validation

- `just validate data/taxa/eukaryota/penicillium_xanthomelinii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_vulpinum.yaml data/taxa/eukaryota/penicillium_westlingii.yaml data/taxa/eukaryota/penicillium_wotroi.yaml data/taxa/eukaryota/penicillium_xanthomelinii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 59256 with the expected reason: `attested rule: Penicillium xanthomelinii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CMV-2013s` and `Penicillium xanthomelinii Visagie & K. Jacobs, 2016`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 305770.
- GOLD aggregate: line 7269 records `organism_count=1` for `NCBITaxon:1297657`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: ten exact rows at lines 20541-20550, covering culture-from-holotype spellings for `CBS 139163`, `CV 1677`, `DAOM 241104`, `DAOMC 241104`, and `DTO 183-C7`.
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
