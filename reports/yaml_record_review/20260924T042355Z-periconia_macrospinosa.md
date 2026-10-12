# Review: Periconia macrospinosa

- Verdict: pass
- Record: `data/taxa/eukaryota/periconia_macrospinosa.yaml`
- Target: `NCBITaxon:97972`

## Target

The record grounds `Periconia macrospinosa` as an exact seeded NCBI species under `NCBITaxon:97971` (`Periconia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 16652.

## Validation

- `just validate data/taxa/eukaryota/periconia_macrospinosa.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/percolomonas_cosmopolitus.yaml data/taxa/eukaryota/perenniporia_fraxinea.yaml data/taxa/eukaryota/periconia_celtidis.yaml data/taxa/eukaryota/periconia_macrospinosa.yaml`: exited successfully
- Lineage audit: checked 17 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53591 with the expected reason: `attested rule: Periconia macrospinosa, 2 sources incl. NCBI`.
- The NCBI raw row has the exact synonym `Periconia macrospinosa Lefebvre & Aar.G. Johnson, 1949` and no broad or related synonyms; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 36364 maps old ID `NCBITaxon:2055983` into `NCBITaxon:97972`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 16652.
- GOLD aggregate: line 45194 records `organism_count=2` for `NCBITaxon:97972`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 30 exact deposit rows and 26 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:2055983` ID is consumed only through the merge map, not as a retained source row.
