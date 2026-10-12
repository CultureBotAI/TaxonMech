# YAML Record Review: Abyssicoccus albus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssicoccus_albus.yaml
- Started UTC: 2026-09-22T06:25:30Z
- Finished UTC: 2026-09-22T06:27:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1817405 |
| label | Abyssicoccus albus |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:1955413 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssicoccus_albus.yaml`. It combines NCBITaxon identity and synonyms, the validly published LPSN name plus synonymized `Auricoccus indicus`, a single GTDB close match, two BacDive strains, MediaDive, GOLD, Madin et al., BactoTraits, StrainInfo overlays, and one ATB assembly.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 281956 maps `NCBITaxon:1817405` to slug `abyssicoccus_albus`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssicoccus_albus.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssicoccus_albus.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssicoccus_albus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 474944 has `NCBITaxon:1817405`, label `Abyssicoccus albus`, rank `SPECIES`, direct parent `NCBITaxon:1955413`, genetic code `11`, exact synonym `Auricoccus indicus`, the expected NCBI related synonyms, source set `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:91061` Bacilli, `CLASS` | line 14761 |
| `NCBITaxon:1385` Caryophanales, `ORDER` | line 1076 |
| `NCBITaxon:3076164` Abyssicoccaceae, `FAMILY` | line 594994 |
| `NCBITaxon:1955413` Abyssicoccus, `GENUS` | line 504265 |

`curation/seed_scope.tsv` line 1591 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 474944 | Supported exactly. |
| LPSN nomenclature, `lpsn:794216`, and `Auricoccus indicus` synonym | `data/raw/lpsn_names.tsv` lines 30770 and 31699 | Supported exactly by the correct-name row plus its synonymized `lpsn:795289` row. |
| GTDB mapping and genome count | `data/raw/gtdb_mappings.tsv` line 62374 and `data/raw/gtdb_species.tsv` line 2828 | Supported exactly: `GTDB:s__Abyssicoccus_albus` maps to `NCBITaxon:1817405` by `skos:closeMatch` with four genomes. |
| BacDive strains and culture collection IDs | `data/raw/bacdive_strains.tsv` lines 54869 and 62745 plus same-taxon rows in `data/raw/culture_collection_strains.tsv` | Supported exactly for `kgmicrobe.strain:bacdive_132558` and `kgmicrobe.strain:bacdive_140460` and their eight combined culture-collection identifiers. |
| Matched assemblies and genome records | `data/raw/strain_assemblies.tsv` lines 25077-25085 and 45432 plus `data/raw/strain_genome_records.tsv` lines 20027-20033 and 35626-35627 | Supported exactly for the BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo-derived entries in YAML. |
| Related records | `data/raw/strain_related_records.tsv` lines 69731-69752 plus an exact gzip scan of `data/straininfo/related_records.tsv.gz` | Supported exactly for the GTDB, NCBI Assembly, BV-BRC, GOLD, and StrainInfo BioProject/BioSample/GOLD/deposit/strain records. |
| StrainInfo links and ATB assembly evidence | `data/straininfo/strain_links.tsv` lines 13595 and 27499, `data/straininfo/assemblies.tsv` line 2240, and `data/atb/strain_links.tsv` line 873 | Supported exactly, including the ATB sample links for `biosample:SAMN10362902`. |
| MediaDive, GOLD, Madin et al., and BactoTraits source counts | `data/raw/mediadive_taxa.tsv` line 5402, `data/raw/gold_organisms.tsv` line 16110, `data/raw/madin_taxa.tsv` line 18513, and `data/raw/bactotraits_taxa.tsv` line 4170 | Supported exactly by two MediaDive media, six GOLD organisms, one Madin trait assertion, and one BactoTraits trait assertion. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 1591 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Abyssicoccus parent, root-first bacterial lineage, genetic code `11`, the exact synonym `Auricoccus indicus`, and five related synonyms.
- LPSN supplies the validly published legitimate correct-name nomenclature block, type strain `DSM-29158`, DOI/PMID publication identifiers, `INSDC:KT935587`, `lpsn:794216`, the `GTDB:s__Abyssicoccus_albus` bridge, and the synonymized `Auricoccus indicus` name.
- GTDB contributes four close-match genomes via `GTDB:s__Abyssicoccus_albus`.
- BacDive contributes two local strains. The DSM 29158 strain is enriched with BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, StrainInfo, and ATB assembly/genome/sample links; the S31 strain carries the complete BacDive INSDC assembly and IMG/PATRIC genome records plus StrainInfo deposit and strain overlays.
- MediaDive, GOLD, Madin et al., and BactoTraits same-taxon count rows are all represented in `source_attestations`.
- No same-taxon curator-added `causal_graphs` are expected or present.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
