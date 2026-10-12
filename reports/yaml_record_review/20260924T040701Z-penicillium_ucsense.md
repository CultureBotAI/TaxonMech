# Review: Penicillium ucsense

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_ucsense.yaml`
- Target: `NCBITaxon:2839758`

## Target

The record grounds `Penicillium ucsense` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 563196.

## Validation

- `just validate data/taxa/eukaryota/penicillium_ucsense.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_tulipae.yaml data/taxa/eukaryota/penicillium_ubiquetum.yaml data/taxa/eukaryota/penicillium_ucsense.yaml data/taxa/eukaryota/penicillium_ulaiense.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63308 with the expected reason: `attested rule: Penicillium ucsense, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has four related synonyms, `Penicillium sp. 2HH`, `Penicillium sp. RFL-2021a`, `Penicillium sp. S1M29`, and `Penicillium ucsense A. Lenz & Houbraken, 2022`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 47278 maps old ID `NCBITaxon:2660642` into `NCBITaxon:2839758`, and line 47279 maps old ID `NCBITaxon:2660643` into `NCBITaxon:2839758`; exact retained-row greps of `data/raw/ncbitaxon_taxa.tsv` found no remaining rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 563196.
- GOLD aggregate: line 27498 records `organism_count=2` for `NCBITaxon:2839758`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have two exact rows for `S1M29` and `2HH`.
- NCBI type material: ten exact rows at lines 130107-130116, covering culture-from-holotype spellings for `2HH`, `CBS 146492`, and `DTO 426-B1` plus holotype spellings for `CBS H-24331`.
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

The retired `NCBITaxon:2660642` and `NCBITaxon:2660643` IDs are consumed only through the merge map, not as retained source rows.
