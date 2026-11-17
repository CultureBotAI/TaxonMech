# Review: Phytophthora multivora

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_multivora.yaml`
- Target: `NCBITaxon:596104`

## Target

The record grounds `Phytophthora multivora` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 141791.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_multivora.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_megakarya.yaml data/taxa/eukaryota/phytophthora_melonis.yaml data/taxa/eukaryota/phytophthora_multivora.yaml data/taxa/eukaryota/phytophthora_nicotianae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 56132 with the expected reason: `attested rule: Phytophthora multivora, 2 sources incl. NCBI`.
- The NCBI raw row has four related synonyms and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` maps four retired IDs to this identifier at lines 81634, 85761-85762, and 87005; anchored lookups found no retained rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- NCBI: one matching taxonomy row at line 141791.
- GOLD aggregate: line 39691 records `organism_count=2` for `NCBITaxon:596104`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have two exact rows for this target.
- NCBI type material: lines 240501-240516 contain 16 exact holotype or `culture from holotype` rows for this target.
- StrainInfo: the exact source catalog has 17 direct strains and 17 deposit matches, but no generated StrainInfo assembly, exclusion, or related-record rows link to this target.

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
