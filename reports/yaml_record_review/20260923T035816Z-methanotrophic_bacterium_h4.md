# YAML Record Review: methanotrophic bacterium H4

- Repository: TaxonMech
- Record: data/taxa/bacteria/methanotrophic_bacterium_h4.yaml
- Started UTC: 2026-09-23T03:58:16Z
- Finished UTC: 2026-09-23T03:58:16Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006206`
- Label: `methanotrophic bacterium H4`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33807` (`unclassified Alphaproteobacteria`)
- Path registry row: `data/taxa/PATHS.tsv:2022`

## Validation

- `just validate-strict data/taxa/bacteria/streptomyces_sp_c1_2011.yaml data/taxa/bacteria/methanotrophic_bacterium_h4.yaml data/taxa/bacteria/arthrobacter_sp_b4_2011.yaml data/taxa/bacteria/bacillus_sp_b2_2011b.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/methanotrophic_bacterium_h4.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-methanotrophic_bacterium_h4.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, and bacterial genetic code match `data/raw/ncbitaxon_taxa.tsv:210684`.
- The record is correctly grounded to NCBI placeholder species `NCBITaxon:1006206` under the `unclassified Alphaproteobacteria` parent.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210684` is the sole pinned source row for this placeholder taxon.
- Exact `rg --no-ignore --hidden` searches over `data/raw/`, `data/atb/`, and `data/straininfo/` for `NCBITaxon:1006206` and `methanotrophic bacterium H4` found no same-taxon auxiliary GTDB, ATB, StrainInfo, GOLD, MediaDive, or Madin rows.
- The exact `H4` label search did hit `data/raw/bacdive_strains.tsv:5816`, but that BacDive designation belongs to `NCBITaxon:179637`, not this methanotrophic placeholder.

## Completeness

- `strain_count: 0` and the single `NCBITAXON` source attestation are complete for the currently pinned local evidence.
- The record has no synonyms, nomenclature block, taxonomy mappings, genome rows, or related records because no same-taxon local sidecar supports them.

## Findings

- No curation findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-check auxiliary source rows if future inventories add same-taxon H4 genome or culture evidence.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
