# Review: Phaeocystis rex

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeocystis_rex.yaml`
- Target: `NCBITaxon:1631189`

## Target

The record grounds `Phaeocystis rex` as an exact seeded NCBI species under `NCBITaxon:33656` (`Phaeocystis`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 424025.

## Validation

- `just validate data/taxa/eukaryota/phaeocystis_rex.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeocystis_cordata.yaml data/taxa/eukaryota/phaeocystis_globosa.yaml data/taxa/eukaryota/phaeocystis_jahnii.yaml data/taxa/eukaryota/phaeocystis_rex.yaml`: exited successfully
- Lineage audit: checked 9 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60931 with the expected reason: `attested rule: Phaeocystis rex, 2 sources incl. NCBI`.
- The two exact synonyms and three related synonyms in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps two old IDs to this target at lines 15076 and 22252; exact retained-row scans found no old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 424025.
- GOLD aggregate: line 13956 records `organism_count=1` for `NCBITaxon:1631189`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, one exact project row, and no exact analysis rows for this target.
- NCBI type material: lines 48232-48239 record eight exact rows for this target.
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
