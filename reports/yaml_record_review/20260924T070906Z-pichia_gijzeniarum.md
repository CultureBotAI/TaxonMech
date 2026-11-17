# Review: Pichia gijzeniarum

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_gijzeniarum.yaml`
- Target: `NCBITaxon:2268992`

## Target

The record grounds `Pichia gijzeniarum` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 522510.

## Validation

- `just validate data/taxa/eukaryota/pichia_gijzeniarum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_ethanolica.yaml data/taxa/eukaryota/pichia_exigua.yaml data/taxa/eukaryota/pichia_fermentans.yaml data/taxa/eukaryota/pichia_gijzeniarum.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 62526 with the expected reason: `attested rule: Pichia gijzeniarum, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 522510.
- GOLD aggregate: line 21347 records `organism_count=1` for `NCBITaxon:2268992`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: two exact rows were found at lines 90445-90446.
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

`Pichia gijzeniarum` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
