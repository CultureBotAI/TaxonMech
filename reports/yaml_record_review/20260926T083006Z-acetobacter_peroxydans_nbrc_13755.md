# YAML Record Review: Acetobacter peroxydans NBRC 13755

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_peroxydans_nbrc_13755.yaml`
- Reviewed UTC: 2026-09-26T08:30:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1307915` |
| label | `Acetobacter peroxydans NBRC 13755` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:104098` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a compact generated strain record under `Acetobacter peroxydans`. It has source attestations from NCBITAXON and GTDB; one GTDB `skos:closeMatch`; two exact synonyms from NCBI and GTDB; and no generated local strains, genome assemblies, genome records, related records, LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 107660 maps `NCBITaxon:1307915` to `acetobacter_peroxydans_nbrc_13755`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_peroxydans_nbrc_13755.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_peroxydans_nbrc_13755.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_peroxydans.yaml data/taxa/bacteria/acetobacter_peroxydans_nbrc_13755.yaml data/taxa/bacteria/acetobacter_persici.yaml data/taxa/bacteria/acetobacter_persici_jcm_25330.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 309518 has `NCBITaxon:1307915`, label `Acetobacter peroxydans NBRC 13755`, rank `STRAIN`, parent `NCBITaxon:104098`, genetic code `11`, source set `ncbitaxon|gtdb`, exact synonym `Acetobacter peroxydans NRIC 0475`, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 67317 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, snapshot date, and exact synonym | `data/raw/ncbitaxon_taxa.tsv` line 309518 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 107660 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 67317 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping and synonym | `data/raw/gtdb_mappings.tsv` line 17794 | Supported exactly by one 18-genome `skos:closeMatch` to `GTDB:s__Acetobacter_peroxydans`. |
| Native GOLD context | `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, `data/gold/analyses.jsonl.gz`, and exact `data/raw/gold_organisms.tsv` scan | Native GOLD has the exact `Go0636236` organism and `Gp0653853`/`Gp0818063` projects for this strain; no processed GOLD aggregate row names the strain, so no GOLD source attestation is generated. |
| Empty auxiliary evidence | Exact scans of BacDive, culture collection, LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, StrainInfo, and processed GOLD aggregate surfaces for `NCBITaxon:1307915` | Supported; no committed processed auxiliary row directly names this strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter peroxydans` parent, the exact 10-ancestor lineage, and one exact synonym.
- GTDB supplies the only taxonomy mapping, one exact synonym, one xref, and the GENOME source attestation.
- Native GOLD contains exact organism/project context, but no processed GOLD aggregate row is keyed to this taxon.
- Raw strain, genome, and related rows keyed through BacDive 24 exist for this child strain, but BacDive 24 is anchored at the species record and this compact child record therefore has no local `strains`, assemblies, genome records, or related records.
- NCBI merged old ID `NCBITaxon:1307916` redirects to this taxon in the raw merge map; the generated YAML does not carry a `retained_old_ids` block for it.
- No exact same-taxon BacDive, culture collection, processed GOLD aggregate, LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, or StrainInfo target row exists in the committed processed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The species-level `Acetobacter peroxydans` record carries the BacDive 24 source row whose culture deposits expand to this strain. Keeping the child strain itself as an NCBI/GTDB-only record is consistent with the generated source anchoring.
