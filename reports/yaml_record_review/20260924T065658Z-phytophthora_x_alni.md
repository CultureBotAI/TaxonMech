# Review: Phytophthora x alni

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_x_alni.yaml`
- Target: `NCBITaxon:299392`

## Target

The record grounds `Phytophthora x alni` as an exact seeded NCBI species under `NCBITaxon:4783` (`Phytophthora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 60950.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_x_alni.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_vignae_f_sp_adzukicola.yaml data/taxa/eukaryota/phytophthora_vignae_f_sp_vignae.yaml data/taxa/eukaryota/phytophthora_x_alni.yaml data/taxa/eukaryota/phytophthora_x_cambivora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 55065 with the expected reason: `attested rule: Phytophthora x alni, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, one related synonym, and no broad synonyms; the YAML mirrors those four synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:1861861` and `NCBITaxon:299391` into this identifier at lines 30380 and 59903; exact retained-row checks found no rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 60950.
- GOLD aggregate: line 30009 records `organism_count=1` for `NCBITaxon:299392`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: five exact rows were found at lines 153747-153751.
- StrainInfo: one direct exact strain and one exact deposit row were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora x alni` is a species-rank NCBI taxon under the `Phytophthora` genus lineage entry.
