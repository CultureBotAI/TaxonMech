# Review: Phaffomyces antillensis

- Verdict: pass
- Record: `data/taxa/eukaryota/phaffomyces_antillensis.yaml`
- Target: `NCBITaxon:54045`

## Target

The record grounds `Phaffomyces antillensis` as an exact seeded NCBI species under `NCBITaxon:83172` (`Phaffomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 6827.

## Validation

- `just validate data/taxa/eukaryota/phaffomyces_antillensis.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phaeotremella_skinneri.yaml data/taxa/eukaryota/phaffia_rhodozyma.yaml data/taxa/eukaryota/phaffomyces_antillensis.yaml data/taxa/eukaryota/phaffomyces_coquimbonensis.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52905 with the expected reason: `attested rule: Phaffomyces antillensis, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Pichia antillensis`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 6827.
- GOLD aggregate: line 38286 records `organism_count=1` for `NCBITaxon:54045`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 231230-231245 record 16 exact `Pichia antillensis` type-material rows.
- StrainInfo: 3 direct exact strains and 18 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
