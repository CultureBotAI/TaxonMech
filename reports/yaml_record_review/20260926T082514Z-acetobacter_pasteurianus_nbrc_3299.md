# YAML Record Review: Acetobacter pasteurianus NBRC 3299

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3299.yaml`
- Reviewed UTC: 2026-09-26T08:25:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1226665` |
| label | `Acetobacter pasteurianus NBRC 3299` |
| rank | `STRAIN` |
| taxon_domain | `BACTERIA` |
| parent_taxon | `NCBITaxon:438` |
| grounding_status | `EXACT` |
| mapping_status | `SEEDED` |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target is a generated strain record under `Acetobacter pasteurianus`. It has source attestations from NCBITAXON, GTDB, and BACDIVE; one BacDive strain with six culture-collection identifiers; eight generated genome assemblies; eight generated genome records, including one AllTheBacteria assembly; 44 generated related records; one GTDB `skos:closeMatch`; one GTDB exact synonym; and no LPSN nomenclature, definitions, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 76110 maps `NCBITaxon:1226665` to `acetobacter_pasteurianus_nbrc_3299`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 ... -name '*-acetobacter_pasteurianus_nbrc_3299.md' ... -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3299.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3284.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_3299.yaml data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus.yaml data/taxa/bacteria/acetobacter_pasteurianus_subsp_pasteurianus_lmg_1262_nbrc_106471.yaml` scanned 4 files with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| History validation | Not rerun; this read-only review does not write a `history/` event. |
| Corpus reproduction | Not rerun for this generated record; the review did not change YAML or generation inputs. |
| Product id-label validation | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 279639 has `NCBITaxon:1226665`, label `Acetobacter pasteurianus NBRC 3299`, rank `STRAIN`, parent `NCBITaxon:438`, genetic code `11`, source set `ncbitaxon|gtdb|bacdive`, no NCBI synonyms, no retired-into redirect, and taxonomy snapshot `2026-09-13`.

The YAML lineage has 10 ancestors and matches the pinned NCBI inventory parent chain exactly; the bounded source scan found 10 checked lineage rows, no missing ancestors, and no mismatched labels, ranks, or parents.

`curation/seed_scope.tsv` line 30376 keeps the strain in scope.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBI identity, label, strain rank, parent, genetic code, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 279639 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 76110 | Supported exactly. |
| Scope rationale | `curation/seed_scope.tsv` line 30376 | Supported exactly by a single seed-scope row. |
| Lineage | 10 NCBI ancestor rows resolved from `data/raw/ncbitaxon_taxa.tsv` | Supported exactly; no ancestor was missing or mismatched. |
| GTDB mapping, exact synonym, and xref | `data/raw/gtdb_mappings.tsv` line 12866 | Supported exactly by one 6-genome `skos:closeMatch` to `GTDB:s__Acetobacter_ascendens`. |
| BacDive strain and deposits | `data/raw/bacdive_strains.tsv` line 58294 and six `data/raw/culture_collection_strains.tsv` rows | Supported exactly for BacDive record 135988, designation `A35`, and the CIP, IAM, IFO, JCM, LMG, and NBRC culture identifiers carried on the generated strain. |
| Genome and related-record links | `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, native GOLD, GTDB, BV-BRC, NCBI assembly, BacDive, AllTheBacteria, and matched culture-deposit evidence | Supported in bounded source scans for the NBRC 3299 source chain, including native GOLD `Go0543988` / `Gp0494898` / `Ga0443344` and AllTheBacteria assembly `atb.assembly:202505.SAMD00035436`. |
| Empty auxiliary evidence | Exact scans of LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, NCBI merged-ID, and same-taxon StrainInfo surfaces for `NCBITaxon:1226665` | Supported; no committed row directly keys those auxiliary sources to this NCBI strain. |

## Completeness

The record is complete for the committed processed source evidence:

- NCBI supplies the strain identity, the direct `Acetobacter pasteurianus` parent, and the exact 10-ancestor lineage.
- GTDB supplies the species mapping to `GTDB:s__Acetobacter_ascendens` and the GENOME source attestation.
- BacDive supplies the lone local strain row and all six culture-collection identifiers.
- The assembly, genome, ATB, BioProject, BioSample, GOLD, and StrainInfo related records are scoped through exact NBRC 3299 culture-deposit matches rather than taxon-level inference alone.
- No exact same-taxon LPSN, MediaDive, Madin et al., BactoTraits, NCBI type-material, or NCBI merged-ID row exists in the committed inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

AllTheBacteria reports `sylph_species: Acetobacter ascendens` for sample `SAMD00035436`, which is consistent with the generated GTDB mapping to `s__Acetobacter_ascendens`.
