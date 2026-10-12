# Review: Penicillium tropicoides

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_tropicoides.yaml`
- Target: `NCBITaxon:911722`

## Target

The record grounds `Penicillium tropicoides` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 192632.

## Validation

- `just validate data/taxa/eukaryota/penicillium_tropicoides.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_thiersii.yaml data/taxa/eukaryota/penicillium_tricolor.yaml data/taxa/eukaryota/penicillium_tropicoides.yaml data/taxa/eukaryota/penicillium_tropicum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56903 with the expected reason: `attested rule: Penicillium tropicoides, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium tropicoides Houbraken, Frisvad and Samson, 2010`; the YAML mirrors that value.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 192632.
- GOLD aggregate: line 44369 records `organism_count=1` for `NCBITaxon:911722`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: four exact rows at lines 272537-272540, covering culture-from-holotype spellings for `CBS 122410` and `IBT 29043`.
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

None.
