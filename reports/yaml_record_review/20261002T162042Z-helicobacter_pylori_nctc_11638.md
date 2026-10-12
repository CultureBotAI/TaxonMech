# YAML Record Review: Helicobacter pylori NCTC 11638

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml
- Started UTC: 2026-10-02T16:20:42Z
- Finished UTC: 2026-10-02T16:20:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102619` |
| Label | `Helicobacter pylori NCTC 11638` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:210` |
| Parent label | `Helicobacter pylori` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Source attestations | `NCBITAXON`, `BACDIVE`, `MEDIADIVE`, `MADIN`, `BACTOTRAITS` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/helicobacter_pylori_nctc_11637_ccug_17874_atcc_43504_jcm_12093.yaml data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml` | Pass: the strict two-file batch scanned 2 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` and parsed strain summary for this YAML | Pass: 1250 lines, 10 lineage entries, 1 synonym, 0 xrefs, 1 BacDive strain, 6 culture collection IDs, 7 genome assemblies, 3 genome records, 62 related records, and 5 source attestations. |
| Direct raw/curation exact-ID scan | Pass: top-level source rows for `NCBITaxon:102619` trace to PATHS, legacy page paths, seed scope, NCBI Taxonomy, BacDive, MediaDive, MADIN, BactoTraits, and the generated YAML. |
| Direct BacDive nested scan | Pass: `kgmicrobe.strain:bacdive_6101` resolves in raw strain assemblies, genome records, and related records, plus StrainInfo overlay rows. |
| Direct lineage source scan | Pass: all 10 lineage identifiers resolve as first-column rows in `data/raw/ncbitaxon_taxa.tsv`. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10831 maps `NCBITaxon:102619` to `helicobacter_pylori_nctc_11638`.
- `curation/seed_scope.tsv` row 14114 keeps this taxon in scope with an attested five-source rule including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 18129 names the exact NCBI strain `Helicobacter pylori NCTC 11638`, under `NCBITaxon:210` / `Helicobacter pylori`.
- No exact top-level GTDB mapping or GOLD aggregate row is present for `NCBITaxon:102619`; the GTDB and GOLD records in the YAML are nested under the BacDive strain through culture-identifier matches to species-level source rows.

## Evidence

- The YAML identifier, strain rank, label, parent species, genetic code, single NCBI synonym, and 10-node lineage agree with the exact NCBI Taxonomy row.
- Source attestation counts match the source aggregate rows: `data/raw/mediadive_taxa.tsv` row 79 for 1 medium, `data/raw/madin_taxa.tsv` row 501 for 4 MADIN trait assertions, and `data/raw/bactotraits_taxa.tsv` row 57 for 1 BactoTraits assertion.
- `data/raw/bacdive_strains.tsv` row 5988 backs the single declared `bacdive:6101` strain and its 6 culture collection IDs.
- `data/raw/culture_collection_strains.tsv` rows 17148, 47275, 58870, 129237, 129238, and 142999 back the six exact culture identifiers.

## Completeness

- The record is complete for the current five top-level source families and for the direct BacDive strain row.
- Nested strain evidence is populated from `data/raw/strain_assemblies.tsv` rows 138160-138166, `data/raw/strain_genome_records.tsv` rows 110703-110705, and `data/raw/strain_related_records.tsv` rows 396626-396647.
- `data/straininfo/strain_links.tsv` rows 95417-95422 add the StrainInfo deposit evidence for `straininfo.strain:48787`; no ATB row currently mentions `kgmicrobe.strain:bacdive_6101`.
- The nested lists contain 7 genome assemblies from BacDive, GTDB, and NCBI Assembly; 3 genome records from BV-BRC and GTDB; and 62 related BioProject, BioSample, GOLD, StrainInfo, and nucleotide-sequence records.
- No top-level taxonomy mapping, xref, or causal graph is expected for the current exact source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml`.
- Re-run `just verify-corpus`.
- Re-run the exact NCBI, BacDive, StrainInfo, ATB, MediaDive, MADIN, and BactoTraits source scans after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- YAML lines 1, 45, 1217, 1219, 1225, 1230, 1235, and 1240 preserve the identifier, strain list, attestation block, and five source IDs.
- Related rows that carry `NCBITaxon:210` are retained only when they match one of the BacDive culture identifiers for this strain.
- Future corrections belong in the upstream source extraction, `data/straininfo/`, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/helicobacter_pylori_nctc_11638.yaml` directly.
