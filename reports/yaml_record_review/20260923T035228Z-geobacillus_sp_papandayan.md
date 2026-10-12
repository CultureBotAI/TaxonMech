# YAML Record Review: Geobacillus sp. 'Papandayan'

- Repository: TaxonMech
- Record: data/taxa/bacteria/geobacillus_sp_papandayan.yaml
- Started UTC: 2026-09-23T03:52:28Z
- Finished UTC: 2026-09-23T03:52:28Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006153`
- Label: `Geobacillus sp. 'Papandayan'`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2642459` (`unclassified Geobacillus`)
- Path registry row: `data/taxa/PATHS.tsv:2015`

## Validation

- `just validate-strict data/taxa/bacteria/geobacillus_sp_mnk.yaml data/taxa/bacteria/geobacillus_sp_manuk.yaml data/taxa/bacteria/geobacillus_sp_papandayan.yaml data/taxa/bacteria/acinetobacter_sp_fm4.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/geobacillus_sp_papandayan.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-geobacillus_sp_papandayan.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, and bacterial genetic code match `data/raw/ncbitaxon_taxa.tsv:210677`, including the quoted `Papandayan` isolate label.
- The record is correctly grounded to NCBI placeholder species `NCBITaxon:1006153` under the `unclassified Geobacillus` parent.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210677` is the sole pinned source row for this placeholder taxon.
- Exact `rg --no-ignore --hidden` searches over `data/raw/`, `data/atb/`, and `data/straininfo/` for `NCBITaxon:1006153` found no same-taxon auxiliary BacDive, GTDB, ATB, StrainInfo, GOLD, MediaDive, or Madin rows.

## Completeness

- `strain_count: 0` and the single `NCBITAXON` source attestation are complete for the currently pinned local evidence.
- The record has no synonyms, nomenclature block, taxonomy mappings, genome rows, or related records because no local sidecar supports them.

## Findings

- No curation findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-check auxiliary source rows if future inventories add `Papandayan` genome or culture evidence.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
