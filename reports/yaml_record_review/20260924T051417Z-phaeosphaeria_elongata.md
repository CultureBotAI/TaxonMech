# Review: Phaeosphaeria elongata

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeosphaeria_elongata.yaml`
- Target: `NCBITaxon:708609`

## Target

The record grounds `Phaeosphaeria elongata` as an exact seeded NCBI species under `NCBITaxon:55067` (`Phaeosphaeria`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 165685.

## Validation

- `just validate data/taxa/eukaryota/phaeosphaeria_elongata.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeomonas_parva.yaml data/taxa/eukaryota/phaeomoniella_chlamydospora.yaml data/taxa/eukaryota/phaeosolenia_platensis.yaml data/taxa/eukaryota/phaeosphaeria_elongata.yaml`: exited successfully
- Lineage audit: checked 17 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 56517 with the expected reason: `attested rule: Phaeosphaeria elongata, 2 sources incl. NCBI`.
- The NCBI raw row has exact synonym `Leptosphaeria elongata`, two related synonyms, and no broad synonyms; the YAML mirrors that source row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 165685.
- GOLD aggregate: line 41757 records `organism_count=1` for `NCBITaxon:708609`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: lines 259416-259419 record the `MICH 14301`, `MICH-14301`, `MICH14301`, and `MICH:14301` holotype designations.
- StrainInfo: one direct exact strain and two exact deposit rows were found for this target; no generated StrainInfo overlay rows were found.

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
