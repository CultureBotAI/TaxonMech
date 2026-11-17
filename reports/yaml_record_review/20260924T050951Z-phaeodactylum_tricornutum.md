# Review: Phaeodactylum tricornutum

- Verdict: pass
- Record: `data/taxa/eukaryota/phaeodactylum_tricornutum.yaml`
- Target: `NCBITaxon:2850`

## Target

The record grounds `Phaeodactylum tricornutum` as an exact seeded NCBI species under `NCBITaxon:2849` (`Phaeodactylum`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 1963.

## Validation

- `just validate data/taxa/eukaryota/phaeodactylum_tricornutum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/phaeocystis_sp_ccmp2192.yaml data/taxa/eukaryota/phaeocystis_sp_ccmp2710.yaml data/taxa/eukaryota/phaeodactylum_tricornutum.yaml data/taxa/eukaryota/phaeodactylum_tricornutum_ccap_1055_1.yaml`: exited successfully
- Lineage audit: checked 13 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 51811 with the expected reason: `attested rule: Phaeodactylum tricornutum, 2 sources incl. NCBI`.
- The exact synonym and related synonym in the YAML match the NCBI raw row.
- `data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:274578` to this target at line 50456; an exact retained-row scan found no old-ID row in `data/raw/ncbitaxon_taxa.tsv`, so no `replaces` entry is expected from the retained taxonomy source.

## Evidence

- NCBI: one matching taxonomy row at line 1963.
- GOLD aggregate: line 27636 records `organism_count=1` for `NCBITaxon:2850`, matching the YAML GOLD attestation count; native GOLD has two exact organism rows, three exact project rows, and no exact analysis rows for this target.
- NCBI type material: no exact rows were found for this target.
- StrainInfo: 12 direct exact strains and 32 deposit rows were found for this target; generated StrainInfo overlay files have no exact target rows.

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
