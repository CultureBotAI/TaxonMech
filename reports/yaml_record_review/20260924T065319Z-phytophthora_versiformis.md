# Review: Phytophthora versiformis

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_versiformis.yaml`
- Target: `NCBITaxon:1833877`

## Target

The record grounds `Phytophthora versiformis` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 477879.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_versiformis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_syringae.yaml data/taxa/eukaryota/phytophthora_tubulina.yaml data/taxa/eukaryota/phytophthora_versiformis.yaml data/taxa/eukaryota/phytophthora_vignae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 61335 with the expected reason: `attested rule: Phytophthora versiformis, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 477879.
- GOLD aggregate: line 16222 records `organism_count=1` for `NCBITaxon:1833877`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: seven exact rows were found at lines 62994-63000.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora versiformis` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
