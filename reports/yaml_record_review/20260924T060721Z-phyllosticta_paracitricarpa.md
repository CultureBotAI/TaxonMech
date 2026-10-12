# Review: Phyllosticta paracitricarpa

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllosticta_paracitricarpa.yaml`
- Target: `NCBITaxon:2016321`

## Target

The record grounds `Phyllosticta paracitricarpa` as an exact seeded NCBI species under `NCBITaxon:121621` (`Phyllosticta`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 510799.

## Validation

- `just validate data/taxa/eukaryota/phyllosticta_paracitricarpa.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phyllosticta_citrichinensis.yaml data/taxa/eukaryota/phyllosticta_paracitricarpa.yaml data/taxa/eukaryota/phyllosticta_rhizophorae.yaml data/taxa/eukaryota/phyllosticta_sp.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 61938 with the expected reason: `attested rule: Phyllosticta paracitricarpa, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 510799.
- GOLD aggregate: line 18759 records `organism_count=1` for `NCBITaxon:2016321`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: lines 77979-77982 record `CBS 14135 7`, `CBS:14135 7`, `CPC 27169`, and `CPC:27169` culture-from-holotype designations.
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
