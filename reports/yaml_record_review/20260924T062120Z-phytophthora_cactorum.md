# Review: Phytophthora cactorum

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_cactorum.yaml`
- Target: `NCBITaxon:29920`

## Target

The record grounds `Phytophthora cactorum` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 3307.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_cactorum.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phytophthora_cactorum.yaml data/taxa/eukaryota/phytophthora_capsici.yaml data/taxa/eukaryota/phytophthora_castanetorum.yaml data/taxa/eukaryota/phytophthora_chlamydospora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52230 with the expected reason: `attested rule: Phytophthora cactorum, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, eight related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` maps seven retired IDs to this identifier at lines 47283 and 81106-81129; anchored lookups found no retained rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- NCBI: one matching taxonomy row at line 3307.
- GOLD aggregate: line 29975 records `organism_count=21` for `NCBITaxon:29920`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have 21 exact rows for this target.
- NCBI type material: lines 153296-153327 contain 32 exact epitype or reference-material rows for this target.
- StrainInfo: the exact source catalog has 103 direct strains and 117 deposit matches, but no generated StrainInfo assembly, exclusion, or related-record rows link to this target.

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
