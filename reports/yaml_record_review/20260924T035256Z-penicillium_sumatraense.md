# Review: Penicillium sumatraense

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sumatraense.yaml`
- Target: `NCBITaxon:70558`

## Target

The record grounds `Penicillium sumatraense` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 9919.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sumatraense.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_subturcoseum.yaml data/taxa/eukaryota/penicillium_sucrivorum.yaml data/taxa/eukaryota/penicillium_sumatraense.yaml data/taxa/eukaryota/penicillium_svalbardense.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53210 with the expected reason: `attested rule: Penicillium sumatraense, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, `Penicillium sumatrense`, no broad synonyms, and two related synonyms, `Penicillium sumatraense Svilv., 1936` and `Penicillium sumatraense Szilvinyi, 1936`; the YAML mirrors those values.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:70558`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 9919.
- GOLD aggregate: line 41699 records `organism_count=1` for `NCBITaxon:70558`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: two exact rows at lines 259083-259084, covering culture-from-lectotype spellings `CBS 281.36` and `CBS:281.36`.
- StrainInfo: exact StrainInfo has 3 direct strains and 4 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:70558`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The exact synonym and two authority-bearing related synonyms agree exactly with the NCBI raw row.
