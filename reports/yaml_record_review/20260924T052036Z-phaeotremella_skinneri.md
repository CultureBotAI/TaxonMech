# Review: Phaeotremella skinneri

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeotremella_skinneri.yaml`
- Target: `NCBITaxon:89928`

## Target

The record grounds `Phaeotremella skinneri` as an exact seeded NCBI species under `NCBITaxon:1905114` (`Phaeotremella`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 14430.

## Validation

- `just validate data/taxa/eukaryota/phaeotremella_skinneri.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phaeotremella_skinneri.yaml data/taxa/eukaryota/phaffia_rhodozyma.yaml data/taxa/eukaryota/phaffomyces_antillensis.yaml data/taxa/eukaryota/phaffomyces_coquimbonensis.yaml`: exited successfully
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53484 with the expected reason: `attested rule: Phaeotremella skinneri, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Cryptococcus skinneri`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 14430.
- GOLD aggregate: line 44075 records `organism_count=1` for `NCBITaxon:89928`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 271623-271644 record 22 exact rows under `Cryptococcus skinneri`, covering `CBS 5029` and `CBS:5029` cultures from type material plus ATCC, BCRC, CCRC, DBVPG, IFO, IGC, JCM, MUCL, NRRL, and UCD type-material designations.
- StrainInfo: 6 direct exact strains and 18 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
