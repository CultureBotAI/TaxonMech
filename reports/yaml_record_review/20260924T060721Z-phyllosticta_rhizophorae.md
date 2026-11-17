# Review: Phyllosticta rhizophorae

- Verdict: pass
- Record: `data/taxa/eukaryota/phyllosticta_rhizophorae.yaml`
- Target: `NCBITaxon:2728938`

## Target

The record grounds `Phyllosticta rhizophorae` as an exact seeded NCBI species under `NCBITaxon:121621` (`Phyllosticta`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 548031.

## Validation

- `just validate data/taxa/eukaryota/phyllosticta_rhizophorae.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phyllosticta_citrichinensis.yaml data/taxa/eukaryota/phyllosticta_paracitricarpa.yaml data/taxa/eukaryota/phyllosticta_rhizophorae.yaml data/taxa/eukaryota/phyllosticta_sp.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63001 with the expected reason: `attested rule: Phyllosticta rhizophorae, 2 sources incl. NCBI`.
- The NCBI raw row has two related synonyms and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 548031.
- GOLD aggregate: line 25382 records `organism_count=4` for `NCBITaxon:2728938`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: lines 114346-114347 record `NCYUCC 19-0352` and `NCYUCC:19-0352` culture-from-holotype designations.
- StrainInfo: 2 direct exact strains and 2 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
