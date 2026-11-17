# Review: Phytophthora capsici

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_capsici.yaml`
- Target: `NCBITaxon:4784`

## Target

The record grounds `Phytophthora capsici` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2059.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_capsici.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_cactorum.yaml data/taxa/eukaryota/phytophthora_capsici.yaml data/taxa/eukaryota/phytophthora_castanetorum.yaml data/taxa/eukaryota/phytophthora_chlamydospora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 51843 with the expected reason: `attested rule: Phytophthora capsici, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym and no related or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 2059.
- GOLD aggregate: line 36640 records `organism_count=8` for `NCBITaxon:4784`, matching the YAML GOLD attestation count; native GOLD has nine exact organism rows, nine exact project rows, and seven exact analysis rows for this target.
- NCBI type material: lines 219794-219811 contain 18 exact holotype or `culture from holotype` rows for this target.
- StrainInfo: the exact source catalog has 95 direct strains and 113 deposit matches, but no generated StrainInfo assembly, exclusion, or related-record rows link to this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive, and no generated StrainInfo overlay rows.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

None.
