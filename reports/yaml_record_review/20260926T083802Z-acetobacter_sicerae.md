# YAML Record Review: Acetobacter sicerae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_sicerae.yaml`
- Reviewed UTC: 2026-09-26T08:38:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:85325` |
| label | `Acetobacter sicerae` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:434` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated species record under `Acetobacter`. It has source attestations from NCBITAXON, LPSN, GTDB, BACDIVE, and GOLD; one LPSN nomenclature row; one GTDB `skos:closeMatch`; five NCBITaxon related synonyms; two BacDive strain rows and one type strain; seven culture collection identifiers; 9 generated genome assemblies; 7 generated genome records; 49 generated related records; and no definitions or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 593763 maps `NCBITaxon:85325` to `acetobacter_sicerae`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_sicerae.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_sicerae.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_senegalensis.yaml data/taxa/bacteria/acetobacter_senegalensis_dsm_18889.yaml data/taxa/bacteria/acetobacter_sicerae.yaml data/taxa/bacteria/acetobacter_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 13148 has `NCBITaxon:85325`, label `Acetobacter sicerae`, rank `SPECIES`, parent `NCBITaxon:434`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|lpsn|gold`, five related synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 9 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 9 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 13842 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, snapshot date, and related synonyms | `data/raw/ncbitaxon_taxa.tsv` line 13148 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 593763 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 13842 | Supported exactly by a single seed-scope row. |
| Lineage | 9 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| LPSN nomenclature and type strain | `data/raw/lpsn_names.tsv` line 28737 | Supported; LPSN carries this as the correct name, links `GTDB:s__Acetobacter_sicerae`, lists LMG-1531 as the type-strain deposit, and supplies accession `INSDC:AJ419840`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 312427 | Supported exactly by one 2-genome `skos:closeMatch` to `GTDB:s__Acetobacter_sicerae`. |
| BacDive strains, culture IDs, assemblies, genome records, and related records | `data/raw/bacdive_strains.tsv` lines 85326 and 90052, seven culture-collection rows, eight same-taxon assembly rows, six same-taxon genome-record rows, and direct related-record rows | Supported; BacDive 167819 is the LMG 1531 type-strain row with genome links, and BacDive 163090 contributes the LMG 1530 strain row with a MediaDive medium and related deposit records. |
| GOLD source attestation | `data/raw/gold_organisms.tsv` line 43237 and native GOLD organism/project/analysis rows | Supported; GOLD has one processed organism aggregate and one exact native organism/project/analysis chain for LMG 1531. |
| Empty auxiliary evidence | Exact scans of MediaDive, Madin et al., and BactoTraits direct source rows for `NCBITaxon:85325` | Supported; no committed source-attestation row directly keys those auxiliary sources to this species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species identity, direct `Acetobacter` parent, exact 9-ancestor lineage, and five related synonyms.
- LPSN supplies the correct-name nomenclature row, the LMG 1531 type-strain designation, and the `GTDB:s__Acetobacter_sicerae` xref.
- GTDB supplies the only taxonomy mapping as `skos:closeMatch`.
- BacDive supplies two exact strain rows: 167819 for the LMG 1531 type strain and 163090 for the LMG 1530 row.
- GOLD, StrainInfo, NCBI Assembly, BV-BRC, GTDB, and AllTheBacteria rows account for the genome and related-record expansion under the BacDive 167819 row.
- NCBI merged old IDs `NCBITaxon:1392217`, `NCBITaxon:1470152`, and `NCBITaxon:1470154` redirect to this taxon in the raw merge map; the generated YAML does not carry a `retained_old_ids` block for them.
- No exact same-taxon Madin et al. or BactoTraits row exists in the committed inventories, and no curator-added `causal_graphs` or definitions are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The non-type BacDive 163090 row contains only medium and related-record evidence; its absence from `genome_assemblies` and `genome_records` is consistent with the committed strain-genome inventories.
