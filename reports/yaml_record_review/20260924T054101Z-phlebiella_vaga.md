# Review: Phlebiella vaga

- Verdict: pass
- Record: `data/taxa/eukaryota/phlebiella_vaga.yaml`
- Target: `NCBITaxon:301136`

## Target

The record grounds `Phlebiella vaga` as an exact seeded NCBI species under `NCBITaxon:139204` (`Phlebiella`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 61430.

## Validation

- `just validate data/taxa/eukaryota/phlebiella_vaga.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phlebiella_tulasnelloidea.yaml data/taxa/eukaryota/phlebiella_vaga.yaml data/taxa/eukaryota/phlebiopsis_gigantea.yaml data/taxa/eukaryota/phlebopus_portentosus.yaml`: exited successfully
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55071 with the expected reason: `attested rule: Phlebiella vaga, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, 13 related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` lines 24767-24770, 24772-24777, and 60455 map 11 retired IDs to this identifier; exact retained-row greps found none of those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 61430.
- GOLD aggregate: line 30139 records `organism_count=2` for `NCBITaxon:301136`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 2 direct exact strains and 2 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
