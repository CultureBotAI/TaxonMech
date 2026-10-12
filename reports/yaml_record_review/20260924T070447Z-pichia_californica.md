# Review: Pichia californica

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_californica.yaml`
- Target: `NCBITaxon:460514`

## Target

The record grounds `Pichia californica` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 103337.

## Validation

- `just validate data/taxa/eukaryota/pichia_californica.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_californica.yaml data/taxa/eukaryota/pichia_cephalocereana.yaml data/taxa/eukaryota/pichia_deserticola.yaml data/taxa/eukaryota/pichia_eremophila.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 55735 with the expected reason: `attested rule: Pichia californica, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, five related synonyms, and no broad synonyms; the YAML mirrors those eight synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:336313` into this identifier at line 68606; an exact retained-row check found no `NCBITaxon:336313` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 103337.
- GOLD aggregate: line 36210 records `organism_count=3` for `NCBITaxon:460514`, matching the YAML GOLD attestation count; native GOLD has three exact organism rows, three exact project rows, and two exact analysis rows for this target.
- NCBI type material: eight exact rows were found at lines 216465-216472.
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

`Pichia californica` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
