# YAML Record Review: Gluconacetobacter tumulicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gluconacetobacter_tumulicola.yaml
- Started UTC: 2026-10-02T10:07:00Z
- Finished UTC: 2026-10-02T10:07:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017177` |
| Label | `Gluconacetobacter tumulicola` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:89583` |
| Parent label | `Gluconacetobacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `5` |
| Type strain | `kgmicrobe.strain:bacdive_133743` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/gluconacetobacter_tumulicola.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/gluconacetobacter_tumulicola.yaml data/taxa/bacteria/spirosoma_sp_hdk211.yaml data/taxa/bacteria/gluconacetobacter_asukensis.yaml data/taxa/bacteria/bacillus_sp_ku7.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: 625960 records were expected, 625960 were found on disk, and 0 were missing, extra, or differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 1065 lines, 9 lineage entries, 1 LPSN nomenclature entry, 1 GTDB taxonomy mapping, 6 NCBI synonyms, 2 xrefs, 5 BacDive strains, and 6 source attestations. |
| Exact report lookup | Pass: `rg --no-ignore --hidden --files reports/yaml_record_review -g '*gluconacetobacter_tumulicola.md'` found no prior report for this stem. |
| Direct source probes | Pass: ignored-inclusive exact-ID and source-ID scans found matching rows in NCBI Taxonomy, LPSN, GTDB, BacDive, GOLD, MADIN, AllTheBacteria, StrainInfo, and strain crosswalk raw inventories. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10265 maps `NCBITaxon:1017177` to `gluconacetobacter_tumulicola`.
- `curation/seed_scope.tsv` row 8654 keeps this taxon in scope as `Gluconacetobacter tumulicola` with 6 sources including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 218600 names the exact NCBI taxon as `Gluconacetobacter tumulicola`, `SPECIES`, parent `NCBITaxon:89583`, and genetic code `11`.
- The 9 YAML lineage entries match raw NCBI rows for root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Acetobacterales, Acetobacteraceae, and Gluconacetobacter.
- `grounding_status: EXACT` and `mapping_status: SEEDED` match a direct seeded NCBI Taxonomy record backed by additional curated source rows.

## Evidence

- The `NCBITAXON` attestation agrees with `data/raw/ncbitaxon_taxa.tsv` row 218600 and its 2026-09-13 snapshot.
- The LPSN nomenclature block agrees with `data/raw/lpsn_names.tsv` row 27074: `lpsn:790085`, `Gluconacetobacter tumulicola`, species rank, `Tazato et al. 2012`, a validly published legitimate correct-name status, type strain `kgmicrobe.strain:JCM-17774`, publications `PMID:22038998`, `DOI:10.1099/ijs.0.034595-0`, `DOI:10.1099/ijs.0.047837-0`, and sequence accession `INSDC:AB627116`.
- The GTDB mapping agrees with `data/raw/gtdb_species.tsv` row 70495 and `data/raw/gtdb_mappings.tsv` row 1175: `GTDB:s__Gluconacetobacter_tumulicola` maps to `NCBITaxon:1017177` with `skos:closeMatch` and 2 genomes.
- The 6 NCBI synonyms in YAML are exactly the alternative-name pipe list on the raw NCBI row.
- `data/raw/bacdive_strains.tsv` rows 56053 and 84345 through 84348 account for all 5 BacDive strains and for the 4 culture-collection IDs on the type strain.
- `data/raw/culture_collection_strains.tsv` rows 10446, 103288 through 103292, 126751, and 140745 ground the BCRC, JCM, LMG, and NCIMB strain aliases to `NCBITaxon:1017177`.
- `data/raw/strain_assemblies.tsv` rows 31845 through 31861 and `data/raw/strain_genome_records.tsv` rows 25135 through 25143 support the type-strain INSDC, BV-BRC, GOLD, GTDB, and NCBI Assembly genome assertions for `LMG 27725` and `JCM 17774`.
- `data/atb/genome_links.tsv` rows 4735 through 4739 connect `atb.assembly:202505.SAMN14650892` and `biosample:SAMN14650892` to the `LMG 27725` type-strain evidence.
- `data/raw/strain_related_records.tsv` rows 86107 through 86144 back the BioProject, BioSample, GOLD analysis, GOLD organism, and GOLD project related-record blocks.
- `data/straininfo/assemblies.tsv` row 2518 and `data/straininfo/strain_links.tsv` rows 15271 through 15273 back `straininfo.strain:380880` and the JCM, LMG, and NCIMB deposit records.
- `data/raw/gold_organisms.tsv` row 293 and `data/raw/madin_taxa.tsv` row 471 agree with the GOLD organism count 3 and MADIN assertion count 10 in `source_attestations`.

## Completeness

- The generated YAML is complete for the maintained raw rows reviewed here: it carries NCBI identity and synonyms, LPSN nomenclature, GTDB mapping, GOLD and MADIN taxon attestations, all 5 BacDive strains, genome records, related records, AllTheBacteria sample links, and StrainInfo cross-links.
- `strain_count: 5` agrees with the 5 BacDive rows for `NCBITaxon:1017177`.
- The record has no `causal_graphs` block; none is expected from the seeded taxon, strain, genome, project, and trait-count inputs.
- `just verify-corpus` reproduced this generated record from maintained inputs, so future edits belong in `data/raw/`, `data/atb/`, `data/straininfo/`, `curation/seed_scope.tsv`, or the seeder rather than in this YAML directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/gluconacetobacter_tumulicola.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/gluconacetobacter_tumulicola.yaml`.
- Re-run `just verify-corpus`.
- Re-run ignored-inclusive exact source probes after any refresh of `data/raw/`, `data/atb/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence and uniqueness checks used `--no-ignore --hidden`, so ignored files were included.
- The review read the full 1065-line YAML and checked the generated sections for lineage, nomenclature, taxonomy mapping, NCBI synonyms, xrefs, 5 nested strains, source attestations, and curation history.
- The source scan intentionally treated `data/straininfo/` and `data/atb/` as maintained inventories because the curation history lists those alongside `data/raw/`.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10265 |
| `curation/seed_scope.tsv` | 8654 |
| `data/raw/ncbitaxon_taxa.tsv` | 218600 |
| `data/raw/lpsn_names.tsv` | 27074 |
| `data/raw/gtdb_mappings.tsv` | 1175 |
| `data/raw/bacdive_strains.tsv` | 56053, 84345-84348 |
| `data/raw/strain_assemblies.tsv` | 31845-31861 |
| `data/raw/strain_related_records.tsv` | 86107-86144 |
| `data/straininfo/strain_links.tsv` | 15271-15273 |
| `data/taxa/bacteria/gluconacetobacter_tumulicola.yaml` | 1 and 1025 |

