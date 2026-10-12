# Review: Pichia inconspicua

- Verdict: pass
- Record: `data/taxa/eukaryota/pichia_inconspicua.yaml`
- Target: `NCBITaxon:52247`

## Target

The record grounds `Pichia inconspicua` as an exact seeded NCBI species under `NCBITaxon:4919` (`Pichia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, synonyms, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6566.

## Validation

- `just validate data/taxa/eukaryota/pichia_inconspicua.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pichia_heedii.yaml data/taxa/eukaryota/pichia_inconspicua.yaml data/taxa/eukaryota/pichia_insulana.yaml data/taxa/eukaryota/pichia_kluyveri.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 52857 with the expected reason: `attested rule: Pichia inconspicua, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, three related synonyms, and no broad synonyms; the YAML mirrors those five synonym assertions.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 6566.
- GOLD aggregate: line 37828 records `organism_count=4` for `NCBITaxon:52247`, matching the YAML GOLD attestation count; native GOLD has four exact organism rows, four exact project rows, and three exact analysis rows for this target.
- NCBI type material: 19 exact rows were found at lines 227792-227810.
- StrainInfo: 15 direct exact strains and 35 exact deposit rows were found for this target; no generated StrainInfo overlay rows target this taxon.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, NCBI synonyms, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Pichia inconspicua` is a species-rank NCBI taxon under the `Pichia` genus lineage entry.
