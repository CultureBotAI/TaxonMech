# Review: Penicillium wotroi

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_wotroi.yaml`
- Target: `NCBITaxon:756376`

## Target

The record grounds `Penicillium wotroi` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 175345.

## Validation

- `just validate data/taxa/eukaryota/penicillium_wotroi.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_vulpinum.yaml data/taxa/eukaryota/penicillium_westlingii.yaml data/taxa/eukaryota/penicillium_wotroi.yaml data/taxa/eukaryota/penicillium_xanthomelinii.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56663 with the expected reason: `attested rule: Penicillium wotroi, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. 1 JH-2010` and `Penicillium wotroi Houbraken, Lopez-Quint., Frisvad & Samson, 2011`; the YAML mirrors those values.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 175345.
- GOLD aggregate: line 42386 records `organism_count=1` for `NCBITaxon:756376`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: six exact rows at lines 262431-262436, covering culture-from-holotype spellings for `CBS 118171` and `IBT 23253` plus holotype spellings for `HUA 170336`.
- StrainInfo: four exact deposit rows and four direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

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
