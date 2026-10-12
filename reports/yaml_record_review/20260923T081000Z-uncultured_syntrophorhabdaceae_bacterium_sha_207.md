# YAML Record Review: uncultured Syntrophorhabdaceae bacterium SHA-207

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_syntrophorhabdaceae_bacterium_sha_207.yaml
- Started UTC: 2026-09-23T08:08:51Z
- Finished UTC: 2026-09-23T08:10:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100737 |
| label | uncultured Syntrophorhabdaceae bacterium SHA-207 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:513581 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/` and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: `data/taxa/bacteria/uncultured_syntrophorhabdaceae_bacterium_sha_207.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_syntrophorhabdaceae_bacterium_sha_207.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: boundary-guarded `rg --no-ignore --hidden` checks for `NCBITaxon:100737`, `uncultured Syntrophorhabdaceae bacterium SHA-207`, and `uncultured_syntrophorhabdaceae_bacterium_sha_207` found only the expected NCBI-derived scope and raw-taxonomy rows across `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/ncbi_type_material.tsv`, `data/atb/`, and `data/straininfo/`. |
| `just validate data/taxa/bacteria/uncultured_syntrophorhabdaceae_bacterium_sha_207.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_53.yaml data/taxa/bacteria/uncultured_bacterium_sha_300.yaml data/taxa/bacteria/uncultured_bacterium_sha_105.yaml data/taxa/bacteria/uncultured_syntrophorhabdaceae_bacterium_sha_207.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes the pinned NCBI Taxonomy species placeholder `NCBITaxon:100737`. Its label, `SPECIES` rank, parent `NCBITaxon:513581`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:17308`.

The root-first lineage through `Thermodesulfobacteriota`, `Syntrophorhabdia`, `Syntrophorhabdales`, `Syntrophorhabdaceae`, and the family-level `environmental samples` node is consistent with the corresponding pinned NCBI inventory rows.

## Evidence

- `source_attestations[0]` is correctly limited to `NCBITAXON`, `source_id: NCBITaxon:100737`, `source_label: uncultured Syntrophorhabdaceae bacterium SHA-207`, `assertion_count: 1`, and `assertion_unit: NAME`, matching the single `ncbitaxon` source row in `data/raw/ncbitaxon_taxa.tsv:17308`.
- The exact synonym `uncultured bacterium SHA-207` matches the NCBI synonym column in `data/raw/ncbitaxon_taxa.tsv:17308` and is correctly sourced to NCBITaxon.
- The seeded scope text matches `curation/seed_scope.tsv:143102`: the taxon was in scope by the attested NCBI rule with one source including NCBI.
- No evidence is over-applied from GTDB, LPSN, BacDive, GOLD, AllTheBacteria, StrainInfo, or NCBI type-material rows.

## Completeness

The record is complete for the source evidence currently attached to this placeholder: it carries the one NCBI synonym available in the raw taxonomy row and omits nomenclature, taxonomy mappings, strain records, genome links, and a causal graph because exact gitignore-independent searches over the scoped local source files found no same-taxon auxiliary rows beyond the NCBI inventory and seed-scope rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If upstream inventories later add GTDB, LPSN, BacDive, ATB, StrainInfo, or NCBI type-material evidence for `NCBITaxon:100737`, rerun `just seed-canary NCBITaxon:100737`, inspect `data/taxa/bacteria/uncultured_syntrophorhabdaceae_bacterium_sha_207.yaml`, and rerun `just validate-strict data/taxa/bacteria/uncultured_syntrophorhabdaceae_bacterium_sha_207.yaml`.

## Additional Notes

- The exact source search guarded `NCBITaxon:100737`, `uncultured Syntrophorhabdaceae bacterium SHA-207`, and `uncultured_syntrophorhabdaceae_bacterium_sha_207` with TSV or numeric boundaries to avoid longer neighboring SHA taxa.
- External live NCBI Taxonomy lookup was not used in this environment; the pinned `2026-09-13` NCBI rows in `data/raw/ncbitaxon_taxa.tsv` are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
