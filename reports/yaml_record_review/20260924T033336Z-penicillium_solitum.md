# Review: Penicillium solitum

- Verdict: pass
- Record: `data/taxa/eukaryota/penicillium_solitum.yaml`
- Target: `NCBITaxon:60172`

## Target

The record grounds `Penicillium solitum` as an exact seeded NCBI species under `NCBITaxon:5073` (`Penicillium`). The YAML identifier, label, rank, parent, grounding status, mapping status, genetic code, and NCBI source attestation match the `data/raw/ncbitaxon_taxa.tsv` row at line 7584.

## Validation

- `just validate data/taxa/eukaryota/penicillium_solitum.yaml`: `No issues found`
- `just validate-strict data/taxa/eukaryota/penicillium_smithii.yaml data/taxa/eukaryota/penicillium_solitum.yaml data/taxa/eukaryota/penicillium_sp.yaml data/taxa/eukaryota/penicillium_sp_cmv_2018d.yaml`: exited successfully
- Lineage audit: checked 15 lineage nodes; no missing nodes and no mismatches

## Identity and Grounding

- `data/seed_scope.tsv` contains the target at line 53016 with the expected reason: `attested rule: Penicillium solitum, 2 sources incl. NCBI`.
- The NCBI raw row has no exact or broad synonyms and has one related synonym, `Penicillium solitum Westling, 1911`; the YAML mirrors that value.
- No `data/raw/ncbi_merged_ids.tsv` rows point into `NCBITaxon:60172`, so no `replaces` entry is expected.

## Evidence

- NCBI: one matching taxonomy row at line 7584.
- GOLD aggregate: line 39774 records `organism_count=14` for `NCBITaxon:60172`, matching the YAML GOLD attestation count. Native GOLD exact rows include 13 unique organisms, 15 projects, and 12 analyses for this target.
- NCBI type material: 23 exact rows at lines 241028-241050, all `type material`, including variants for `ATCC 9923`, `CBS 288.36`, `CBS 424.89`, `FRR 937`, `IBT 3948`, `IFO 7765`, `IMI 039810`, `IMI 092225`, `MUCL 28668`, `MUCL 29173`, and `NRRL 937`.
- StrainInfo: exact StrainInfo has 67 direct strains and 102 deposit rows for this target, but the BacDive-derived StrainInfo overlay emitted no `assemblies.tsv`, `exclusions.tsv`, or `related_records.tsv.gz` rows for `NCBITaxon:60172`.

## Completeness

The generated record is complete for the seeded scope: it includes NCBI identity, the attesting GOLD aggregate count, all NCBI synonyms, and the expected seeded history. Exact target scans found no rows in raw BacDive, culture-collection, strain assembly, strain genome, or strain related-record TSVs, and no rows in BactoTraits, GTDB, LPSN, Madin, or MediaDive auxiliary files.

## Findings

No findings.

## Recommended Edits

No YAML edits are recommended.

## Follow-up Checks

None required.

## Additional Notes

The native GOLD row count is larger than the generated GOLD assertion count because the YAML records the aggregate organism count, not every native project or analysis row.
