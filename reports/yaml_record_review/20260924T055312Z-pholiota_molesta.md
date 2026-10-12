# Review: Pholiota molesta

- Verdict: pass
- Record: `data/taxa/eukaryota/pholiota_molesta.yaml`
- Target: `NCBITaxon:2066989`

## Target

The record grounds `Pholiota molesta` as an exact seeded NCBI species under `NCBITaxon:13205` (`Pholiota`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 515200.

## Validation

- `just validate data/taxa/eukaryota/pholiota_molesta.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/pholiota_microspora.yaml data/taxa/eukaryota/pholiota_molesta.yaml data/taxa/eukaryota/phoma_herbarum.yaml data/taxa/eukaryota/phoma_leveillei.yaml`: 4 files scanned with 0 errors
- Lineage audit: checked 14 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 62244 with the expected reason: `attested rule: Pholiota molesta, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym and no exact or broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` has no retired IDs that merge into this identifier.

## Evidence

- NCBI: one matching taxonomy row at line 515200.
- GOLD aggregate: line 19745 records `organism_count=1` for `NCBITaxon:2066989`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: lines 82388-82398 record `AHS65008`, `MICH 5323`, `MICH-5323`, `MICH5323`, and `MICH:5323` holotype designations plus `TENN F-028830`, `TENN-F-028830`, `TENN:028830`, `TENN:028830 (isotype)`, `TENN:F-028830`, and `TENNF-028830` isotype designations.
- StrainInfo: one direct exact strain and one exact deposit row were found for this target; no generated StrainInfo overlay rows were found.

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
