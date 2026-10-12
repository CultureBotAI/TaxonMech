# Review: Perkinsus chesapeaki

- Verdict: pass
- Record: `data/taxa/eukaryota/perkinsus_chesapeaki.yaml`
- Target: `NCBITaxon:330153`

## Target

The record grounds `Perkinsus chesapeaki` as an exact seeded NCBI species under `NCBITaxon:28000` (`Perkinsus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 67421.

## Validation

- `just validate data/taxa/eukaryota/perkinsus_chesapeaki.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/perkinsus_chesapeaki.yaml data/taxa/eukaryota/perkinsus_marinus.yaml data/taxa/eukaryota/perkinsus_marinus_atcc_50983.yaml data/taxa/eukaryota/perkinsus_olseni.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 55243 with the expected reason: `attested rule: Perkinsus chesapeaki, 2 sources incl. NCBI`.
- The NCBI raw row has two exact synonyms, `Perkinsus andrewsi` and `Perkinsus sp. ATCC 50807`, no broad synonyms, and one related synonym, `Perkinsus chesapeaki McLaughlin, Tall, Shaheen, El Sayed & Faisal, 2000`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 8963 maps old ID `NCBITaxon:123361` into `NCBITaxon:330153`, line 66007 maps old ID `NCBITaxon:321611` into `NCBITaxon:330153`, and line 66027 maps old ID `NCBITaxon:321957` into `NCBITaxon:330153`; exact retained-row greps of `data/raw/ncbitaxon_taxa.tsv` found no remaining rows for those old IDs, so no `replaces` entries are expected.

## Evidence

- NCBI: one matching taxonomy row at line 67421.
- GOLD aggregate: line 32257 records `organism_count=2` for `NCBITaxon:330153`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, one exact project row, and one exact analysis row for this target.
- NCBI type material: four exact rows at lines 178331-178334, covering hapantotype spellings for `ATCC PRA-65`.
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

The retired `NCBITaxon:123361`, `NCBITaxon:321611`, and `NCBITaxon:321957` IDs are consumed only through the merge map, not as retained source rows.
