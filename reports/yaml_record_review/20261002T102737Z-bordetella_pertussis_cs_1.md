# YAML Record Review: Bordetella pertussis CS-1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bordetella_pertussis_cs_1.yaml
- Started UTC: 2026-10-02T10:27:37Z
- Finished UTC: 2026-10-02T10:27:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017265` |
| Label | `Bordetella pertussis CS-1` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:520` |
| Parent label | `Bordetella pertussis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bordetella_pertussis_cs_1.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/bordetella_pertussis_cs_1.yaml data/taxa/bacteria/lactococcus_garvieae_uniud074.yaml data/taxa/bacteria/bacillus_sp_m85.yaml data/taxa/bacteria/agromyces_sp_nioc742.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 66 lines, 10 lineage entries, 0 strains, 2 NCBITaxon synonyms, 0 xrefs, and 2 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed, NCBI, and MADIN rows; confirmed all 10 lineage rows; and found no exact GTDB, strain, or genome rows for `NCBITaxon:1017265`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*bordetella_pertussis_cs_1.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017265)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `legacy_page_paths.tsv`, `PATHS.tsv`, `seed_scope.tsv`, `madin_taxa.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10301 maps `NCBITaxon:1017265` to `bordetella_pertussis_cs_1`.
- `curation/seed_scope.tsv` row 57216 keeps this taxon in scope with an attested NCBI+MADIN rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218635 names `NCBITaxon:1017265` as `Bordetella pertussis CS-1`.
- `data/raw/madin_taxa.tsv` row 475 supplies the 4 MADIN trait assertions preserved in `source_attestations`.
- The YAML identifier, strain rank, label, parent species, NCBI synonyms, and genetic code agree with the exact NCBI Taxonomy row.

## Evidence

- The NCBI attestation is `source_id: NCBITaxon:1017265`, `source_label: Bordetella pertussis CS-1`, `assertion_count: 1`, and `assertion_unit: NAME`.
- The MADIN attestation is `source_id: NCBITaxon:1017265`, `source_label: Bordetella pertussis CS-1`, `assertion_count: 4`, and `assertion_unit: TRAIT_ASSERTION`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:520` / `Bordetella pertussis`.
- NCBI contributes two exact synonyms, `Bordetella pertussis str. CS-1` and `Bordetella pertussis strain CS-1`.
- The generated curation event accurately reports a 2026-09-13 seed from committed inventories.

## Completeness

- The record is complete for the exact NCBI and MADIN rows currently present for this taxon.
- The NCBI synonyms in `data/raw/ncbitaxon_taxa.tsv` are both represented as `EXACT_SYNONYM` entries.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, and exact strain-related source rows.
- The raw-source scan found no exact GTDB, GOLD, MediaDive, AllTheBacteria, genome-assembly, or causal-graph rows for `NCBITaxon:1017265`.
- No top-level `taxonomy_mappings`, `xrefs`, `genomes`, `strains`, or `causal_graphs` blocks are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bordetella_pertussis_cs_1.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/bordetella_pertussis_cs_1.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10301 |
| `curation/legacy_page_paths.tsv` | 600 |
| `curation/seed_scope.tsv` | 57216 |
| `data/raw/madin_taxa.tsv` | 475 |
| `data/raw/ncbitaxon_taxa.tsv` | 218635 |
| `data/taxa/bacteria/bordetella_pertussis_cs_1.yaml` | 1, 39, 49, and 55 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/bordetella_pertussis_cs_1.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `xrefs`, `genomes`, `strains`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/bordetella_pertussis_cs_1.yaml` directly.
