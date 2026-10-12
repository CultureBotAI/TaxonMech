# Review: Phaeocystis cordata

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeocystis_cordata.yaml`
- Target: `NCBITaxon:118079`

## Target

The record grounds `Phaeocystis cordata` as an exact seeded NCBI species under `NCBITaxon:33656` (`Phaeocystis`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 22082.

## Validation

- `just validate data/taxa/eukaryota/phaeocystis_cordata.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeocystis_cordata.yaml data/taxa/eukaryota/phaeocystis_globosa.yaml data/taxa/eukaryota/phaeocystis_jahnii.yaml data/taxa/eukaryota/phaeocystis_rex.yaml`: exited successfully
- Lineage audit: checked 9 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53839 with the expected reason: `attested rule: Phaeocystis cordata, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that pattern.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 22082.
- GOLD aggregate: line 3969 records `organism_count=2` for `NCBITaxon:118079`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, one exact project row, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 2 direct exact strains and 3 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
