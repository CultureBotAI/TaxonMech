# Review: Pichia cephalocereana

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_cephalocereana.yaml`
- Target: `NCBITaxon:53940`

## Target

The record grounds `Pichia cephalocereana` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6806.

## Validation

- `just validate data/taxa/eukaryota/pichia_cephalocereana.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_californica.yaml data/taxa/eukaryota/pichia_cephalocereana.yaml data/taxa/eukaryota/pichia_deserticola.yaml data/taxa/eukaryota/pichia_eremophila.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52899 with the expected reason: `attested rule: Pichia cephalocereana, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, two related synonyms, and no broad synonyms; the YAML mirrors those three synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 6806.
- GOLD aggregate: line 38257 records `organism_count=1` for `NCBITaxon:53940`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: five exact rows were found at lines 230989-230993.
- StrainInfo: three direct exact strains and 11 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia cephalocereana` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
