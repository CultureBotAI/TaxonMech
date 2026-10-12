# Review: Phoma leveillei

- Verdict: pass
- Record: `data/taxa/eukaryota/phoma_leveillei.yaml`
- Target: `NCBITaxon:196108`

## Target

The record grounds `Phoma leveillei` as an exact seeded NCBI species under `NCBITaxon:37463` (`Phoma`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 38941.

## Validation

- `just validate data/taxa/eukaryota/phoma_leveillei.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pholiota_microspora.yaml data/taxa/eukaryota/pholiota_molesta.yaml data/taxa/eukaryota/phoma_herbarum.yaml data/taxa/eukaryota/phoma_leveillei.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 17 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54430 with the expected reason: `attested rule: Phoma leveillei, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, one related synonym, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 29347 maps retired `NCBITaxon:1826962` to this identifier; an exact retained-row grep found no `NCBITaxon:1826962` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 38941.
- GOLD aggregate: line 18027 records `organism_count=1` for `NCBITaxon:196108`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 19 direct exact strains and 25 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
