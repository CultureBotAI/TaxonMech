# Review: Phellinidium pouzarii

- Verdict: pass
- Record: `data/taxa/eukaryota/phellinidium_pouzarii.yaml`
- Target: `NCBITaxon:167371`

## Target

The record grounds `Phellinidium pouzarii` as an exact seeded NCBI species under `NCBITaxon:218112` (`Phellinidium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 34262.

## Validation

- `just validate data/taxa/eukaryota/phellinidium_pouzarii.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phascolomyces_articulosus.yaml data/taxa/eukaryota/phellinidium_ferrugineofuscum.yaml data/taxa/eukaryota/phellinidium_pouzarii.yaml data/taxa/eukaryota/phellinus_igniarius.yaml`: zero errors across 4 files
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 54233 with the expected reason: `attested rule: Phellinidium pouzarii, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Phellinus pouzarii`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 34262.
- GOLD aggregate: line 14393 records `organism_count=1` for `NCBITaxon:167371`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
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

None.
