# Review: Phytophthora lateralis MPF6

- Verdict: pass
- Record: `data/taxa/eukaryota/phytophthora_lateralis_mpf6.yaml`
- Target: `NCBITaxon:1249587`

## Target

The record grounds `Phytophthora lateralis MPF6` as an exact seeded NCBI strain under `NCBITaxon:129355` (`Phytophthora lateralis`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 288164.

## Validation

- `just validate data/taxa/eukaryota/phytophthora_lateralis_mpf6.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phytophthora_infestans.yaml data/taxa/eukaryota/phytophthora_kernoviae.yaml data/taxa/eukaryota/phytophthora_lateralis_mpf6.yaml data/taxa/eukaryota/phytophthora_macrochlamydospora.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 11 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `curation/seed_scope.tsv` contains the target at line 58686 with the expected reason: `attested rule: Phytophthora lateralis MPF6, 2 sources incl. NCBI`.
- The NCBI raw row has no exact, related, or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 288164.
- GOLD aggregate: line 5998 records `organism_count=7` for `NCBITaxon:1249587`, matching the YAML GOLD attestation count; native GOLD has eight exact organism rows, one exact project row, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this strain target.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

`Phytophthora lateralis MPF6` is a strain-rank NCBI taxon under the `Phytophthora lateralis` species lineage entry, not a separate species-level record.
