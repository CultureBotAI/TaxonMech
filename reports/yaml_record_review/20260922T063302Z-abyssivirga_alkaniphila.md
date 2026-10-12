# YAML Record Review: Abyssivirga alkaniphila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssivirga_alkaniphila.yaml
- Started UTC: 2026-09-22T06:31:35Z
- Finished UTC: 2026-09-22T06:33:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1675854 |
| label | Abyssivirga alkaniphila |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:1792300 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssivirga_alkaniphila.yaml`. It combines NCBITaxon identity, a deprecated but validly published LPSN name synonymized to `Vallitalea guaymasensis`, one BacDive-derived type strain, MediaDive, GOLD, BactoTraits, and StrainInfo overlays.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 242998 maps `NCBITaxon:1675854` to slug `abyssivirga_alkaniphila`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssivirga_alkaniphila.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssivirga_alkaniphila.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssivirga_alkaniphila.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 437260 has `NCBITaxon:1675854`, label `Abyssivirga alkaniphila`, rank `SPECIES`, direct parent `NCBITaxon:1792300`, genetic code `11`, related synonyms `Abyssivirga alkaniphila Schouw et al. 2016` and `Defluviitaleaceae bacterium L81`, source set `ncbitaxon|bacdive|lpsn|mediadive|gold|bactotraits`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:186801` Clostridia, `CLASS` | line 37029 |
| `NCBITaxon:3085636` Lachnospirales, `ORDER` | line 596686 |
| `NCBITaxon:2603322` Vallitaleaceae, `FAMILY` | line 535867 |
| `NCBITaxon:1792300` Abyssivirga, `GENUS` | line 465957 |

`curation/seed_scope.tsv` line 12644 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 437260 | Supported exactly. |
| Deprecated LPSN nomenclature block and Vallitalea synonym target | `data/raw/lpsn_names.tsv` lines 30611 and 27884 | Supported: `lpsn:794021` names `NCBITaxon:1675854`, marks the name deprecated and not the correct name, and points to correct-name `lpsn:790983` for `Vallitalea guaymasensis`. |
| BacDive type strain and culture collection IDs | `data/raw/bacdive_strains.tsv` line 54789 and `data/raw/culture_collection_strains.tsv` lines 76014 and 106899 | Supported; BacDive provides strain `L81`, BacDive id `132478`, and the two YAML culture IDs for this taxon. |
| Synonym-routed BacDive, BV-BRC, and GOLD assemblies and genome records | `data/raw/strain_assemblies.tsv` lines 24754-24756 and `data/raw/strain_genome_records.tsv` lines 19746-19749 | Supported; these matched rows are for the same BacDive-local strain but carry `Vallitalea guaymasensis` and `NCBITaxon:1185412` from the LPSN-correct-name side of the synonymy. |
| Related records | `data/raw/strain_related_records.tsv` lines 68887-68897 plus an exact gzip scan of `data/straininfo/related_records.tsv.gz` | Supported exactly for the BV-BRC, GOLD, and StrainInfo BioProject/BioSample/GOLD/deposit/strain records. |
| NCBI type-material evidence | `data/raw/ncbi_type_material.tsv` lines 51375-51380 | Supported by the committed type-strain spelling variants for `DSM 29592`, `JCM 30920`, and `L81`. |
| MediaDive, GOLD, and BactoTraits source counts | `data/raw/mediadive_taxa.tsv` line 4839, `data/raw/gold_organisms.tsv` line 14438, and `data/raw/bactotraits_taxa.tsv` line 3791 | Supported exactly by two MediaDive media, three GOLD organisms, and 24 BactoTraits trait assertions. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 12644 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Abyssivirga parent, root-first bacterial lineage, genetic code `11`, and two related synonyms.
- LPSN supplies the deprecated-but-validly-published `lpsn:794021` name, its type strain designations, DOI/PMID publication identifiers, `INSDC:KP233895`, and a synonym link to the correct `Vallitalea guaymasensis` name.
- BacDive contributes one type strain with culture collection IDs `DSM-29592` and `JCM-30920`.
- The strain is enriched with BacDive, BV-BRC, GOLD, and StrainInfo assembly/genome/related-record rows, including synonym-routed rows that use `Vallitalea guaymasensis` and `NCBITaxon:1185412`.
- MediaDive, GOLD, and BactoTraits same-taxon count rows are all represented in `source_attestations`.
- No same-taxon GTDB mapping, Madin et al. row, ATB overlap, or curator-added `causal_graphs` are expected or present.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
