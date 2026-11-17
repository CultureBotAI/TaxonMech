# YAML Record Review: Abyssalbus ytuae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssalbus_ytuae.yaml
- Started UTC: 2026-09-22T06:23:00Z
- Finished UTC: 2026-09-22T06:25:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2926907 |
| label | Abyssalbus ytuae |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2967089 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssalbus_ytuae.yaml`. It combines NCBITaxon identity and synonyms, the validly published LPSN name, a single GTDB close match, a GOLD count, one BacDive-derived type strain, and BacDive genome accessions.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 393566 maps `NCBITaxon:2926907` to slug `abyssalbus_ytuae`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssalbus_ytuae.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssalbus_ytuae.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssalbus_ytuae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 572775 has `NCBITaxon:2926907`, label `Abyssalbus ytuae`, rank `SPECIES`, direct parent `NCBITaxon:2967089`, genetic code `11`, NCBI synonyms `Abyssalbus ytuae Xu et al. 2022` and `Flavobacteriaceae bacterium MT3330`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1783270` FCB group, `CLADE` | line 464833 |
| `NCBITaxon:68336` Bacteroidota/Chlorobiota group, `CLADE` | line 9325 |
| `NCBITaxon:976` Bacteroidota, `PHYLUM` | line 754 |
| `NCBITaxon:117743` Flavobacteriia, `CLASS` | line 22021 |
| `NCBITaxon:200644` Flavobacteriales, `ORDER` | line 39661 |
| `NCBITaxon:49546` Flavobacteriaceae, `FAMILY` | line 6293 |
| `NCBITaxon:2967089` Abyssalbus, `GENUS` | line 579884 |

`curation/seed_scope.tsv` line 19992 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 572775 | Supported exactly. |
| LPSN nomenclature block, xref, type designation, publications, and sequence accession | `data/raw/lpsn_names.tsv` line 5421 | Supported exactly by `lpsn:29444`; LPSN also supplies `GTDB:s__Abyssalbus_ytuae` for the close match note. |
| GTDB mapping and genome count | `data/raw/gtdb_mappings.tsv` line 235100 and `data/raw/gtdb_species.tsv` line 2821 | Supported exactly: `GTDB:s__Abyssalbus_ytuae` maps to `NCBITaxon:2926907` by `skos:closeMatch` with one genome. |
| BacDive type strain and culture collection IDs | `data/raw/bacdive_strains.tsv` line 92416 and `data/raw/culture_collection_strains.tsv` lines 121533 and 130879 | Supported; BacDive provides strain `MT3330`, BacDive id `170183`, and the two YAML culture IDs for this taxon. |
| BacDive genome assembly and external genome records | `data/raw/strain_assemblies.tsv` line 92795 and `data/raw/strain_genome_records.tsv` lines 74718-74719 | Supported exactly for the complete INSDC, IMG, and PATRIC/BV-BRC records. |
| NCBI type-material evidence | `data/raw/ncbi_type_material.tsv` lines 142146-142155 | Supported by the committed type-strain spelling variants for `KCTC 82823`, `MCCC 1K06012`, and `MT3330`. |
| GOLD organism count | `data/raw/gold_organisms.tsv` line 28797 | Supported exactly by a count of one. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 19992 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Abyssalbus parent, root-first bacterial lineage, genetic code `11`, and two related synonyms.
- LPSN supplies the validly published legitimate correct-name nomenclature block, type strain `KCTC-82823`, DOI/PMID publication identifiers, `INSDC:ON495953`, `lpsn:29444`, and the GTDB close-match bridge.
- GTDB contributes one close-match genome via `GTDB:s__Abyssalbus_ytuae`.
- BacDive supplies one local strain with assembly `ncbi.assembly:GCA_022807975`, IMG genome `img.taxon:8074039445`, and PATRIC/BV-BRC genome `patric:2926907.3`; an exact gzip scan of `data/straininfo/related_records.tsv.gz` returned no BacDive-local related-record overlay rows for this strain.
- GOLD contributes one same-taxon organism count.
- No same-taxon MediaDive, Madin et al., BactoTraits, ATB, or StrainInfo overlay rows were present in the exact gitignore-independent source scans, and there are no curator-added `causal_graphs`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
