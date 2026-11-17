# YAML Record Review: Escherichia coli OUT:H18

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_out_h18.yaml
- Started UTC: 2026-10-02T10:25:42Z
- Finished UTC: 2026-10-02T10:25:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017261` |
| Label | `Escherichia coli OUT:H18` |
| Rank | `NO_RANK` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:562` |
| Parent label | `Escherichia coli` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/escherichia_coli_out_h18.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/enterococcaceae_bacterium_enrichment_culture_clone_pttcbs1.yaml data/taxa/bacteria/escherichia_coli_out_h18.yaml data/taxa/bacteria/bacillus_sp_av_2011.yaml data/taxa/bacteria/bordetella_pertussis_cs.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 59 lines, 10 lineage entries, 0 strains, 0 synonyms, 0 xrefs, and 2 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed, NCBI, and GOLD rows; confirmed all 10 lineage rows; and found no strain or genome rows for `NCBITaxon:1017261`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*escherichia_coli_out_h18.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017261)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `legacy_page_paths.tsv`, `PATHS.tsv`, `seed_scope.tsv`, `gold_organisms.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10298 maps `NCBITaxon:1017261` to `escherichia_coli_out_h18`.
- `curation/seed_scope.tsv` row 57215 keeps this taxon in scope with an attested NCBI+GOLD rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218632 names `NCBITaxon:1017261` as `Escherichia coli OUT:H18`.
- `data/raw/gold_organisms.tsv` row 297 preserves the single GOLD organism count for the same exact taxon.
- The YAML identifier, label, rank, parent taxon, genetic code, and NCBI/GOLD source attestations agree with those raw rows.

## Evidence

- The NCBI attestation is `source_id: NCBITaxon:1017261`, `source_label: Escherichia coli OUT:H18`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The GOLD attestation is `source_id: NCBITaxon:1017261`, `source_label: Escherichia coli OUT:H18`, `assertion_count: 1`, and `assertion_unit: ORGANISM`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:562` / `Escherichia coli`.
- The generated curation event accurately reports a 2026-09-13 seed from committed inventories.

## Completeness

- The record is complete for the exact NCBI and GOLD rows currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, and exact strain-related source rows.
- The raw-source scan found no exact LPSN, GTDB, MADIN, MediaDive, AllTheBacteria, xref, genome, or causal-graph evidence for `NCBITaxon:1017261`.
- No native GOLD project or analysis rows were found for this exact taxon.
- No top-level `strains`, `taxonomy_mappings`, `synonyms`, `xrefs`, `genomes`, or `causal_graphs` blocks are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_out_h18.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/escherichia_coli_out_h18.yaml`.
- Re-run `just verify-corpus`.
- Re-run a bounded or direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10298 |
| `curation/legacy_page_paths.tsv` | 598 |
| `curation/seed_scope.tsv` | 57215 |
| `data/raw/gold_organisms.tsv` | 297 |
| `data/raw/ncbitaxon_taxa.tsv` | 218632 |
| `data/taxa/bacteria/escherichia_coli_out_h18.yaml` | 1, 43, and 49 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/escherichia_coli_out_h18.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/escherichia_coli_out_h18.yaml` directly.
