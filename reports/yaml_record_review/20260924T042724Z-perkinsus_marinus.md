# Review: Perkinsus marinus

- Verdict: pass
- Record: `data/taxa/eukaryota/perkinsus_marinus.yaml`
- Target: `NCBITaxon:31276`

## Target

The record grounds `Perkinsus marinus` as an exact seeded NCBI species under `NCBITaxon:28000` (`Perkinsus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 3313.

## Validation

- `just validate data/taxa/eukaryota/perkinsus_marinus.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/perkinsus_chesapeaki.yaml data/taxa/eukaryota/perkinsus_marinus.yaml data/taxa/eukaryota/perkinsus_marinus_atcc_50983.yaml data/taxa/eukaryota/perkinsus_olseni.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52236 with the expected reason: `attested rule: Perkinsus marinus, 2 sources incl. NCBI`.
- The NCBI raw row has the exact synonym `Dermocystidium marinum`, no broad synonyms, and two related synonyms, `Dermocystidium marinum Mackin, H.M.Owen & Collier, 1950` and `Perkinsus marinus (Mackin, H.M.Owen & Collier) Levine, 1978`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 3313.
- GOLD aggregate: line 31555 records `organism_count=1` for `NCBITaxon:31276`, matching the YAML GOLD attestation count; native GOLD has one exact organism row and no exact project or analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 57 exact deposit rows and 57 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The GOLD attestation covers records filed directly under this species; descendant taxa are not gathered, matching the YAML source note.
