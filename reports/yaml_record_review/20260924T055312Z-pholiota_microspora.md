# Review: Pholiota microspora

- Verdict: pass
- Record: `data/taxa/eukaryota/pholiota_microspora.yaml`
- Target: `NCBITaxon:1538424`

## Target

The record grounds `Pholiota microspora` as an exact seeded NCBI species under `NCBITaxon:13205` (`Pholiota`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 396457.

## Validation

- `just validate data/taxa/eukaryota/pholiota_microspora.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/pholiota_microspora.yaml data/taxa/eukaryota/pholiota_molesta.yaml data/taxa/eukaryota/phoma_herbarum.yaml data/taxa/eukaryota/phoma_leveillei.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60430 with the expected reason: `attested rule: Pholiota microspora, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, four related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 88843 maps retired `NCBITaxon:61267` to this identifier; an exact retained-row grep found no `NCBITaxon:61267` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 396457.
- GOLD aggregate: line 12239 records `organism_count=1` for `NCBITaxon:1538424`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
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
