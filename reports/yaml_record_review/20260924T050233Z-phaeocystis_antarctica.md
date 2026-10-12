# Review: Phaeocystis antarctica

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeocystis_antarctica.yaml`
- Target: `NCBITaxon:33657`

## Target

The record grounds `Phaeocystis antarctica` as an exact seeded NCBI species under `NCBITaxon:33656` (`Phaeocystis`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 3572.

## Validation

- `just validate data/taxa/eukaryota/phaeocystis_antarctica.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeoannellomyces_elegans.yaml data/taxa/eukaryota/phaeococcomyces_sp.yaml data/taxa/eukaryota/phaeocystis_antarctica.yaml data/taxa/eukaryota/phaeocystis_cf_globosa.yaml`: exited successfully
- Lineage audit: checked 9 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52261 with the expected reason: `attested rule: Phaeocystis antarctica, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that pattern.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 3572.
- GOLD aggregate: line 32471 records `organism_count=3` for `NCBITaxon:33657`, matching the YAML GOLD attestation count; native GOLD has four exact organism rows, one exact project row, and one exact analysis row for this target.
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
