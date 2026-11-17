# Review: Phoma herbarum

- Verdict: pass
- Record: `data/taxa/eukaryota/phoma_herbarum.yaml`
- Target: `NCBITaxon:73001`

## Target

The record grounds `Phoma herbarum` as an exact seeded NCBI species under `NCBITaxon:37463` (`Phoma`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 10244.

## Validation

- `just validate data/taxa/eukaryota/phoma_herbarum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pholiota_microspora.yaml data/taxa/eukaryota/pholiota_molesta.yaml data/taxa/eukaryota/phoma_herbarum.yaml data/taxa/eukaryota/phoma_leveillei.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 17 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53248 with the expected reason: `attested rule: Phoma herbarum, 2 sources incl. NCBI`.
- The NCBI raw row has four exact synonyms, five related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 12766, 26788, 26817, 30301, and 86915 map five retired IDs to this identifier; exact retained-row greps found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 10244.
- GOLD aggregate: line 42036 records `organism_count=1` for `NCBITaxon:73001`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 260764-260771 record `UAMH 10909` and `UAMH:10909` holotypes, `PD 84/676` and `PD:84/676` cultures from holotype, `HMAS 246691` and `HMAS:246691` holotypes, and `CBS 615.75` and `CBS:615.75` reference-material designations.
- StrainInfo: 50 direct exact strains and 66 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
