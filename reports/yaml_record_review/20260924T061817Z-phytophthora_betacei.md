# Review: Phytophthora betacei

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_betacei.yaml`
- Target: `NCBITaxon:2714593`

## Target

The record grounds `Phytophthora betacei` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 546304.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_betacei.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_aleatoria.yaml data/taxa/eukaryota/phytophthora_andina.yaml data/taxa/eukaryota/phytophthora_betacei.yaml data/taxa/eukaryota/phytophthora_boehmeriae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 62979 with the expected reason: `attested rule: Phytophthora betacei, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 546304.
- GOLD aggregate: line 25162 records `organism_count=1` for `NCBITaxon:2714593`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 112834-112839 contain six exact holotype or `culture from holotype` rows for this target.
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
