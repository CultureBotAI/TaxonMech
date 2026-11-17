# Review: Penicillium svalbardense

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_svalbardense.yaml`
- Target: `NCBITaxon:756462`

## Target

The record grounds `Penicillium svalbardense` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 175356.

## Validation

- `just validate data/taxa/eukaryota/penicillium_svalbardense.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_subturcoseum.yaml data/taxa/eukaryota/penicillium_sucrivorum.yaml data/taxa/eukaryota/penicillium_sumatraense.yaml data/taxa/eukaryota/penicillium_svalbardense.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56665 with the expected reason: `attested rule: Penicillium svalbardense, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. EXF-1307` and `Penicillium svalbardense Frisvad, Sonjak & Gunde-Cim., 2007`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 74501 maps old ID `NCBITaxon:383374` into `NCBITaxon:756462`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 175356.
- GOLD aggregate: line 42388 records `organism_count=1` for `NCBITaxon:756462`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: 13 exact rows at lines 262439-262451, covering culture-from-holotype spellings for `CBS 122416` and `IBT 23856` plus holotype spellings for `EX F1307`.
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

The retired `NCBITaxon:383374` ID is consumed only through the merge map, not as a retained source row.
