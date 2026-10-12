# Review: Pichia kluyveri

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_kluyveri.yaml`
- Target: `NCBITaxon:36015`

## Target

The record grounds `Pichia kluyveri` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 4029.

## Validation

- `just validate data/taxa/eukaryota/pichia_kluyveri.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_heedii.yaml data/taxa/eukaryota/pichia_inconspicua.yaml data/taxa/eukaryota/pichia_insulana.yaml data/taxa/eukaryota/pichia_kluyveri.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52298 with the expected reason: `attested rule: Pichia kluyveri, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, one related synonym, and no broad synonyms; the YAML mirrors those two synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` maps retired `NCBITaxon:53938` into this identifier at line 85224; an exact retained-row check found no `NCBITaxon:53938` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` edge is expected in the YAML.

## Evidence

- NCBI: one matching taxonomy row at line 4029.
- GOLD aggregate: line 33235 records `organism_count=2` for `NCBITaxon:36015`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, two exact project rows, and one exact analysis row for this target.
- NCBI type material: 17 exact rows were found at lines 193436-193452.
- StrainInfo: 78 direct exact strains and 110 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia kluyveri` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
