# Review: Peronospora belbahrii

- Verdict: pass
- Record: `data/taxa/eukaryota/peronospora_belbahrii.yaml`
- Target: `NCBITaxon:622444`

## Target

The record grounds `Peronospora belbahrii` as an exact seeded NCBI species under `NCBITaxon:70742` (`Peronospora`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 143440.

## Validation

- `just validate data/taxa/eukaryota/peronospora_belbahrii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peroneutypa_scoparia.yaml data/taxa/eukaryota/peronospora_belbahrii.yaml data/taxa/eukaryota/peronospora_effusa.yaml data/taxa/eukaryota/peronospora_tabacina.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56166 with the expected reason: `attested rule: Peronospora belbahrii, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has two related synonyms, `Peronospora belbahrii Thines, 2009` and `Peronospora sp. HV2280`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 87136 maps old ID `NCBITaxon:575819` into `NCBITaxon:622444`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 143440.
- GOLD aggregate: line 39938 records `organism_count=2` for `NCBITaxon:622444`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have two exact rows for this target.
- NCBI type material: one exact row at line 242390 for type material `HOH HUH770`.
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

The retired `NCBITaxon:575819` ID is consumed only through the merge map, not as a retained source row.
