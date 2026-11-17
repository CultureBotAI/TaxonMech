# YAML Record Review: Salmonella enterica subsp. enterica serovar Typhimurium str. 798

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.yaml`
- Started UTC: 2026-09-23T11:42:49Z
- Finished UTC: 2026-09-23T11:42:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.yaml` |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1008297` |
| Label | `Salmonella enterica subsp. enterica serovar Typhimurium str. 798` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:90371` / `Salmonella enterica subsp. enterica serovar Typhimurium` |
| Grounding | `EXACT` |
| Mapping | `SEEDED` |

This is a generated NCBI strain record with NCBI, GTDB, GOLD, and Madin source attestations.

## Validation

| Check | Result |
|---|---|
| Full target read | Passed; `sed -n '1,320p' data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.yaml` covered all 92 lines. |
| Prior-report search | Passed; `find reports/yaml_record_review -maxdepth 1 -type f -name '*-salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.md'` found no prior report. `find` includes ignored report files. |
| Strict schema | Passed; `just validate-strict data/taxa/bacteria/shewanella_sp_96.yaml data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.yaml data/taxa/bacteria/mycobacterium_leprae_kyoto_2.yaml data/taxa/bacteria/richelia_cyanobiont_of_rhizosolenia_sp.yaml` scanned 4 files with 0 error rows. |
| LinkML schema | Passed; `just validate data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.yaml` returned `No issues found`. |
| Same-taxon source search | Passed; `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found `NCBITaxon:1008297` in `PATHS.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/madin_taxa.tsv`. |
| History validation | Skipped; this read-only review did not add a `history/` decision record. |
| Corpus reproduction | Skipped; generated `data/taxa` YAML was not edited, and earlier full-corpus reproduction over the 625,960-record corpus was already clean. |
| Product ID/label validation | Skipped; this record has no `causal_graphs` or curator-added graph nodes. |

## Identity and Grounding

The NCBI identity is exact: `data/raw/ncbitaxon_taxa.tsv:211303` has `NCBITaxon:1008297`, the same strain label, rank `STRAIN`, parent `NCBITaxon:90371`, genetic code `11`, and the NCBI exact synonym `Salmonella enterica subsp. enterica serovar Typhimurium strain 798`.

The GOLD and Madin attestations are row-count attestations keyed to the same NCBI identifier: `data/raw/gold_organisms.tsv:193` and `data/raw/madin_taxa.tsv:388` each carry count `1` for `NCBITaxon:1008297`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1095` maps the species cluster `GTDB:s__Salmonella_enterica` to this NCBI strain ID with `skos:closeMatch` and a genome count of `21527`; that species cluster is much broader than strain 798 and should not become a strain-level exact synonym or exact-looking xref.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| NCBI strain identity | `data/raw/ncbitaxon_taxa.tsv:211303` | Supported exactly. |
| NCBI strain exact synonym | `data/raw/ncbitaxon_taxa.tsv:211303` | Supported exactly. |
| GOLD source attestation | `data/raw/gold_organisms.tsv:193` | Supported as a one-row `ORGANISM` attestation for this NCBI ID. |
| Madin source attestation | `data/raw/madin_taxa.tsv:388` | Supported as a one-row `TRAIT_ASSERTION` attestation for this NCBI ID. |
| `GTDB:s__Salmonella_enterica` as a taxonomy mapping on the strain record | `data/raw/gtdb_mappings.tsv:1095` | The raw row exists, but its species-cluster scope is broader than the NCBI strain. |
| `Salmonella enterica` as a GTDB `EXACT_SYNONYM` for strain 798 | Generated from `data/raw/gtdb_mappings.tsv:1095` by `src/taxonmech/seed.py` | Unsupported because the synonym denotes a species-level GTDB cluster, not this strain. |
| `GTDB:s__Salmonella_enterica` as an xref for strain 798 | Generated from `data/raw/gtdb_mappings.tsv:1095` by `src/taxonmech/seed.py` | Over-scoped for the same reason. |

## Completeness

NCBI, GOLD, and Madin attestations are complete for the exact rows found in the committed inventories. No `data/atb` or `data/straininfo` rows were found for `NCBITaxon:1008297`.

The exact ignored-report `find` search found no earlier review for `salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `GTDB:s__Salmonella_enterica` is a species-cluster row attached directly to a `STRAIN` record, and `src/taxonmech/seed.py` currently promotes every identity GTDB mapping to `xrefs` plus an `EXACT_SYNONYM`. That makes strain 798 look exactly synonymous with the whole `Salmonella enterica` species cluster. | `data/raw/gtdb_mappings.tsv` generation and the GTDB mapping/synonym projection in `src/taxonmech/seed.py` |

## Recommended Edits

- Filter GTDB species-cluster mappings so they are not promoted as strain-level exact synonyms or exact-looking xrefs on NCBI `STRAIN` records; the future fix belongs in `data/raw/gtdb_mappings.tsv` generation and `src/taxonmech/seed.py`, not in generated `data/taxa`.
- After the seed fix, regenerate this record and confirm `GTDB:s__Salmonella_enterica` is absent from `xrefs` and `Salmonella enterica` is absent as a GTDB `EXACT_SYNONYM` on this strain.

## Follow-up Checks

- Re-run `just validate-strict data/taxa/bacteria/salmonella_enterica_subsp_enterica_serovar_typhimurium_str_798.yaml` after the seeding change.
- Re-run `just verify-corpus` after regeneration to prove `data/taxa` reproduces from the maintained inputs.
- Search for `NCBITaxon:1008297` in regenerated `data/raw/gtdb_mappings.tsv` and the regenerated YAML to confirm the GTDB species cluster no longer produces strain-level exact synonymy.

## Additional Notes

No live NCBI, GTDB, GOLD, or Madin lookup was available during this review; local pinned `data/raw` rows were treated as source of truth. The same GTDB strain/scope issue appears on many NCBI strain records that map to broad GTDB species clusters.
