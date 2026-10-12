# Review: Phycomyces blakesleeanus

- Verdict: pass
- Record: `data/taxa/eukaryota/phycomyces_blakesleeanus.yaml`
- Target: `NCBITaxon:4837`

## Target

The record grounds `Phycomyces blakesleeanus` as an exact seeded NCBI species under `NCBITaxon:4836` (`Phycomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2086.

## Validation

- `just validate data/taxa/eukaryota/phycomyces_blakesleeanus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phoma_sp.yaml data/taxa/eukaryota/phomopsis_sp.yaml data/taxa/eukaryota/phragmotaenium_flavum.yaml data/taxa/eukaryota/phycomyces_blakesleeanus.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 51854 with the expected reason: `attested rule: Phycomyces blakesleeanus, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 2086.
- GOLD aggregate: line 36825 records `organism_count=30` for `NCBITaxon:4837`, matching the YAML GOLD attestation count; native GOLD has 30 exact organism rows, 60 exact project rows, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 144 direct exact strains and 225 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
