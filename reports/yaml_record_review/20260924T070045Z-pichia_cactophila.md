# Review: Pichia cactophila

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_cactophila.yaml`
- Target: `NCBITaxon:53657`

## Target

The record grounds `Pichia cactophila` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonym, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6793.

## Validation

- `just validate data/taxa/eukaryota/pichia_cactophila.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytopythium_vexans.yaml data/taxa/eukaryota/pichia_awuae.yaml data/taxa/eukaryota/pichia_cabralensis.yaml data/taxa/eukaryota/pichia_cactophila.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52889 with the expected reason: `attested rule: Pichia cactophila, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that synonym assertion.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 6793.
- GOLD aggregate: line 38212 records `organism_count=1` for `NCBITaxon:53657`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: 22 exact rows were found at lines 230677-230698.
- StrainInfo: 28 direct exact strains and 43 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the NCBI synonym, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia cactophila` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
