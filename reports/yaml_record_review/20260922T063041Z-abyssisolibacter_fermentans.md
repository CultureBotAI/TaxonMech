# YAML Record Review: Abyssisolibacter fermentans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssisolibacter_fermentans.yaml
- Started UTC: 2026-09-22T06:29:20Z
- Finished UTC: 2026-09-22T06:30:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1766203 |
| label | Abyssisolibacter fermentans |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2683336 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abyssisolibacter_fermentans.yaml`. It combines NCBITaxon identity and synonyms, the validly published LPSN name, a single GTDB close match, a GOLD count, one BacDive-derived type strain with one medium, and BacDive genome accessions.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 268200 maps `NCBITaxon:1766203` to slug `abyssisolibacter_fermentans`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssisolibacter_fermentans.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssisolibacter_fermentans.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssisolibacter_fermentans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 461608 has `NCBITaxon:1766203`, label `Abyssisolibacter fermentans`, rank `SPECIES`, direct parent `NCBITaxon:2683336`, genetic code `11`, the expected three NCBI related synonyms, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:186801` Clostridia, `CLASS` | line 37029 |
| `NCBITaxon:186802` Eubacteriales, `ORDER` | line 37030 |
| `NCBITaxon:31979` Clostridiaceae, `FAMILY` | line 3375 |
| `NCBITaxon:2683336` Abyssisolibacter, `GENUS` | line 543366 |

`curation/seed_scope.tsv` line 16314 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 461608 | Supported exactly. |
| LPSN nomenclature block, xref, type designations, publications, and sequence accession | `data/raw/lpsn_names.tsv` line 8876 | Supported exactly by `lpsn:55696`; LPSN also supplies `GTDB:s__Abyssisolibacter_fermentans` for the close match note. |
| GTDB mapping and genome count | `data/raw/gtdb_mappings.tsv` line 55655 and `data/raw/gtdb_species.tsv` line 2829 | Supported exactly: `GTDB:s__Abyssisolibacter_fermentans` maps to `NCBITaxon:1766203` by `skos:closeMatch` with one genome. |
| BacDive type strain, culture collection IDs, and medium count | `data/raw/bacdive_strains.tsv` line 86292 and `data/raw/culture_collection_strains.tsv` lines 107289 and 116377 | Supported; BacDive provides id `164056`, the two YAML culture IDs, and one medium. |
| BacDive genome assembly and external genome records | `data/raw/strain_assemblies.tsv` line 77598 and `data/raw/strain_genome_records.tsv` lines 60263-60264 | Supported exactly for the contig-level INSDC, IMG, and PATRIC/BV-BRC records. |
| NCBI type-material evidence | `data/raw/ncbi_type_material.tsv` lines 57873-57880 | Supported by the committed type-strain spelling variants for `JCM 31420`, `KCTC 15524`, and `MCWD3`. |
| GOLD organism count | `data/raw/gold_organisms.tsv` line 15389 | Supported exactly by a count of one. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 16314 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct Abyssisolibacter parent, root-first bacterial lineage, genetic code `11`, and three related synonyms.
- LPSN supplies the validly published legitimate correct-name nomenclature block, type strains `JCM-31420` and `KCTC-15524`, DOI/PMID publication identifiers, `INSDC:KU510224`, `lpsn:55696`, and the GTDB close-match bridge.
- GTDB contributes one close-match genome via `GTDB:s__Abyssisolibacter_fermentans`.
- BacDive supplies one type strain with `medium_count: 1`, assembly `ncbi.assembly:GCA_001559865`, IMG genome `img.taxon:2684622596`, and PATRIC/BV-BRC genome `patric:1766203.5`; an exact gzip scan of `data/straininfo/related_records.tsv.gz` returned no BacDive-local related-record overlay rows for this strain.
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
