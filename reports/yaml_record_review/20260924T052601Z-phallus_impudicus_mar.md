# Review: Phallus impudicus MAR

- Verdict: pass
- Record: `data/taxa/eukaryota/phallus_impudicus_mar.yaml`
- Target: `NCBITaxon:1150939`

## Target

The record grounds `Phallus impudicus MAR` as an exact seeded NCBI strain under `NCBITaxon:146781` (`Phallus impudicus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 251813.

## Validation

- `just validate data/taxa/eukaryota/phallus_impudicus_mar.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phallus_impudicus_mar.yaml data/taxa/eukaryota/phanerochaete_carnosa.yaml data/taxa/eukaryota/phanerochaete_sordida.yaml data/taxa/eukaryota/phanerodontia_chrysosporium.yaml`: zero errors across 4 files
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58007 with the expected reason: `attested rule: Phallus impudicus MAR, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, broad, or related synonyms; the YAML mirrors that absence.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 251813.
- GOLD aggregate: line 3053 records `organism_count=1` for `NCBITaxon:1150939`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
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
