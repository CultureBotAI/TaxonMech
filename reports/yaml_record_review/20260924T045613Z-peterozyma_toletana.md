# Review: Peterozyma toletana

- Verdict: pass
- Record: `data/taxa/eukaryota/peterozyma_toletana.yaml`
- Target: `NCBITaxon:1196395`

## Target

The record grounds `Peterozyma toletana` as an exact seeded NCBI species under `NCBITaxon:1196393` (`Peterozyma`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 269133.

## Validation

- `just validate data/taxa/eukaryota/peterozyma_toletana.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peterozyma_toletana.yaml data/taxa/eukaryota/peterozyma_xylosa.yaml data/taxa/eukaryota/pezicula_carpinea.yaml data/taxa/eukaryota/pezicula_radicicola.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58287 with the expected reason: `attested rule: Peterozyma toletana, 2 sources incl. NCBI`.
- The two exact synonyms and three related synonyms in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:53652` to this target at line 85134; an exact retained-row scan found no old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 269133.
- GOLD aggregate: line 4729 records `organism_count=1` for `NCBITaxon:1196395`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 12935-12939 record five exact rows for this target.
- StrainInfo: 13 direct exact strains and 29 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
