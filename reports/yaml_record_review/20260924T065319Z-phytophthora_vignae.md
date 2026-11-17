# Review: Phytophthora vignae

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_vignae.yaml`
- Target: `NCBITaxon:67595`

## Target

The record grounds `Phytophthora vignae` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonym, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 8970.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_vignae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_syringae.yaml data/taxa/eukaryota/phytophthora_tubulina.yaml data/taxa/eukaryota/phytophthora_versiformis.yaml data/taxa/eukaryota/phytophthora_vignae.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53148 with the expected reason: `attested rule: Phytophthora vignae, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that synonym assertion.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 8970.
- GOLD aggregate: line 41072 records `organism_count=1` for `NCBITaxon:67595`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this direct target.
- NCBI type material: ten exact rows were found at lines 253560-253569.
- StrainInfo: eight direct exact strains and 14 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the NCBI synonym, the direct-target GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora vignae` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry; its GOLD attestation intentionally counts only records filed directly under this taxon.
