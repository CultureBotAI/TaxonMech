# Review: Phaeotremella fagi

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeotremella_fagi.yaml`
- Target: `NCBITaxon:334123`

## Target

The record grounds `Phaeotremella fagi` as an exact seeded NCBI species under `NCBITaxon:1905114` (`Phaeotremella`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 68372.

## Validation

- `just validate data/taxa/eukaryota/phaeotremella_fagi.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeosphaeria_sp.yaml data/taxa/eukaryota/phaeosphaeriaceae_sp_src1lsm3a.yaml data/taxa/eukaryota/phaeosphaeriaceae_sp_um_1110.yaml data/taxa/eukaryota/phaeotremella_fagi.yaml`: exited successfully
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55265 with the expected reason: `attested rule: Phaeotremella fagi, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Cryptococcus fagi`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 68372.
- GOLD aggregate: line 32389 records `organism_count=1` for `NCBITaxon:334123`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 179468-179469 record `CBS 9964` and `CBS:9964` as cultures from type material.
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
