# Review: Phytophthora castanetorum

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_castanetorum.yaml`
- Target: `NCBITaxon:1985165`

## Target

The record grounds `Phytophthora castanetorum` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 508071.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_castanetorum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_cactorum.yaml data/taxa/eukaryota/phytophthora_capsici.yaml data/taxa/eukaryota/phytophthora_castanetorum.yaml data/taxa/eukaryota/phytophthora_chlamydospora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 61819 with the expected reason: `attested rule: Phytophthora castanetorum, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 508071.
- GOLD aggregate: line 18376 records `organism_count=1` for `NCBITaxon:1985165`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 76563-76566 contain four exact `culture from holotype` rows for this target.
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
