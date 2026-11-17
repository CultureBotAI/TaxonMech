# Review: Penicillium terrenum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_terrenum.yaml`
- Target: `NCBITaxon:1507553`

## Target

The record grounds `Penicillium terrenum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 387190.

## Validation

- `just validate data/taxa/eukaryota/penicillium_terrenum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_taurinense.yaml data/taxa/eukaryota/penicillium_terrarumae.yaml data/taxa/eukaryota/penicillium_terrenum.yaml data/taxa/eukaryota/penicillium_terrigenum.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 60370 with the expected reason: `attested rule: Penicillium terrenum, 2 sources incl. NCBI`.
- The NCBI raw row has the exact synonym `Eupenicillium terrenum`, no broad synonyms, and two related synonyms, `Eupenicillium terrenum D.B. Scott, 1968` and `Penicillium terrenum D.B. Scott, 1968`; the YAML mirrors those values.
- `data/raw/ncbi_merged_ids.tsv` line 92802 maps old ID `NCBITaxon:69803` into `NCBITaxon:1507553`; an exact retained-row grep of `data/raw/ncbitaxon_taxa.tsv` found no remaining row for that old ID, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 387190.
- GOLD aggregate: line 11859 records `organism_count=1` for `NCBITaxon:1507553`, matching the YAML GOLD attestation count; native GOLD organism, project, and analysis files have no exact rows for this target.
- NCBI type material: eight exact rows at lines 37825-37832, covering type-material spellings for `ATCC 18547`, `CBS 313.67`, `CSIR 1022`, and `IMI 136208`.
- StrainInfo: 33 exact deposit rows and 11 direct exact strains were found for this target, but no generated StrainInfo overlay rows were emitted.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, MediaDive, or generated StrainInfo overlay files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The retired `NCBITaxon:69803` ID is consumed only through the merge map, not as a retained source row.
