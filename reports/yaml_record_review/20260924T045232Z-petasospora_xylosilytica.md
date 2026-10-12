# Review: Petasospora xylosilytica

- Verdict: pass
- Record: `data/taxa/eukaryota/petasospora_xylosilytica.yaml`
- Target: `NCBITaxon:1667614`

## Target

The record grounds `Petasospora xylosilytica` as an exact seeded NCBI species under `NCBITaxon:3713381` (`Petasospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 435117.

## Validation

- `just validate data/taxa/eukaryota/petasospora_xylosilytica.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/petasospora_veronae.yaml data/taxa/eukaryota/petasospora_xishuangbannaensis.yaml data/taxa/eukaryota/petasospora_xylosilytica.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 61007 with the expected reason: `attested rule: Petasospora xylosilytica, 2 sources incl. NCBI`.
- The exact synonym and eight related synonyms in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps five old IDs to this target at lines 6974, 11302, 22841, 22842, and 79289; exact retained-row scans found no old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 435117.
- GOLD aggregate: line 14353 records `organism_count=1` for `NCBITaxon:1667614`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 50861-50866 record six exact rows for this target.
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
