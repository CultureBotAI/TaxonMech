# Review: Pichia fermentans

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_fermentans.yaml`
- Target: `NCBITaxon:53655`

## Target

The record grounds `Pichia fermentans` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6791.

## Validation

- `just validate data/taxa/eukaryota/pichia_fermentans.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_ethanolica.yaml data/taxa/eukaryota/pichia_exigua.yaml data/taxa/eukaryota/pichia_fermentans.yaml data/taxa/eukaryota/pichia_gijzeniarum.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52887 with the expected reason: `attested rule: Pichia fermentans, 2 sources incl. NCBI`.
- The NCBI raw row has five exact synonyms, seven related synonyms, and no broad synonyms; the YAML mirrors those 12 synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:51726` and `NCBITaxon:65960` into this identifier at lines 83374 and 90877; exact retained-row checks found no rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 6791.
- GOLD aggregate: line 38210 records `organism_count=1` for `NCBITaxon:53655`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: 30 exact rows were found at lines 230633-230662.
- StrainInfo: 104 direct exact strains and 160 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia fermentans` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
