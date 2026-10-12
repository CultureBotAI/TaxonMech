# YAML Record Review: Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM 12093

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml
- Started UTC: 2026-10-02T16:20:42Z
- Finished UTC: 2026-10-02T16:20:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102618` |
| Label | `Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM 12093` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:210` |
| Parent label | `Helicobacter pylori` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `GTDB`, `BACDIVE`, `MEDIADIVE`, `GOLD`, `MADIN`, `BACTOTRAITS` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml` | Pass: the strict two-file batch scanned 2 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` and parsed strain summary for this YAML | Pass: 5046 lines, 10 lineage entries, 5 synonyms, 1 xref, 1 BacDive strain, 13 culture collection IDs, 58 genome assemblies, 39 genome records, 239 related records, and 7 source attestations. |
| Direct raw/curation exact-ID scan | Pass: top-level source rows for `NCBITaxon:102618` trace to PATHS, legacy page paths, seed scope, NCBI Taxonomy, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, and the generated YAML. |
| Direct BacDive nested scan | Pass: `kgmicrobe.strain:bacdive_6102` resolves in raw strain assemblies, genome records, and related records, plus StrainInfo and ATB overlay rows. |
| Direct lineage source scan | Pass: all 10 lineage identifiers resolve as first-column rows in `data/raw/ncbitaxon_taxa.tsv`. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10830 maps `NCBITaxon:102618` to `helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093`.
- `curation/seed_scope.tsv` row 5894 keeps this taxon in scope with an attested seven-source rule including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 18128 names the exact NCBI strain `Helicobacter pylori NCTC 11637 = CCUG 17874 = ATCC 43504 = JCM 12093`, under `NCBITaxon:210` / `Helicobacter pylori`.
- `data/raw/gtdb_mappings.tsv` row 1200 maps `GTDB:s__Helicobacter_pylori` to `NCBITaxon:102618` with `skos:closeMatch` and a 633-genome count.
- `data/raw/ncbi_merged_ids.tsv` rows 878 and 11357 preserve old NCBI ids that now merge into `NCBITaxon:102618`; they do not conflict with the canonical identifier.

## Evidence

- The YAML identifier, strain rank, label, parent species, genetic code, and 10-node lineage agree with the exact NCBI Taxonomy row.
- NCBI supplies the exact synonyms `Helicobacter pylori ATCC 43504` and `Helicobacter pylori JCM 12093`, and the related synonyms `Helicobacter pylori CCUG 17874` and `Helicobacter pylori NCTC 11637`.
- The GTDB taxonomy mapping, xref, `skos:closeMatch` predicate, and 633-genome attestation are backed by `data/raw/gtdb_species.tsv` row 73699 and `data/raw/gtdb_mappings.tsv` row 1200.
- Source attestation counts match the source aggregate rows: `data/raw/mediadive_taxa.tsv` row 78 for 3 media, `data/raw/gold_organisms.tsv` row 324 for 3 GOLD organisms, `data/raw/madin_taxa.tsv` row 500 for 5 MADIN trait assertions, and `data/raw/bactotraits_taxa.tsv` row 56 for 7 BactoTraits assertions.
- `data/raw/bacdive_strains.tsv` row 5989 backs the single declared `bacdive:6102` strain and its 13 culture collection IDs; `data/raw/culture_collection_strains.tsv` rows 5408, 16699, 17147, 44290, 70739, 82482, 99712, 111914, 124475, 124476, 129235, 129236, and 142998 back the exact culture identifiers.

## Completeness

- The record is complete for the current seven top-level source families and for the direct BacDive strain row.
- Nested strain evidence is populated from `data/raw/strain_assemblies.tsv` rows 138167-138214, `data/raw/strain_genome_records.tsv` rows 110706-110743, and `data/raw/strain_related_records.tsv` rows 396648-396769.
- `data/straininfo/assemblies.tsv` rows 10645-10654 and `data/straininfo/strain_links.tsv` rows 95423-95435 add the StrainInfo genome and deposit evidence for `straininfo.strain:10524`.
- `data/atb/strain_links.tsv` row 4814 and `data/atb/genome_links.tsv` rows 21053-21058 add the AllTheBacteria evidence linked to `kgmicrobe.strain:bacdive_6102`.
- The nested lists contain 58 genome assemblies from BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo; 39 genome records from AllTheBacteria, BacDive, BV-BRC, GOLD, and GTDB; and 239 related BioProject, BioSample, GOLD, StrainInfo, and nucleotide-sequence records.
- No top-level causal graphs are present or expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml`.
- Re-run `just verify-corpus`.
- Re-run the exact NCBI, BacDive, GTDB, StrainInfo, ATB, MediaDive, GOLD, MADIN, and BactoTraits source scans after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- YAML lines 1, 66, 5001, 5003, 5009, 5015, 5020, 5025, 5030, and 5035 preserve the identifier, strain list, attestation block, and seven source IDs.
- Related rows that carry `NCBITaxon:210` are retained only when they match one of the BacDive culture identifiers for this strain.
- Future corrections belong in the upstream source extraction, `data/straininfo/`, `data/atb/`, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml` directly.
