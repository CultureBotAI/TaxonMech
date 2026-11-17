# YAML Record Review: Abiotrophia defectiva

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abiotrophia_defectiva.yaml
- Started UTC: 2026-09-22T04:31:24Z
- Finished UTC: 2026-09-22T04:33:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:46125 |
| label | Abiotrophia defectiva |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:46123 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abiotrophia_defectiva.yaml`. It carries LPSN nomenclature, two pooled GTDB `skos:broadMatch` mappings, four synonyms, a close LPSN xref, the close LPSN-linked GTDB xref, 39 local strain entries, 21 generated assembly rows, 16 generated genome rows, 185 generated related-record rows, no causal graphs, and source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, GOLD, and MADIN.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 511299 maps `NCBITaxon:46125` to slug `abiotrophia_defectiva`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abiotrophia_defectiva.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abiotrophia_defectiva.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abiotrophia_defectiva.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 5773 has `NCBITaxon:46125`, label `Abiotrophia defectiva`, rank `SPECIES`, direct parent `NCBITaxon:46123`, genetic code `11`, the NCBI exact synonym `Streptococcus defectivus`, the two NCBI related synonyms represented in YAML, source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:91061` Bacilli, `CLASS` | line 14761 |
| `NCBITaxon:186826` Lactobacillales, `ORDER` | line 37043 |
| `NCBITaxon:186827` Aerococcaceae, `FAMILY` | line 37044 |
| `NCBITaxon:46123` Abiotrophia, `GENUS` | line 5771 |

`curation/seed_scope.tsv` line 8423 keeps this taxon in scope through the attested-source rule.

`data/raw/lpsn_names.tsv` line 14787 supports `lpsn:772468` as the correct species name with the authority `(Bouvet et al. 1989) Kawamura et al. 1995`, its `NCBITaxon:46125` and `GTDB:s__Abiotrophia_defectiva` cross-references, six type-strain designations, PMID/DOI publications, and INSDC accession `D50541`. The synonym `Streptococcus defectivus` is backed both by that row's synonym fields and the LPSN synonym row at line 20078.

`data/raw/gtdb_mappings.tsv` lines 291088-291089 map `GTDB:s__Abiotrophia_defectiva` and `GTDB:s__Abiotrophia_defectiva_A` to `NCBITaxon:46125` with `skos:broadMatch`; their GTDB species rows are `data/raw/gtdb_species.tsv` lines 2807-2808.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 5773 | Supported exactly. |
| LPSN correct-name nomenclature and synonym | `data/raw/lpsn_names.tsv` lines 14787 and 20078 | Supported exactly. |
| Two GTDB broad mappings | `data/raw/gtdb_mappings.tsv` lines 291088-291089 and `data/raw/gtdb_species.tsv` lines 2807-2808 | Supported with 25 total GTDB genomes pooled onto this taxon. |
| BacDive strain aggregate | Structured parse of the YAML plus exact `kgmicrobe.strain:bacdive_219` source checks | Supported; the generated YAML has 39 strain entries and includes the BacDive 219 strain that is filed under descendant `NCBITaxon:592010` via `classified_as`. |
| GOLD and MADIN source attestations | `data/raw/gold_organisms.tsv` line 36217 and `data/raw/madin_taxa.tsv` line 24750 | Supported with 50 GOLD organisms and 3 Madin trait assertions filed directly under `NCBITaxon:46125`. |
| Strain assembly, genome, related-record, StrainInfo, and ATB overlays | Exact gitignore-independent scans for `kgmicrobe.strain:bacdive_219` across `data/raw/strain_*`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` | Supported; BacDive 219 alone contributes 19 raw assembly rows, 15 raw genome rows, 39 raw related-record rows, 2 StrainInfo assembly rows, 4 StrainInfo deposit links, 1 ATB strain link, and 3 ATB genome links. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 511299 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 8423 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct genus parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- LPSN supplies the validly published correct name, its `Streptococcus defectivus` synonym, type-strain designations, DOI/PMID publication references, and the INSDC sequence accession.
- GTDB supplies two broad species mappings; `s__Abiotrophia_defectiva` is also LPSN-linked but is still broad at the NCBI mapping layer because the GTDB species pool spans child strain labels as well as this NCBI species.
- BacDive, GOLD, StrainInfo, AllTheBacteria, and assembly source rows generate the expected large strain/genome/related-record block under this species, including one BacDive row classified under the descendant ATCC 49176 strain.
- MADIN contributes direct trait assertions represented as a source attestation.
- With no curator-added `causal_graphs`, the optional causal-graph section is correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
