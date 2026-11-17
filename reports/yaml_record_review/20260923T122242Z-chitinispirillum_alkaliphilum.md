# YAML Record Review: Chitinispirillum alkaliphilum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chitinispirillum_alkaliphilum.yaml
- Started UTC: 2026-09-23T12:20:29Z
- Finished UTC: 2026-09-23T12:22:44Z
- Verdict: pass

## Target

- Path: `data/taxa/bacteria/chitinispirillum_alkaliphilum.yaml`
- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1008392`
- Label: `Chitinispirillum alkaliphilum`
- Rank/domain: `SPECIES` in `BACTERIA`
- Parent: `NCBITaxon:1860139` (`Chitinispirillum`)
- Grounding/mapping: `EXACT` / `SEEDED`
- Generated status: generated from committed source inventories under `data/raw/`, `data/atb/`, and `data/straininfo/`; future fixes belong in those maintained inputs or in the seeder, not in `data/taxa/`.

## Validation

- `just validate-strict data/taxa/bacteria/chitinispirillum_alkaliphilum.yaml data/taxa/bacteria/haloalkaliphilic_bacterium_acht6_2.yaml data/taxa/bacteria/haloalkaliphilic_bacterium_acht7.yaml data/taxa/bacteria/vibrio_sp_jz08is34.yaml` passed: 4 files scanned, 0 files with errors, 0 total error rows.
- `just validate data/taxa/bacteria/chitinispirillum_alkaliphilum.yaml` passed with `No issues found`.
- `just validate-history` was skipped because this read-only review did not add or modify any `history/` decisions.
- `just validate-products` was skipped because this record has no `causal_graphs` or curator-added graph nodes to check through the product label gate.
- `just verify-corpus` was skipped for this focused review; earlier full-corpus reproduction over 625,960 records was clean.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1008392` with label `Chitinispirillum alkaliphilum`, rank `SPECIES`, parent `NCBITaxon:1860139`, genetic code `11`, and source list `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|bactotraits`, matching the YAML identity and source attestations.
- The lineage is root-first, stays under Bacteria, and reaches the NCBI genus parent `NCBITaxon:1860139` carried by the NCBI source row.
- `data/raw/lpsn_names.tsv` maps `lpsn:794264` to the same NCBI taxon and name, marks the name legitimate, validly published, and correct, carries the `DSM-24539` type-strain designation, and supplies the DOI, PMID, and `INSDC:JF304644` sequence accession emitted in `nomenclature`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Chitinispirillum_alkaliphilum` to `NCBITaxon:1008392` as `skos:closeMatch` with `genome_count` 1. On this species-level record, the GTDB species-cluster xref and mapping predicate do not overstate a strain-level identity.

## Evidence

- The two NCBI related synonyms, `Chitinispirillum alkaliphilum Sorokin et al. 2016` and `haloalkaliphilic bacterium ACht6-1`, are present verbatim in the NCBI row's synonym field and are correctly weaker than exact synonyms.
- `data/raw/bacdive_strains.tsv` has BacDive strain `140164`, designation `ACht6-1`, NCBI taxon `1008392`, LPSN ID `794264`, and culture IDs `DSM-24539` and `UNIQEM%20U893`, supporting the single BacDive strain block.
- `data/raw/culture_collection_strains.tsv` links both `kgmicrobe.strain:DSM-24539` and `kgmicrobe.strain:UNIQEM%20U893` to `NCBITaxon:1008392`; NCBI type-material rows also list `DSM 24539`, `DSM:24539`, `UNIQEM U893`, and `ACht6-1`.
- `data/raw/strain_assemblies.tsv` links `kgmicrobe.strain:bacdive_140164` to `ncbi.assembly:GCA_001045525` from BacDive reference `66792` with taxon `NCBITaxon:1008392`, assembly level `contig`, and the emitted assembly name.
- `data/raw/strain_genome_records.tsv` links the same BacDive strain to `img.taxon:2636415956` and `patric:1008392.4` with the same BacDive reference, assembly level, name, taxon, and source fields emitted in `genome_records`.
- `data/raw/strain_related_records.tsv` carries two GOLD organism links for `gold:Go0613762`, one through `ORGANISM CULTURE COLLECTION ID` and one through `ORGANISM STRAIN`; both are faithfully represented under the strain's `related_records`.
- `data/straininfo/strain_links.tsv` links the BacDive strain to `straininfo.strain:405783`, deposit `straininfo.deposit:913033`, matched `DSM-24539`, `DOI:10.60712/SI-ID405783.3`, and an available deposit status, supporting the StrainInfo related-record evidence.
- Aggregate source attestations match maintained count rows: `data/raw/gold_organisms.tsv` reports 3 GOLD organisms, `data/raw/mediadive_taxa.tsv` reports 1 MediaDive medium, and `data/raw/bactotraits_taxa.tsv` reports 1 BactoTraits assertion for `NCBITaxon:1008392`.

## Completeness

- `strain_count: 1` matches the single BacDive strain that is classed to this taxon in the maintained inventories.
- No optional causal graph is expected for this generated species record.
- The exact ignored-file-aware `find reports/yaml_record_review -maxdepth 1 -type f -name '*-chitinispirillum_alkaliphilum.md'` check found no prior report before this one was written.
- Ignored-file-aware exact `rg` checks over `data/raw`, `data/atb`, `data/straininfo`, `data/bacdive`, and `data/gold` found the maintained NCBI, LPSN, GTDB, BacDive, GOLD, StrainInfo, MediaDive, and BactoTraits rows used by the record and found no contradictory same-taxon auxiliary row.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None beyond the routine next `just verify-corpus` or `just qc` run after future source or seeder edits.

## Additional Notes

- Live authority pages were not queried during this batch; the checked-in pinned inventories in `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the reproducible source of truth.
- The GOLD aggregate count is larger than the two GOLD `related_records` on the BacDive strain, but the record keeps GOLD organism-count attestation separate from strain-specific GOLD organism links, which matches the repository's source model.
