# YAML Record Review: Ogataea parapolymorpha

- Repository: TaxonMech
- Record: data/taxa/eukaryota/ogataea_parapolymorpha.yaml
- Started UTC: 2026-09-23T03:39:50Z
- Finished UTC: 2026-09-23T03:39:50Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005962`
- Label: `Ogataea parapolymorpha`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:461281` (`Ogataea`)
- Path registry row: `data/taxa/PATHS.tsv:1997`

## Validation

- `just validate-strict data/taxa/eukaryota/ogataea_parapolymorpha.yaml data/taxa/bacteria/trabulsiella_guamensis_atcc_49490.yaml data/taxa/bacteria/tatumella_ptyseos_atcc_33301.yaml data/taxa/bacteria/klebsiella_planticola_atcc_33531.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/eukaryota/ogataea_parapolymorpha.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-ogataea_parapolymorpha.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, eukaryotic domain, parent taxon, genetic code, and NCBI-derived synonyms match `data/raw/ncbitaxon_taxa.tsv:210660`.
- The record sits under `Ogataea` in the fungal lineage and uses genetic code `1`, matching the pinned NCBI row.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to `NCBITaxon:1005962`.

## Evidence

- `curation/seed_scope.tsv:57180` keeps this species in scope through two attesting sources, NCBI and GOLD.
- `data/raw/gold_organisms.tsv:156` supplies the four GOLD organisms summarized by the GOLD source attestation.
- `NCBITaxon:871575`, `Ogataea parapolymorpha DL-1`, appears separately as a child strain record in the local NCBI snapshot; the YAML correctly scopes the GOLD source attestation to records filed directly under `NCBITaxon:1005962`.
- A gitignore-independent `rg --no-ignore --hidden` scan over GTDB, strain raw, ATB, and StrainInfo files found no same-ID strain rows that should be projected directly under this species record.

## Completeness

- The NCBI exact and related synonyms are present, and no local GTDB, BacDive, LPSN, ATB, or StrainInfo projections are available for this exact species taxon.
- `strain_count: 0` is consistent with the absence of direct same-taxon local strain rows.
- The two `source_attestations` entries match the available high-level local evidence for `NCBITaxon:1005962`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if direct GTDB, BacDive, LPSN, ATB, or StrainInfo evidence is imported for `NCBITaxon:1005962`.
- Re-review if descendant strain GOLD records start being rolled up into species-level records rather than represented separately.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
