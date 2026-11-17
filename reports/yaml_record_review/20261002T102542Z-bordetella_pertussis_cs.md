# YAML Record Review: Bordetella pertussis CS

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bordetella_pertussis_cs.yaml
- Started UTC: 2026-10-02T10:25:42Z
- Finished UTC: 2026-10-02T10:25:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017264` |
| Label | `Bordetella pertussis CS` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:520` |
| Parent label | `Bordetella pertussis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/bordetella_pertussis_cs.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/enterococcaceae_bacterium_enrichment_culture_clone_pttcbs1.yaml data/taxa/bacteria/escherichia_coli_out_h18.yaml data/taxa/bacteria/bacillus_sp_av_2011.yaml data/taxa/bacteria/bordetella_pertussis_cs.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 84 lines, 10 lineage entries, 1 GTDB taxonomy mapping, 3 synonyms, 1 xref, and 3 source attestations. |
| Direct raw-source and lineage scans for this YAML | Pass: found the expected seed, NCBI, GTDB, MADIN, and exact GTDB species rows; confirmed all 10 lineage rows; and found no strain or genome rows for `NCBITaxon:1017264`. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*bordetella_pertussis_cs.md'` | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:(1017264)([^0-9]\|$)' data curation` | Pass: all checked occurrences trace to `legacy_page_paths.tsv`, `PATHS.tsv`, `seed_scope.tsv`, `madin_taxa.tsv`, `gtdb_mappings.tsv`, `ncbitaxon_taxa.tsv`, and this generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10300 maps `NCBITaxon:1017264` to `bordetella_pertussis_cs`.
- `curation/seed_scope.tsv` row 36092 keeps this taxon in scope with an attested NCBI+GTDB+MADIN rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218634 names `NCBITaxon:1017264` as `Bordetella pertussis CS`.
- `data/raw/gtdb_mappings.tsv` row 1178 maps `NCBITaxon:1017264` to `GTDB:s__Bordetella_pertussis` with `skos:closeMatch` and 1381 genomes.
- `data/raw/gtdb_species.tsv` row 19211 preserves `GTDB:s__Bordetella_pertussis` under `GTDB:g__Bordetella` with the same 1381-genome count.
- `data/raw/madin_taxa.tsv` row 474 supplies the 4 MADIN trait assertions preserved in `source_attestations`.

## Evidence

- The YAML identifier, strain rank, label, parent species, and genetic code agree with the exact NCBI Taxonomy row.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:520` / `Bordetella pertussis`.
- GTDB contributes the single `skos:closeMatch` mapping to `GTDB:s__Bordetella_pertussis`, the matching xref, and the `Bordetella pertussis` exact synonym.
- NCBI contributes two exact synonyms, `Bordetella pertussis str. CS` and `Bordetella pertussis strain CS`.
- MADIN is represented only as the `TRAIT_ASSERTION` source attestation count for the exact taxon.

## Completeness

- The record is complete for the exact NCBI, GTDB, and MADIN rows currently present for this taxon.
- The GTDB mapping predicate, species identifier, species label, and genome count match the raw `gtdb_mappings.tsv` row.
- The NCBI synonyms in `data/raw/ncbitaxon_taxa.tsv` are both represented as `EXACT_SYNONYM` entries.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, and exact strain-related source rows.
- The raw-source scan found no exact GOLD, MediaDive, AllTheBacteria, genome-assembly, or causal-graph rows for `NCBITaxon:1017264`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bordetella_pertussis_cs.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/bordetella_pertussis_cs.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10300 |
| `curation/legacy_page_paths.tsv` | 599 |
| `curation/seed_scope.tsv` | 36092 |
| `data/raw/madin_taxa.tsv` | 474 |
| `data/raw/gtdb_mappings.tsv` | 1178 |
| `data/raw/gtdb_species.tsv` | 19211 |
| `data/raw/ncbitaxon_taxa.tsv` | 218634 |
| `data/taxa/bacteria/bordetella_pertussis_cs.yaml` | 1, 39, 45, 56, 61, 67, and 73 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/bordetella_pertussis_cs.yaml`.
- The generated record has no top-level `nomenclature`, `genomes`, `strains`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/bordetella_pertussis_cs.yaml` directly.
