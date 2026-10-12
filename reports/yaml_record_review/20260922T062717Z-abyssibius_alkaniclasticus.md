# YAML Record Review: Abyssibius alkaniclasticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssibius_alkaniclasticus.yaml
- Started UTC: 2026-09-22T06:25:30Z
- Finished UTC: 2026-09-22T06:27:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2881234 |
| label | Abyssibius alkaniclasticus |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:3029205 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssibius_alkaniclasticus.yaml`. It combines NCBITaxon identity and synonyms, the validly published LPSN name, a single GTDB close match, one GOLD count, and one BacDive-derived type strain without source-provided genome or StrainInfo overlays.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 388004 maps `NCBITaxon:2881234` to slug `abyssibius_alkaniclasticus`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssibius_alkaniclasticus.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssibius_alkaniclasticus.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssibius_alkaniclasticus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 567209 has `NCBITaxon:2881234`, label `Abyssibius alkaniclasticus`, rank `SPECIES`, direct parent `NCBITaxon:3029205`, genetic code `11`, NCBI synonyms `Abyssibius alkaniclasticus Wei et al. 2023` and `Rhodobacteraceae bacterium 960558`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:28211` Alphaproteobacteria, `CLASS` | line 2912 |
| `NCBITaxon:204455` Rhodobacterales, `ORDER` | line 40377 |
| `NCBITaxon:31989` Paracoccaceae, `FAMILY` | line 3384 |
| `NCBITaxon:3029205` Abyssibius, `GENUS` | line 587247 |

`curation/seed_scope.tsv` line 19705 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 567209 | Supported exactly. |
| LPSN nomenclature block, xref, type designation, publications, and sequence accession | `data/raw/lpsn_names.tsv` line 6298 | Supported exactly by `lpsn:36886`; LPSN also supplies `GTDB:s__Abyssibius_alkaniclasticus` for the close match note. |
| GTDB mapping and genome count | `data/raw/gtdb_mappings.tsv` line 228774 and `data/raw/gtdb_species.tsv` line 2826 | Supported exactly: `GTDB:s__Abyssibius_alkaniclasticus` maps to `NCBITaxon:2881234` by `skos:closeMatch` with two genomes. |
| BacDive type strain and culture collection IDs | `data/raw/bacdive_strains.tsv` line 92906 and `data/raw/culture_collection_strains.tsv` lines 121466 and 130817 | Supported; BacDive provides strain `960558`, BacDive id `170673`, and the two YAML culture IDs for this taxon. |
| NCBI type-material evidence | `data/raw/ncbi_type_material.tsv` lines 135744-135753 | Supported by the committed type-strain spelling variants for `KCTC 82619`, `MCCC 1K04727`, and `960558`. |
| GOLD organism count | `data/raw/gold_organisms.tsv` line 28051 | Supported exactly by a count of one. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 19705 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Abyssibius parent, root-first bacterial lineage, genetic code `11`, and two related synonyms.
- LPSN supplies the validly published legitimate correct-name nomenclature block, type strain `KCTC-82619`, DOI/PMID publication identifiers, `INSDC:OK489460`, `lpsn:36886`, and the GTDB close-match bridge.
- GTDB contributes two close-match genomes via `GTDB:s__Abyssibius_alkaniclasticus`.
- BacDive supplies one type strain with two culture collection IDs and no BacDive genome rows; an exact gzip scan of `data/straininfo/related_records.tsv.gz` returned no BacDive-local related-record overlay rows for this strain.
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
