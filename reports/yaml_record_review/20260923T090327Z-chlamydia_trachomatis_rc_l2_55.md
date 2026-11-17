# YAML Record Review: Chlamydia trachomatis RC-L2/55

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml
- Started UTC: 2026-09-23T09:02:15Z
- Finished UTC: 2026-09-23T09:03:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007870 |
| label | Chlamydia trachomatis RC-L2/55 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:813 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-chlamydia_trachomatis_rc_l2_55.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact anchored `rg --no-ignore --hidden` checks found the NCBI, GTDB, and Madin rows for `NCBITaxon:1007870` across `data/raw/`, `data/atb/`, and `data/straininfo/`. No same-strain LPSN, BacDive, AllTheBacteria, StrainInfo, GOLD, MediaDive, BactoTraits, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/verticillium_longisporum.yaml data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml data/taxa/bacteria/chlamydia_trachomatis_rc_j_971.yaml data/taxa/bacteria/curtobacterium_sp_tn4w_19.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The NCBI portion of the record denotes pinned strain taxon `NCBITaxon:1007870`, with label `Chlamydia trachomatis RC-L2/55`, `STRAIN` rank, parent species `NCBITaxon:813`, and bacterial genetic code `11` matching `data/raw/ncbitaxon_taxa.tsv:211060`.

The lineage is root-first and correctly reaches the parent species through `Bacteria`, `Pseudomonadati`, `PVC group`, `Chlamydiota`, `Chlamydiia`, `Chlamydiales`, `Chlamydiaceae`, the no-rank `Chlamydia/Chlamydophila group`, and `Chlamydia`.

The GTDB overlay is over-scoped for this strain. `data/raw/gtdb_mappings.tsv:1090` maps the 210-genome species cluster `GTDB:s__Chlamydia_trachomatis` to this one NCBI strain as `skos:closeMatch`; the same local GTDB ID is reused on dozens of NCBI taxa, and `data/raw/lpsn_names.tsv:21707` plus `data/raw/gtdb_mappings.tsv:311645` tie the cluster to the species `Chlamydia trachomatis` / `NCBITaxon:813` rather than to a single RC strain.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:211060` supports the NCBI identifier, label, `STRAIN` rank, parent, genetic code, and exact strain synonyms `Chlamydia trachomatis str. RC-L2/55` and `Chlamydia trachomatis strain RC-L2/55`.
- `data/raw/madin_taxa.tsv:385` supports the Madin source attestation with one `TRAIT_ASSERTION`.
- `data/raw/gtdb_mappings.tsv:1090` is the maintained input for the currently emitted GTDB taxonomy mapping, exact synonym, xref, and GTDB source attestation.
- `data/raw/gtdb_species.tsv:42013` shows the projected GTDB cluster has 210 genomes, and the exact local search found the same GTDB species cluster mapped onto many NCBI strain taxa.

## Completeness

The NCBI and Madin parts of the record are complete. The consequential gap is representational: the GTDB species cluster should not be exposed as an exact equivalent of the strain-level `NCBITaxon:1007870` record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | `GTDB:s__Chlamydia_trachomatis` is projected as a `skos:closeMatch`, exact synonym, xref, and exact-looking source attestation on strain `Chlamydia trachomatis RC-L2/55`. | `data/raw/gtdb_mappings.tsv:1090` maps a 210-genome species cluster to `NCBITaxon:1007870`; the same GTDB species is shared across dozens of NCBI taxa, and `data/raw/lpsn_names.tsv:21707` links it to the parent species name. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` |

## Recommended Edits

1. Correct the GTDB mapping input so `GTDB:s__Chlamydia_trachomatis` is not emitted as a close/exact match for `NCBITaxon:1007870`, or change the seeder so species clusters mapped to NCBI strain records are retained only as defensibly non-exact species-cluster relationships.
2. Regenerate `data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml` so it drops the GTDB-derived `Chlamydia trachomatis` exact synonym, the `GTDB:s__Chlamydia_trachomatis` xref, and the GTDB source attestation unless a corrected non-exact mapping remains.

## Follow-up Checks

After the mapping fix, rerun `just seed-canary NCBITaxon:1007870`, inspect `data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml`, and rerun `just validate-strict data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml`. Also search `data/raw/gtdb_mappings.tsv` for `GTDB:s__Chlamydia_trachomatis` to verify that close/exact projections are no longer being attached to `Chlamydia trachomatis` strain records.

## Additional Notes

- External live NCBI, GTDB, LPSN, and Madin lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
