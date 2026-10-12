# Review: Phanerochaete sordida

- Verdict: pass
- Record: `data/taxa/eukaryota/phanerochaete_sordida.yaml`
- Target: `NCBITaxon:48140`

## Target

The record grounds `Phanerochaete sordida` as an exact seeded NCBI species under `NCBITaxon:5305` (`Phanerochaete`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6135.

## Validation

- `just validate data/taxa/eukaryota/phanerochaete_sordida.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phallus_impudicus_mar.yaml data/taxa/eukaryota/phanerochaete_carnosa.yaml data/taxa/eukaryota/phanerochaete_sordida.yaml data/taxa/eukaryota/phanerodontia_chrysosporium.yaml`: zero errors across 4 files
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52745 with the expected reason: `attested rule: Phanerochaete sordida, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, one related synonym, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 6135.
- GOLD aggregate: line 36770 records `organism_count=1` for `NCBITaxon:48140`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 17 direct exact strains and 22 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
