# YAML Record Review: uncultured Hormoscilla sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_hormoscilla_sp.yaml
- Started UTC: 2026-09-23T08:57:43Z
- Finished UTC: 2026-09-23T08:59:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007660 |
| label | uncultured Hormoscilla sp. |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:1007659 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/uncultured_hormoscilla_sp.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_hormoscilla_sp.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found the NCBI row, the one GTDB species row, and the one GTDB mapping row for `NCBITaxon:1007660` / `GTDB:s__Hormoscilla_sp963921275`; no same-taxon LPSN, BacDive, AllTheBacteria, StrainInfo, Madin, GOLD, MediaDive, BactoTraits, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/uncultured_hormoscilla_sp.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/dechloromonas_sp_missr.yaml data/taxa/bacteria/uncultured_hormoscilla_sp.yaml data/taxa/bacteria/pseudomonas_sp_pk.yaml data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI species placeholder `NCBITaxon:1007660`, with label `uncultured Hormoscilla sp.`, direct parent `NCBITaxon:1007659` / `environmental samples`, and bacterial genetic code `11` matching `data/raw/ncbitaxon_taxa.tsv:211058`.

The lineage is root-first and reaches the environmental-samples parent through `Bacteria`, `Bacillati`, the `Cyanobacteriota/Melainabacteria group`, `Cyanobacteriota`, `Cyanophyceae`, `Gomontiellales`, `Gomontiellaceae`, and `Hormoscilla`.

The GTDB overlay is narrow enough for the generated exact-looking projection: `data/raw/gtdb_mappings.tsv:1088` maps the one-genome species cluster `GTDB:s__Hormoscilla_sp963921275` only to this NCBI taxon as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:74362` confirms the same one-genome species row.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:211058` supports the NCBI identifier, label, rank, parent, genetic code, raw `ncbitaxon|gtdb` source set, and `2026-09-13` snapshot date.
- `data/raw/gtdb_mappings.tsv:1088` supports the single `taxonomy_mappings` entry, GTDB exact synonym `Hormoscilla sp963921275`, `GTDB:s__Hormoscilla_sp963921275` xref, and GTDB source attestation.
- `data/raw/gtdb_species.tsv:74362` supports the GTDB species ID, label, genus parent, and `genome_count: 1`.

## Completeness

The record is complete for a generated uncultured NCBI placeholder with one unshared one-genome GTDB close match. It correctly has no nomenclature, strain entries, StrainInfo deposits, GOLD organisms, Madin assertions, MediaDive assertions, BactoTraits assertions, or AllTheBacteria rows in the pinned source inventory.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI and GTDB lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
