# Review: Peziza echinospora

- Verdict: pass
- Record: `data/taxa/eukaryota/peziza_echinospora.yaml`
- Target: `NCBITaxon:61495`

## Target

The record grounds `Peziza echinospora` as an exact seeded NCBI species under `NCBITaxon:40593` (`Peziza`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7794.

## Validation

- `just validate data/taxa/eukaryota/peziza_echinospora.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peziza_echinospora.yaml data/taxa/eukaryota/pezizomycotina_sp.yaml data/taxa/eukaryota/pezizomycotina_sp_arf18.yaml data/taxa/eukaryota/phaeangium_lefebvrei.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53041 with the expected reason: `attested rule: Peziza echinospora, 2 sources incl. NCBI`.
- The exact synonym and related synonym in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7794.
- GOLD aggregate: line 39879 records `organism_count=1` for `NCBITaxon:61495`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this target.
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
