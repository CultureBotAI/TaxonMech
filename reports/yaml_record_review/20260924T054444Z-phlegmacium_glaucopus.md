# Review: Phlegmacium glaucopus

- Verdict: pass
- Record: `data/taxa/eukaryota/phlegmacium_glaucopus.yaml`
- Target: `NCBITaxon:171480`

## Target

The record grounds `Phlegmacium glaucopus` as an exact seeded NCBI species under `NCBITaxon:2339270` (`Phlegmacium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 34997.

## Validation

- `just validate data/taxa/eukaryota/phlegmacium_glaucopus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlebopus_sp.yaml data/taxa/eukaryota/phlegmacium_cistoglaucopus.yaml data/taxa/eukaryota/phlegmacium_glaucopus.yaml data/taxa/eukaryota/phlegmacium_glaucopus_at_2004_276.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54263 with the expected reason: `attested rule: Phlegmacium glaucopus, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 58656 maps retired `NCBITaxon:2954798` to this identifier; an exact retained-row grep found no `NCBITaxon:2954798` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 34997.
- GOLD aggregate: line 14870 records `organism_count=1` for `NCBITaxon:171480`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, eight exact project rows, and one exact analysis row for this target.
- NCBI type material: lines 54566-54567 record `S CFP786` and `S F44760` neotype designations.
- StrainInfo: one direct exact strain and one exact deposit row were found for this target; no generated StrainInfo overlay rows were found.

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
