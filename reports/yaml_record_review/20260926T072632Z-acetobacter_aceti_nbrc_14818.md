# YAML Record Review: Acetobacter aceti NBRC 14818

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_aceti_nbrc_14818.yaml`
- Reviewed UTC: 2026-09-26T07:26:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:887700` |
| label | `Acetobacter aceti NBRC 14818` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:435` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter aceti` with source attestations from NCBITAXON, GTDB, GOLD, BACDIVE, MEDIADIVE, MADIN, and BACTOTRAITS. The YAML contains one GTDB `skos:closeMatch`, eight exact synonyms, one GTDB xref, one BacDive-derived local strain, 23 culture collection IDs, 27 genome assemblies, 17 genome records, 137 related records, and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 603423 maps `NCBITaxon:887700` to `acetobacter_aceti_nbrc_14818`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_aceti_nbrc_14818.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_aceti_nbrc_14818.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_aceti_1023.yaml data/taxa/bacteria/acetobacter_aceti_atcc_23746.yaml data/taxa/bacteria/acetobacter_aceti_nbrc_14818.yaml data/taxa/bacteria/acetobacter_aceti_nric_0242.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 188931 has `NCBITaxon:887700`, label `Acetobacter aceti NBRC 14818`, rank `STRAIN`, parent `NCBITaxon:435`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|mediadive|gold|madin_etal|bactotraits`, seven exact NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 11 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 11 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 7061 keeps the strain in scope. The exact same-taxon auxiliary rows are `data/raw/gtdb_mappings.tsv` line 316873, `data/raw/gold_organisms.tsv` line 43915, `data/raw/bactotraits_taxa.tsv` line 9277, `data/raw/mediadive_taxa.tsv` line 13717, and `data/raw/madin_taxa.tsv` line 32126.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, seven exact synonyms, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 188931 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 603423 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 7061 | Supported exactly by a single seed-scope row. |
| Lineage | 11 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 316873 | Supported exactly by one 7-genome `skos:closeMatch` to `GTDB:s__Acetobacter_aceti`. |
| BacDive strain identity and culture IDs | `data/raw/bacdive_strains.tsv` line 3 and 23 `data/raw/culture_collection_strains.tsv` rows keyed to `NCBITaxon:887700` | Supported; BacDive record 2 carries the generated `kgmicrobe.strain:bacdive_2` strain and 23 normalized culture collection IDs. |
| GOLD organism count and GOLD project evidence | `data/raw/gold_organisms.tsv` line 43915 plus exact native GOLD scans | Supported; the processed aggregate has `organism_count=1`, and the native GOLD tables contain 2 organism rows, 2 project rows, and 2 analysis rows for this taxon. |
| Genome and related-record evidence | Exact scans of `data/raw/strain_assemblies.tsv` and `data/raw/strain_genome_records.tsv` and `data/raw/strain_related_records.tsv` for `NCBITaxon:887700` | Supported; 23 raw assemblies, 16 raw genome records, and 45 raw related records contribute to the generated BacDive strain block. |
| BactoTraits, MediaDive, and Madin et al. attestations | `data/raw/bactotraits_taxa.tsv` line 9277, `data/raw/mediadive_taxa.tsv` line 13717, and `data/raw/madin_taxa.tsv` line 32126 | Supported exactly with 1 BactoTraits assertion, 3 MediaDive media IDs, and 2 Madin et al. assertions. |
| Empty same-taxon LPSN, StrainInfo, NCBI type-material, and NCBI merged-id surfaces | Exact scans for `NCBITaxon:887700` | Supported; no committed LPSN, StrainInfo overlay, NCBI type-material, or merged-old-ID row names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, seven exact synonyms, the direct `Acetobacter aceti` parent, and the root-first 11-ancestor lineage.
- GTDB supplies the only taxonomy mapping, one exact GTDB synonym, one xref, and a GENOME source attestation.
- BacDive supplies the canonical local strain, and the culture-collection table contributes the 23 normalized culture IDs attached to that strain.
- GOLD, BV-BRC, GTDB, NCBI Assembly, BacDive, and AllTheBacteria rows resolve onto the single generated BacDive 2 strain block.
- BactoTraits, MediaDive, and Madin et al. each supply one aggregate source attestation for the strain.
- No exact LPSN name, StrainInfo overlay, NCBI type-material, NCBI merged-id evidence, generated definition, or curator-added causal graph is present for this strain identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The native GOLD rows include both NBRC 14818 and DSM 3508 organism/project pairs for `NCBITaxon:887700`; the generated local strain block normalizes them through the shared BacDive 2 culture collection identity.
