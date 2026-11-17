# YAML Record Review: Marivirga tractuosa

- Repository: TaxonMech
- Record: data/taxa/bacteria/marivirga_tractuosa.yaml
- Started UTC: 2026-09-23T03:42:38Z
- Finished UTC: 2026-09-23T03:42:38Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006`
- Label: `Marivirga tractuosa`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:869806` (`Marivirga`)
- Path registry row: `data/taxa/PATHS.tsv:2002`

## Validation

- `just validate-strict data/taxa/bacteria/leminorella_grimontii_atcc_33999_dsm_5078.yaml data/taxa/bacteria/marivirga_tractuosa.yaml data/taxa/bacteria/kluyvera_ascorbata_atcc_33433.yaml data/taxa/bacteria/citrobacter_freundii_atcc_8090_mtcc_1658_nbrc_12681.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/marivirga_tractuosa.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-marivirga_tractuosa.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and NCBI-derived synonyms match the pinned short-ID row in `data/raw/ncbitaxon_taxa.tsv:780`.
- The LPSN block matches `data/raw/lpsn_names.tsv:25837`: `lpsn:788713`, authority `(Lewin 1969) Nedashkovskaya et al. 2010`, correct-name status, type-strain designations, DOI/PMID publications, and `INSDC:AB078072`.
- The YAML contains both GTDB mappings from `data/raw/gtdb_mappings.tsv:1048` and `data/raw/gtdb_mappings.tsv:1049`, with explicit `skos:broadMatch` predicates and no GTDB exact synonym.
- `grounding_status: EXACT` is appropriate because the record is grounded to the current NCBI species and LPSN correct-name entry; the pooled GTDB projections are explicitly marked as broad mappings.

## Evidence

- The raw source list in `data/raw/ncbitaxon_taxa.tsv:780` and the source attestations show NCBI, LPSN, GTDB, BacDive, GOLD, and Madin evidence for this species.
- The record has `strain_count: 2`: the type strain from `bacdive:5473`, partly classified under child strain `NCBITaxon:643867`, and a second BacDive strain whose StrainInfo deposit rows are filed directly under `NCBITaxon:1006`.
- Exact `rg --no-ignore --hidden` source scans anchored on `NCBITaxon:1006` confirmed the short ID did not cross-match to neighboring six-digit records while finding the local GTDB, BacDive/GOLD genome, StrainInfo, and related-record rows projected into the YAML.
- `data/straininfo/assemblies.tsv:10082` contributes the DSM 4126 StrainInfo genome assembly retained under the matched BacDive type strain.

## Completeness

- The record projects the local LPSN nomenclature, two broad GTDB taxonomy mappings, two BacDive strains, GOLD organism records, Madin source evidence, and strain-level assembly/genome/related records available for this species and its DSM 4126 child strain.
- The NCBI, LPSN, GTDB, BacDive, GOLD, and Madin source attestations match the local source families available for `NCBITaxon:1006`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if GTDB collapses `GTDB:s__Marivirga_tractuosa` and `GTDB:s__Marivirga_tractuosa_A` or changes their mapping predicates from `skos:broadMatch`.
- Re-review the record if local roll-up behavior for child strain `NCBITaxon:643867` changes.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
