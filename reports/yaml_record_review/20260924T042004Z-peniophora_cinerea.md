# Review: Peniophora cinerea

- Verdict: pass
- Record: `data/taxa/eukaryota/peniophora_cinerea.yaml`
- Target: `NCBITaxon:55348`

## Target

The record grounds `Peniophora cinerea` as an exact seeded NCBI species under `NCBITaxon:40463` (`Peniophora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7007.

## Validation

- `just validate data/taxa/eukaryota/peniophora_cinerea.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_xyleborini.yaml data/taxa/eukaryota/penidiella_ellipsoidea.yaml data/taxa/eukaryota/peniophora_cinerea.yaml data/taxa/eukaryota/peniophora_sp.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52945 with the expected reason: `attested rule: Peniophora cinerea, 2 sources incl. NCBI`.
- The NCBI raw row has the exact synonym `Corticium cinereum`, no broad synonyms, and three related synonyms, `Corticium cinereum Pers., 1794`, `Peniophora cinerea (Pers.) Cooke, 1879`, and `Peniophora sp. MUT 4993`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 22415 maps old ID `NCBITaxon:1635071` into `NCBITaxon:55348`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7007.
- GOLD aggregate: line 38655 records `organism_count=1` for `NCBITaxon:55348`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 19 exact deposit rows and 18 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:1635071` ID is consumed only through the merge map, not as a retained source row.
