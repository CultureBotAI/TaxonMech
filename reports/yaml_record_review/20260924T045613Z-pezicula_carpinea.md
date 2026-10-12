# Review: Pezicula carpinea

- Verdict: pass
- Record: `data/taxa/eukaryota/pezicula_carpinea.yaml`
- Target: `NCBITaxon:101854`

## Target

The record grounds `Pezicula carpinea` as an exact seeded NCBI species under `NCBITaxon:101853` (`Pezicula`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 17703.

## Validation

- `just validate data/taxa/eukaryota/pezicula_carpinea.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/peterozyma_toletana.yaml data/taxa/eukaryota/peterozyma_xylosa.yaml data/taxa/eukaryota/pezicula_carpinea.yaml data/taxa/eukaryota/pezicula_radicicola.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53662 with the expected reason: `attested rule: Pezicula carpinea, 2 sources incl. NCBI`.
- The exact synonym and two related synonyms in the YAML match the NCBI raw row.
- No rows in `data/raw/ncbi_merged_ids.tsv` target this identifier, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 17703.
- GOLD aggregate: line 304 records `organism_count=1` for `NCBITaxon:101854`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files each have one exact row for this target.
- NCBI type material: lines 1199-1200 record two exact rows for this target.
- StrainInfo: 9 direct exact strains and 9 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
