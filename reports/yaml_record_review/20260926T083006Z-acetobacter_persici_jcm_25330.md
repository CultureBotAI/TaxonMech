# YAML Record Review: Acetobacter persici JCM 25330

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_persici_jcm_25330.yaml`
- Reviewed UTC: 2026-09-26T08:30:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1236503` |
| label | `Acetobacter persici JCM 25330` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:1076596` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter persici`. It has source attestations from NCBITAXON, GTDB, BACDIVE, and GOLD; one GTDB `skos:closeMatch`; four NCBITaxon exact synonyms; one BacDive type-strain row with five culture collection identifiers; 10 generated genome assemblies; 6 generated genome records; 29 generated related records; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 79882 maps `NCBITaxon:1236503` to `acetobacter_persici_jcm_25330`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_persici_jcm_25330.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_persici_jcm_25330.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_peroxydans.yaml data/taxa/bacteria/acetobacter_peroxydans_nbrc_13755.yaml data/taxa/bacteria/acetobacter_persici.yaml data/taxa/bacteria/acetobacter_persici_jcm_25330.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 283203 has `NCBITaxon:1236503`, label `Acetobacter persici JCM 25330`, rank `STRAIN`, parent `NCBITaxon:1076596`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive|gold`, four exact synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 22379 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, snapshot date, and exact synonyms | `data/raw/ncbitaxon_taxa.tsv` line 283203 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 79882 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 22379 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` line 13571 | Supported exactly by one 16-genome `skos:closeMatch` to `GTDB:s__Acetobacter_persici`. |
| BacDive strain, culture IDs, assemblies, genome records, and related crosslinks | `data/raw/bacdive_strains.tsv` line 85573, culture-collection rows for BacDive 163337, raw strain rows, and matched StrainInfo deposit rows | Supported; BacDive 163337 supplies the direct type strain and its five culture collection identifiers. |
| GOLD source attestation | `data/raw/gold_organisms.tsv` line 5665 and native GOLD organism/project rows | Supported; the processed aggregate has one exact organism, while native GOLD has exact `Go0044398` and `Go0091940` organisms and project `Gp0091940`. |
| Empty auxiliary evidence | Exact scans of LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, and direct StrainInfo target surfaces for `NCBITaxon:1236503` | Supported; no committed auxiliary row directly names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter persici` parent, the exact 10-ancestor lineage, and four exact synonyms.
- GTDB supplies the only taxonomy mapping as `skos:closeMatch`.
- BacDive 163337 supplies the exact same-taxon type-strain evidence and five culture collection identifiers.
- GOLD supplies one processed organism aggregate for the strain, and the native GOLD snapshot contains both JCM 25330 and LMG 26458 organism names for the same BacDive culture-deposit cluster.
- StrainInfo rows in the YAML are scoped through BacDive culture deposit matches rather than direct `NCBITaxon:1236503` target rows.
- No exact same-taxon LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, or direct StrainInfo target row exists in the committed processed inventories, and no curator-added `causal_graphs` or definitions are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The generated genome and related-record sections mix raw rows keyed directly to `NCBITaxon:1236503` with deposit-matched rows from the parent species context; the source provenance keeps those support paths explicit.
