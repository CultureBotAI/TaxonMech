# Review: Phaeocystis globosa

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeocystis_globosa.yaml`
- Target: `NCBITaxon:33658`

## Target

The record grounds `Phaeocystis globosa` as an exact seeded NCBI species under `NCBITaxon:33656` (`Phaeocystis`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 3573.

## Validation

- `just validate data/taxa/eukaryota/phaeocystis_globosa.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeocystis_cordata.yaml data/taxa/eukaryota/phaeocystis_globosa.yaml data/taxa/eukaryota/phaeocystis_jahnii.yaml data/taxa/eukaryota/phaeocystis_rex.yaml`: exited successfully
- Lineage audit: checked 9 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52262 with the expected reason: `attested rule: Phaeocystis globosa, 2 sources incl. NCBI`.
- The four exact synonyms and 25 related synonyms in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps 24 old IDs to this target at lines 21586, 26618-26620, 26622-26625, 30051, 31836-31839, 46133, 79431-79437, 79441, and 79443-79444; exact retained-row scans found no old-ID rows in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 3573.
- GOLD aggregate: line 32472 records `organism_count=8` for `NCBITaxon:33658`, matching the YAML GOLD attestation count; native GOLD has seven exact organism rows, seven exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 17 direct exact strains and 17 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
