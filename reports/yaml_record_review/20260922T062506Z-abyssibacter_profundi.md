# YAML Record Review: Abyssibacter profundi

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssibacter_profundi.yaml
- Started UTC: 2026-09-22T06:23:00Z
- Finished UTC: 2026-09-22T06:25:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2182787 |
| label | Abyssibacter profundi |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2320199 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssibacter_profundi.yaml`. It combines NCBITaxon identity and synonyms, the validly published LPSN name, a single GTDB close match, a GOLD count, one BacDive-derived type strain with one medium, and BacDive genome accessions.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 332514 maps `NCBITaxon:2182787` to slug `abyssibacter_profundi`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssibacter_profundi.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssibacter_profundi.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssibacter_profundi.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 520977 has `NCBITaxon:2182787`, label `Abyssibacter profundi`, rank `SPECIES`, direct parent `NCBITaxon:2320199`, genetic code `11`, NCBI synonyms `Abyssibacter profundi Zhou et al. 2018` and `Salinisphaeraceae bacterium OUC007`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:1236` Gammaproteobacteria, `CLASS` | line 952 |
| `NCBITaxon:135613` Chromatiales, `ORDER` | line 27091 |
| `NCBITaxon:3103149` Oceanococcaceae, `FAMILY` | line 598809 |
| `NCBITaxon:2320199` Abyssibacter, `GENUS` | line 524944 |

`curation/seed_scope.tsv` line 17270 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 520977 | Supported exactly. |
| LPSN nomenclature block, xref, type designation, publications, and sequence accession | `data/raw/lpsn_names.tsv` line 33070 | Supported exactly by `lpsn:797925`; LPSN also supplies `GTDB:s__Abyssibacter_profundi` for the close match note. |
| GTDB mapping and genome count | `data/raw/gtdb_mappings.tsv` line 171414 and `data/raw/gtdb_species.tsv` line 2822 | Supported exactly: `GTDB:s__Abyssibacter_profundi` maps to `NCBITaxon:2182787` by `skos:closeMatch` with two genomes. |
| BacDive type strain, culture collection IDs, and medium count | `data/raw/bacdive_strains.tsv` line 82074 and `data/raw/culture_collection_strains.tsv` lines 107742, 120365, and 130608 | Supported; BacDive provides strain `OUC007`, BacDive id `159837`, all three YAML culture IDs, and one medium. |
| BacDive genome assembly and external genome records | `data/raw/strain_assemblies.tsv` line 69040 and `data/raw/strain_genome_records.tsv` lines 53722-53723 | Supported exactly for the contig-level INSDC, IMG, and PATRIC/BV-BRC records. |
| NCBI type-material evidence | `data/raw/ncbi_type_material.tsv` lines 87181-87186 | Supported by the committed type-strain spelling variants for `KCTC 52933`, `MCCC 1K03450`, and `OUC007`. |
| GOLD organism count | `data/raw/gold_organisms.tsv` line 20794 | Supported exactly by a count of one. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 17270 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Abyssibacter parent, root-first bacterial lineage, genetic code `11`, and two related synonyms.
- LPSN supplies the validly published legitimate correct-name nomenclature block, type strain `KCTC-52933`, DOI/PMID publication identifiers, `INSDC:KY612316`, `lpsn:797925`, and the GTDB close-match bridge.
- GTDB contributes two close-match genomes via `GTDB:s__Abyssibacter_profundi`.
- BacDive supplies one local strain with `medium_count: 1`, assembly `ncbi.assembly:GCA_003151135`, IMG genome `img.taxon:2831460164`, and PATRIC/BV-BRC genome `patric:2182787.3`; an exact gzip scan of `data/straininfo/related_records.tsv.gz` returned no BacDive-local related-record overlay rows for this strain.
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
