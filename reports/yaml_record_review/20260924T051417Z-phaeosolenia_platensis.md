# Review: Phaeosolenia platensis

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeosolenia_platensis.yaml`
- Target: `NCBITaxon:269161`

## Target

The record grounds `Phaeosolenia platensis` as an exact seeded NCBI species under `NCBITaxon:269160` (`Phaeosolenia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 55602.

## Validation

- `just validate data/taxa/eukaryota/phaeosolenia_platensis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeomonas_parva.yaml data/taxa/eukaryota/phaeomoniella_chlamydospora.yaml data/taxa/eukaryota/phaeosolenia_platensis.yaml data/taxa/eukaryota/phaeosphaeria_elongata.yaml`: exited successfully
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54910 with the expected reason: `attested rule: Phaeosolenia platensis, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Phaeosolenia densa`, related synonym `Phaeosolenia platensis Speg., 1902`, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 55602.
- GOLD aggregate: line 24839 records `organism_count=1` for `NCBITaxon:269161`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this target.
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
