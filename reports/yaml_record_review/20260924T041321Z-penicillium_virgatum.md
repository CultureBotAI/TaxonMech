# Review: Penicillium virgatum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_virgatum.yaml`
- Target: `NCBITaxon:282147`

## Target

The record grounds `Penicillium virgatum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 57472.

## Validation

- `just validate data/taxa/eukaryota/penicillium_virgatum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_verhagenii.yaml data/taxa/eukaryota/penicillium_verrucosum.yaml data/taxa/eukaryota/penicillium_virgatum.yaml data/taxa/eukaryota/penicillium_viridicatum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54969 with the expected reason: `attested rule: Penicillium virgatum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium virgatum Nirenberg & Kwasna, 2005`; the YAML mirrors that value.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 57472.
- GOLD aggregate: line 27262 records `organism_count=1` for `NCBITaxon:282147`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 128194-128199, covering culture-from-isotype spellings for `BBA 65745`, `CBS 114838`, and `IMI 391742`.
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
