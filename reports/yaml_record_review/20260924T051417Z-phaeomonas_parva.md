# Review: Phaeomonas parva

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeomonas_parva.yaml`
- Target: `NCBITaxon:124430`

## Target

The record grounds `Phaeomonas parva` as an exact seeded NCBI species under `NCBITaxon:124429` (`Phaeomonas`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 23713.

## Validation

- `just validate data/taxa/eukaryota/phaeomonas_parva.yaml`: exited successfully
- `just validate-strict data/taxa/eukaryota/phaeomonas_parva.yaml data/taxa/eukaryota/phaeomoniella_chlamydospora.yaml data/taxa/eukaryota/phaeosolenia_platensis.yaml data/taxa/eukaryota/phaeosphaeria_elongata.yaml`: exited successfully
- Lineage audit: checked 10 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53901 with the expected reason: `attested rule: Phaeomonas parva, 2 sources incl. NCBI`.
- The NCBI raw row has one related synonym, `Phaeomonas parva D.Honda & Inouye, 2002`, and no exact or broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 23713.
- GOLD aggregate: line 5884 records `organism_count=1` for `NCBITaxon:124430`, matching the YAML GOLD attestation count; native GOLD has one exact organism row and no exact project or analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: one direct exact strain and one exact deposit row were found for this target; no generated StrainInfo overlay rows were found.

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
