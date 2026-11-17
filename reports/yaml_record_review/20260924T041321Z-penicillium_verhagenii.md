# Review: Penicillium verhagenii

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_verhagenii.yaml`
- Target: `NCBITaxon:1562060`

## Target

The record grounds `Penicillium verhagenii` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 401631.

## Validation

- `just validate data/taxa/eukaryota/penicillium_verhagenii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_verhagenii.yaml data/taxa/eukaryota/penicillium_verrucosum.yaml data/taxa/eukaryota/penicillium_virgatum.yaml data/taxa/eukaryota/penicillium_viridicatum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60467 with the expected reason: `attested rule: Penicillium verhagenii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium verhagenii Houbraken, 2014`; the YAML mirrors that value.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 401631.
- GOLD aggregate: line 12508 records `organism_count=1` for `NCBITaxon:1562060`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: four exact rows at lines 42479-42482, covering culture-from-holotype spellings for `CBS 137959` and `DTO 193-A1`.
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
