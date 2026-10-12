# Review: Penicillium hesseltinei

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sp_cmv_2018d.yaml`
- Target: `NCBITaxon:2184411`

## Target

The record grounds the seeded `Penicillium sp. CMV-2018d` synonym to the accepted NCBI species `Penicillium hesseltinei` under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 521168.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sp_cmv_2018d.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_smithii.yaml data/taxa/eukaryota/penicillium_solitum.yaml data/taxa/eukaryota/penicillium_sp.yaml data/taxa/eukaryota/penicillium_sp_cmv_2018d.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 62471 with the expected reason: `attested rule: Penicillium sp. CMV-2018d, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium hesseltinei Visagie, Overy, Seifert & Frisvad, 2025` and `Penicillium sp. CMV-2018d`; the YAML mirrors those values.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:2184411`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 521168.
- GOLD aggregate: line 20826 records `organism_count=1` for `NCBITaxon:2184411`, matching the YAML GOLD attestation count. Native GOLD exact rows include one organism, `Go0679380` at line 504011, one project, `Gp0781368` at line 580405, and one analysis at line 411861.
- NCBI type material: 14 exact rows at lines 87271-87284, covering culture-from-holotype spellings for `DAOM 251664`, `DAOMC 251664`, and `IBT 12396` plus holotype spellings for `DAOM 749218`.
- StrainInfo: no direct exact strains or deposit rows were found for this target.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The report filename follows the seeded YAML stem, while the review target follows the accepted NCBI identifier and label now present in the record.
