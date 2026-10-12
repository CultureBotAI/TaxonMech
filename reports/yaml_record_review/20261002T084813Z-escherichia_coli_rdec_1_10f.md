# YAML Record Review: Escherichia coli RDEC-1 (10f)

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml
- Started UTC: 2026-10-02T08:48:13Z
- Finished UTC: 2026-10-02T08:48:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017026` |
| Label | `Escherichia coli RDEC-1 (10f)` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:562` |
| Parent label | `Escherichia coli` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml data/taxa/bacteria/escherichia_coli_c309_64_10g.yaml data/taxa/bacteria/escherichia_coli_c186_61_10h.yaml data/taxa/bacteria/escherichia_coli_87_1713_10i.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 59 lines, 10 lineage entries, 0 strains, 0 synonyms, 0 xrefs, and 2 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml` | Not applicable: the NCBI-only helper exited with `NCBI source mismatch` because the record intentionally combines NCBITaxon and MADIN evidence. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*escherichia_coli_rdec_1_10f.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017026)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `madin_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10189 maps `NCBITaxon:1017026` to `escherichia_coli_rdec_1_10f`.
- `curation/seed_scope.tsv` row 57210 keeps this strain in scope with an attested NCBI and MADIN rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218524 names `NCBITaxon:1017026` as `Escherichia coli RDEC-1 (10f)`.
- The YAML identifier, label, strain rank, parent species, and genetic code agree with that raw NCBI row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a direct NCBI Taxonomy seed.

## Evidence

- The NCBITAXON source attestation is `source_id: NCBITaxon:1017026`, `source_label: Escherichia coli RDEC-1 (10f)`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The MADIN source attestation is `source_id: NCBITaxon:1017026`, `source_label: Escherichia coli RDEC-1 (10f)`, `assertion_count: 4`, and `assertion_unit: TRAIT_ASSERTION`.
- `data/raw/madin_taxa.tsv` row 465 supports the direct MADIN assertion count of 4.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:562` / `Escherichia coli`.
- The generated curation event accurately reports a 2026-09-13 seed from committed inventories.

## Completeness

- The record is complete for a strain-level NCBITaxon seed with direct MADIN trait evidence.
- `strain_count: 0` is appropriate because no BacDive or StrainInfo strain row is maintained for this exact NCBI taxon.
- MADIN is represented as a count-style source attestation and does not create strain, synonym, or causal graph blocks.
- No GTDB, LPSN, GOLD, MediaDive, or BactoTraits attestation is maintained for this NCBI row, and none is asserted.
- No empty optional fields are required.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml`.
- Re-run the MADIN and NCBI raw-row scans after any source refresh.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- The 2026-09-13 NCBI snapshot and the direct MADIN count are the only source families named by the raw NCBI row.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10189 |
| `curation/seed_scope.tsv` | 57210 |
| `data/raw/ncbitaxon_taxa.tsv` | 218524 |
| `data/raw/madin_taxa.tsv` | 465 |
| `data/taxa/bacteria/escherichia_coli_rdec_1_10f.yaml` | 1, 43, and 49 |
