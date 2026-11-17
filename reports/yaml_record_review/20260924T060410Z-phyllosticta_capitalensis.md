# Review: Phyllosticta capitalensis

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllosticta_capitalensis.yaml`
- Target: `NCBITaxon:121624`

## Target

The record grounds `Phyllosticta capitalensis` as an exact seeded NCBI species under `NCBITaxon:121621` (`Phyllosticta`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 22795.

## Validation

- `just validate data/taxa/eukaryota/phyllosticta_capitalensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phyllosticta_capitalensis.yaml data/taxa/eukaryota/phyllosticta_citriasiana.yaml data/taxa/eukaryota/phyllosticta_citribraziliensis.yaml data/taxa/eukaryota/phyllosticta_citricarpa.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53874 with the expected reason: `attested rule: Phyllosticta capitalensis, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 104, 8395, and 40570 map three retired IDs to this identifier; exact retained-row greps found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 22795.
- GOLD aggregate: line 5149 records `organism_count=9` for `NCBITaxon:121624`, matching the YAML GOLD attestation count; native GOLD has nine exact organism rows, 15 exact project rows, and one exact analysis row for this target.
- NCBI type material: lines 14440-14443 record `CBS 128856`, `CBS:128856`, `CPC 18848`, and `CPC:18848` culture-from-epitype designations.
- StrainInfo: 30 direct exact strains and 42 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
