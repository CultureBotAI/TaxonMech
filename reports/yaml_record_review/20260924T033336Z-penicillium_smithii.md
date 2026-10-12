# Review: Penicillium smithii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_smithii.yaml`
- Target: `NCBITaxon:1167578`

## Target

The record grounds `Penicillium smithii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 257896.

## Validation

- `just validate data/taxa/eukaryota/penicillium_smithii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_smithii.yaml data/taxa/eukaryota/penicillium_solitum.yaml data/taxa/eukaryota/penicillium_sp.yaml data/taxa/eukaryota/penicillium_sp_cmv_2018d.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 58099 with the expected reason: `attested rule: Penicillium smithii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium smithii Quintan., 1982`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:1167578`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 257896.
- GOLD aggregate: line 3567 records `organism_count=1` for `NCBITaxon:1167578`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: eight exact rows at lines 10893-10900, all culture from neotype, covering `CBS 276.83`, `CECT 2744`, `DTO 187-F7`, and `IMI 259693` delimiter variants.
- StrainInfo: exact StrainInfo has 8 direct strains and 11 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:1167578`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The StrainInfo evidence is exact at source but does not overlay onto a generated BacDive-derived local strain.
