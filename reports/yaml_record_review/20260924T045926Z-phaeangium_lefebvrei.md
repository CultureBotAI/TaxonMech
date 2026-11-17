# Review: Phaeangium lefebvrei

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeangium_lefebvrei.yaml`
- Target: `NCBITaxon:164550`

## Target

The record grounds `Phaeangium lefebvrei` as an exact seeded NCBI species under `NCBITaxon:164549` (`Phaeangium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 33783.

## Validation

- `just validate data/taxa/eukaryota/phaeangium_lefebvrei.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peziza_echinospora.yaml data/taxa/eukaryota/pezizomycotina_sp.yaml data/taxa/eukaryota/pezizomycotina_sp_arf18.yaml data/taxa/eukaryota/phaeangium_lefebvrei.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54206 with the expected reason: `attested rule: Phaeangium lefebvrei, 2 sources incl. NCBI`.
- The exact synonym and related synonym in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:164551` to this target at line 22905; an exact retained-row scan found no old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 33783.
- GOLD aggregate: line 14119 records `organism_count=2` for `NCBITaxon:164550`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, four exact project rows, and no exact analysis rows for this target.
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
