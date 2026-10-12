# Review: Penicillium ubiquetum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_ubiquetum.yaml`
- Target: `NCBITaxon:1131563`

## Target

The record grounds `Penicillium ubiquetum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 245732.

## Validation

- `just validate data/taxa/eukaryota/penicillium_ubiquetum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_tulipae.yaml data/taxa/eukaryota/penicillium_ubiquetum.yaml data/taxa/eukaryota/penicillium_ucsense.yaml data/taxa/eukaryota/penicillium_ulaiense.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 57829 with the expected reason: `attested rule: Penicillium ubiquetum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has nine related synonyms, `Penicillium sp. CBS 117212`, `Penicillium sp. CBS 124317`, `Penicillium sp. CBS 124318`, `Penicillium sp. CBS 124450`, `Penicillium sp. CBS 126436`, `Penicillium sp. CBS 126437`, `Penicillium sp. CBS 126438`, `Penicillium sp. CBS 126439`, and `Penicillium ubiquetum Houbraken, Frisvad & Samson 2011`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 245732.
- GOLD aggregate: line 2675 records `organism_count=1` for `NCBITaxon:1131563`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 8323-8328, covering culture-from-holotype spellings for `CBS 126437` plus type-material spellings for `DTO 78B5` and `IBT 22226`.
- StrainInfo: one exact deposit row and one direct exact strain were found for this target, but no generated StrainInfo overlay rows were emitted.

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
