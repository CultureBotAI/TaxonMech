# YAML Record Review: Marinococcus sp. HOB7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/marinococcus_sp_hob7.yaml
- Started UTC: 2026-09-23T08:46:28Z
- Finished UTC: 2026-09-23T08:47:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007608 |
| label | Marinococcus sp. HOB7 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2629087 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/` and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: all 54 lines of `data/taxa/bacteria/marinococcus_sp_hob7.yaml` were read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-marinococcus_sp_hob7.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks for `NCBITaxon:1007608`, `Marinococcus sp. HOB7`, and `marinococcus_sp_hob7` found only the expected NCBI raw-taxonomy row across `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`. |
| `just validate data/taxa/bacteria/marinococcus_sp_hob7.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/halomonas_sp_hob4.yaml data/taxa/bacteria/halomonas_sp_hob8.yaml data/taxa/bacteria/marinococcus_sp_hob7.yaml data/taxa/bacteria/nocardia_sp_aoa2.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species placeholder `NCBITaxon:1007608`. Its label, `SPECIES` rank, parent `NCBITaxon:2629087`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:211047`.

The root-first lineage through `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, `Bacillaceae`, `Marinococcus`, and `unclassified Marinococcus` is consistent with the corresponding pinned NCBI inventory rows.

## Evidence

- `source_attestations[0]` is correctly limited to `NCBITAXON`, `source_id: NCBITaxon:1007608`, `source_label: Marinococcus sp. HOB7`, `assertion_count: 1`, and `assertion_unit: NAME`, matching the single `ncbitaxon` source row in `data/raw/ncbitaxon_taxa.tsv:211047`.
- No evidence is over-applied from GTDB, LPSN, BacDive, GOLD, MediaDive, AllTheBacteria, StrainInfo, or NCBI type-material rows.

## Completeness

The record is complete for the source evidence currently attached to this placeholder. It correctly omits synonyms, nomenclature, taxonomy mappings, strain records, genome links, and a causal graph because exact gitignore-independent searches over `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv` found no same-taxon auxiliary rows beyond the NCBI inventory row.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories later add GTDB, LPSN, BacDive, ATB, StrainInfo, or NCBI type-material evidence for `NCBITaxon:1007608`, rerun `just seed-canary NCBITaxon:1007608`, inspect `data/taxa/bacteria/marinococcus_sp_hob7.yaml`, and rerun `just validate-strict data/taxa/bacteria/marinococcus_sp_hob7.yaml`.

## Additional Notes

- External live NCBI Taxonomy lookup was not used in this environment; the pinned `2026-09-13` NCBI rows in `data/raw/ncbitaxon_taxa.tsv` are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
