# YAML Record Review: Aphanizomenon sp. 'Norman Lake isolate'

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/aphanizomenon_sp_norman_lake_isolate.yaml
- Started UTC: 2026-09-23T08:11:22Z
- Finished UTC: 2026-09-23T08:13:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100739 |
| label | Aphanizomenon sp. 'Norman Lake isolate' |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2622046 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/` and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: `data/taxa/bacteria/aphanizomenon_sp_norman_lake_isolate.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-aphanizomenon_sp_norman_lake_isolate.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks for `NCBITaxon:100739`, `Aphanizomenon sp. 'Norman Lake isolate'`, and `aphanizomenon_sp_norman_lake_isolate` found only the expected NCBI-derived scope and raw-taxonomy rows across `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/ncbi_type_material.tsv`, `data/atb/`, and `data/straininfo/`. |
| `just validate data/taxa/bacteria/aphanizomenon_sp_norman_lake_isolate.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/aphanizomenon_sp_little_crooked_lake_isolate.yaml data/taxa/bacteria/aphanizomenon_sp_norman_lake_isolate.yaml data/taxa/bacteria/aphanizomenon_sp_bc_aph_9601.yaml data/taxa/archaea/uncultured_sulfolobales_ms1.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species placeholder `NCBITaxon:100739`. Its quoted label, `SPECIES` rank, parent `NCBITaxon:2622046`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:17310`.

The root-first cyanobacterial lineage through `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Nostocales`, `Aphanizomenonaceae`, `Aphanizomenon`, and `unclassified Aphanizomenon` is consistent with the corresponding pinned NCBI inventory rows.

## Evidence

- `source_attestations[0]` is correctly limited to `NCBITAXON`, `source_id: NCBITaxon:100739`, `source_label: Aphanizomenon sp. 'Norman Lake isolate'`, `assertion_count: 1`, and `assertion_unit: NAME`, matching the single `ncbitaxon` source row in `data/raw/ncbitaxon_taxa.tsv:17310`.
- The seeded scope text matches `curation/seed_scope.tsv:143104`: the taxon was in scope by the attested NCBI rule with one source including NCBI.
- No evidence is over-applied from GTDB, LPSN, BacDive, GOLD, AllTheBacteria, StrainInfo, or NCBI type-material rows.

## Completeness

The record is complete for the source evidence currently attached to this placeholder. It correctly omits synonyms, nomenclature, taxonomy mappings, strain records, genome links, and a causal graph because exact gitignore-independent searches over the scoped local source files found no same-taxon auxiliary rows beyond the NCBI inventory and seed-scope rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories later add GTDB, LPSN, BacDive, ATB, StrainInfo, or NCBI type-material evidence for `NCBITaxon:100739`, rerun `just seed-canary NCBITaxon:100739`, inspect `data/taxa/bacteria/aphanizomenon_sp_norman_lake_isolate.yaml`, and rerun `just validate-strict data/taxa/bacteria/aphanizomenon_sp_norman_lake_isolate.yaml`.

## Additional Notes

- External live NCBI Taxonomy lookup was not used in this environment; the pinned `2026-09-13` NCBI rows in `data/raw/ncbitaxon_taxa.tsv` are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
