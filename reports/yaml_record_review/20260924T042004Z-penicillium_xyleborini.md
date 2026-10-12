# Review: Penicillium xyleborini

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_xyleborini.yaml`
- Target: `NCBITaxon:2927845`

## Target

The record grounds `Penicillium xyleborini` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 572892.

## Validation

- `just validate data/taxa/eukaryota/penicillium_xyleborini.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_xyleborini.yaml data/taxa/eukaryota/penidiella_ellipsoidea.yaml data/taxa/eukaryota/peniophora_cinerea.yaml data/taxa/eukaryota/peniophora_sp.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 63378 with the expected reason: `attested rule: Penicillium xyleborini, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Penicillium sp. CN001D4` and `Penicillium xyleborini Visagie & W.J. Nel, 2021`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 52553 maps old ID `NCBITaxon:2804540` into `NCBITaxon:2927845`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 572892.
- GOLD aggregate: line 28809 records `organism_count=1` for `NCBITaxon:2927845`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: five exact rows at lines 142235-142239, covering culture-from-holotype rows for `CMW 56800` and `CN 001D4` plus holotype spellings for `PREM 63078`.
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

The retired `NCBITaxon:2804540` ID is consumed only through the merge map, not as a retained source row.
