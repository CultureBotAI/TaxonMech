# Review: Penicillium taurinense

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_taurinense.yaml`
- Target: `NCBITaxon:2036924`

## Target

The record grounds `Penicillium taurinense` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 512850.

## Validation

- `just validate data/taxa/eukaryota/penicillium_taurinense.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_taurinense.yaml data/taxa/eukaryota/penicillium_terrarumae.yaml data/taxa/eukaryota/penicillium_terrenum.yaml data/taxa/eukaryota/penicillium_terrigenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 62126 with the expected reason: `attested rule: Penicillium taurinense, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. SP-2017a` and `Penicillium taurinense S. Prencipe, Houbraken & D. Spadaro,`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 512850.
- GOLD aggregate: line 19264 records `organism_count=1` for `NCBITaxon:2036924`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 79995-80000, covering culture-from-holotype spellings for `CBS 145672` and `DTO 333- B8` plus holotype spellings for `CBS H-24332`.
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
