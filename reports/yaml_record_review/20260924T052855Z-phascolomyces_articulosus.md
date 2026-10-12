# Review: Phascolomyces articulosus

- Verdict: pass
- Record: `data/taxa/eukaryota/phascolomyces_articulosus.yaml`
- Target: `NCBITaxon:60185`

## Target

The record grounds `Phascolomyces articulosus` as an exact seeded NCBI species under `NCBITaxon:60184` (`Phascolomyces`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7588.

## Validation

- `just validate data/taxa/eukaryota/phascolomyces_articulosus.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phascolomyces_articulosus.yaml data/taxa/eukaryota/phellinidium_ferrugineofuscum.yaml data/taxa/eukaryota/phellinidium_pouzarii.yaml data/taxa/eukaryota/phellinus_igniarius.yaml`: zero errors across 4 files
- Lineage audit: checked 12 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53019 with the expected reason: `attested rule: Phascolomyces articulosus, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym, `Phascolomyces articulosus Boedijn, 1958`, and no exact or broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7588.
- GOLD aggregate: line 39777 records `organism_count=1` for `NCBITaxon:60185`, matching the YAML GOLD attestation count; native GOLD has one exact organism row, two exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 6 direct exact strains and 11 exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
