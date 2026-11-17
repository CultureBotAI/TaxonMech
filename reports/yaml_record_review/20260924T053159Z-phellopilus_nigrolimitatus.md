# Review: Phellopilus nigrolimitatus

- Verdict: pass
- Record: `data/taxa/eukaryota/phellopilus_nigrolimitatus.yaml`
- Target: `NCBITaxon:127956`

## Target

The record grounds `Phellopilus nigrolimitatus` as an exact seeded NCBI species under `NCBITaxon:218113` (`Phellopilus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 24523.

## Validation

- `just validate data/taxa/eukaryota/phellopilus_nigrolimitatus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phellinus_viticola.yaml data/taxa/eukaryota/phellopilus_nigrolimitatus.yaml data/taxa/eukaryota/phenoliferia_glacialis.yaml data/taxa/eukaryota/phenoliferia_psychrophenolica.yaml`: zero errors across 4 files
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53909 with the expected reason: `attested rule: Phellopilus nigrolimitatus, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, three related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 24523.
- GOLD aggregate: line 6524 records `organism_count=1` for `NCBITaxon:127956`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 6 direct exact strains and 6 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
