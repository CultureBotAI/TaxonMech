# Review: Percolomonas cosmopolitus

- Verdict: pass
- Record: `data/taxa/eukaryota/percolomonas_cosmopolitus.yaml`
- Target: `NCBITaxon:63605`

## Target

The record grounds `Percolomonas cosmopolitus` as an exact seeded NCBI species under `NCBITaxon:63604` (`Percolomonas`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7999.

## Validation

- `just validate data/taxa/eukaryota/percolomonas_cosmopolitus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/percolomonas_cosmopolitus.yaml data/taxa/eukaryota/perenniporia_fraxinea.yaml data/taxa/eukaryota/periconia_celtidis.yaml data/taxa/eukaryota/periconia_macrospinosa.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53066 with the expected reason: `attested rule: Percolomonas cosmopolitus, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7999.
- GOLD aggregate: line 40141 records `organism_count=2` for `NCBITaxon:63605`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows and no exact project or analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: one exact deposit row and one direct exact strain were found for this target, but no generated StrainInfo overlay rows were emitted.

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
