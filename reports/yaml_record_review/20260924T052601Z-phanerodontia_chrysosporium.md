# Review: Phanerodontia chrysosporium

- Verdict: pass
- Record: `data/taxa/eukaryota/phanerodontia_chrysosporium.yaml`
- Target: `NCBITaxon:2822231`

## Target

The record grounds `Phanerodontia chrysosporium` as an exact seeded NCBI species under `NCBITaxon:2492674` (`Phanerodontia`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 560750.

## Validation

- `just validate data/taxa/eukaryota/phanerodontia_chrysosporium.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phallus_impudicus_mar.yaml data/taxa/eukaryota/phanerochaete_carnosa.yaml data/taxa/eukaryota/phanerochaete_sordida.yaml data/taxa/eukaryota/phanerodontia_chrysosporium.yaml`: zero errors across 4 files
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63293 with the expected reason: `attested rule: Phanerodontia chrysosporium, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, four related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 84974 and 100292 map retired `NCBITaxon:5306` and `NCBITaxon:981175` to this identifier; exact retained-row greps found neither old ID in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 560750.
- GOLD aggregate: line 27278 records `organism_count=4` for `NCBITaxon:2822231`, matching the YAML GOLD attestation count; native GOLD has five exact organism rows, 115 exact project rows, and three exact analysis rows for this target.
- NCBI type material: lines 128300-128301 record `IFM 47473` and `IFM:47473` as `Sporotrichum pruinosum` type strains.
- StrainInfo: 94 direct exact strains and 172 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
