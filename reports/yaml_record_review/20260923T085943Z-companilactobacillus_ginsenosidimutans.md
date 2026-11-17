# YAML Record Review: Companilactobacillus ginsenosidimutans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml
- Started UTC: 2026-09-23T08:57:43Z
- Finished UTC: 2026-09-23T08:59:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007676 |
| label | Companilactobacillus ginsenosidimutans |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2767879 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| strain_count | 1 |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-companilactobacillus_ginsenosidimutans.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found the expected NCBI, LPSN, GTDB, BacDive, StrainInfo, GOLD, Madin, MediaDive, BactoTraits, culture-collection, strain-genome, and NCBI type-material rows for `NCBITaxon:1007676` / `Companilactobacillus ginsenosidimutans`. |
| `just validate data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/dechloromonas_sp_missr.yaml data/taxa/bacteria/uncultured_hormoscilla_sp.yaml data/taxa/bacteria/pseudomonas_sp_pk.yaml data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI species `NCBITaxon:1007676`, with label `Companilactobacillus ginsenosidimutans`, `SPECIES` rank, direct parent `NCBITaxon:2767879`, and bacterial genetic code `11` matching `data/raw/ncbitaxon_taxa.tsv:211059`.

The LPSN row `data/raw/lpsn_names.tsv:2027` names `Companilactobacillus ginsenosidimutans` as a legitimate, validly published ICNP correct name with authority `Zheng et al. 2020`, species page `https://lpsn.dsmz.de/species/companilactobacillus-ginsenosidimutans`, type designations `kgmicrobe.strain:DSM-24154T` and `kgmicrobe.strain:LMG-31607`, sequence accession `INSDC:HQ389549`, and a direct link to `NCBITaxon:1007676`.

The GTDB mapping is rank-compatible and identity-preserving: `data/raw/gtdb_mappings.tsv:1089` maps the one-genome species cluster `GTDB:s__Companilactobacillus_ginsenosidimutans` to this same NCBI species as `skos:closeMatch`, and the LPSN row links the same GTDB species to the correct name.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:211059` supports the NCBI identity plus the exact old-name synonym `Lactobacillus ginsenosidimutans` and the three related NCBI synonyms emitted in YAML.
- `data/raw/bacdive_strains.tsv:22880` supports the single BacDive strain `bacdive:23075`, its NCBI and LPSN links, and the DSM 24154 / EMML 3041 culture-collection IDs.
- `data/raw/strain_assemblies.tsv:108317` and `data/raw/strain_genome_records.tsv:87129` support the BacDive INSDC and IMG genome records emitted for `kgmicrobe.strain:bacdive_23075`.
- `data/raw/gold_organisms.tsv:187` and `data/raw/strain_related_records.tsv:313810` to `data/raw/strain_related_records.tsv:313811` support the two GOLD organism links to `gold:Go0613535`.
- `data/straininfo/strain_links.tsv:80481` supports the StrainInfo deposit and strain related records for `DSM 24154`.
- `data/raw/madin_taxa.tsv:384`, `data/raw/bactotraits_taxa.tsv:39`, and `data/raw/mediadive_taxa.tsv:54` support the generated Madin, BactoTraits, and MediaDive source attestations.

## Completeness

The record is complete for the maintained local source set. It carries the LPSN nomenclature, one species-level GTDB close match, old-name and authority synonyms from NCBI, the BacDive strain with assembly/genome links, the two GOLD organism matches, the StrainInfo strain/deposit evidence, and all expected source attestations.

The pinned NCBI type-material rows at `data/raw/ncbi_type_material.tsv:605` through `data/raw/ncbi_type_material.tsv:610` are not separately projected into `nomenclature`; TaxonMech currently derives the type designations from LPSN for this field.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI, LPSN, GTDB, BacDive, StrainInfo, GOLD, Madin, MediaDive, and BactoTraits lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
