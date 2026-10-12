# Review: Penicillium shearii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_shearii.yaml`
- Target: `NCBITaxon:904690`

## Target

The record grounds `Penicillium shearii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 190616.

## Validation

- `just validate data/taxa/eukaryota/penicillium_shearii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_shearii.yaml data/taxa/eukaryota/penicillium_sicoris.yaml data/taxa/eukaryota/penicillium_simile.yaml data/taxa/eukaryota/penicillium_simplicissimum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56863 with the expected reason: `attested rule: Penicillium shearii, 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, `Eupenicillium shearii`, no broad synonyms, and one related synonym, `Penicillium shearii Stolk & D.B. Scott, 1967`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 92801 maps old ID `NCBITaxon:69801` into `NCBITaxon:904690`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 190616.
- GOLD aggregate: line 44141 records `organism_count=1` for `NCBITaxon:904690`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: 14 exact rows at lines 271950-271963, covering culture-from-holotype spellings `CBS 290.48` / `CBS:290.48` plus type-material spellings for `ATCC 10410`, `IFO 6088`, `IMI 039739`, `IMI 039739iv`, `NRRL 715`, and `QM 1870`.
- StrainInfo: exact StrainInfo has 48 direct strains and 69 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:904690`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The StrainInfo hits are direct source rows only; they do not create a generated local strain overlay for this target without a matched BacDive-derived local strain.
