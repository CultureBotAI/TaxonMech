# YAML Record Review: Priestia megaterium WSH-002

- Repository: TaxonMech
- Record: data/taxa/bacteria/priestia_megaterium_wsh_002.yaml
- Started UTC: 2026-09-23T03:47:32Z
- Finished UTC: 2026-09-23T03:47:32Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006007`
- Label: `Priestia megaterium WSH-002`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1404` (`Priestia megaterium`)
- Path registry row: `data/taxa/PATHS.tsv:2008`

## Validation

- `just validate-strict data/taxa/bacteria/buttiauxella_agrestis_atcc_33320.yaml data/taxa/archaea/metallosphaera_cuprina.yaml data/taxa/archaea/metallosphaera_cuprina_ar_4.yaml data/taxa/bacteria/priestia_megaterium_wsh_002.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/priestia_megaterium_wsh_002.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-priestia_megaterium_wsh_002.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, and renamed `Bacillus megaterium` NCBI exact strain synonyms match `data/raw/ncbitaxon_taxa.tsv:210670`.
- The record is correctly grounded to the NCBI strain `NCBITaxon:1006007` under parent species `Priestia megaterium`.
- `data/raw/gtdb_mappings.tsv:1055` maps the 135-genome GTDB species cluster `GTDB:s__Priestia_zanthoxyli` to the WSH-002 child strain as `skos:closeMatch`.

## Evidence

- `data/raw/madin_taxa.tsv:356` supplies the five Madin trait assertions summarized by the `MADIN` source attestation.
- `data/raw/gtdb_species.tsv:144425` supplies the 135-genome count projected into the GTDB source attestation.
- An exact `rg --no-ignore --hidden` lookup for `NCBITaxon:1006007`, `WSH-002`, and `Priestia megaterium WSH-002` found no same-strain assembly, genome, related-record, StrainInfo, or ATB rows in the checked local sidecars.

## Completeness

- The NCBI, GTDB, and Madin attestations are represented.
- The empty strain payload is consistent with the checked local raw inventories: only NCBI, GTDB, and Madin rows were present for `NCBITaxon:1006007`.

## Findings

- Major: the GTDB species cluster `GTDB:s__Priestia_zanthoxyli` is projected as a `skos:closeMatch`, xref, and exact synonym `Priestia zanthoxyli` onto the narrower NCBI strain `NCBITaxon:1006007`.

## Recommended Edits

- Owner: `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py`. Suppress species-cluster exact synonyms and strain-level `skos:closeMatch` projections when a GTDB species maps to a narrower NCBI strain.

## Follow-up Checks

- After the GTDB projection is corrected, regenerate this YAML and verify that `Priestia zanthoxyli` is no longer an exact synonym of `Priestia megaterium WSH-002`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
