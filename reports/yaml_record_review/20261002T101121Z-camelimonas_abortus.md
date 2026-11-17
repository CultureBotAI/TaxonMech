# YAML Record Review: Camelimonas abortus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/camelimonas_abortus.yaml
- Started UTC: 2026-10-02T10:11:21Z
- Finished UTC: 2026-10-02T10:11:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017184` |
| Label | `Camelimonas abortus` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1017183` |
| Parent label | `Camelimonas` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `1` |
| Type strain | `kgmicrobe.strain:bacdive_1675` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `MEDIADIVE`, `GOLD`, `MADIN`, `BACTOTRAITS` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/camelimonas_abortus.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/camelimonas_abortus.yaml data/taxa/bacteria/bacterium_ksw1.yaml data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs1.yaml data/taxa/bacteria/enterococcus_sp_enrichment_culture_clone_ptmrs13.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the generated corpus reproduced exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 815 lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB taxonomy mapping, 2 NCBI synonyms, 2 xrefs, 1 BacDive strain, and 8 source attestations. |
| Exact report lookup | Pass: `rg --no-ignore --hidden --files reports/yaml_record_review -g '*camelimonas_abortus.md'` found no prior report for this stem. |
| Direct source probes | Needs curation: exact-ID and source-ID scans found expected NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, MADIN, BactoTraits, and StrainInfo rows, plus two cross-taxon GOLD organism rows owned by `data/raw/strain_related_records.tsv`. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10269 maps `NCBITaxon:1017184` to `camelimonas_abortus`.
- `curation/seed_scope.tsv` row 4035 keeps this taxon in scope as `Camelimonas abortus` with 8 sources including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 218604 names the exact NCBI taxon as `Camelimonas abortus`, `SPECIES`, parent `NCBITaxon:1017183`, and genetic code `11`.
- The 9 YAML lineage entries match raw NCBI rows for root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Chelatococcaceae, and Camelimonas.
- `grounding_status: EXACT` and `mapping_status: SEEDED` match a direct seeded NCBI Taxonomy record backed by additional curated source rows.

## Evidence

- The `NCBITAXON` attestation agrees with `data/raw/ncbitaxon_taxa.tsv` row 218604 and its 2026-09-13 snapshot.
- The LPSN nomenclature block agrees with `data/raw/lpsn_names.tsv` row 26855: `lpsn:789852`, `Camelimonas abortus`, species rank, `Kampfer et al. 2012`, validly published legitimate correct-name status, type strain designations `CCUG-61094`, `CIP-110303`, and `DSM-24741`, the expected PMID/DOIs, and `INSDC:MT758014`.
- The GTDB mapping agrees with `data/raw/gtdb_species.tsv` row 40262 and `data/raw/gtdb_mappings.tsv` row 1177: `GTDB:s__Camelimonas_abortus` maps to `NCBITaxon:1017184` with `skos:closeMatch` and 2 genomes.
- The 2 NCBI synonyms in YAML are the two alternative names on the raw NCBI row.
- `data/raw/bacdive_strains.tsv` row 1671 supports `kgmicrobe.strain:bacdive_1675`, its B1252 / UK34/07-5 designation, and the four culture-collection aliases in the YAML.
- `data/raw/strain_assemblies.tsv` rows 84512 through 84525 and `data/raw/strain_genome_records.tsv` rows 67083 through 67088 support the INSDC, BV-BRC, GOLD, GTDB, and NCBI Assembly genome assertions for `CCM 7941`.
- `data/raw/strain_related_records.tsv` rows 253816 through 253837 and 253840 through 253849 support the Camelimonas BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related-record blocks.
- `data/raw/mediadive_taxa.tsv` row 69, `data/raw/bactotraits_taxa.tsv` row 49, `data/raw/madin_taxa.tsv` row 473, and `data/raw/gold_organisms.tsv` row 295 agree with the non-name source-attestation counts.
- `data/straininfo/strain_links.tsv` rows 69535 through 69537 support the DSM, CCUG, and CIP StrainInfo deposit related-record blocks.

## Completeness

- Most sections are complete for the maintained rows reviewed here: NCBI identity and synonyms, LPSN nomenclature, GTDB mapping, the BacDive type strain, genome records, and same-taxon related records all have direct upstream rows.
- The record is materially over-complete because it imports two GOLD organism rows from another taxon into this `Camelimonas abortus` YAML.
- No causal graph is expected for this generated taxon, strain, genome, medium-count, and trait-count record.
- `just verify-corpus` confirmed that this YAML is generated from maintained inputs, so the fix belongs upstream of YAML emission.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Two `Sphingobium rhizovicinum CCM 7941` GOLD organism records with `taxon_id: NCBITaxon:432308` are nested in the `Camelimonas abortus` strain related records. | `data/taxa/bacteria/camelimonas_abortus.yaml` lines 517-538 mirror `data/raw/strain_related_records.tsv` rows 253838-253839, which attach `gold:Go0030110` to `kgmicrobe.strain:bacdive_1675` through the `CCM 7941` string while retaining the source taxon `NCBITaxon:432308`. | The raw strain-related-record GOLD matching transform that writes `data/raw/strain_related_records.tsv`. |

## Recommended Edits

- Update the GOLD organism matching transform so organism-only rows whose source `taxon_id` differs from the owning BacDive strain's taxon do not attach to `kgmicrobe.strain:bacdive_1675` solely through a culture identifier collision.
- Regenerate `data/raw/strain_related_records.tsv` and the seeded YAML corpus so rows 253838-253839 disappear from `data/taxa/bacteria/camelimonas_abortus.yaml`.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/camelimonas_abortus.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/camelimonas_abortus.yaml`.
- Re-run `just verify-corpus`.
- Re-run an ignored-inclusive scan for `gold:Go0030110`, `Sphingobium rhizovicinum CCM 7941`, and `NCBITaxon:432308` against `data/taxa/bacteria/camelimonas_abortus.yaml`; the fixed YAML should have no hits.

## Additional Notes

- Absence and uniqueness checks used `--no-ignore --hidden`, so ignored files were included.
- The review read the full 815-line YAML and checked the generated lineage, nomenclature, taxonomy mapping, synonym, xref, strain, genome, related-record, source-attestation, and curation-history sections.
- `data/raw/culture_collection_strains.tsv` maps `kgmicrobe.strain:CCM-7941` to `NCBITaxon:1017184` and maps the Sphingobium type strain to `kgmicrobe.strain:CCM-7491`, so the reviewed cross-taxon rows are not supported by that culture-collection table.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10269 |
| `curation/seed_scope.tsv` | 4035 |
| `data/raw/ncbitaxon_taxa.tsv` | 218604 |
| `data/raw/lpsn_names.tsv` | 26855 |
| `data/raw/gtdb_mappings.tsv` | 1177 |
| `data/raw/bacdive_strains.tsv` | 1671 |
| `data/raw/strain_assemblies.tsv` | 84512-84525 |
| `data/raw/strain_related_records.tsv` | 253816-253849 |
| `data/straininfo/strain_links.tsv` | 69535-69537 |
| `data/taxa/bacteria/camelimonas_abortus.yaml` | 1, 517, 528, 765 |

