# Review: Pichia cabralensis

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_cabralensis.yaml`
- Target: `NCBITaxon:1249861`

## Target

The record grounds `Pichia cabralensis` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 288278.

## Validation

- `just validate data/taxa/eukaryota/pichia_cabralensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytopythium_vexans.yaml data/taxa/eukaryota/pichia_awuae.yaml data/taxa/eukaryota/pichia_cabralensis.yaml data/taxa/eukaryota/pichia_cactophila.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 58689 with the expected reason: `attested rule: Pichia cabralensis, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, three related synonyms, and no broad synonyms; the YAML mirrors those four synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:687203` into this identifier at line 92252; an exact retained-row check found no `NCBITaxon:687203` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 288278.
- GOLD aggregate: line 6010 records `organism_count=1` for `NCBITaxon:1249861`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: five exact rows were found at lines 16935-16939.
- StrainInfo: three direct exact strains and six exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia cabralensis` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
