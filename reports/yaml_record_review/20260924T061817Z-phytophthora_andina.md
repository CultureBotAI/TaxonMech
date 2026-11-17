# Review: Phytophthora andina

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_andina.yaml`
- Target: `NCBITaxon:283009`

## Target

The record grounds `Phytophthora andina` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 57562.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_andina.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_aleatoria.yaml data/taxa/eukaryota/phytophthora_andina.yaml data/taxa/eukaryota/phytophthora_betacei.yaml data/taxa/eukaryota/phytophthora_boehmeriae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 54976 with the expected reason: `attested rule: Phytophthora andina, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:983691` to this identifier at line 100366; the old ID has no retained row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- NCBI: one matching taxonomy row at line 57562.
- GOLD aggregate: line 27377 records `organism_count=1` for `NCBITaxon:283009`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 129116-129133 contain 18 exact `culture from holotype` rows for this target.
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
