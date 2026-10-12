# Review: Phyllosticta citriasiana

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllosticta_citriasiana.yaml`
- Target: `NCBITaxon:595635`

## Target

The record grounds `Phyllosticta citriasiana` as an exact seeded NCBI species under `NCBITaxon:121621` (`Phyllosticta`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 141412.

## Validation

- `just validate data/taxa/eukaryota/phyllosticta_citriasiana.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phyllosticta_capitalensis.yaml data/taxa/eukaryota/phyllosticta_citriasiana.yaml data/taxa/eukaryota/phyllosticta_citribraziliensis.yaml data/taxa/eukaryota/phyllosticta_citricarpa.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56131 with the expected reason: `attested rule: Phyllosticta citriasiana, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 141412.
- GOLD aggregate: line 39680 records `organism_count=4` for `NCBITaxon:595635`, matching the YAML GOLD attestation count; native GOLD has three exact organism rows, six exact project rows, and one exact analysis row for this target.
- NCBI type material: lines 240446-240447 record `CBS 120486` and `CBS:120486` culture-from-holotype designations.
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
