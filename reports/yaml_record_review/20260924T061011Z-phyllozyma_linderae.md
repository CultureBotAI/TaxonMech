# Review: Phyllozyma linderae

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllozyma_linderae.yaml`
- Target: `NCBITaxon:69979`

## Target

The record grounds `Phyllozyma linderae` as an exact seeded NCBI species under `NCBITaxon:1798851` (`Phyllozyma`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 9724.

## Validation

- `just validate data/taxa/eukaryota/phyllozyma_linderae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phyllosticta_sp_cpc_27169.yaml data/taxa/eukaryota/phyllozyma_linderae.yaml data/taxa/eukaryota/phyllozyma_linderae_cbs_7893.yaml data/taxa/eukaryota/physcia_stellaris.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53197 with the expected reason: `attested rule: Phyllozyma linderae, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 9724.
- GOLD aggregate: line 41605 records `organism_count=1` for `NCBITaxon:69979`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: lines 258566-258574 record `CBS 7893` and `CBS:7893` culture-from-type-material designations plus seven JCM, KCTC, and NRRL type-material designations.
- StrainInfo: 2 direct exact strains and 5 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
