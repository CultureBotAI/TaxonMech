# YAML Record Review: Abiotrophia defectiva ATCC 49176

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abiotrophia_defectiva_atcc_49176.yaml
- Started UTC: 2026-09-22T04:31:24Z
- Finished UTC: 2026-09-22T04:33:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:592010 |
| label | Abiotrophia defectiva ATCC 49176 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:46125 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial strain record at `data/taxa/bacteria/abiotrophia_defectiva_atcc_49176.yaml`. It carries two NCBI exact synonyms, two pooled GTDB `skos:broadMatch` mappings, one BacDive-derived local strain with 21 assembly rows, 16 genome rows, 54 related records, no causal graphs, and source attestations from NCBITAXON, GTDB, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 549369 maps `NCBITaxon:592010` to slug `abiotrophia_defectiva_atcc_49176`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abiotrophia_defectiva_atcc_49176.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abiotrophia_defectiva_atcc_49176.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abiotrophia_defectiva_atcc_49176.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 140365 has `NCBITaxon:592010`, label `Abiotrophia defectiva ATCC 49176`, rank `STRAIN`, direct parent `NCBITaxon:46125`, genetic code `11`, exact synonyms `Abiotrophia defectiva str. ATCC 49176` and `Abiotrophia defectiva strain ATCC 49176`, source set `ncbitaxon|gtdb|bacdive|mediadive|madin_etal|bactotraits`, and snapshot date `2026-09-13`.

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
| `NCBITaxon:46125` Abiotrophia defectiva, `SPECIES` | line 5773 |

`curation/seed_scope.tsv` line 14557 keeps this taxon in scope through the attested-source rule.

`data/raw/gtdb_mappings.tsv` lines 298060-298061 map `GTDB:s__Abiotrophia_defectiva` and `GTDB:s__Abiotrophia_sp001815865` to `NCBITaxon:592010` with `skos:broadMatch`; their GTDB species rows are `data/raw/gtdb_species.tsv` lines 2807 and 2809.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, exact synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 140365 | Supported exactly. |
| Two GTDB broad mappings | `data/raw/gtdb_mappings.tsv` lines 298060-298061 and `data/raw/gtdb_species.tsv` lines 2807 and 2809 | Supported with 45 total GTDB genomes pooled onto this strain taxon. |
| BacDive local strain | `data/raw/bacdive_strains.tsv` line 219 | Supported; BacDive 219 is filed under `NCBITaxon:592010`, carries the LPSN `lpsn:772468` cross-reference, and records ATCC 49176, CCUG 27639, CIP 103242, DSM 9849, and SC 10 culture IDs. |
| MediaDive, Madin, and BactoTraits source attestations | `data/raw/mediadive_taxa.tsv` line 11871, `data/raw/madin_taxa.tsv` line 27594, and `data/raw/bactotraits_taxa.tsv` line 7927 | Supported with one medium, five Madin trait assertions, and two BactoTraits assertions. |
| Assembly, genome, related-record, StrainInfo, and ATB overlays | Exact gitignore-independent scans for `kgmicrobe.strain:bacdive_219` across `data/raw/strain_*`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` | Supported; the generated record correctly keeps original source taxon IDs on rows from ATCC 49176 and parent-species FDAARGOS/StrainInfo evidence. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 549369 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 14557 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the strain identity, direct species parent, root-first bacterial lineage, genetic code `11`, two exact synonyms, and the NCBITAXON source attestation.
- GTDB supplies the two broad species mappings that pool onto this strain label.
- BacDive supplies the local strain anchor, and BV-BRC, GOLD, NCBI Assembly, GTDB, StrainInfo, and AllTheBacteria source rows generate the expected assembly, genome, and related-record blocks.
- MediaDive, Madin et al., and BactoTraits supply the directly filed medium and trait counts represented in `source_attestations`.
- No LPSN nomenclature is expected at this strain rank; the BacDive row's LPSN link correctly points to the parent species nomenclature already modeled on `NCBITaxon:46125`.
- With no curator-added `causal_graphs`, the optional causal-graph section is correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
