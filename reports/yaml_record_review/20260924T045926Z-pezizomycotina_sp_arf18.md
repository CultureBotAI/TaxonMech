# Review: Pezizomycotina sp. ARF18

- Verdict: pass
- Record: `data/taxa/eukaryota/pezizomycotina_sp_arf18.yaml`
- Target: `NCBITaxon:1427494`

## Target

The record grounds `Pezizomycotina sp. ARF18` as an exact seeded NCBI species under `NCBITaxon:150231` (`unclassified Pezizomycotina`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 356665.

## Validation

- `just validate data/taxa/eukaryota/pezizomycotina_sp_arf18.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peziza_echinospora.yaml data/taxa/eukaryota/pezizomycotina_sp.yaml data/taxa/eukaryota/pezizomycotina_sp_arf18.yaml data/taxa/eukaryota/phaeangium_lefebvrei.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60096 with the expected reason: `attested rule: Pezizomycotina sp. ARF18, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 356665.
- GOLD aggregate: line 10232 records `organism_count=1` for `NCBITaxon:1427494`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
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
