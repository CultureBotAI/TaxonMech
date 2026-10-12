# Review: Phlebiella tulasnelloidea

- Verdict: pass
- Record: `data/taxa/eukaryota/phlebiella_tulasnelloidea.yaml`
- Target: `NCBITaxon:2817877`

## Target

The record grounds `Phlebiella tulasnelloidea` as an exact seeded NCBI species under `NCBITaxon:139204` (`Phlebiella`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 559452.

## Validation

- `just validate data/taxa/eukaryota/phlebiella_tulasnelloidea.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlebiella_tulasnelloidea.yaml data/taxa/eukaryota/phlebiella_vaga.yaml data/taxa/eukaryota/phlebiopsis_gigantea.yaml data/taxa/eukaryota/phlebopus_portentosus.yaml`: exited successfully
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63284 with the expected reason: `attested rule: Phlebiella tulasnelloidea, 2 sources incl. NCBI`.
- The NCBI raw row has three exact synonyms, four related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 51094 maps retired `NCBITaxon:2761446` to this identifier; an exact retained-row grep found no `NCBITaxon:2761446` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 559452.
- GOLD aggregate: line 27170 records `organism_count=1` for `NCBITaxon:2817877`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: one direct exact strain and one exact deposit row were found for this target; no generated StrainInfo overlay rows were found.

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
