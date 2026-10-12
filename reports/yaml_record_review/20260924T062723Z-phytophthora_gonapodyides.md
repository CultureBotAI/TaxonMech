# Review: Phytophthora gonapodyides

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_gonapodyides.yaml`
- Target: `NCBITaxon:78237`

## Target

The record grounds `Phytophthora gonapodyides` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 11377.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_gonapodyides.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_fragariae.yaml data/taxa/eukaryota/phytophthora_gonapodyides.yaml data/taxa/eukaryota/phytophthora_hibernalis.yaml data/taxa/eukaryota/phytophthora_idaei.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53322 with the expected reason: `attested rule: Phytophthora gonapodyides, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 11377.
- GOLD aggregate: line 42717 records `organism_count=1` for `NCBITaxon:78237`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 264319-264336 contain 18 exact epitype or `culture from epitype` rows for this target.
- StrainInfo: the exact source catalog has 12 direct strains and 15 deposit matches, but no generated StrainInfo assembly, exclusion, or related-record rows link to this target.

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
