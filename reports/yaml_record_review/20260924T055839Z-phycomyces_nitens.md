# Review: Phycomyces nitens

- Verdict: pass
- Record: `data/taxa/eukaryota/phycomyces_nitens.yaml`
- Target: `NCBITaxon:269771`

## Target

The record grounds `Phycomyces nitens` as an exact seeded NCBI species under `NCBITaxon:4836` (`Phycomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 55763.

## Validation

- `just validate data/taxa/eukaryota/phycomyces_nitens.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phycomyces_blakesleeanus_nrrl_1555.yaml data/taxa/eukaryota/phycomyces_nitens.yaml data/taxa/eukaryota/phycomyces_sp_jgi_2019a.yaml data/taxa/eukaryota/phyllachora_maydis.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54913 with the expected reason: `attested rule: Phycomyces nitens, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, one related synonym, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 55763.
- GOLD aggregate: line 24946 records `organism_count=6` for `NCBITaxon:269771`, matching the YAML GOLD attestation count; native GOLD has six exact organism rows, nine exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 36 direct exact strains and 70 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

None.
