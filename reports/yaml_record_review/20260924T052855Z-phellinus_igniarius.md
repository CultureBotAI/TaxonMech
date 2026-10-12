# Review: Phellinus igniarius

- Verdict: pass
- Record: `data/taxa/eukaryota/phellinus_igniarius.yaml`
- Target: `NCBITaxon:40472`

## Target

The record grounds `Phellinus igniarius` as an exact seeded NCBI species under `NCBITaxon:40470` (`Phellinus`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 4622.

## Validation

- `just validate data/taxa/eukaryota/phellinus_igniarius.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phascolomyces_articulosus.yaml data/taxa/eukaryota/phellinidium_ferrugineofuscum.yaml data/taxa/eukaryota/phellinidium_pouzarii.yaml data/taxa/eukaryota/phellinus_igniarius.yaml`: zero errors across 4 files
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 52438 with the expected reason: `attested rule: Phellinus igniarius, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Boletus igniarius`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- `data/raw/ncbi_merged_ids.tsv` line 13178 maps retired `NCBITaxon:1349030` to this identifier; an exact retained-row grep found no `NCBITaxon:1349030` row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 4622.
- GOLD aggregate: line 34557 records `organism_count=1` for `NCBITaxon:40472`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and one exact analysis row for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 19 direct exact strains and 20 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
