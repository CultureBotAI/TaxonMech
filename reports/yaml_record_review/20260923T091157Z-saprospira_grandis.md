# YAML Record Review: Saprospira grandis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/saprospira_grandis.yaml
- Started UTC: 2026-09-23T09:09:58Z
- Finished UTC: 2026-09-23T09:11:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1008 |
| label | Saprospira grandis |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:1007 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| strain_count | 2 |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/saprospira_grandis.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-saprospira_grandis.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact anchored `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found the expected NCBI, LPSN, GTDB, BacDive, AllTheBacteria, StrainInfo, GOLD, Madin, culture-collection, strain-genome, and NCBI type-material rows for `NCBITaxon:1008` / `Saprospira grandis`. |
| `just validate data/taxa/bacteria/saprospira_grandis.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_lks_107.yaml data/taxa/bacteria/bacillus_sp_lks_108.yaml data/taxa/bacteria/bacillus_sp_lks_11.yaml data/taxa/bacteria/saprospira_grandis.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI species `NCBITaxon:1008`, with label `Saprospira grandis`, direct parent `NCBITaxon:1007`, and bacterial genetic code `11` matching `data/raw/ncbitaxon_taxa.tsv:782`.

The LPSN row `data/raw/lpsn_names.tsv:19763` names `Saprospira grandis` as a legitimate, validly published ICNP correct name with authority `Gross 1911 (Approved Lists 1980)`, type-strain designations `ATCC-23119`, `JCM-21750`, and `LMG-10407`, and sequence accession `INSDC:M58795`.

The GTDB mapping on this record is species-level and source-backed: `data/raw/gtdb_mappings.tsv:1092` maps two-genome `GTDB:s__Saprospira_grandis` to `NCBITaxon:1008` as `skos:closeMatch`, and the LPSN row links the same GTDB species to the same species name. The exact GTDB search also found this cluster on descendant strain `NCBITaxon:984262`; that over-projection should be assessed on the strain record and does not invalidate the species-level mapping reviewed here.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:782` supports the NCBI identifier, label, rank, parent, genetic code, related authority synonym, and raw source set.
- `data/raw/lpsn_names.tsv:19763` supports the LPSN nomenclature, type-strain list, DOI, and sequence accession.
- `data/raw/bacdive_strains.tsv:85482` supports the direct type strain `bacdive:163246`; `kgmicrobe.strain:bacdive_14045` is also represented with `classified_as: NCBITaxon:694433` for descendant strain `Saprospira grandis DSM 2844`.
- `data/raw/strain_assemblies.tsv:75957`, `data/raw/strain_genome_records.tsv:59126`, `data/atb/strain_links.tsv:2462`, and `data/atb/genome_links.tsv:10417` to `data/atb/genome_links.tsv:10418` support the direct strain genome and AllTheBacteria evidence.
- `data/straininfo/strain_links.tsv:64696` through `data/straininfo/strain_links.tsv:64701` support the StrainInfo deposits for the direct BacDive strain, while `data/straininfo/strain_links.tsv:27485` and `data/straininfo/assemblies.tsv:3590` through `data/straininfo/assemblies.tsv:3591` support the DSM 2844 descendant strain evidence.
- `data/raw/gold_organisms.tsv:189` and `data/raw/madin_taxa.tsv:387` support the direct GOLD and Madin source attestations.

## Completeness

The generated species record is complete for the maintained local source set. It carries the NCBI identity, NCBI authority synonym, LPSN nomenclature, one GTDB species mapping, one direct BacDive type strain with ATB/BV-BRC/GOLD/StrainInfo evidence, one descendant BacDive strain filed under `NCBITaxon:694433`, and all expected source attestations.

The pinned NCBI type-material rows at `data/raw/ncbi_type_material.tsv:621` through `data/raw/ncbi_type_material.tsv:627` duplicate the LPSN type-strain designations; TaxonMech currently derives the YAML `nomenclature` type strains from LPSN.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI, LPSN, GTDB, BacDive, StrainInfo, GOLD, Madin, and AllTheBacteria lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The exact `NCBITaxon:1008` source search used a non-digit guard to avoid false matches to longer `NCBITaxon:1008...` identifiers.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
