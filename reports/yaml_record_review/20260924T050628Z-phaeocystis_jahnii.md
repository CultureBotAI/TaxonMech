# Review: Phaeocystis jahnii

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeocystis_jahnii.yaml`
- Target: `NCBITaxon:118080`

## Target

The record grounds `Phaeocystis jahnii` as an exact seeded NCBI species under `NCBITaxon:33656` (`Phaeocystis`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 22083.

## Validation

- `just validate data/taxa/eukaryota/phaeocystis_jahnii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeocystis_cordata.yaml data/taxa/eukaryota/phaeocystis_globosa.yaml data/taxa/eukaryota/phaeocystis_jahnii.yaml data/taxa/eukaryota/phaeocystis_rex.yaml`: exited successfully
- Lineage audit: checked 9 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53840 with the expected reason: `attested rule: Phaeocystis jahnii, 2 sources incl. NCBI`.
- The five related synonyms in the YAML match the NCBI raw row, which has no exact or broad synonyms.
- `data/raw/ncbi_merged_ids.tsv` maps four old IDs to this target at lines 26621 and 79438-79440; exact retained-row scans found no old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 22083.
- GOLD aggregate: line 3970 records `organism_count=1` for `NCBITaxon:118080`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: one direct exact strain and one deposit row were found for this target; generated StrainInfo overlay files have no exact target rows.

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
