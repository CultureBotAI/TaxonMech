# Review: Penicillium sp.

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_sp.yaml`
- Target: `NCBITaxon:5081`

## Target

The record grounds `Penicillium sp.` as an exact seeded NCBI species under `NCBITaxon:2593313` (`unclassified Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 2222.

## Validation

- `just validate data/taxa/eukaryota/penicillium_sp.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_smithii.yaml data/taxa/eukaryota/penicillium_solitum.yaml data/taxa/eukaryota/penicillium_sp.yaml data/taxa/eukaryota/penicillium_sp_cmv_2018d.yaml`: exited successfully
- Lineage audit: checked 16 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 51931 with the expected reason: `attested rule: Penicillium sp., 2 sources incl. NCBI`.
- The NCBI raw row has one exact synonym, `Eupenicillium sp.`, and no broad or related synonyms; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 33306 maps old ID `NCBITaxon:1955093` into `NCBITaxon:5081`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 2222.
- GOLD aggregate: line 37456 records `organism_count=9` for `NCBITaxon:5081`, matching the YAML GOLD attestation count. Native GOLD exact rows include 4 unique organisms and 8 projects, with no analyses for this target.
- NCBI type material: no exact rows were found for this target.
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

This target is intentionally parented to `unclassified Penicillium`; the YAML lineage includes both the `Penicillium` genus and the unclassified parent node.
