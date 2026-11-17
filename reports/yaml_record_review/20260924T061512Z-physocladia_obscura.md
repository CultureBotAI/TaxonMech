# Review: Physocladia obscura

- Verdict: pass
- Record: `data/taxa/eukaryota/physocladia_obscura.yaml`
- Target: `NCBITaxon:109957`

## Target

The record grounds `Physocladia obscura` as an exact seeded NCBI species under `NCBITaxon:109956` (`Physocladia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 19746.

## Validation

- `just validate data/taxa/eukaryota/physocladia_obscura.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/physocladia_obscura.yaml data/taxa/eukaryota/physocladia_sp.yaml data/taxa/eukaryota/phytomonas_francai.yaml data/taxa/eukaryota/phytophthora_agathidicida.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 53755 with the expected reason: `attested rule: Physocladia obscura, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, one related synonym, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 19746.
- GOLD aggregate: line 1844 records `organism_count=1` for `NCBITaxon:109957`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
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
