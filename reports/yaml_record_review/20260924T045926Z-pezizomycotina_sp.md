# Review: Pezizomycotina sp.

- Verdict: pass
- Record: `data/taxa/eukaryota/pezizomycotina_sp.yaml`
- Target: `NCBITaxon:1891160`

## Target

The record grounds `Pezizomycotina sp.` as an exact seeded NCBI species under `NCBITaxon:150231` (`unclassified Pezizomycotina`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 491006.

## Validation

- `just validate data/taxa/eukaryota/pezizomycotina_sp.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/peziza_echinospora.yaml data/taxa/eukaryota/pezizomycotina_sp.yaml data/taxa/eukaryota/pezizomycotina_sp_arf18.yaml data/taxa/eukaryota/phaeangium_lefebvrei.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 61462 with the expected reason: `attested rule: Pezizomycotina sp., 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 491006.
- GOLD aggregate: line 17031 records `organism_count=1` for `NCBITaxon:1891160`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
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
