# Review: Penicillium terrigenum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_terrigenum.yaml`
- Target: `NCBITaxon:1131585`

## Target

The record grounds `Penicillium terrigenum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 245746.

## Validation

- `just validate data/taxa/eukaryota/penicillium_terrigenum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_taurinense.yaml data/taxa/eukaryota/penicillium_terrarumae.yaml data/taxa/eukaryota/penicillium_terrenum.yaml data/taxa/eukaryota/penicillium_terrigenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 57836 with the expected reason: `attested rule: Penicillium terrigenum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has three related synonyms, `Penicillium sp. CBS 127354`, `Penicillium sp. DTO 9D4`, and `Penicillium terrigenum Seifert, Houbraken, Frisvad & Samson 2011`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 245746.
- GOLD aggregate: line 2683 records `organism_count=1` for `NCBITaxon:1131585`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 8362-8367, covering culture-from-holotype spellings for `CBS 127354` plus type-material spellings for `DTO 9D4` and `IBT 30769`.
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
