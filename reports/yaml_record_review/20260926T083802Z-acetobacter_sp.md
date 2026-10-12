# YAML Record Review: Acetobacter sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_sp.yaml`
- Reviewed UTC: 2026-09-26T08:38:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:440` |
| label | `Acetobacter sp.` |
| rank | `SPECIES` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:2628570` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated placeholder NCBI species record under `unclassified Acetobacter`. It has source attestations from NCBITAXON, GTDB, BACDIVE, and MEDIADIVE; 19 GTDB `skos:broadMatch` mappings; five BacDive strain rows with 10 culture collection identifiers; 21 generated related records; and no LPSN nomenclature, synonyms, xrefs, local genome assemblies, local genome records, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 505328 maps `NCBITaxon:440` to `acetobacter_sp`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_sp.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_sp.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_senegalensis.yaml data/taxa/bacteria/acetobacter_senegalensis_dsm_18889.yaml data/taxa/bacteria/acetobacter_sicerae.yaml data/taxa/bacteria/acetobacter_sp.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 334 has `NCBITaxon:440`, label `Acetobacter sp.`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 29948 keeps the species in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, species rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 334 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 505328 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 29948 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mappings | 19 `data/raw/gtdb_mappings.tsv` rows beginning at line 289544 | Supported exactly; all 19 rows are pooled `skos:broadMatch` mappings from this broad NCBI placeholder into GTDB species clusters. |
| BacDive strains and culture IDs | `data/raw/bacdive_strains.tsv` lines 53890, 71124, 79501, 85333, and 85334 plus 10 culture-collection rows | Supported; the five exact BacDive rows are source strains 131579, 148860, 157262, 163097, and 163098. |
| MediaDive attestation | `data/raw/mediadive_taxa.tsv` line 10241 | Supported exactly by one direct MediaDive medium assertion. |
| Empty genome evidence | Exact scans of `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, native GOLD, processed GOLD aggregate, and direct StrainInfo target surfaces for `NCBITaxon:440` | Supported; no committed same-taxon row names assemblies, genome records, GOLD organisms, or StrainInfo evidence for this placeholder species. |
| Empty nomenclatural evidence | Exact scans of LPSN, Madin et al., BactoTraits, NCBI type-material, and NCBI merged-ID surfaces for `NCBITaxon:440` | Supported; no committed auxiliary row names this placeholder species. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the species-rank placeholder identity, the `unclassified Acetobacter` parent, and the exact 10-ancestor lineage.
- GTDB supplies 19 broad mappings; the generated record does not present any of those pooled species-level clusters as equivalence to this broad NCBI placeholder.
- BacDive supplies five exact strain rows with 10 culture collection identifiers.
- MediaDive supplies one direct medium assertion.
- The generated `strain_count: 5` matches the five BacDive rows keyed to `NCBITaxon:440`.
- There are no same-taxon raw assembly, genome-record, related-record, native GOLD, processed GOLD, direct StrainInfo, LPSN, Madin et al., BactoTraits, type-material, or merged-ID rows in the committed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

Several related records under the five BacDive rows point to StrainInfo or GOLD identifiers whose own source taxon differs from `NCBITaxon:440`; those rows are deposit-level crosslinks from the BacDive culture identifiers and are not presented as direct source attestations for `Acetobacter sp.`.
