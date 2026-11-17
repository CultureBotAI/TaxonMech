# Review: Phragmotaenium flavum

- Verdict: pass
- Record: `data/taxa/eukaryota/phragmotaenium_flavum.yaml`
- Target: `NCBITaxon:58914`

## Target

The record grounds `Phragmotaenium flavum` as an exact seeded NCBI species under `NCBITaxon:169883` (`Phragmotaenium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7442.

## Validation

- `just validate data/taxa/eukaryota/phragmotaenium_flavum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phoma_sp.yaml data/taxa/eukaryota/phomopsis_sp.yaml data/taxa/eukaryota/phragmotaenium_flavum.yaml data/taxa/eukaryota/phycomyces_blakesleeanus.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52998 with the expected reason: `attested rule: Phragmotaenium flavum, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 7442.
- GOLD aggregate: line 39572 records `organism_count=5` for `NCBITaxon:58914`, matching the YAML GOLD attestation count; native GOLD has five exact organism rows and no exact project or analysis rows for this target.
- NCBI type material: lines 239823-239824 record `IFO 6833` and `IFO:6833` type-material designations.
- StrainInfo: 2 direct exact strains and 6 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
