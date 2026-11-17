# Review: Phytophthora constricta

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_constricta.yaml`
- Target: `NCBITaxon:929565`

## Target

The record grounds `Phytophthora constricta` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 195803.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_constricta.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_cinnamomi.yaml data/taxa/eukaryota/phytophthora_citricola.yaml data/taxa/eukaryota/phytophthora_colocasiae.yaml data/taxa/eukaryota/phytophthora_constricta.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 56928 with the expected reason: `attested rule: Phytophthora constricta, 2 sources incl. NCBI`.
- The NCBI raw row has four related synonyms and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:488866` to this identifier at line 81636; the old ID has no retained row in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- NCBI: one matching taxonomy row at line 195803.
- GOLD aggregate: line 44622 records `organism_count=1` for `NCBITaxon:929565`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 273588-273603 contain 16 exact `culture from holotype` rows for this target.
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
