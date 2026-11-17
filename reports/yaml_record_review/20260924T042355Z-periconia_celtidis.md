# Review: Periconia celtidis

- Verdict: pass
- Record: `data/taxa/eukaryota/periconia_celtidis.yaml`
- Target: `NCBITaxon:2777685`

## Target

The record grounds `Periconia celtidis` as an exact seeded NCBI species under `NCBITaxon:97971` (`Periconia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 554204.

## Validation

- `just validate data/taxa/eukaryota/periconia_celtidis.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/percolomonas_cosmopolitus.yaml data/taxa/eukaryota/perenniporia_fraxinea.yaml data/taxa/eukaryota/periconia_celtidis.yaml data/taxa/eukaryota/periconia_macrospinosa.yaml`: exited successfully
- Lineage audit: checked 17 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63228 with the expected reason: `attested rule: Periconia celtidis, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Periconia celtidis Tennakoon, C.H. Kuo & K.D. Hyde, 2021` and `Periconia sp. DST-2020b`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 554204.
- GOLD aggregate: line 26360 records `organism_count=1` for `NCBITaxon:2777685`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: two exact rows at lines 120885-120886, covering holotype spellings for `MFLU 19-2784`.
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
