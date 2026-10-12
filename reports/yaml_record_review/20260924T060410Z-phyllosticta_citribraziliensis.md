# Review: Phyllosticta citribraziliensis

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllosticta_citribraziliensis.yaml`
- Target: `NCBITaxon:989973`

## Target

The record grounds `Phyllosticta citribraziliensis` as an exact seeded NCBI species under `NCBITaxon:121621` (`Phyllosticta`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 206160.

## Validation

- `just validate data/taxa/eukaryota/phyllosticta_citribraziliensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phyllosticta_capitalensis.yaml data/taxa/eukaryota/phyllosticta_citriasiana.yaml data/taxa/eukaryota/phyllosticta_citribraziliensis.yaml data/taxa/eukaryota/phyllosticta_citricarpa.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 57086 with the expected reason: `attested rule: Phyllosticta citribraziliensis, 2 sources incl. NCBI`.
- The NCBI raw row has three related synonyms and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 88143 maps retired `NCBITaxon:595636` to this identifier; an exact retained-row grep found no `NCBITaxon:595636` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 206160.
- GOLD aggregate: line 45372 records `organism_count=2` for `NCBITaxon:989973`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, four exact project rows, and no exact analysis rows for this target.
- NCBI type material: lines 276573-276574 record `CBS 100098` and `CBS:100098` culture-from-holotype designations.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

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
