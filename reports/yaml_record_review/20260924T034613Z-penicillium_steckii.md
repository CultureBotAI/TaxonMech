# Review: Penicillium steckii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_steckii.yaml`
- Target: `NCBITaxon:303698`

## Target

The record grounds `Penicillium steckii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 62136.

## Validation

- `just validate data/taxa/eukaryota/penicillium_steckii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_sp_str_12.yaml data/taxa/eukaryota/penicillium_spathulatum.yaml data/taxa/eukaryota/penicillium_spinulosum.yaml data/taxa/eukaryota/penicillium_steckii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55094 with the expected reason: `attested rule: Penicillium steckii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium steckii K.M. Zalessky, 1927`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:303698`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 62136.
- GOLD aggregate: line 30429 records `organism_count=1` for `NCBITaxon:303698`, matching the YAML GOLD attestation count. Native GOLD exact rows include one organism, `Go0372910` at line 276576, one project, `Gp0219701` at line 146262, and one analysis at line 125296.
- NCBI type material: two exact rows at lines 158252-158253, covering culture-from-neotype spellings `CBS 260.55` and `CBS:260.55`.
- StrainInfo: exact StrainInfo has 23 direct strains and 33 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:303698`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The native GOLD evidence agrees by exact NCBI taxon ID with the accepted `Penicillium steckii` record.
